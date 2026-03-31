

<!-- Start of Syntax__000086a5-6616-2780-2fc8-0460ab9a3e5b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (XYZ, ElementId)

---



|  |
| --- |
| [Point Class](9a9591f5-e6d2-6af5-8642-b14fdd1ee5ec.htm)   [See Also](#seeAlsoToggle) |

Creates a point at the given coordinates and assigns it the specified GraphicsStyle.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static Point Create( 	XYZ coord, 	ElementId id ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	coord As XYZ, _ 	id As ElementId _ ) As Point ``` |

 

| Visual C++ |
| --- |
| ``` public: static Point^ Create( 	XYZ^ coord,  	ElementId^ id ) ``` |

#### Parameters

coord
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The coordinates where the point will be created.

id
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the GraphicsStyle element from which to apply the point properties.

#### Return Value

A Point object.

# See Also

[Point Class](9a9591f5-e6d2-6af5-8642-b14fdd1ee5ec.htm)

[Create Overload](fcc27c7e-5491-fea0-9adc-98db9e27076c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0081a44a-4f6b-317a-9238-0f3c6fbd0fe2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [ThinLinesOptions Class](1d348cae-3e60-f890-5262-da795d927ea4.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 16.0.0.0 (16.0.0.0)   
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

[ThinLinesOptions Class](1d348cae-3e60-f890-5262-da795d927ea4.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__0083cc42-0897-f28e-1ded-49863ab428a1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GradientNoiseSize Property

---



|  |
| --- |
| [Gradient Class](2b517b49-c915-74a9-bb6f-2a233d6706be.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Size" from the "Gradient" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string GradientNoiseSize { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GradientNoiseSize As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ GradientNoiseSize { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble" within the range of "0, 1000000000".

# See Also

[Gradient Class](2b517b49-c915-74a9-bb6f-2a233d6706be.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__072adfe0-63f0-3613-f5a5-6c3cb4110f00.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.EditingFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](900bfd40-b8db-86b8-009f-d7dee39471b6.htm)   [See Also](#seeAlsoToggle) |

Failures related to editing operations.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class EditingFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class EditingFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class EditingFailures abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BuiltInFailures EditingFailures

# See Also

[BuiltInFailures EditingFailures Members](900bfd40-b8db-86b8-009f-d7dee39471b6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__072b35eb-44b7-75f3-6a41-70cca19782e7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpaceSeparationLinesOverlap Property

---



|  |
| --- |
| [BuiltInFailures OverlapFailures Class](b5f85718-fcb7-9396-e706-6d04f0c25c34.htm)   [See Also](#seeAlsoToggle) |

Highlighted space separation lines overlap. One of them may be ignored when Revit finds space boundaries. Delete one of the lines.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SpaceSeparationLinesOverlap { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpaceSeparationLinesOverlap As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SpaceSeparationLinesOverlap { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures OverlapFailures Class](b5f85718-fcb7-9396-e706-6d04f0c25c34.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__072be1bd-244a-3ed0-c9e6-930218de9b6c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FbxLightTemperatureLoss Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Temperature Loss"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FbxLightTemperatureLoss { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FbxLightTemperatureLoss As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FbxLightTemperatureLoss { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__072e1e86-5ddf-b23c-9f18-9ead2ed9899d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DividedSurfaceLoopsOfSplittingCurves Property

---



|  |
| --- |
| [BuiltInFailures DividedSurfaceFailures Class](6c670503-f89e-7ee3-1883-af2a9576f390.htm)   [See Also](#seeAlsoToggle) |

Curve elements forming a closed loop currently cannot be used as splitters and are ignored.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DividedSurfaceLoopsOfSplittingCurves { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DividedSurfaceLoopsOfSplittingCurves As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DividedSurfaceLoopsOfSplittingCurves { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DividedSurfaceFailures Class](6c670503-f89e-7ee3-1883-af2a9576f390.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__072ee20e-d270-31ea-5949-d9aa9ec8529c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalVisualLightTransmittance Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Visual Light Transmittance"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnalyticalVisualLightTransmittance { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticalVisualLightTransmittance As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnalyticalVisualLightTransmittance { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__073a2681-a75f-ecae-96b0-f56d8ffa8979.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [PipeFittingAndAccessoryPressureDropUIData Class](6dcc2335-c5a0-2122-82ed-566efa781f41.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.UI.Plumbing](a4cc3644-f568-6568-9c2f-dcdb6eafdf6b.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
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

[PipeFittingAndAccessoryPressureDropUIData Class](6dcc2335-c5a0-2122-82ed-566efa781f41.htm)

[Autodesk.Revit.UI.Plumbing Namespace](a4cc3644-f568-6568-9c2f-dcdb6eafdf6b.htm)

<!-- Start of Syntax__073a4884-30b4-965f-ae11-db1123e7eb0a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveFilter Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Removes a filter from the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void RemoveFilter( 	ElementId filterElementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveFilter ( _ 	filterElementId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveFilter( 	ElementId^ filterElementId ) ``` |

#### Parameters

filterElementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     ElementId of the filter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Filter is not applied to the view. -or- ElementId is not associated with a FilterElement. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The element "this View" does not belong to a project document. -or- The view type does not support Visibility/Graphics Overriddes. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__073a73a6-c221-8150-6a40-dba8677d1b79.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureVRepeat Property

---



|  |
| --- |
| [Gradient Class](2b517b49-c915-74a9-bb6f-2a233d6706be.htm)   [See Also](#seeAlsoToggle) |

The property labeled "V Repeat" from the "Gradient" schema.

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

[Gradient Class](2b517b49-c915-74a9-bb6f-2a233d6706be.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__073aaf81-3df4-f4f6-c999-905b5c2cd7f7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Insert Method

---



|  |
| --- |
| [GroupSet Class](cac73a6e-e521-7af1-281c-22c8e5245c03.htm)   [See Also](#seeAlsoToggle) |

Insert the specified group into the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool Insert( 	Group item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Insert ( _ 	item As Group _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Insert( 	Group^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB Group](ca54af3c-52d8-0aed-cd22-440ec2584b89.htm)    
     The group to be inserted into the set.

#### Return Value

Returns whether the group was inserted into the set.

# See Also

[GroupSet Class](cac73a6e-e521-7af1-281c-22c8e5245c03.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__073ecb79-f98a-c1e0-bcaa-bba62ef5e919.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CdPerMSup2 Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol cd/mÂ², indicating unit Candelas per square meter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CdPerMSup2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CdPerMSup2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CdPerMSup2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__073f35f9-8a25-b8d7-7e75-a2e3ec8c7e0f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [BRepBuilderSurfaceGeometry Class](c21d4101-cc15-1990-ee9f-994b487bf95d.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
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

[BRepBuilderSurfaceGeometry Class](c21d4101-cc15-1990-ee9f-994b487bf95d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__074c4930-5ae8-fe51-738f-f602442b3a20.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpaceSet Constructor

---



|  |
| --- |
| [SpaceSet Class](ff608354-dee5-99f7-fca3-d8b20ff5733d.htm)   [See Also](#seeAlsoToggle) |

Initializes a new instance of the  [SpaceSet](ff608354-dee5-99f7-fca3-d8b20ff5733d.htm)  class

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public SpaceSet() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: SpaceSet() ``` |

# See Also

[SpaceSet Class](ff608354-dee5-99f7-fca3-d8b20ff5733d.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__074d8dfc-b6f7-1d8f-4fa9-60505024ff0f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [CurveArrArrayIterator Class](cdd6e636-1a16-2e4a-90db-ada0fcf0b074.htm)   [See Also](#seeAlsoToggle) |

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

[CurveArrArrayIterator Class](cdd6e636-1a16-2e4a-90db-ada0fcf0b074.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__075b16aa-21c6-a35c-a9bd-270d67583982.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureScaleLock Property

---



|  |
| --- |
| [Checker Class](ff4ecb34-6fef-402a-5cee-c7937974b8d2.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Scale Lock" from the "Checker" schema.

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

[Checker Class](ff4ecb34-6fef-402a-5cee-c7937974b8d2.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__075e9938-be39-b27b-4583-1ec2f1cee14b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportLinetypeKey Constructor

---



|  |
| --- |
| [ExportLinetypeKey Class](7f67a1c8-cc9b-9b17-aa87-664657ee9d7d.htm)   [See Also](#seeAlsoToggle) |

Constructs a new default ExportLinetypeKey.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ExportLinetypeKey() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: ExportLinetypeKey() ``` |

# See Also

[ExportLinetypeKey Class](7f67a1c8-cc9b-9b17-aa87-664657ee9d7d.htm)

[ExportLinetypeKey Overload](33628875-475d-4d9b-38bd-b3116bd56aa7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__076acc54-94ff-19e0-49ff-aec9c194fd5c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NoElementSelected Property

---



|  |
| --- |
| [BuiltInFailures SelectionFailures Class](027c3831-3eae-0a5a-8512-e30773a37ee7.htm)   [See Also](#seeAlsoToggle) |

No element selected.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NoElementSelected { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NoElementSelected As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NoElementSelected { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SelectionFailures Class](027c3831-3eae-0a5a-8512-e30773a37ee7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__076c03d2-6659-3f1e-40e8-cc1d4810984b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [FillGrid Class](6dfc3e2f-c869-d06e-876e-49c4007f7e59.htm)   [See Also](#seeAlsoToggle) |

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

[FillGrid Class](6dfc3e2f-c869-d06e-876e-49c4007f7e59.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__076d7999-c933-38ad-a225-f24832d1942f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FailedToChangeWallJointsTypeFailure Property

---



|  |
| --- |
| [BuiltInFailures WallJoinFailures Class](575d7542-9a7a-e3c9-7f11-0cc040d74aac.htm)   [See Also](#seeAlsoToggle) |

Some of the joints you have selected can only have one wall joint type, so these joints haven't been changed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FailedToChangeWallJointsTypeFailure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FailedToChangeWallJointsTypeFailure As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FailedToChangeWallJointsTypeFailure { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures WallJoinFailures Class](575d7542-9a7a-e3c9-7f11-0cc040d74aac.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__077b9ce9-f06b-8522-3967-746be8776f3a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanExecuteEventArgs Class

---



|  |
| --- |
| [Members](fbfd252f-590b-d8a5-5ab2-70cd40ea00ad.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by AddInCommandBinding's CanExecute event.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class CanExecuteEventArgs : CommandEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class CanExecuteEventArgs _ 	Inherits CommandEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class CanExecuteEventArgs : public CommandEventArgs ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitEventArgs](2995a67a-3135-8032-a92a-079b6f9d6954.htm)    
  [Autodesk.Revit.UI.Events CommandEventArgs](c3d77fea-4752-aade-9e0b-95cc79461aa6.htm)    
  Autodesk.Revit.UI.Events CanExecuteEventArgs

# See Also

[CanExecuteEventArgs Members](fbfd252f-590b-d8a5-5ab2-70cd40ea00ad.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__077e58a6-977e-be35-6e20-dd07daa1fdd0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetTypeId Method

---



|  |
| --- |
| [DirectShape Class](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.htm)   [See Also](#seeAlsoToggle) |

Sets the DirectShapeType for the DirectShape element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void SetTypeId( 	ElementId typeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetTypeId ( _ 	typeId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetTypeId( 	ElementId^ typeId ) ``` |

#### Parameters

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ID of the type corresponding to this DirectShape element. May only be set once.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | typeId is not a valid Element identifier. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShape Class](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__077e6fbd-8634-346c-6f62-50b6dde554de.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAnalyticalShadingSurfaces Method

---



|  |
| --- |
| [EnergyAnalysisDetailModel Class](858aed23-8a94-a70a-c1fc-ca03523e2f02.htm)   [See Also](#seeAlsoToggle) |

The collection of analytical shading surfaces.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<EnergyAnalysisSurface> GetAnalyticalShadingSurfaces() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAnalyticalShadingSurfaces As IList(Of EnergyAnalysisSurface) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<EnergyAnalysisSurface^>^ GetAnalyticalShadingSurfaces() ``` |

#### Return Value

Returns the analytical shading surfaces after model calculation.

# See Also

[EnergyAnalysisDetailModel Class](858aed23-8a94-a70a-c1fc-ca03523e2f02.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__077f903a-9a86-f729-ab53-7775c7b6b838.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BendWidth Property

---



|  |
| --- |
| [StructuralSectionSigmaProfile Class](896820d0-8a2f-f67e-bcd6-de74da7e4b05.htm)   [See Also](#seeAlsoToggle) |

Bend segment width.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public double BendWidth { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BendWidth As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double BendWidth { 	double get (); 	void set (double value); } ``` |

# See Also

[StructuralSectionSigmaProfile Class](896820d0-8a2f-f67e-bcd6-de74da7e4b05.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__078cf0bc-d3a2-8298-234f-a204f7fa0058.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextPosition Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Text Position"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TextPosition { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextPosition As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TextPosition { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__079b1aca-c29f-4db5-2b36-c67c3802a623.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnresolvableErrorInFamilyWarn Property

---



|  |
| --- |
| [BuiltInFailures GeneralFailures Class](d4679f32-45d9-bec2-e0ff-168c3aee6de9.htm)   [See Also](#seeAlsoToggle) |

An error occurred in family "[Name]" that cannot be automatically resolved.\nError Information:\n"[Text]"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId UnresolvableErrorInFamilyWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property UnresolvableErrorInFamilyWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ UnresolvableErrorInFamilyWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GeneralFailures Class](d4679f32-45d9-bec2-e0ff-168c3aee6de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__079b5caa-f180-d6cc-7d9d-59627aea4106.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewtonsPerSquareMillimeter Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Newtons per square millimeter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId NewtonsPerSquareMillimeter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NewtonsPerSquareMillimeter As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ NewtonsPerSquareMillimeter { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__079c68bf-3bb5-7146-2631-91a33885b9c5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ToggleButtonData Constructor (String, String, String, String)

---



|  |
| --- |
| [ToggleButtonData Class](ca92168b-f675-ce48-f1e3-fd5640762ad8.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of ToggleButtonData, where the ToggleButton will execute an ExternalCommand when clicked.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ToggleButtonData( 	string name, 	string text, 	string assemblyName, 	string className ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	name As String, _ 	text As String, _ 	assemblyName As String, _ 	className As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ToggleButtonData( 	String^ name,  	String^ text,  	String^ assemblyName,  	String^ className ) ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The internal name of the new button.

text
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The user visible text seen on the new button.

assemblyName
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The assembly path of the button.

className
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The name of the class containing the implementation for the command.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when    a null reference (  Nothing  in Visual Basic)  is passed for one or more arguments. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when an empty string is passed for one or more arguments. |

# See Also

[ToggleButtonData Class](ca92168b-f675-ce48-f1e3-fd5640762ad8.htm)

[ToggleButtonData Overload](9799f894-5817-8748-644d-4972567995fc.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__079d2186-d55c-d22d-7dff-cdf913399f8c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Value Property

---



|  |
| --- |
| [DoubleParameterValue Class](561ef32b-c3bc-3847-ef2a-27f4a011e650.htm)   [See Also](#seeAlsoToggle) |

The stored value

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public double Value { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Value As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Value { 	double get (); 	void set (double value); } ``` |

# See Also

[DoubleParameterValue Class](561ef32b-c3bc-3847-ef2a-27f4a011e650.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__079ec918-e752-32e4-e776-79aaa0f33fad.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetCurrentResolutionType Method

---



|  |
| --- |
| [FailureMessageAccessor Class](753477d8-b720-97a0-26f5-439d49de418c.htm)   [See Also](#seeAlsoToggle) |

Sets the type of a resolution to be used to resolve the failure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void SetCurrentResolutionType( 	FailureResolutionType resolutionType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetCurrentResolutionType ( _ 	resolutionType As FailureResolutionType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetCurrentResolutionType( 	FailureResolutionType resolutionType ) ``` |

#### Parameters

resolutionType
:   Type:  [Autodesk.Revit.DB FailureResolutionType](786e6422-f66d-5320-99f9-e530819e50a1.htm)    
     The type of failure resolution to be used to resolve the failure.

# Remarks

When FailuresAccessor is used to resolve failures, it will execute resolutions based on current resolution type. If no current resolution type is set, the default resolution type will be used. Setting is performed on the FailureMessageAccessor object itself, so if there are several accessors issued for the same FailureMessage, setting of the resolution type performed on one of them does not impact the others.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This FailureMessageAccessor has no resolution of resolutionType. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailureMessageAccessor has not been properly initialized. -or- This FailureMessageAccessor does not have any resolutions. |

# See Also

[FailureMessageAccessor Class](753477d8-b720-97a0-26f5-439d49de418c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__080c7d43-0546-b996-b0f1-6ca0ad79bc53.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CustomAxis Property

---



|  |
| --- |
| [IFCExtrusionCreationData Class](9447a335-6861-0533-6896-e6ff1fd41761.htm)   [See Also](#seeAlsoToggle) |

The custom extrusion axis to try when generating an extrusion.

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

[IFCExtrusionCreationData Class](9447a335-6861-0533-6896-e6ff1fd41761.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__080e5a91-8c72-8c1e-ca29-2a1f0229218a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Name Property

---



|  |
| --- |
| [Zone Class](b47e1280-b436-5f9d-17dc-5b315b50c5ee.htm)   [See Also](#seeAlsoToggle) |

Get or Set the Name of the Zone.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public override string Name { set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides WriteOnly Property Name As String 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property String^ Name { 	void set (String^ value) override; } ``` |

# Remarks

This property is used to get or set the Name of the Zone.

# See Also

[Zone Class](b47e1280-b436-5f9d-17dc-5b315b50c5ee.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__080e616b-7b8b-6c5d-3ea0-b63143875836.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanTopologySetIterator Constructor

---



|  |
| --- |
| [PlanTopologySetIterator Class](c3a4f46a-eaee-bdfa-df86-e803a7ccdf4b.htm)   [See Also](#seeAlsoToggle) |

For Internal Use Only.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PlanTopologySetIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: PlanTopologySetIterator() ``` |

# Remarks

This constructor is exposed to enable support for COM interop only. This object should never be created by the developer.

# See Also

[PlanTopologySetIterator Class](c3a4f46a-eaee-bdfa-df86-e803a7ccdf4b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__081c29af-0877-a5ce-bb49-e39ba262a43f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SplitRegionHorizontally Method

---



|  |
| --- |
| [ViewCropRegionShapeManager Class](2610cb66-5dae-9fc8-4e83-7dfe88085abb.htm)   [See Also](#seeAlsoToggle) |

Splits horizontally one region in split crop.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void SplitRegionHorizontally( 	int regionIndex, 	double leftPart, 	double rightPart ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SplitRegionHorizontally ( _ 	regionIndex As Integer, _ 	leftPart As Double, _ 	rightPart As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SplitRegionHorizontally( 	int regionIndex,  	double leftPart,  	double rightPart ) ``` |

#### Parameters

regionIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index of region to be split horizontally (numbering starts with 0).

leftPart
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Relative portion of the original region to become the new left region (0 to 1).

rightPart
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Relative portion of the original region to become the new right region (0 to 1).

# Remarks

This function splits the crop into two regions: one occupying the left quarter of the crop, and the other the right quarter of the crop.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The provided view region proportions are not valid. -or- The provided region index is invalid. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The crop of the associated view is not permitted to have multiple regions. -or- The view has non-rectangular crop shape set. -or- The view crop is already split vertically. |

# See Also

[ViewCropRegionShapeManager Class](2610cb66-5dae-9fc8-4e83-7dfe88085abb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__081cca9f-fac9-68b1-8d07-a7da5c001501.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MSup3PerHMSup2 Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol mÂ³/(hÂ·mÂ²), indicating unit Cubic meters per hour square meter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MSup3PerHMSup2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MSup3PerHMSup2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MSup3PerHMSup2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__081d9e72-73d3-5853-81d0-da1427bd9b1d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationPartExceededAngleFlexToleranceWarning Property

---



|  |
| --- |
| [BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)   [See Also](#seeAlsoToggle) |

The angle flex is greater than the maximum angle flex tolerance defined by the fabrication part. Connections with this part may not be properly aligned and may appear to be skewed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FabricationPartExceededAngleFlexToleranceWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationPartExceededAngleFlexToleranceWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FabricationPartExceededAngleFlexToleranceWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__081e145b-8e09-a6bd-b77b-1e7a7fe8a4cd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Point Property

---



|  |
| --- |
| [BoundaryConditions Class](58a98f0e-e2e5-4c8b-bea1-8228b30f1685.htm)   [See Also](#seeAlsoToggle) |

Returns the position of point boundary conditions.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ Point { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Point As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Point { 	XYZ^ get (); } ``` |

# Remarks

Boundary conditions should be BoundaryConditionsType::Point type. Otherwise exception is thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidObjectException](8092dec2-113a-0823-1a09-a46c11f99fea.htm) | Thrown when BoundaryConditions is not a BoundaryConditionsType::Point type. |

# See Also

[BoundaryConditions Class](58a98f0e-e2e5-4c8b-bea1-8228b30f1685.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__081f2683-cad8-cd20-8d11-0e188767a479.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDirectContext3DHandleSettings Method

---



|  |
| --- |
| [DirectContext3DHandleOverrides Class](8bef65c6-70bc-1a10-a9a4-47c8ec2cd842.htm)   [See Also](#seeAlsoToggle) |

Gets override settings associated with a DirectContext3D handle instance or type.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public DirectContext3DHandleSettings GetDirectContext3DHandleSettings( 	Document aDoc, 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDirectContext3DHandleSettings ( _ 	aDoc As Document, _ 	elementId As ElementId _ ) As DirectContext3DHandleSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: DirectContext3DHandleSettings^ GetDirectContext3DHandleSettings( 	Document^ aDoc,  	ElementId^ elementId ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document where elementId resides.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of the overridden element.

#### Return Value

The override settings assigned to the handle element, if present, or a default override settings if nothing was found.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The ElementId elementId is not a valid DirectContext3D handle instance or type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectContext3DHandleOverrides Class](8bef65c6-70bc-1a10-a9a4-47c8ec2cd842.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__082ab201-3b7f-3519-0a85-5af9cdb312b7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurveArrArrayIterator Constructor

---



|  |
| --- |
| [CurveArrArrayIterator Class](cdd6e636-1a16-2e4a-90db-ada0fcf0b074.htm)   [See Also](#seeAlsoToggle) |

For Internal Use Only.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public CurveArrArrayIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: CurveArrArrayIterator() ``` |

# Remarks

This constructor is exposed to enable support for COM interop only. This object should never be created by the developer.

# See Also

[CurveArrArrayIterator Class](cdd6e636-1a16-2e4a-90db-ada0fcf0b074.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__082ce770-10a9-7e3b-85f2-bde3c42a92c4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InitialColor Class

---



|  |
| --- |
| [Members](cf1a4db7-c49d-ff7a-b8dd-ddf9a70fb706.htm)   [See Also](#seeAlsoToggle) |

This class is the base class for calculating initial light color.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class InitialColor : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class InitialColor _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class InitialColor : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Lighting InitialColor    
  [Autodesk.Revit.DB.Lighting CustomInitialColor](b08ddf7b-2264-9067-2be7-cfc771872db5.htm)    
  [Autodesk.Revit.DB.Lighting PresetInitialColor](820a579a-c999-f721-0b9c-d98c499c2c1e.htm)

# See Also

[InitialColor Members](cf1a4db7-c49d-ff7a-b8dd-ddf9a70fb706.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__082f904e-47c3-a99d-894a-a87986d42605.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ComboBoxMemberData Constructor

---



|  |
| --- |
| [ComboBoxMemberData Class](aba69b9c-dae6-c872-8dea-91ef7fda5e81.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of ComboBoxMemberData.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ComboBoxMemberData( 	string name, 	string text ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	name As String, _ 	text As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ComboBoxMemberData( 	String^ name,  	String^ text ) ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The internal name of the ComboBoxMember.

text
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The user visible text seen on the item.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when    a null reference (  Nothing  in Visual Basic)  is passed for one or more arguments. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when an empty string is passed for one or more arguments. |

# See Also

[ComboBoxMemberData Class](aba69b9c-dae6-c872-8dea-91ef7fda5e81.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__083c7ab0-9885-cd48-a8c4-3fa40d64c52b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AttachToHanger Method

---



|  |
| --- |
| [FabricationRodInfo Class](b52fe314-2639-a697-cf97-b3e4824818f8.htm)   [See Also](#seeAlsoToggle) |

Attaches the hanger rod to another bearer hanger.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void AttachToHanger( 	ElementId hangerId, 	int rodIndex, 	XYZ position ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AttachToHanger ( _ 	hangerId As ElementId, _ 	rodIndex As Integer, _ 	position As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AttachToHanger( 	ElementId^ hangerId,  	int rodIndex,  	XYZ^ position ) ``` |

#### Parameters

hangerId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of the bearer hanger to which the rod attaches.

rodIndex
:   Type:  System Int32    
     The index of the rod.

position
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The position of the rod end. It should be on bearer centerline.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The hanger is not a bearer hanger. -or- the point is not on hanger bearer centerline. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the index rodIndex is should be in range of rod count. |

# See Also

[FabricationRodInfo Class](b52fe314-2639-a697-cf97-b3e4824818f8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__083c8dcf-61be-2182-90f3-bdcb62c70302.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEmpty Property

---



|  |
| --- |
| [ComponentRepeaterSlot Class](395d3527-1315-038e-8a47-80920f063cc6.htm)   [See Also](#seeAlsoToggle) |

A flag indicating whether the slot is currently empty.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

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

# See Also

[ComponentRepeaterSlot Class](395d3527-1315-038e-8a47-80920f063cc6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__083ebef8-24ba-5485-1ee3-d7e8f94977d8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [OpenOptions Class](c0004971-3810-eeb8-72bd-e116886ec3c8.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [OpenOptions](c0004971-3810-eeb8-72bd-e116886ec3c8.htm)

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

[OpenOptions Class](c0004971-3810-eeb8-72bd-e116886ec3c8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__083f5a56-31c6-e8b7-dc22-cf0f4c25608a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OfPoint Method

---



|  |
| --- |
| [Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)   [See Also](#seeAlsoToggle) |

Applies the transformation to the point and returns the result.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public UV OfPoint( 	UV point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function OfPoint ( _ 	point As UV _ ) As UV ``` |

 

| Visual C++ |
| --- |
| ``` public: UV^ OfPoint( 	UV^ point ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     The point to transform.

#### Return Value

The transformed point.

# Remarks

Transformation of a point is affected by the translational part of the transformation.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__084b59c0-4be0-e552-905d-125a05bb458a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurrentObject Property

---



|  |
| --- |
| [ConduitSizeIterator Class](d7607991-c8de-5ad1-b615-24ec9c30d39d.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` internal Object CurrentObject { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Friend ReadOnly Property CurrentObject As Object 	Get ``` |

 

| Visual C++ |
| --- |
| ``` internal: virtual property Object^ CurrentObject { 	Object^ get () sealed; } ``` |

#### Implements

 [IEnumerator Current](http://msdn2.microsoft.com/en-us/library/khfze649)

# See Also

[ConduitSizeIterator Class](d7607991-c8de-5ad1-b615-24ec9c30d39d.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__084e6fe7-7661-5111-26a0-1313d7442f0d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetInnerRule Method

---



|  |
| --- |
| [FilterInverseRule Class](bd21b884-c026-5a16-4470-72172b71db4a.htm)   [See Also](#seeAlsoToggle) |

Gets the rule being inverted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void SetInnerRule( 	FilterRule innerRule ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetInnerRule ( _ 	innerRule As FilterRule _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetInnerRule( 	FilterRule^ innerRule ) ``` |

#### Parameters

innerRule
:   Type:  [Autodesk.Revit.DB FilterRule](a8f202ca-3c88-ecc4-fa93-549b26a412d7.htm)    
     The rule to invert.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FilterInverseRule Class](bd21b884-c026-5a16-4470-72172b71db4a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__085bed8c-760b-dfad-08f6-28fe0db2a272.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasAssociatedParts Method (Document, ElementId)

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Checks if an element has associated parts.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool HasAssociatedParts( 	Document hostDocument, 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function HasAssociatedParts ( _ 	hostDocument As Document, _ 	elementId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool HasAssociatedParts( 	Document^ hostDocument,  	ElementId^ elementId ) ``` |

#### Parameters

hostDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element to be checked for associated Parts

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

<!-- Start of Syntax__085c3760-17d9-b595-8bd2-b3659902fd01.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPartCustomDataReal Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Get custom data real value for the specified custom data.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public double GetPartCustomDataReal( 	int customId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPartCustomDataReal ( _ 	customId As Integer _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetPartCustomDataReal( 	int customId ) ``` |

#### Parameters

customId
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The identifier of the custom data field to get.

#### Return Value

Returns the real number of the custom data. If the data is not a number it will return 0.0.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The custom data does not exist on the part. |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__086b03c7-6a46-a825-1cae-9739a7819d4f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UngroupMembers Method

---



|  |
| --- |
| [Group Class](ca54af3c-52d8-0aed-cd22-440ec2584b89.htm)   [See Also](#seeAlsoToggle) |

Ungroups the group.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> UngroupMembers() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function UngroupMembers As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ UngroupMembers() ``` |

#### Return Value

If successful, the ids of the members of group are returned.

# Remarks

Removes all the members from the group and deletes the group. Note that the reference to this group object will become invalid once this method is called.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if the group cannot be ungrouped. |

# See Also

[Group Class](ca54af3c-52d8-0aed-cd22-440ec2584b89.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__086c6100-798a-6998-f8e0-fac6d856e6be.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetBendProfile Method

---



|  |
| --- |
| [FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Sets new profile that defines the shape of the Fabric Sheet bending.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void SetBendProfile( 	CurveLoop bendProfile ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetBendProfile ( _ 	bendProfile As CurveLoop _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetBendProfile( 	CurveLoop^ bendProfile ) ``` |

#### Parameters

bendProfile
:   Type:  [Autodesk.Revit.DB CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     A profile that defines the bending shape of the fabric sheet. The profile can be provided without fillets (eg. for L shape, only two lines not two lines and one arc), if so, then fillets (in example one arc) will be automatically generated basing on the Bend Diameter parameter defined in the Fabric Wire system family. If the provided profile has no corners (has a tangent defined at each point except the ends), no fillets will be generated. The provided profile defines the center-curve of a wire.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void ModifyBentFabricSheet(Document document, FabricSheet bentFabricSheet)
{
   CurveLoop newBendingProfile = CurveLoop.CreateViaOffset(bentFabricSheet.GetBendProfile(), 0.5, new XYZ(0, 0, -1));
   bentFabricSheet.SetBendProfile(newBendingProfile);

   // Give the user some information
   TaskDialog.Show("Revit", string.Format("Bent Fabric Sheet ID='{0}' modified successfully.", bentFabricSheet.Id.ToString()));
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub ModifyBentFabricSheet(document As Document, bentFabricSheet As FabricSheet)
    Dim newBendingProfile As CurveLoop = CurveLoop.CreateViaOffset(bentFabricSheet.GetBendProfile(), 0.5, New XYZ(0, 0, -1))
    bentFabricSheet.SetBendProfile(newBendingProfile)

    ' Give the user some information
    TaskDialog.Show("Revit", String.Format("Bent Fabric Sheet ID='{0}' modified successfully.", bentFabricSheet.Id.ToString()))
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the bend profile contains an overlap or intersecting segments. -or- Thrown when the bend profile is empty. -or- Thrown when the bend profile contains an empty loop. -or- Thrown when the bend profile contains multiple loops. -or- Thrown when the bend profile contains a closed loop. -or- Thrown when the bend profile contains two or more arcs that are not separated from one another by a straight segment. -or- Thrown when the bend profile contains too short segments which prevent the fillets from being added. The fillet radius is taken from Bend Diameter parameter defined in the Fabric Wire system family. -or- Thrown when the provided profile cannot be used as a bending shape for this fabric sheet. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidObjectException](8092dec2-113a-0823-1a09-a46c11f99fea.htm) | The data-setting method is not applicable to fabric sheets that are flat. |

# See Also

[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__086fb666-7be0-f093-516e-670b149be97d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetEqualityFormula Method

---



|  |
| --- |
| [DimensionType Class](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.htm)   [See Also](#seeAlsoToggle) |

Gets an ordered list of the entries in the equality formula definition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public IList<DimensionEqualityLabelFormatting> GetEqualityFormula() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetEqualityFormula As IList(Of DimensionEqualityLabelFormatting) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<DimensionEqualityLabelFormatting^>^ GetEqualityFormula() ``` |

#### Return Value

An ordered list of the entries in the equality formula definition.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The given DimensionType cannot be assigned an equality formula as it is not continuous linear or angular. |

# See Also

[DimensionType Class](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__086feb27-8f3d-4fef-993a-d0ea64343ff2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamProfileUsage Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Profile Usage"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FamProfileUsage { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FamProfileUsage As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FamProfileUsage { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__087a7c14-1a6e-7022-c47b-923e90f4c5be.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCloudModelPath Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Gets the cloud model path of the cloud model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019.1

# Syntax

| C# |
| --- |
| ``` public ModelPath GetCloudModelPath() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCloudModelPath As ModelPath ``` |

 

| Visual C++ |
| --- |
| ``` public: ModelPath^ GetCloudModelPath() ``` |

#### Return Value

The cloud model path

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This Document is a not cloud model, cannot execute this operation. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__087c5fa5-6b5d-19a6-e3bb-6ede5e7bbe22.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DeleteWorksetOption Property

---



|  |
| --- |
| [DeleteWorksetSettings Class](1952e14e-42d8-d672-0e72-d5fb1a83b73a.htm)   [See Also](#seeAlsoToggle) |

The current delete workset option.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022.1

# Syntax

| C# |
| --- |
| ``` public DeleteWorksetOption DeleteWorksetOption { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DeleteWorksetOption As DeleteWorksetOption 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property DeleteWorksetOption DeleteWorksetOption { 	DeleteWorksetOption get (); 	void set (DeleteWorksetOption value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[DeleteWorksetSettings Class](1952e14e-42d8-d672-0e72-d5fb1a83b73a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71fe4c5b-2975-6b7f-d945-0ea32275db54.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reset Method

---



|  |
| --- |
| [FilteredElementIterator Class](bb879a42-15eb-1704-7abc-0f4509ca89d2.htm)   [See Also](#seeAlsoToggle) |

Resets the iterator to the beginning.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

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

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The FilteredElementCollector that yielded this iterator has been reset by another operation. No further iteration is permitted with this iterator. |

# See Also

[FilteredElementIterator Class](bb879a42-15eb-1704-7abc-0f4509ca89d2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72a2b8b0-1da8-2726-9da6-c03d76e13288.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AllowCancellation Property

---



|  |
| --- |
| [TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)   [See Also](#seeAlsoToggle) |

Whether the task dialog can be cancelled if no cancel button is specified.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool AllowCancellation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AllowCancellation As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool AllowCancellation { 	bool get (); 	void set (bool value); } ``` |

# Remarks

The default value is true. If there is a cancel button in the task dialog, the it always can be cancelled.

# See Also

[TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__72a66105-55d1-3930-8934-2d46d5dd064d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OfVector Method

---



|  |
| --- |
| [Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)   [See Also](#seeAlsoToggle) |

Applies the transformation to the vector and returns the result.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public UV OfVector( 	UV vector ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function OfVector ( _ 	vector As UV _ ) As UV ``` |

 

| Visual C++ |
| --- |
| ``` public: UV^ OfVector( 	UV^ vector ) ``` |

#### Parameters

vector
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     The vector to transform.

#### Return Value

The transformed vector.

# Remarks

Transformation of a vector is not affected by the translational part of the transformation.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72a77aba-919c-7436-d057-759163d92c35.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InsertFilter Method

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Adds a new filter at the specified position in the list.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void InsertFilter( 	ScheduleFilter filter, 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub InsertFilter ( _ 	filter As ScheduleFilter, _ 	index As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void InsertFilter( 	ScheduleFilter^ filter,  	int index ) ``` |

#### Parameters

filter
:   Type:  [Autodesk.Revit.DB ScheduleFilter](a5dfec9f-1efd-b507-d079-eabcbf5032f8.htm)    
     The filter to add.

index
:   Type:  System Int32    
     The index in the list of filters.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The field ID is not the ID of a field in this ScheduleDefinition. -or- The field and filter type cannot be used to filter this ScheduleDefinition. -or- The filter value is not valid for the field and filter type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | index is not a valid insert position. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This ScheduleDefinition does not support filters. -or- The resulting filter count would be greater than 8. |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72a97f5d-3544-b7fb-8d71-f8d3ee89dc15.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FbxLightPhotometricFile Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Photometric Web File"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FbxLightPhotometricFile { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FbxLightPhotometricFile As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FbxLightPhotometricFile { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72abdaf3-fffd-e658-64ed-3b4fe12c76c5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MepCoolingCoilType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Cooling Coil"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MepCoolingCoilType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MepCoolingCoilType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MepCoolingCoilType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72ac893d-d76a-2606-6bab-3d180b552610.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LinkLoadContent Class

---



|  |
| --- |
| [Members](b1462f47-12b9-9924-c007-31871ebe5a6d.htm)   [See Also](#seeAlsoToggle) |

This class is used by IExternalResourceServers to return Link data to Revit when their LoadResource method is invoked. It also contains additional information used by IExternalResourceUIServers to display link load status results to the user.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class LinkLoadContent : ExternalResourceLoadContent ``` |

 

| Visual Basic |
| --- |
| ``` Public Class LinkLoadContent _ 	Inherits ExternalResourceLoadContent ``` |

 

| Visual C++ |
| --- |
| ``` public ref class LinkLoadContent : public ExternalResourceLoadContent ``` |

# Remarks

This class handles Revit links.

Revit links must be loaded from a path accessible to Revit. Server implementors should provide Revit with a ModelPath representing a location from which to load the link. Revit will handle the actual file loading.

Servers which represent non-local file locations will need to create their own implementation for copying or moving files to a Revit-accessible location.

The link data path used for link loading may be different from the path displayed to the user. The link data path represents the literal location of the file, whereas the link's display path represents what the user sees as the name of the link. See  [!:Autodesk::Revit::DB::ExternalResourceReference::InSessionPath]  for more details on display paths.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ExternalResourceLoadContent](1747ac99-aaa5-70b9-5d1f-89e72539f497.htm)    
  Autodesk.Revit.DB LinkLoadContent

# See Also

[LinkLoadContent Members](b1462f47-12b9-9924-c007-31871ebe5a6d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72ad30b1-8e8d-49f2-6e03-a8132f6f53e6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EndTreatment Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"End Treatment"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId EndTreatment { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property EndTreatment As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ EndTreatment { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72ae5b7f-66b7-e2df-fa64-2e69926ad4d4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OpaqueLuminanceModifier Property

---



|  |
| --- |
| [AdvancedOpaque Class](e8a19a97-fc76-71ad-c713-f2a62415475f.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Luminance Scale" from the "AdvancedOpaque" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string OpaqueLuminanceModifier { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property OpaqueLuminanceModifier As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ OpaqueLuminanceModifier { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDoubleArray4d". This property allows a connected asset.

# See Also

[AdvancedOpaque Class](e8a19a97-fc76-71ad-c713-f2a62415475f.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__72b65231-27d4-79b2-1193-136bab814951.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCouplerId Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Get the id of the Rebar Coupler that is applied to the rebar at the specified end.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public ElementId GetCouplerId( 	int end ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCouplerId ( _ 	end As Integer _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetCouplerId( 	int end ) ``` |

#### Parameters

end
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     0 for the start Rebar Coupler, 1 for the end Rebar Coupler.

#### Return Value

The id of a Rebar Coupler, or invalidElementId if the rebar has no Rebar Coupler at the specified end.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | end must be 0 or 1. |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__72c298ca-57c1-b008-3dcd-21f88eb47ab1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsFailureResolutionPermitted Method (FailureMessageAccessor, FailureResolutionType)

---



|  |
| --- |
| [FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)   [See Also](#seeAlsoToggle) |

Checks if resolution of the failure using given resolution type is permitted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool IsFailureResolutionPermitted( 	FailureMessageAccessor failure, 	FailureResolutionType resolutionType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsFailureResolutionPermitted ( _ 	failure As FailureMessageAccessor, _ 	resolutionType As FailureResolutionType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsFailureResolutionPermitted( 	FailureMessageAccessor^ failure,  	FailureResolutionType resolutionType ) ``` |

#### Parameters

failure
:   Type:  [Autodesk.Revit.DB FailureMessageAccessor](753477d8-b720-97a0-26f5-439d49de418c.htm)    
     Accessor to the failure to be resolved.

resolutionType
:   Type:  [Autodesk.Revit.DB FailureResolutionType](786e6422-f66d-5320-99f9-e530819e50a1.htm)    
     Type of the failure resolution to be used.

#### Return Value

True if resolution of the failure using given resolution type is permitted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | failure has not been properly initialized. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailuresAccessor is inactive (is used outside of failures processing). |

# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)

[IsFailureResolutionPermitted Overload](0f2c43b9-a308-01a3-7407-147e47b1efb3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72c74a9f-1091-5ddb-69d6-93837af6bfee.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DeformationType Property

---



|  |
| --- |
| [RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)   [See Also](#seeAlsoToggle) |

Defines bar deformation type.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public RebarDeformationType DeformationType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DeformationType As RebarDeformationType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property RebarDeformationType DeformationType { 	RebarDeformationType get (); 	void set (RebarDeformationType value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__72cf1870-d3cd-35c7-e9e4-182c88c90c2e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralAttachmentStartValueDistance Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Start Attachment Distance"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralAttachmentStartValueDistance { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralAttachmentStartValueDistance As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralAttachmentStartValueDistance { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72cfbdd1-8109-feef-3e57-2d19211fca2f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BeamVJustification Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"z-Direction Justification"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BeamVJustification { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BeamVJustification As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BeamVJustification { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72d1407d-44a9-70c7-3b16-14efca9fe31a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SubCategoryName Property

---



|  |
| --- |
| [ExportLayerKey Class](64d77004-5c0c-9af2-cae4-39448bbaffe9.htm)   [See Also](#seeAlsoToggle) |

The subcategrory Name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public string SubCategoryName { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SubCategoryName As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ SubCategoryName { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ExportLayerKey Class](64d77004-5c0c-9af2-cae4-39448bbaffe9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72dada0e-854b-c0e4-20d0-eda8827f6b2d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DuplicateFieldRemovedFromKeySchedule Property

---



|  |
| --- |
| [BuiltInFailures ScheduleViewFailures Class](13d33852-f996-21d4-3d9b-f37c90785120.htm)   [See Also](#seeAlsoToggle) |

Duplicate fields across key schedules will be removed after paste.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DuplicateFieldRemovedFromKeySchedule { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DuplicateFieldRemovedFromKeySchedule As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DuplicateFieldRemovedFromKeySchedule { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ScheduleViewFailures Class](13d33852-f996-21d4-3d9b-f37c90785120.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72dd9385-9284-9c79-ac98-bfc2da582a5c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DimensionEqualityLabelFormatting Constructor

---



|  |
| --- |
| [DimensionEqualityLabelFormatting Class](019b51cc-346a-5861-f093-669a7446c874.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a DimensionEqualityLabelFormatting object with specified settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public DimensionEqualityLabelFormatting( 	int leadingSpaces, 	string prefix, 	LabelType labelType, 	string suffix, 	FormatOptions formatOptions ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	leadingSpaces As Integer, _ 	prefix As String, _ 	labelType As LabelType, _ 	suffix As String, _ 	formatOptions As FormatOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: DimensionEqualityLabelFormatting( 	int leadingSpaces,  	String^ prefix,  	LabelType labelType,  	String^ suffix,  	FormatOptions^ formatOptions ) ``` |

#### Parameters

leadingSpaces
:   Type:  System Int32    
     The number of spaces to include before the parameter value.

prefix
:   Type:  System String    
     The prefix to include before the parameter value.

labelType
:   Type:  [Autodesk.Revit.DB LabelType](018ae2fa-99f8-5788-40bb-d6ca5de2681c.htm)    
     The parameter value to be shown.

suffix
:   Type:  System String    
     The suffix to include after the parameter value.

formatOptions
:   Type:  [Autodesk.Revit.DB FormatOptions](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)    
     The format options to use for the parameter value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[DimensionEqualityLabelFormatting Class](019b51cc-346a-5861-f093-669a7446c874.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72dff106-1130-55db-bb3e-bd86143798e1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HotConductorsNumber Property

---



|  |
| --- |
| [ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)   [See Also](#seeAlsoToggle) |

The HotConductors Number of the Electrical System.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public int HotConductorsNumber { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HotConductorsNumber As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int HotConductorsNumber { 	int get (); } ``` |

# Remarks

This property is used to retrieve the HotConductors Number of the Electrical System.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This property only available when System Type is Power! |

# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__72e42fbb-3bd0-305e-23ee-1affe0004731.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AllInvisibleInPlanViewWarn Property

---



|  |
| --- |
| [BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)   [See Also](#seeAlsoToggle) |

None of the created elements are visible in [View Type] View. You may want to check the active view, its Parameters, and Visibility settings, as well as any Plan Regions and their settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId AllInvisibleInPlanViewWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AllInvisibleInPlanViewWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ AllInvisibleInPlanViewWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72ed89c3-546e-c6d8-78ef-95ce7530de98.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShowGridsOnLevel Method

---



|  |
| --- |
| [View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)   [See Also](#seeAlsoToggle) |

This method displays the grid lines in this 3DView on the given Level.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void ShowGridsOnLevel( 	ElementId levelId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ShowGridsOnLevel ( _ 	levelId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ShowGridsOnLevel( 	ElementId^ levelId ) ``` |

#### Parameters

levelId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the Level where grids should be displayed.

# Remarks

Grids will be displayed only if they intersects Level's plane.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72ef1294-fa52-f4e0-6309-7cd24fa5de33.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecPowerFactorState Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Power Factor State"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecPowerFactorState { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecPowerFactorState As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecPowerFactorState { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72ef40eb-20ae-d7ef-0ab5-8c52ddd4b813.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EnergyAnalysisSurface Class

---



|  |
| --- |
| [Members](3604ada3-b09e-c40c-530e-9be4d88cd59e.htm)   [See Also](#seeAlsoToggle) |

Analytical surface. The collection of analytic openings belonging to this analytical parent surface

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class EnergyAnalysisSurface : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class EnergyAnalysisSurface _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class EnergyAnalysisSurface : public Element ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB.Analysis EnergyAnalysisSurface

# See Also

[EnergyAnalysisSurface Members](3604ada3-b09e-c40c-530e-9be4d88cd59e.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__72f56d1c-20b6-871a-11f5-323d7d31bbf4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationPartFitFailure Property

---



|  |
| --- |
| [BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)   [See Also](#seeAlsoToggle) |

Fabrication Part Fitting Failed to Fit

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FabricationPartFitFailure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationPartFitFailure As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FabricationPartFitFailure { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72f90a20-b987-e603-6f1a-2372d580b424.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSpareLoadValue Method

---



|  |
| --- |
| [PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)   [See Also](#seeAlsoToggle) |

Gets the value of the apparent load parameter for a spare

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double GetSpareLoadValue( 	int row, 	int column, 	ElementId idLoadParameter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSpareLoadValue ( _ 	row As Integer, _ 	column As Integer, _ 	idLoadParameter As ElementId _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetSpareLoadValue( 	int row,  	int column,  	ElementId^ idLoadParameter ) ``` |

#### Parameters

row
:   Type:  System Int32    
     A row where the valid spare is

column
:   Type:  System Int32    
     A column where the valid spare is

idLoadParameter
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     One of 4 valid load parameters: RBS\_ELEC\_APPARENT\_LOAD, RBS\_ELEC\_APPARENT\_LOAD\_PHASEA, RBS\_ELEC\_APPARENT\_LOAD\_PHASEB, RBS\_ELEC\_APPARENT\_LOAD\_PHASEC

#### Return Value

The value of the spare's load parameter

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The load parameter id is not valid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | The row column combination does not represent a valid spare. |

# See Also

[PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__72fa88cd-5c96-bab5-e7f7-76ecd42c7e9f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPipeScheduleId Method

---



|  |
| --- |
| [PipeScheduleType Class](d580725f-60f3-034a-e358-d4ed8896d915.htm)   [See Also](#seeAlsoToggle) |

Returns an existing pipe schedule type with the same name.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static ElementId GetPipeScheduleId( 	Document doc, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetPipeScheduleId ( _ 	doc As Document, _ 	name As String _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ GetPipeScheduleId( 	Document^ doc,  	String^ name ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document

name
:   Type:  System String    
     The name of requested schedule type.

#### Return Value

Returns the element id of request schedule type, or invalidElementId if the name is not found.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PipeScheduleType Class](d580725f-60f3-034a-e358-d4ed8896d915.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__72fd8d98-d76a-6eda-b513-c0839457cdec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [DuplicateTypeNamesHandlerArgs Class](939b55de-12e5-2117-5fbc-471f8bb009c9.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [DuplicateTypeNamesHandlerArgs](939b55de-12e5-2117-5fbc-471f8bb009c9.htm)

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

[DuplicateTypeNamesHandlerArgs Class](939b55de-12e5-2117-5fbc-471f8bb009c9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__72fdfc1b-ae4b-1474-1b22-1c050193dc41.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CopyModel Method

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Copies an existing model to a new file. Overwriting a file of the same name is allowed.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void CopyModel( 	ModelPath sourceModelPath, 	string destFilePath, 	bool overwrite ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub CopyModel ( _ 	sourceModelPath As ModelPath, _ 	destFilePath As String, _ 	overwrite As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void CopyModel( 	ModelPath^ sourceModelPath,  	String^ destFilePath,  	bool overwrite ) ``` |

#### Parameters

sourceModelPath
:   Type:  [Autodesk.Revit.DB ModelPath](40a84c72-e4b8-72ac-2f71-3216c66a11b3.htm)    
     The path of the file-based or server-based source model.

destFilePath
:   Type:  System String    
     The path of the destination file.

overwrite
:   Type:  System Boolean    
     True if the destination file can be overwritten; otherwise, false.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given path sourceModelPath is a cloud path which is not supported in this method. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions CentralModelAccessDeniedException](3e38b7b1-1ee8-c7f0-6cdd-bacf67bf61f4.htm) | Access to the central model was denied. A possible reason is because the model was under maintenance. |
| [Autodesk.Revit.Exceptions CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.htm) | The central model is missing. -or- An internal error happened on the central model, please contact the server administrator. |
| [Autodesk.Revit.Exceptions DirectoryNotFoundException](e6614e11-0fd4-df20-0d2d-02722b779128.htm) | Thrown when the directory of destination file doesn't exist. |
| [Autodesk.Revit.Exceptions FileArgumentAlreadyExistsException](bffdd5da-7a0a-2450-efa8-84a1deeebae3.htm) | The destination file exists and can't be overwritten. -or- destFilePath is pointing to a folder that already exists and cannot be deleted. |
| [Autodesk.Revit.Exceptions FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The Revit model specified by sourceModelPath doesn't exist. |
| [Autodesk.Revit.Exceptions InvalidPathArgumentException](3f3c93a6-008b-f9de-40d4-5cd99bb32b34.htm) | The destination file name includes one or more invalid characters. |
| [Autodesk.Revit.Exceptions RevitServerCommunicationException](a0003d89-0113-6623-65da-0db5c568bfb6.htm) | The server-based central model could not be accessed because of a network communication error. |
| [Autodesk.Revit.Exceptions RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.htm) | An internal error happened on the server, please contact the server administrator. |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__72feac6d-3f77-10ea-8ba8-087ab43e76b2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAlmostEqualTo Method (XYZ)

---



|  |
| --- |
| [XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)   [See Also](#seeAlsoToggle) |

Determines whether this vector and the specified vector are the same within the tolerance (1.0e-09).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsAlmostEqualTo( 	XYZ source ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsAlmostEqualTo ( _ 	source As XYZ _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsAlmostEqualTo( 	XYZ^ source ) ``` |

#### Parameters

source
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vector to compare with this vector.

#### Return Value

True if the vectors are the same; otherwise, false.

# Remarks

This routine uses Revit's default tolerance to compare two vectors to see if they are almost equivalent. Because the tolerance is small enough this can also be used to compare two points.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when source is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

[IsAlmostEqualTo Overload](dcad6f16-9898-2f6f-1325-5bae45de241a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73a164cb-516a-947a-7afa-f852f7f57950.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsLossCoefficient Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Loss Coefficient"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsLossCoefficient { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsLossCoefficient As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsLossCoefficient { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73a1847b-6090-cab9-df11-42653f3bf77c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DividedSurfaceFacetNumber Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Facet number"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DividedSurfaceFacetNumber { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DividedSurfaceFacetNumber As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DividedSurfaceFacetNumber { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73a1cbc7-9bf3-cd80-4015-febaa1f4b820.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsCurvetypeDefaultElbowParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Elbow"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsCurvetypeDefaultElbowParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsCurvetypeDefaultElbowParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsCurvetypeDefaultElbowParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73ad46f5-f5cf-44c3-af15-2e4e3e194070.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VertexPositionNormalColored Constructor

---



|  |
| --- |
| [VertexPositionNormalColored Class](aa354e03-2b25-b5a4-5634-c3518518c0d3.htm)   [See Also](#seeAlsoToggle) |

Constructs the vertex from a point, a normal vector, and a color.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public VertexPositionNormalColored( 	XYZ position, 	XYZ normal, 	ColorWithTransparency color ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	position As XYZ, _ 	normal As XYZ, _ 	color As ColorWithTransparency _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: VertexPositionNormalColored( 	XYZ^ position,  	XYZ^ normal,  	ColorWithTransparency^ color ) ``` |

#### Parameters

position
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vertex's position.

normal
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vertex's normal vector.

color
:   Type:  [Autodesk.Revit.DB ColorWithTransparency](b68f80e1-5ea0-a485-ec3e-7dd077043230.htm)    
     The vertex's color.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[VertexPositionNormalColored Class](aa354e03-2b25-b5a4-5634-c3518518c0d3.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__73b449f5-d5b2-bf98-da72-867aa3e69894.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Origin Property

---



|  |
| --- |
| [PipeFittingAndAccessoryData Class](05db3129-7016-4054-1e93-1c718f1ae3bf.htm)   [See Also](#seeAlsoToggle) |

The origin position of the pipe fitting or pipe accessory.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public XYZ Origin { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Origin As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Origin { 	XYZ^ get (); } ``` |

# See Also

[PipeFittingAndAccessoryData Class](05db3129-7016-4054-1e93-1c718f1ae3bf.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__73b54d32-6cf5-fe6c-4b7c-9b5367907b96.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OnLocalLinkSharedCoordinatesSaved Method

---



|  |
| --- |
| [IOnLocalLinkSharedCoordinatesSavedCallback Interface](b6b41945-2aa8-0089-c05b-87aaf3d6fd42.htm)   [See Also](#seeAlsoToggle) |

Revit will call this method whenever shared coordinates changes are saved to a linked document provided by an IExternalResourceServer. This call is a notification to the server provider that one of their Revit or DWG links has changed locally, and they should upload the new version back to their server.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` void OnLocalLinkSharedCoordinatesSaved( 	ExternalResourceReference changedResource ) ``` |

 

| Visual Basic |
| --- |
| ``` Sub OnLocalLinkSharedCoordinatesSaved ( _ 	changedResource As ExternalResourceReference _ ) ``` |

 

| Visual C++ |
| --- |
| ``` void OnLocalLinkSharedCoordinatesSaved( 	ExternalResourceReference^ changedResource ) ``` |

#### Parameters

changedResource
:   Type:  [Autodesk.Revit.DB ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.htm)    
     The ExternalResourceReference whose shared coordinates have been saved.

# See Also

[IOnLocalLinkSharedCoordinatesSavedCallback Interface](b6b41945-2aa8-0089-c05b-87aaf3d6fd42.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73b71ec0-6769-a135-0fa1-f3d35835cda2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FilterToSelect Property

---



|  |
| --- |
| [FilterDialog Class](9d0df7ca-0a3d-12b3-26b7-d28752220f59.htm)   [See Also](#seeAlsoToggle) |

The filter element to be selected once Show is invoked.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public ElementId FilterToSelect { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FilterToSelect As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ FilterToSelect { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

#### Field Value

The default is InvalidElementId, resulting in selecting the first available (if any) FilterElement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The supplied ElementId id is not of a FilterElement. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[FilterDialog Class](9d0df7ca-0a3d-12b3-26b7-d28752220f59.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__73bab121-8422-54f2-91f2-1d6602fc8e3d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadMomentMx1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Mx 1"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LoadMomentMx1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoadMomentMx1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LoadMomentMx1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73bbfcdf-4760-b676-98d7-f54e44912457.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)   [See Also](#seeAlsoToggle) |

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

[ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73c9751f-df8c-04cc-e628-81e582f5c777.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewOpening Method (Element, CurveArray, eRefFace)

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [See Also](#seeAlsoToggle) |

Creates a new opening in a beam, brace and column.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Opening NewOpening( 	Element famInstElement, 	CurveArray profile, 	eRefFace iFace ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewOpening ( _ 	famInstElement As Element, _ 	profile As CurveArray, _ 	iFace As eRefFace _ ) As Opening ``` |

 

| Visual C++ |
| --- |
| ``` public: Opening^ NewOpening( 	Element^ famInstElement,  	CurveArray^ profile,  	eRefFace iFace ) ``` |

#### Parameters

famInstElement
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     host element of the opening, can be a beam, brace and column.

profile
:   Type:  [Autodesk.Revit.DB CurveArray](55103aad-38fd-45d2-6bf7-67a5203e99f3.htm)    
     profile of the opening.

iFace
:   Type:  [Autodesk.Revit.Creation eRefFace](900d9088-2ea5-1953-3b01-0c9cc141825a.htm)    
     face on which opening is based on.

#### Return Value

If successful, an Opening object is returned.

# Remarks

This method forms opening on a beam, brace and column.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the family instance element does not exist in the given document. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[NewOpening Overload](60e2eb94-618e-9f1a-4fbd-ca5dfc394e16.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__73cb3f98-8d3c-938e-e921-70450fae6d0c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CeilingThickness Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Thickness"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CeilingThickness { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CeilingThickness As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CeilingThickness { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73d0c05b-2201-2d6a-f621-3ddd44fec416.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Directcontext3dLoaded Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Loaded"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Directcontext3dLoaded { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Directcontext3dLoaded As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Directcontext3dLoaded { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73d187f1-a65b-88cd-152b-5c378488d5e6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CircularDependencyConstraintError Property

---



|  |
| --- |
| [BuiltInFailures RegenFailures Class](c7726de2-e4f0-8861-8115-0ef9de7935b1.htm)   [See Also](#seeAlsoToggle) |

Highlighted constraints cause a circular chain of references.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CircularDependencyConstraintError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CircularDependencyConstraintError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CircularDependencyConstraintError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RegenFailures Class](c7726de2-e4f0-8861-8115-0ef9de7935b1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73d1e6ac-2349-d36b-dbd6-2b71ed0043b4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointVisibilityParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Visibility/Graphics Overrides"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PointVisibilityParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PointVisibilityParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PointVisibilityParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73d4c2f4-93f9-e3ab-45fe-0319e73dc4fd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NotSupportConcentricBend Property

---



|  |
| --- |
| [BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)   [See Also](#seeAlsoToggle) |

Conduit with Fittings do not support Concentric Bend Radius, the bend radius of the conduit fittings will be same.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NotSupportConcentricBend { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NotSupportConcentricBend As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NotSupportConcentricBend { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73d576ac-386c-e76b-3048-bd29b2010424.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpotLightDistribution Constructor (SpotLightDistribution)

---



|  |
| --- |
| [SpotLightDistribution Class](aaf39909-187f-cc63-fd13-a0d607c382d2.htm)   [See Also](#seeAlsoToggle) |

Creates a copy of the given spotlight distribution

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public SpotLightDistribution( 	SpotLightDistribution other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	other As SpotLightDistribution _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: SpotLightDistribution( 	SpotLightDistribution^ other ) ``` |

#### Parameters

other
:   Type:  [Autodesk.Revit.DB.Lighting SpotLightDistribution](aaf39909-187f-cc63-fd13-a0d607c382d2.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SpotLightDistribution Class](aaf39909-187f-cc63-fd13-a0d607c382d2.htm)

[SpotLightDistribution Overload](38a5dec5-9c39-a486-b94a-2fc57b266ac9.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__73d61523-7280-b04d-480f-9ae04a9373af.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [BRepBuilderPersistentIds Class](c9dd5c21-1d35-9f12-ec28-553e699a6ee2.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [BRepBuilderPersistentIds](c9dd5c21-1d35-9f12-ec28-553e699a6ee2.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

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

 IDisposable Dispose

# See Also

[BRepBuilderPersistentIds Class](c9dd5c21-1d35-9f12-ec28-553e699a6ee2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73d73f0b-de18-e558-96a6-b69eec98a2e7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsRunEndWithRiser Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"End with Riser": End with Riser

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsRunEndWithRiser { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsRunEndWithRiser As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsRunEndWithRiser { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73d870e0-a408-719c-58bd-1fb2ab8f9e5b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InsertableObject Class

---



|  |
| --- |
| [Members](35730b62-7de0-ac82-1db5-8cb92f4efa94.htm)   [See Also](#seeAlsoToggle) |

A base class you all types that are insertable.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class InsertableObject : ElementType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class InsertableObject _ 	Inherits ElementType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class InsertableObject : public ElementType ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  Autodesk.Revit.DB InsertableObject    
  [Autodesk.Revit.DB FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)

# See Also

[InsertableObject Members](35730b62-7de0-ac82-1db5-8cb92f4efa94.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73daf06b-19f2-f414-1da4-8ab0f0e97090.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalThermalResistance Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Thermal Resistance (R)"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnalyticalThermalResistance { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticalThermalResistance As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnalyticalThermalResistance { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73df0a9a-d0d6-33fe-0fd9-ce2c1f77255e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EnableSnaps Property

---



|  |
| --- |
| [ImageInstance Class](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)   [See Also](#seeAlsoToggle) |

When true the ImageInstance will have its snaps enabled, but only if  [CanHaveSnaps](ac6a3521-50ad-3573-11b1-d29038730dae.htm)  is true

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public bool EnableSnaps { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property EnableSnaps As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool EnableSnaps { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The image does not have snaps |

# See Also

[ImageInstance Class](ff77d6c8-a94a-067a-cd95-4f2cd3ec8dcc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73dfc3b1-7e48-d825-6675-9d6f64cbd2f4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SlantedColumnTopCutStyle Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top Cut Style"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SlantedColumnTopCutStyle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SlantedColumnTopCutStyle As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SlantedColumnTopCutStyle { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73e42274-0b32-4109-db26-7c980504264d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAssociatedParts Method (Document, ElementId, Boolean, Boolean)

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Returns all Parts that are associated with the given element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetAssociatedParts( 	Document hostDocument, 	ElementId elementId, 	bool includePartsWithAssociatedParts, 	bool includeAllChildren ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetAssociatedParts ( _ 	hostDocument As Document, _ 	elementId As ElementId, _ 	includePartsWithAssociatedParts As Boolean, _ 	includeAllChildren As Boolean _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetAssociatedParts( 	Document^ hostDocument,  	ElementId^ elementId,  	bool includePartsWithAssociatedParts,  	bool includeAllChildren ) ``` |

#### Parameters

hostDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document of the element.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element to be checked for associated Parts.

includePartsWithAssociatedParts
:   Type:  System Boolean    
     If true, include parts that have associated parts.

includeAllChildren
:   Type:  System Boolean    
     If true, return all associated Parts recursively for all children. If false, only return immediate children.

#### Return Value

Parts that are associated to the element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[GetAssociatedParts Overload](6b2d5339-1140-72c4-3535-bfe452e55506.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73e4424f-62d5-9a03-d400-5d5b525f0b8b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsConduitDiameterParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Diameter(Trade Size)"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsConduitDiameterParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsConduitDiameterParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsConduitDiameterParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73e50d33-1d8c-7181-8220-404a077b4dec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [PlanTopologySet Class](37cd93b8-bed4-0000-a389-48d5305d908e.htm)   [See Also](#seeAlsoToggle) |

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

[PlanTopologySet Class](37cd93b8-bed4-0000-a389-48d5305d908e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73e56449-890f-e446-9190-6e787f928886.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLength Method

---



|  |
| --- |
| [XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)   [See Also](#seeAlsoToggle) |

Gets the length of this vector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double GetLength() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLength As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetLength() ``` |

# Remarks

In 3-D Euclidean space, the length of the vector is the square root of the sum of the three coordinates squared.

# See Also

[XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73e92b11-d12b-4806-cba4-493e2af7cb84.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalysisDisplayDiagramSettings Constructor (AnalysisDisplayDiagramSettings)

---



|  |
| --- |
| [AnalysisDisplayDiagramSettings Class](57e0c5ff-555c-7345-ac24-3592207a4d70.htm)   [See Also](#seeAlsoToggle) |

Constructs a new copy of the input AnalysisDisplayDiagramSettings object.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public AnalysisDisplayDiagramSettings( 	AnalysisDisplayDiagramSettings other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	other As AnalysisDisplayDiagramSettings _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: AnalysisDisplayDiagramSettings( 	AnalysisDisplayDiagramSettings^ other ) ``` |

#### Parameters

other
:   Type:  [Autodesk.Revit.DB.Analysis AnalysisDisplayDiagramSettings](57e0c5ff-555c-7345-ac24-3592207a4d70.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AnalysisDisplayDiagramSettings Class](57e0c5ff-555c-7345-ac24-3592207a4d70.htm)

[AnalysisDisplayDiagramSettings Overload](3ebc2c54-a595-90aa-0d4b-d7cef773fc6f.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__73eb12c2-04a6-a91d-20f0-a1586f56782a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DWGExportOptions Constructor (DWGExportOptions)

---



|  |
| --- |
| [DWGExportOptions Class](3e510f02-1a4c-3e4f-f923-e96972d03862.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of DWGExportOptions as a copy of the export options.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public DWGExportOptions( 	DWGExportOptions option ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	option As DWGExportOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: DWGExportOptions( 	DWGExportOptions^ option ) ``` |

#### Parameters

option
:   Type:  [Autodesk.Revit.DB DWGExportOptions](3e510f02-1a4c-3e4f-f923-e96972d03862.htm)    
     The options to be copied.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DWGExportOptions Class](3e510f02-1a4c-3e4f-f923-e96972d03862.htm)

[DWGExportOptions Overload](fed934a6-3769-7d07-15bc-099b4b551461.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73ec2f54-3aaa-07a8-7779-35b23781d904.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reference Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Reference"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Reference { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Reference As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Reference { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73ec75cc-ece0-ff16-6499-2878d17801f8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WattsPerSquareMeter Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Watts per square meter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId WattsPerSquareMeter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WattsPerSquareMeter As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ WattsPerSquareMeter { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73ec79a7-417e-4086-15ef-c3ea7613bb7b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CouplerCoupledEngagement Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bar Engagement 2"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CouplerCoupledEngagement { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CouplerCoupledEngagement As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CouplerCoupledEngagement { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73f257dc-72c4-a654-30bc-af124906d05a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallTypeIncompatibleWithTapered Property

---



|  |
| --- |
| [BuiltInFailures WallFailures Class](22d82d7e-a7d6-c096-991c-728df0b2d61c.htm)   [See Also](#seeAlsoToggle) |

This wall's type is not compatible with the Tapered cross-section. Tapered walls require a variable thickness layer.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId WallTypeIncompatibleWithTapered { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WallTypeIncompatibleWithTapered As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ WallTypeIncompatibleWithTapered { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures WallFailures Class](22d82d7e-a7d6-c096-991c-728df0b2d61c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73f60bde-33db-d258-4f9c-c9a2848eaa37.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumberSystemReferenceOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Offset from Reference"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId NumberSystemReferenceOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NumberSystemReferenceOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ NumberSystemReferenceOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__73f8ee06-a9c1-a869-fcd0-6e1de91eacc9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HookLength0 Property

---



|  |
| --- |
| [RebarBendData Class](027b5619-ad82-74b3-1d78-efe86a1ef96b.htm)   [See Also](#seeAlsoToggle) |

The extension length of the hook at the start.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double HookLength0 { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property HookLength0 As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double HookLength0 { 	double get (); 	void set (double value); } ``` |

# See Also

[RebarBendData Class](027b5619-ad82-74b3-1d78-efe86a1ef96b.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__73feeafa-ff8e-653e-faab-9441738c3cb4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundaryDirectionZ Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Z Translation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BoundaryDirectionZ { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BoundaryDirectionZ As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BoundaryDirectionZ { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74a79a79-cfcc-c001-4554-59691beb69cc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LeaderRightAttachment Property

---



|  |
| --- |
| [TextNote Class](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)   [See Also](#seeAlsoToggle) |

Attachment position of leaders on the right side of the text note.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public LeaderAtachement LeaderRightAttachment { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LeaderRightAttachment As LeaderAtachement 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property LeaderAtachement LeaderRightAttachment { 	LeaderAtachement get (); 	void set (LeaderAtachement value); } ``` |

# Remarks

The property controls the vertical position of leaders attached to the right side of the note.

Change of the value will affect all leaders currently attached to the right side.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[TextNote Class](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74aa151d-25ba-3449-25fa-34e39b58358e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SlantedColumnBaseCutStyle Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Base Cut Style"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SlantedColumnBaseCutStyle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SlantedColumnBaseCutStyle As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SlantedColumnBaseCutStyle { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74b144b8-0906-bba0-0bac-30d058481422.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLayerSelection Method

---



|  |
| --- |
| [BaseImportOptions Class](75898e94-cff4-fb64-c613-9596599444c4.htm)   [See Also](#seeAlsoToggle) |

Get all set layers name which user want to import into Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ICollection<string> GetLayerSelection() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLayerSelection As ICollection(Of String) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<String^>^ GetLayerSelection() ``` |

#### Return Value

The layers' name.

# See Also

[BaseImportOptions Class](75898e94-cff4-fb64-c613-9596599444c4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74b280e6-bccb-703b-e63d-341bc64ed729.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddOption Method

---



|  |
| --- |
| [IFCExportOptions Class](db8ed2bb-8949-7a7f-e09a-29f6c9916f42.htm)   [See Also](#seeAlsoToggle) |

Adds a new named option to the options structure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void AddOption( 	string name, 	string value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddOption ( _ 	name As String, _ 	value As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddOption( 	String^ name,  	String^ value ) ``` |

#### Parameters

name
:   Type:  System String    
     The option name.

value
:   Type:  System String    
     The option value.

# Remarks

Named options can be used to set options not accessible through the standard IFC export user interface. It is up to the implementation of the IExporterIFC interface to customize export behavior based on these options.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCExportOptions Class](db8ed2bb-8949-7a7f-e09a-29f6c9916f42.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74b36104-2aec-565b-d4a5-f1887ea8f005.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsSection Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Section"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsSection { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsSection As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsSection { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74be020b-ad05-834c-71ba-8dcd7cf6ae37.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EnergyModelType Property

---



|  |
| --- |
| [EnergyAnalysisDetailModelOptions Class](18297392-d94a-cdab-feb3-81482771c44d.htm)   [See Also](#seeAlsoToggle) |

It indicates whether the energy model is based on rooms/spaces or building elements.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public EnergyModelType EnergyModelType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property EnergyModelType As EnergyModelType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property EnergyModelType EnergyModelType { 	EnergyModelType get (); 	void set (EnergyModelType value); } ``` |

# Remarks

The default value is EnergyModelType::SpatialElement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[EnergyAnalysisDetailModelOptions Class](18297392-d94a-cdab-feb3-81482771c44d.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__74be3d37-1531-4986-ac1b-ece7c0068e34.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetEnumerator Method

---



|  |
| --- |
| [ReferencePointArray Class](4780adea-9e68-b0b4-09c7-68f7752dd650.htm)   [See Also](#seeAlsoToggle) |

Retrieve a forward moving iterator to the array.

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

Returns a forward moving iterator to the array.

#### Implements

 [IEnumerable GetEnumerator](http://msdn2.microsoft.com/en-us/library/5zae5365)

# See Also

[ReferencePointArray Class](4780adea-9e68-b0b4-09c7-68f7752dd650.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74be759c-3b7a-04f5-3d7a-4f524613ae92.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WattsPerSquareMeterKelvin Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Watts per square meter kelvin.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId WattsPerSquareMeterKelvin { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WattsPerSquareMeterKelvin As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ WattsPerSquareMeterKelvin { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74c136a2-5b05-9eab-4df5-fc1c0930b21b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetObjectData Method

---



|  |
| --- |
| [AutoJoinFailedException Class](666f8a45-18c9-0a1f-1a3f-eaa0ac96f23f.htm)   [See Also](#seeAlsoToggle) |

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

[AutoJoinFailedException Class](666f8a45-18c9-0a1f-1a3f-eaa0ac96f23f.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__74c37398-abb6-e955-8325-41ae9ce34ffc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralBeamEnd1Elevation Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"End Level Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralBeamEnd1Elevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralBeamEnd1Elevation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralBeamEnd1Elevation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74c90acb-a638-f840-afbe-d3cf5f78bf23.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsServiceAvailable Method

---



|  |
| --- |
| [ShapeImporter Class](d6120e08-f260-577d-b6cf-3fe5b042a54e.htm)   [See Also](#seeAlsoToggle) |

Checks whether the data conversion service is available.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static bool IsServiceAvailable() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsServiceAvailable As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsServiceAvailable() ``` |

#### Return Value

True if the data conversion service is available, false otherwise.

# Remarks

ShapeImporter relies on optional data conversion functionality. This function checks whether it is available.

# See Also

[ShapeImporter Class](d6120e08-f260-577d-b6cf-3fe5b042a54e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74cb7799-030d-aa76-0009-f2ac59aee9a8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFaceOffset Method

---



|  |
| --- |
| [FreeFormElement Class](27b9411a-d368-1541-b7db-b5157a58c581.htm)   [See Also](#seeAlsoToggle) |

Offsets a planar face of the free form element a certain distance in the normal direction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetFaceOffset( 	Face face, 	double offset ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFaceOffset ( _ 	face As Face, _ 	offset As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFaceOffset( 	Face^ face,  	double offset ) ``` |

#### Parameters

face
:   Type:  [Autodesk.Revit.DB Face](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)    
     The face to offset.

offset
:   Type:  System Double    
     The magnitude of the offset. A positive value offsets out of the input solid. A negative value offsets into the solid shape.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | face does not belong to the solid. -or- The face to be offset should be planar and satisfy constraints of its parent element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FreeFormElement Class](27b9411a-d368-1541-b7db-b5157a58c581.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74cdd110-13db-3ae0-1f66-5ab208f3ea7c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Position Property

---



|  |
| --- |
| [VertexPosition Class](718e49aa-9e17-6f2d-2013-141b5cfeefdd.htm)   [See Also](#seeAlsoToggle) |

The vertex's position.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public XYZ Position { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Position As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Position { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[VertexPosition Class](718e49aa-9e17-6f2d-2013-141b5cfeefdd.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__74cff3fa-9380-2c30-9fa9-b0e839a2c8e4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TransactionGroup Constructor (Document)

---



|  |
| --- |
| [TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)   [See Also](#seeAlsoToggle) |

Constructs a transaction group object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public TransactionGroup( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	document As Document _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: TransactionGroup( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document for which this transaction group is being used.

# Remarks

The group does not start until its Start method is called.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)

[TransactionGroup Overload](34d0ec0c-037e-3604-2ec4-845e80237192.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74d01c4a-9032-e740-2338-e9a8ec6711d5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionShape Property

---



|  |
| --- |
| [AnalyticalMember Class](57c87ac5-a82e-5c7e-2f06-6dbf1f697566.htm)   [See Also](#seeAlsoToggle) |

The structural section shape of the Analytical Member.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public StructuralSectionShape StructuralSectionShape { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property StructuralSectionShape As StructuralSectionShape 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property StructuralSectionShape StructuralSectionShape { 	StructuralSectionShape get (); } ``` |

# See Also

[AnalyticalMember Class](57c87ac5-a82e-5c7e-2f06-6dbf1f697566.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__74d89f8a-88bd-a68b-b0ec-b1e5de920eb2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetAdditionalReferencesToDimension Method

---



|  |
| --- |
| [MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)   [See Also](#seeAlsoToggle) |

Sets the additional references which the dimension will witness.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public void SetAdditionalReferencesToDimension( 	IList<Reference> referencesToDimension ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetAdditionalReferencesToDimension ( _ 	referencesToDimension As IList(Of Reference) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetAdditionalReferencesToDimension( 	IList<Reference^>^ referencesToDimension ) ``` |

#### Parameters

referencesToDimension
:   Type:  System.Collections.Generic IList   [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The additional references which the dimension will witness.

# Remarks

The additional references to dimension cannot come from the same category as the MultiReferenceAnnotationType's reference category.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Some references come from elements which directly match the reference category required by the MultiReferenceAnnotationType. For those elements please use SetElementsToDimension. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74dc90bb-9ef9-eacd-5589-c9adf5e3ad54.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OwnerId Property

---



|  |
| --- |
| [AnalyticalLink Class](b552fb54-8dff-6690-e16e-cc46cbc46d6b.htm)   [See Also](#seeAlsoToggle) |

ElementId of Analytical Element which created the AnalyticalLink (if any) invalidElementId if this Analytical Link was created by the User or API

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId OwnerId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property OwnerId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ OwnerId { 	ElementId^ get (); } ``` |

# See Also

[AnalyticalLink Class](b552fb54-8dff-6690-e16e-cc46cbc46d6b.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__74ddc2d9-4fd7-71e9-ace7-d17e0b5f58f2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SymbolicCurveArray Constructor

---



|  |
| --- |
| [SymbolicCurveArray Class](a8ca9e0e-9838-96e4-5e6b-d5ffc11ea968.htm)   [See Also](#seeAlsoToggle) |

Initializes a new instance of the  [SymbolicCurveArray](a8ca9e0e-9838-96e4-5e6b-d5ffc11ea968.htm)  class

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public SymbolicCurveArray() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: SymbolicCurveArray() ``` |

# See Also

[SymbolicCurveArray Class](a8ca9e0e-9838-96e4-5e6b-d5ffc11ea968.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74e09dc3-6b9a-cc3b-a493-d6a20a60bfd6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### gbXMLBuildingType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Enumerations for gbXML (Green Building XML) format, used for energy analysis, schema version 0.34.

This enumeration corresponds to the buildingType attribute in gbXML and is used to specify the most predominant building use type.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public enum gbXMLBuildingType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration gbXMLBuildingType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class gbXMLBuildingType ``` |

# Members

| Member name | Description |
| --- | --- |
| CustomizeBuildingType |  |
| NoBuildingType |  |
| AutomotiveFacility |  |
| ConventionCenter |  |
| Courthouse |  |
| DiningBarLoungeOrLeisure |  |
| DiningCafeteriaFastFood |  |
| DiningFamily |  |
| Dormitory |  |
| ExerciseCenter |  |
| FireStation |  |
| Gymnasium |  |
| HospitalOrHealthcare |  |
| Hotel |  |
| Library |  |
| Manufacturing |  |
| Motel |  |
| MotionPictureTheatre |  |
| MultiFamily |  |
| Museum |  |
| Office |  |
| ParkingGarage |  |
| Penitentiary |  |
| PerformingArtsTheater |  |
| PoliceStation |  |
| PostOffice |  |
| ReligiousBuilding |  |
| Retail |  |
| SchoolOrUniversity |  |
| SingleFamily |  |
| SportsArena |  |
| TownHall |  |
| Transportation |  |
| Warehouse |  |
| Workshop |  |
| NoOfBuildingTypes |  |

# See Also

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__74e169cb-cacb-62be-b29e-c9f7867939a5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Acceleration Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Acceleration, in discipline Structural.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Acceleration { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Acceleration As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Acceleration { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74e61398-d5d5-18d5-9481-e3ca301547fd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Jitter Property

---



|  |
| --- |
| [ViewDisplaySketchyLines Class](c92b463b-1b59-695d-f06b-a76dacfaf2f0.htm)   [See Also](#seeAlsoToggle) |

The jitter defines jitteriness of the line. Values between 0 and 10.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public int Jitter { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Jitter As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int Jitter { 	int get (); 	void set (int value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The jitter value is not valid. The valid range is 0 to 10. |

# See Also

[ViewDisplaySketchyLines Class](c92b463b-1b59-695d-f06b-a76dacfaf2f0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74e725cd-a74e-5ac6-d01e-0d1022208eb1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFormatOptions Method

---



|  |
| --- |
| [ColorFillScheme Class](c405eb5b-14fa-0fea-a750-dcd9925a90b0.htm)   [See Also](#seeAlsoToggle) |

Returns the FormatOptions of the scheme.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public FormatOptions GetFormatOptions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFormatOptions As FormatOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: FormatOptions^ GetFormatOptions() ``` |

# Remarks

This method will return the default FormatOptions if the scheme is by value.

# See Also

[ColorFillScheme Class](c405eb5b-14fa-0fea-a750-dcd9925a90b0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74ebe136-7b78-b967-fc75-d1d8a9dd4deb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCFatalExportError Property

---



|  |
| --- |
| [BuiltInFailures ExportFailures Class](19402678-01cb-797a-d499-ce5dfef1a47b.htm)   [See Also](#seeAlsoToggle) |

There has been an unrecoverable error during export. Export will now be aborted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId IFCFatalExportError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property IFCFatalExportError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ IFCFatalExportError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ExportFailures Class](19402678-01cb-797a-d499-ce5dfef1a47b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74f0507d-932c-4449-94a1-19fc10006e3a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecMaxPoleBreakers Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Max Number of Single Pole Breakers"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecMaxPoleBreakers { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecMaxPoleBreakers As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecMaxPoleBreakers { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74f08994-5ee8-a7a5-a1e1-6632f1176b06.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDefault Property

---



|  |
| --- |
| [ComponentRepeaterSlot Class](395d3527-1315-038e-8a47-80920f063cc6.htm)   [See Also](#seeAlsoToggle) |

A flag indicating whether the slot currently holds an instance of the default family type of the component repeater.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsDefault { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsDefault As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsDefault { 	bool get (); } ``` |

# See Also

[ComponentRepeaterSlot Class](395d3527-1315-038e-8a47-80920f063cc6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74f1b375-2d5e-9d51-2d84-6f8c46c6880f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FtSup3PerMin Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol ftÂ³/min, indicating unit Cubic feet per minute.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FtSup3PerMin { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FtSup3PerMin As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FtSup3PerMin { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74f1e361-be78-c1ca-2b66-8df934fd33d3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralStartReleaseMy Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Start My"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralStartReleaseMy { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralStartReleaseMy As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralStartReleaseMy { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74f22437-bc58-12ba-cc8c-82d849a7c577.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCreateStringers Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Can't create stringers geometry.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCreateStringers { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCreateStringers As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCreateStringers { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74f3a986-a399-97ec-6068-df8e37a0fe67.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LayoutRuleFixedNumber Constructor

---



|  |
| --- |
| [LayoutRuleFixedNumber Class](5a2f6d39-0919-d5be-d146-bb985a4ab851.htm)   [See Also](#seeAlsoToggle) |

Constructor of LayoutRuleFixedNumber.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public LayoutRuleFixedNumber( 	int numberOfLines ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	numberOfLines As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: LayoutRuleFixedNumber( 	int numberOfLines ) ``` |

#### Parameters

numberOfLines
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The value of numberOfLines must be positive.

# Remarks

Create a LayoutRuleFixedNumber object with the number of the beams and this number must be positive.

# See Also

[LayoutRuleFixedNumber Class](5a2f6d39-0919-d5be-d146-bb985a4ab851.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74f51f30-242d-3254-923e-e9ca26cf9cea.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectorProfileType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Shape"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ConnectorProfileType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ConnectorProfileType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ConnectorProfileType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74f7386b-347f-2ac6-f236-cd079a64c0e4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GradientNoiseLow Property

---



|  |
| --- |
| [Gradient Class](2b517b49-c915-74a9-bb6f-2a233d6706be.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Low" from the "Gradient" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string GradientNoiseLow { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GradientNoiseLow As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ GradientNoiseLow { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble" within the range of "0, 1".

# See Also

[Gradient Class](2b517b49-c915-74a9-bb6f-2a233d6706be.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__74fd2288-34d7-3e1c-a919-2907c7c7826a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionLangleBoltDiameterShorterFlange Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bolt Diameter Shorter Flange"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralSectionLangleBoltDiameterShorterFlange { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralSectionLangleBoltDiameterShorterFlange As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralSectionLangleBoltDiameterShorterFlange { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74fd98e3-daac-ca79-ab60-df34473077b8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Item Property

---



|  |
| --- |
| [Definitions Class](5ff217ff-215d-9d1a-6555-3f45b34a5517.htm)   [See Also](#seeAlsoToggle) |

Retrieves a definition by a given name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Definition this[ 	string name ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Item ( _ 	name As String _ ) As Definition 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Definition^ Item[String^ name] { 	Definition^ get (String^ name); } ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The name of the parameter definition for which to search.

# Remarks

If the definition is not found then    a null reference (  Nothing  in Visual Basic)  will be returned.

# See Also

[Definitions Class](5ff217ff-215d-9d1a-6555-3f45b34a5517.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__74fd9e8e-1178-e153-02c7-0703c2703191.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsStructureEnabled Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Checks whether or not the structure discipline is enabled, and enable or disable it.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsStructureEnabled { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsStructureEnabled As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsStructureEnabled { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The current product type is not ProductType.Revit and discipline controls are not enabled. |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__75a0b4b5-8472-46f8-28e2-010db022257e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SystemsAnalysisReport Property

---



|  |
| --- |
| [ExternalResourceTypes BuiltInExternalResourceTypes Class](3f1b13ff-0488-0a46-b646-21c2e29398e7.htm)   [See Also](#seeAlsoToggle) |

An external resource type representing systems analysis report path.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ExternalResourceType SystemsAnalysisReport { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SystemsAnalysisReport As ExternalResourceType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ExternalResourceType^ SystemsAnalysisReport { 	ExternalResourceType^ get (); } ``` |

# See Also

[ExternalResourceTypes BuiltInExternalResourceTypes Class](3f1b13ff-0488-0a46-b646-21c2e29398e7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75a20905-c88b-df7e-1adc-d6beb096bec9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, String)

---



|  |
| --- |
| [EndTreatmentType Class](107f2dd4-7a92-e67e-0b79-a1c8c87dbf35.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new EndTreatmentType in a document and adds the input string to the endTreatment parameter.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static EndTreatmentType Create( 	Document doc, 	string strTreatment ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	doc As Document, _ 	strTreatment As String _ ) As EndTreatmentType ``` |

 

| Visual C++ |
| --- |
| ``` public: static EndTreatmentType^ Create( 	Document^ doc,  	String^ strTreatment ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

strTreatment
:   Type:  System String

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void NewEndTreatmentForCouplerType(Document doc, ElementId couplerTypeId)
{
    EndTreatmentType treatmentType = EndTreatmentType.Create(doc, "Custom");
    FamilySymbol couplerType = doc.GetElement(couplerTypeId) as FamilySymbol;
    Parameter param = couplerType.get_Parameter(BuiltInParameter.COUPLER_MAIN_ENDTREATMENT);
    param.Set(treatmentType.Id);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub NewEndTreatmentForCouplerType(doc As Document, couplerTypeId As ElementId)
    Dim treatmentType As EndTreatmentType = EndTreatmentType.Create(doc, "Custom")
    Dim couplerType As FamilySymbol = TryCast(doc.GetElement(couplerTypeId), FamilySymbol)
    Dim param As Parameter = couplerType.Parameter(BuiltInParameter.COUPLER_MAIN_ENDTREATMENT)
    param.[Set](treatmentType.Id)
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[EndTreatmentType Class](107f2dd4-7a92-e67e-0b79-a1c8c87dbf35.htm)

[Create Overload](bfa0b5ed-b4e3-dcba-67f9-7ea73bf408b2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__75a398d8-700a-317e-9417-e7cd7c73022b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InstanceMoveBaseWithGrids Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Move Base With Grids"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId InstanceMoveBaseWithGrids { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InstanceMoveBaseWithGrids As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ InstanceMoveBaseWithGrids { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75aa8f4d-b301-6d8d-9cf2-ca3718e7346d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsEnergyAnalysisBuildingEnvelopeAnalyticalSpaceIdentificationResolution Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Analytical Space Resolution"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsEnergyAnalysisBuildingEnvelopeAnalyticalSpaceIdentificationResolution { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsEnergyAnalysisBuildingEnvelopeAnalyticalSpaceIdentificationResolution As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsEnergyAnalysisBuildingEnvelopeAnalyticalSpaceIdentificationResolution { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75acb45f-3855-9a37-84ac-3f9b3e37fd23.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### STLExportResolution Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing possible options to control the tessellation quality.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021.1   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` [ObsoleteAttribute("This enum is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'ExportResolution' enum instead.")] public enum STLExportResolution ``` |

 

| Visual Basic |
| --- |
| ``` <ObsoleteAttribute("This enum is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'ExportResolution' enum instead.")> _ Public Enumeration STLExportResolution ``` |

 

| Visual C++ |
| --- |
| ``` [ObsoleteAttribute(L"This enum is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'ExportResolution' enum instead.")] public enum class STLExportResolution ``` |

# Members

| Member name | Description |
| --- | --- |
| Custom | STL exporting with custom resolution (all possible STL tessellation parameters have default values). |
| Fine | STL exporting with fine resolution. |
| Medium | STL exporting with medium resolution. |
| Coarse | STL exporting with coarse resolution. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75ae60e9-2efa-3103-0ad4-100841a7e13f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CitySetIterator Constructor

---



|  |
| --- |
| [CitySetIterator Class](fe078250-71c4-6a19-ac0d-6d674b86fac9.htm)   [See Also](#seeAlsoToggle) |

For Internal Use Only.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public CitySetIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: CitySetIterator() ``` |

# Remarks

This constructor is exposed to enable support for COM interop only. This object should never be created by the developer.

# See Also

[CitySetIterator Class](fe078250-71c4-6a19-ac0d-6d674b86fac9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75b056bc-5893-d9a8-0fc5-89c52d79cfab.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VertexPositionColored Constructor

---



|  |
| --- |
| [VertexPositionColored Class](f99deacd-3167-46ff-6abf-5d27bdbd2c6a.htm)   [See Also](#seeAlsoToggle) |

Constructs the vertex from a point and a color.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public VertexPositionColored( 	XYZ position, 	ColorWithTransparency color ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	position As XYZ, _ 	color As ColorWithTransparency _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: VertexPositionColored( 	XYZ^ position,  	ColorWithTransparency^ color ) ``` |

#### Parameters

position
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vertex's position.

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

<!-- Start of Syntax__75b8966b-3ec3-50cb-8b58-8f79b770490f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaxNumberOfCircuits Property

---



|  |
| --- |
| [ElectricalEquipment Class](a93a0589-784b-27a3-c7d0-1122921a7a23.htm)   [See Also](#seeAlsoToggle) |

The maximum number of circuits for switchboard. The quantity of circuits can be assigned to switchboard through breaker.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public int MaxNumberOfCircuits { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MaxNumberOfCircuits As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int MaxNumberOfCircuits { 	int get (); 	void set (int value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The input max number of circuits value is invalid for switchboard. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The electrical equipment is not a switchboard equipment. |

# See Also

[ElectricalEquipment Class](a93a0589-784b-27a3-c7d0-1122921a7a23.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__75b9525d-3b8d-70d8-55de-a193b9eb5e76.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCTransformSetter Class

---



|  |
| --- |
| [Members](b0df91b3-d049-1988-7023-bd3121923fc6.htm)   [See Also](#seeAlsoToggle) |

A state-based class that forces an extra transformation applied to objects being exported.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class IFCTransformSetter : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class IFCTransformSetter _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class IFCTransformSetter : IDisposable ``` |

# Remarks

IFC has a system of local placements; these are created from a set of transforms in Revit. Sometimes there is a need to create a 'fake' transform to get the right local placement structure for IFC. This class is intended to maintain the transformation for the duration that it is needed. To ensure that the lifetime of the object is correctly managed, you should declare an instance of this class as a part of a 'using' statement in C# or similar construct in other lanuguages.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.IFC IFCTransformSetter

# See Also

[IFCTransformSetter Members](b0df91b3-d049-1988-7023-bd3121923fc6.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__75b99645-4c94-e9ac-9b2b-2017a5b8ce8a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsConnectedTo Method

---



|  |
| --- |
| [Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)   [See Also](#seeAlsoToggle) |

Identifies if the connector is connected to the specified connector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsConnectedTo( 	Connector connector ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsConnectedTo ( _ 	connector As Connector _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsConnectedTo( 	Connector^ connector ) ``` |

#### Parameters

connector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the argument is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75b9e44c-cea1-6726-adc5-cd9880261c39.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WorksetJoinWarn Property

---



|  |
| --- |
| [BuiltInFailures AutoJoinFailures Class](4a5aa425-e362-bf95-a1a0-2b4e41236917.htm)   [See Also](#seeAlsoToggle) |

Two elements were not automatically joined because one or both is not editable.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId WorksetJoinWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WorksetJoinWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ WorksetJoinWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AutoJoinFailures Class](4a5aa425-e362-bf95-a1a0-2b4e41236917.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75ba21e6-72ec-de95-5e45-8d20630260e3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanHaveStructuralSection Method

---



|  |
| --- |
| [Family Class](f51d019d-6ff3-692b-d1d2-b497cab564de.htm)   [See Also](#seeAlsoToggle) |

Identifies if this Family can have a structural section.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool CanHaveStructuralSection() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanHaveStructuralSection As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanHaveStructuralSection() ``` |

#### Return Value

True if the Family can have structural section, false otherwise.

# See Also

[Family Class](f51d019d-6ff3-692b-d1d2-b497cab564de.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75c08530-6404-75e6-eb36-729bd01fadf5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DefaultConstructionMassShade Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Mass Shade"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DefaultConstructionMassShade { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DefaultConstructionMassShade As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DefaultConstructionMassShade { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75c2437e-b583-0a0f-d79b-17116d581861.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CommonTintToggle Property

---



|  |
| --- |
| [Metal Class](618a6255-d79c-e405-6804-994c56317dc4.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Tint" from the "Metal" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string CommonTintToggle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CommonTintToggle As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ CommonTintToggle { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyBoolean".

# See Also

[Metal Class](618a6255-d79c-e405-6804-994c56317dc4.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__75c39be6-5f78-9dd2-061e-13b846e739d5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsBubbleVisibleInView Method

---



|  |
| --- |
| [DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)   [See Also](#seeAlsoToggle) |

Identifies if the bubble is visible or not in a view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool IsBubbleVisibleInView( 	DatumEnds datumEnd, 	View view ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsBubbleVisibleInView ( _ 	datumEnd As DatumEnds, _ 	view As View _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsBubbleVisibleInView( 	DatumEnds datumEnd,  	View^ view ) ``` |

#### Parameters

datumEnd
:   Type:  [Autodesk.Revit.DB DatumEnds](60cdd5d4-8c6c-320b-7b8b-1cc4487edd9c.htm)    
     The end of the datum plane.

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view on which the DatumPlane shows.

#### Return Value

True if the bubble is visible, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The datum plane cannot be visible in the view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This datum plane doesn't support bubble operations. |

# See Also

[DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75c5c1af-f478-1446-c35c-aa5759fc4824.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElementTaskNotFinished Property

---



|  |
| --- |
| [BuiltInFailures SteelElementFailures Class](296689ea-2e78-02be-66d2-e945e1c94408.htm)   [See Also](#seeAlsoToggle) |

Advance Steel tasks not finished.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SteelElementTaskNotFinished { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElementTaskNotFinished As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SteelElementTaskNotFinished { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SteelElementFailures Class](296689ea-2e78-02be-66d2-e945e1c94408.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75c640b9-9904-7882-43fc-a4dfc25ff53c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShellLayerType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Used to distinguish exterior and interior shell layers.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public enum ShellLayerType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ShellLayerType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ShellLayerType ``` |

# Members

| Member name | Description |
| --- | --- |
| Interior | Interior shell layer. |
| Exterior | Exterior shell layer. |

# Remarks

Used as an argument to methods of CompoundStructure that deal with shell layers.

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75c8c8fa-b61d-832c-bcec-f438b7ee3e10.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnstableConstraintInFamily Property

---



|  |
| --- |
| [BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)   [See Also](#seeAlsoToggle) |

Constraints between geometry in the family can behave unpredictably on parameter modification. To make the family reliable, constrain geometry to levels, reference planes, or reference lines.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId UnstableConstraintInFamily { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property UnstableConstraintInFamily As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ UnstableConstraintInFamily { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75c9d2c7-a402-ea8b-9e7c-f8bc3510bbd5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Room Class

---



|  |
| --- |
| [Members](21d28ce3-3c1a-43cd-9714-0fe7223c5636.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Provides access to the room topology in Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public class Room : SpatialElement ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Room _ 	Inherits SpatialElement ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Room : public SpatialElement ``` |

# Remarks

The room object can be queried for its boundary for use in space planning tools.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void Getinfo_Room(Room room)
{
    string message = "Room: ";

    //get the name of the room
    message += "\nRoom Name: " + room.Name;

    //get the room position
    LocationPoint location = room.Location as LocationPoint;
    XYZ point = location.Point;
    message += "\nRoom position: " + XYZToString(point);

    //get the room number
    message += "\nRoom number: " + room.Number;

    IList<IList<Autodesk.Revit.DB.BoundarySegment>> segments = room.GetBoundarySegments(new SpatialElementBoundaryOptions());
    if (null != segments)  //the room may not be bound
    {
        foreach (IList<Autodesk.Revit.DB.BoundarySegment> segmentList in segments)
        {
            message += "\nBoundarySegment of the room: ";
            foreach (Autodesk.Revit.DB.BoundarySegment boundarySegment in segmentList)
            {
                // Get curve start point
                XYZ start = boundarySegment.GetCurve().GetEndPoint(0);
                message += "\nCurve start point: " + XYZToString(start);
                // Get curve end point
                XYZ end = boundarySegment.GetCurve().GetEndPoint(1);
                message += " Curve end point: " + XYZToString(end);

                // Show the boundary elements
                message += "\nBoundary element id: " + boundarySegment.ElementId.ToString();
            }
        }
    }

    TaskDialog.Show("Revit",message);
}

// output the point's three coordinates
string XYZToString(XYZ point)
{
    return "(" + point.X + ", " + point.Y + ", " + point.Z + ")";
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub Getinfo_Room(room As Room)
    Dim message As String = "Room: "

    'get the name of the room
    message += vbLf & "Room Name: " & Convert.ToString(room.Name)

    'get the room position
    Dim location As LocationPoint = TryCast(room.Location, LocationPoint)
    Dim point As XYZ = location.Point
    message += vbLf & "Room position: " & XYZToString(point)

    'get the room number
    message += vbLf & "Room number: " & Convert.ToString(room.Number)

    Dim segments As IList(Of IList(Of Autodesk.Revit.DB.BoundarySegment)) = room.GetBoundarySegments(New SpatialElementBoundaryOptions())
    If segments IsNot Nothing Then
        'the room may not be bound
        For Each segmentList As IList(Of Autodesk.Revit.DB.BoundarySegment) In segments
            message += vbLf & "BoundarySegment of the room: "
            For Each boundarySegment As Autodesk.Revit.DB.BoundarySegment In segmentList
                ' Get curve start point
          Dim start As XYZ = boundarySegment.GetCurve().GetEndPoint(0)
                message += vbLf & "Curve start point: " & XYZToString(start)
                ' Get curve end point
          Dim [end] As XYZ = boundarySegment.GetCurve().GetEndPoint(1)
                message += " Curve end point: " & XYZToString([end])

                ' Show the boundary elements
          message += vbLf & "Boundary element id: " + boundarySegment.ElementId.ToString()
            Next
        Next
    End If

    TaskDialog.Show("Revit", message)
End Sub

' output the point's three coordinates
Private Function XYZToString(point As XYZ) As String
    Return "(" & Convert.ToString(point.X) & ", " & Convert.ToString(point.Y) & ", " & Convert.ToString(point.Z) & ")"
End Function
```

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB SpatialElement](e73594e8-23aa-899f-82fb-3490def8ece2.htm)    
  Autodesk.Revit.DB.Architecture Room

# See Also

[Room Members](21d28ce3-3c1a-43cd-9714-0fe7223c5636.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__75c9e598-0e0e-f666-a6a5-2cbc266d8be9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [WorksetPreview Class](5091902c-a286-eb9e-d65b-3d421d741c69.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [WorksetPreview](5091902c-a286-eb9e-d65b-3d421d741c69.htm)

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

[WorksetPreview Class](5091902c-a286-eb9e-d65b-3d421d741c69.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75cb7394-3f9b-5aff-48cd-d097eb4553ba.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFaces Method

---



|  |
| --- |
| [IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)   [See Also](#seeAlsoToggle) |

Gets the IfcFace handles created representing the processed geometry and stored in this object.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<ICollection<IFCAnyHandle>> GetFaces() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFaces As IList(Of ICollection(Of IFCAnyHandle)) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ICollection<IFCAnyHandle^>^>^ GetFaces() ``` |

#### Return Value

The collection of face handles.

# See Also

[IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__75cde538-cccd-aa5b-9e53-4ec5d5c085d4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [FamilyThermalProperties Class](9d9b2125-8398-9b55-8219-cbda4456ab7b.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [FamilyThermalProperties](9d9b2125-8398-9b55-8219-cbda4456ab7b.htm)

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

[FamilyThermalProperties Class](9d9b2125-8398-9b55-8219-cbda4456ab7b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75d1c78b-31b0-a5b3-abce-ebd57653d6f4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetGUID Method

---



|  |
| --- |
| [AddInId Class](31859d69-72c7-03fb-83e1-5c7719dca253.htm)   [See Also](#seeAlsoToggle) |

value of the AddInId as a GUID

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public Guid GetGUID() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetGUID As Guid ``` |

 

| Visual C++ |
| --- |
| ``` public: Guid GetGUID() ``` |

#### Return Value

GUID value of the AddInId

# See Also

[AddInId Class](31859d69-72c7-03fb-83e1-5c7719dca253.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75d66b3c-6ac0-55c7-10be-6d97e1b41e48.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MatchlineBottomOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bottom Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MatchlineBottomOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MatchlineBottomOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MatchlineBottomOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75d6caeb-62d1-d31f-47fe-618ac7cedf19.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SolidOptions Class

---



|  |
| --- |
| [Members](0c4adb90-a951-bbeb-6243-0aac89cdbad9.htm)   [See Also](#seeAlsoToggle) |

A class containing optional information to control the properties of the Solid generated by the GeometryCreationUtilities routines.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class SolidOptions : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class SolidOptions _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SolidOptions : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB SolidOptions

# See Also

[SolidOptions Members](0c4adb90-a951-bbeb-6243-0aac89cdbad9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75d78b96-0bd1-2fd5-3618-df48a5c5f1d3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsUpdaterRegistered Method (UpdaterId)

---



|  |
| --- |
| [UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.htm)   [See Also](#seeAlsoToggle) |

Checks whether updater with the given id is registered

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static bool IsUpdaterRegistered( 	UpdaterId id ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsUpdaterRegistered ( _ 	id As UpdaterId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsUpdaterRegistered( 	UpdaterId^ id ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.DB UpdaterId](16a9604f-51bd-ce34-f145-17ae06b7c1cf.htm)    
     Id of the updater being tested.

#### Return Value

Returns true if the updater is registered.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.htm)

[IsUpdaterRegistered Overload](62e89fa9-b9e6-41ab-8cfd-9bc6d0b6b6a0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75da6967-bc49-85f8-5630-7a13dc679609.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetVertexStreamPositionNormal Method

---



|  |
| --- |
| [VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)   [See Also](#seeAlsoToggle) |

Gets a stream that can be used to write vertices of type  [VertexPositionNormal](a40efda7-6e2f-a455-f65e-02b10b0bc1b4.htm)  into the buffer.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public VertexStreamPositionNormal GetVertexStreamPositionNormal() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetVertexStreamPositionNormal As VertexStreamPositionNormal ``` |

 

| Visual C++ |
| --- |
| ``` public: VertexStreamPositionNormal^ GetVertexStreamPositionNormal() ``` |

#### Return Value

The stream that can be used to write into this buffer.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if the buffer is not mapped. -or- Thrown if the buffer has insufficient space. |

# See Also

[VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__75dc0ee7-6f2f-2fb0-807a-c1d42d3b6c19.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Item Property

---



|  |
| --- |
| [ReferencePointArray Class](4780adea-9e68-b0b4-09c7-68f7752dd650.htm)   [See Also](#seeAlsoToggle) |

Gets or sets a reference at a specified index within the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual ReferencePoint this[ 	int index ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Property Item ( _ 	index As Integer _ ) As ReferencePoint 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property ReferencePoint^ Item[int index] { 	ReferencePoint^ get (int index); 	void set (int index, ReferencePoint^ value); } ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the reference to be set or retrieved.

#### Return Value

Returns the reference at the specified index.

# See Also

[ReferencePointArray Class](4780adea-9e68-b0b4-09c7-68f7752dd650.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75e1056d-07de-cfe4-6bb3-5a549bcbbe69.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundaryConditionFamilySymbolRoller Property

---



|  |
| --- |
| [StructuralSettings Class](1d1b89be-c2ae-ca39-01ce-f5b01178fb1e.htm)   [See Also](#seeAlsoToggle) |

The id of the FamilySymbol to represent a roller boundary condition.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElementId BoundaryConditionFamilySymbolRoller { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BoundaryConditionFamilySymbolRoller As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ BoundaryConditionFamilySymbolRoller { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[StructuralSettings Class](1d1b89be-c2ae-ca39-01ce-f5b01178fb1e.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__75e265b0-7433-2253-62c5-7e4309dce74d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextLabelType Property

---



|  |
| --- |
| [AnalysisDisplayMarkersAndTextSettings Class](bb940def-7483-32c6-01cb-1c79e6666290.htm)   [See Also](#seeAlsoToggle) |

Type of diagram text label visualization.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public AnalysisDisplayStyleMarkerTextLabelType TextLabelType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property TextLabelType As AnalysisDisplayStyleMarkerTextLabelType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property AnalysisDisplayStyleMarkerTextLabelType TextLabelType { 	AnalysisDisplayStyleMarkerTextLabelType get (); 	void set (AnalysisDisplayStyleMarkerTextLabelType value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[AnalysisDisplayMarkersAndTextSettings Class](bb940def-7483-32c6-01cb-1c79e6666290.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__75e2d74e-a5df-548e-86a9-5497796d71ff.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DoorNumber Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Mark"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DoorNumber { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DoorNumber As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DoorNumber { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75e8479b-2d95-e0fd-a35e-7eb5d13345df.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [CurtainGridSetIterator Class](b8aa3f5a-d84c-a10b-34a0-4562c2fc2ed3.htm)   [See Also](#seeAlsoToggle) |

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

[CurtainGridSetIterator Class](b8aa3f5a-d84c-a10b-34a0-4562c2fc2ed3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75ea4fee-6afc-f4dc-81d4-921b3579a016.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsPipeReynoldsNumberParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Reynolds Number"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsPipeReynoldsNumberParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsPipeReynoldsNumberParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsPipeReynoldsNumberParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75ec6239-fd89-118f-f754-80d7b825c666.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotGenerateRamp Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Couldn't generate surfaces for ramp.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotGenerateRamp { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotGenerateRamp As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotGenerateRamp { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75ef5f70-9782-0947-22f3-e06023aff88a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Append Method

---



|  |
| --- |
| [IntersectionResultArray Class](4742c1e8-0566-73c6-de42-04d98a503dfc.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual void Append( 	IntersectionResult item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Sub Append ( _ 	item As IntersectionResult _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Append( 	IntersectionResult^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB IntersectionResult](0b6f0c2e-e3a2-3e27-fa52-0f4f9f2ca6f0.htm)

# See Also

[IntersectionResultArray Class](4742c1e8-0566-73c6-de42-04d98a503dfc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75f0ccb7-eb19-bd3b-ca7b-7720670e70c8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsPipeJointtypeParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Connection Type"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsPipeJointtypeParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsPipeJointtypeParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsPipeJointtypeParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75f4e1f0-a543-5f50-9958-030c0fa2a2dd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InsertWaypoint Method

---



|  |
| --- |
| [PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)   [See Also](#seeAlsoToggle) |

Insert a waypoint at the specified index

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020.2

# Syntax

| C# |
| --- |
| ``` public void InsertWaypoint( 	XYZ waypoint, 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub InsertWaypoint ( _ 	waypoint As XYZ, _ 	index As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void InsertWaypoint( 	XYZ^ waypoint,  	int index ) ``` |

#### Parameters

waypoint
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The waypoint to insert.

index
:   Type:  System Int32    
     The index to insert the waypoint at.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Index is invalid for an existing or new waypoint for this path. -or- This functionality is not available in Revit LT. -or- Cannot perform this operation for a path of travel in a group. |

# See Also

[PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__75f55d9e-9fb1-2d91-1a04-83963c68eb50.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HvacSlope Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Slope, in discipline HVAC.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId HvacSlope { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property HvacSlope As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ HvacSlope { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75f60a0b-3afa-13b7-559a-b70122c92fad.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetGBSId Method

---



|  |
| --- |
| [ConceptualConstructionType Class](59d96c60-67ae-cb70-d3a6-59e18a434eca.htm)   [See Also](#seeAlsoToggle) |

Gets the Green Building Studio identifier associated with the construction.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public int GetGBSId( 	ElementId massSurfaceSubCategoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetGBSId ( _ 	massSurfaceSubCategoryId As ElementId _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int GetGBSId( 	ElementId^ massSurfaceSubCategoryId ) ``` |

#### Parameters

massSurfaceSubCategoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ElementId of a valid Mass subcategory of a MassSurfaceData.

#### Return Value

Returns the integer id used to represent the ConceptualConstructionType.

# Remarks

Sometimes the GBSId is different for the same ConceptualConstructionType depending on the mass subcategory it is related to. This is usually the case, for example, for window and skylight constructions, which do not share GBSid's even when they share ConceptualConstructionTypes.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input Element massSurfaceSubCategoryId is not a valid subcategory value for MassSurfaceData. -or- The ElementId massSurfaceSubCategoryId is not appropriate for this ConceptualConstructionType. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ConceptualConstructionType Class](59d96c60-67ae-cb70-d3a6-59e18a434eca.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__75f7a413-1b73-a7fc-cef1-75c9972e6652.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetShearModulus Method

---



|  |
| --- |
| [StructuralAsset Class](39c2e2ad-474e-2514-bc15-07c24a989a61.htm)   [See Also](#seeAlsoToggle) |

Sets the shear modulus of the asset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetShearModulus( 	double shearModulus ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetShearModulus ( _ 	shearModulus As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetShearModulus( 	double shearModulus ) ``` |

#### Parameters

shearModulus
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)

# Remarks

The shear modulus is one-dimensional for wood-based and isotropic materials. This method sets the x, y, and z components to the same value. The value is in Newtons per foot meter (N/(ft Â· m)).

# See Also

[StructuralAsset Class](39c2e2ad-474e-2514-bc15-07c24a989a61.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75f8aca2-6dbe-c124-02fa-001620407989.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsTaggingLink Property

---



|  |
| --- |
| [SpatialElementTag Class](0a20cdd6-6e44-bc77-a4c3-2d35470ba911.htm)   [See Also](#seeAlsoToggle) |

Identifies if the tag has reference to a spatial element in a linked document or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public bool IsTaggingLink { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsTaggingLink As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsTaggingLink { 	bool get (); } ``` |

# See Also

[SpatialElementTag Class](0a20cdd6-6e44-bc77-a4c3-2d35470ba911.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__75fe8039-cddc-a565-ee2a-9833c24114a9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GutterType Property

---



|  |
| --- |
| [Gutter Class](ca383537-7a16-718f-e527-a05dbdd2353e.htm)   [See Also](#seeAlsoToggle) |

Retrieves/set an object that represents the type of the Gutter.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public GutterType GutterType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property GutterType As GutterType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property GutterType^ GutterType { 	GutterType^ get (); 	void set (GutterType^ value); } ``` |

# See Also

[Gutter Class](ca383537-7a16-718f-e527-a05dbdd2353e.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__76a06a2b-4702-10ef-3a78-294394805da4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SampleValue Property

---



|  |
| --- |
| [TableCellCombinedParameterData Class](f2303148-6e5e-d143-3725-3ac12c04ea86.htm)   [See Also](#seeAlsoToggle) |

The sample/example value for the parameter in text form

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public string SampleValue { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SampleValue As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ SampleValue { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[TableCellCombinedParameterData Class](f2303148-6e5e-d143-3725-3ac12c04ea86.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76a31fda-45cb-2f7b-4296-6e174d0990d3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApparentCurrent Property

---



|  |
| --- |
| [ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)   [See Also](#seeAlsoToggle) |

The ApparentCurrent value of the Electrical System.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public double ApparentCurrent { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ApparentCurrent As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ApparentCurrent { 	double get (); } ``` |

# Remarks

This property is used to retrieve the ApparentCurrent value of the Electrical System.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This property only available when System Type is Power! |

# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__76a3c46d-031e-37c6-d8c2-3342a60d8bc5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetHookRotationAngle Method

---



|  |
| --- |
| [RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)   [See Also](#seeAlsoToggle) |

Gets the out of plane hook rotation angle at the specified end.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public double GetHookRotationAngle( 	int iEnd ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetHookRotationAngle ( _ 	iEnd As Integer _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetHookRotationAngle( 	int iEnd ) ``` |

#### Parameters

iEnd
:   Type:  System Int32    
     0 for the start , 1 for the end.

#### Return Value

Returns the out of plane hook rotation angle at the specified end.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | iEnd must be 0 or 1. |

# See Also

[RebarShape Class](0a370e32-eaba-785e-7e1f-9330929525fc.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__76a70892-c62f-f77d-18b6-eda50f2111da.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBoundaries Method

---



|  |
| --- |
| [FaceSplitter Class](ba55587f-4f1e-7f4c-5b1c-864e10cab304.htm)   [See Also](#seeAlsoToggle) |

Gets the boundaries.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public IList<CurveLoop> GetBoundaries() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBoundaries As IList(Of CurveLoop) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<CurveLoop^>^ GetBoundaries() ``` |

#### Return Value

The face splitter boundaries.

# See Also

[FaceSplitter Class](ba55587f-4f1e-7f4c-5b1c-864e10cab304.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76ac3b0e-6d59-5e49-c53b-53be65b11cea.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDone Method

---



|  |
| --- |
| [ExportLayerTableIterator Class](24174426-8fd0-a24c-8ee0-1d32532e6f77.htm)   [See Also](#seeAlsoToggle) |

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

[ExportLayerTableIterator Class](24174426-8fd0-a24c-8ee0-1d32532e6f77.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76b78948-f425-6b6f-7a54-5fa39bd7180b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.RevisionFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](d73da6c7-818e-a12d-b238-d5f93eea5175.htm)   [See Also](#seeAlsoToggle) |

Failures about Revision Settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class RevisionFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class RevisionFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RevisionFailures abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BuiltInFailures RevisionFailures

# See Also

[BuiltInFailures RevisionFailures Members](d73da6c7-818e-a12d-b238-d5f93eea5175.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76b7ab91-364a-aa06-9dbb-89fee0527665.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PaperFormat Property

---



|  |
| --- |
| [PDFExportOptions Class](e4236fc8-f8e7-fc74-1b81-9e3a4d9e966b.htm)   [See Also](#seeAlsoToggle) |

Paper format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public ExportPaperFormat PaperFormat { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PaperFormat As ExportPaperFormat 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ExportPaperFormat PaperFormat { 	ExportPaperFormat get (); 	void set (ExportPaperFormat value); } ``` |

# Remarks

When the PaperFormat is ExportPaperFormat.Default, which means "Use Sheet Size".

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The input paper format is invalid |

# See Also

[PDFExportOptions Class](e4236fc8-f8e7-fc74-1b81-9e3a4d9e966b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76bee86d-3c34-7ee1-4349-cd7abcbf3d78.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewType Property

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

The type of the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ViewType ViewType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ViewType As ViewType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ViewType ViewType { 	ViewType get (); } ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void GetViewType(Autodesk.Revit.DB.View view)
{
    // Get the view type of the given view, and format the prompt string
    String prompt = "The view is ";

    switch (view.ViewType)
    {
        case ViewType.AreaPlan:
            prompt += "an area view.";
            break;
        case ViewType.CeilingPlan:
            prompt += "a reflected ceiling plan view.";
            break;
        case ViewType.ColumnSchedule:
            prompt += "a column schedule view.";
            break;
        case ViewType.CostReport:
            prompt += "a cost report view.";
            break;
        case ViewType.Detail:
            prompt += "a detail view.";
            break;
        case ViewType.DraftingView:
            prompt += "a drafting view.";
            break;
        case ViewType.DrawingSheet:
            prompt += "a drawing sheet view.";
            break;
        case ViewType.Elevation:
            prompt += "an elevation view.";
            break;
        case ViewType.EngineeringPlan:
            prompt += "an engineering view.";
            break;
        case ViewType.FloorPlan:
            prompt += "afloor plan view.";
            break;
        case ViewType.Internal:
            prompt += "Revit's internal view.";
            break;
        case ViewType.Legend:
            prompt += "a legend view.";
            break;
        case ViewType.LoadsReport:
            prompt += "a loads report view.";
            break;
        case ViewType.PanelSchedule:
            prompt += "a panel schedule view.";
            break;
        case ViewType.PresureLossReport:
            prompt += "a pressure loss report view.";
            break;
        case ViewType.Rendering:
            prompt += "a rendering view.";
            break;
        case ViewType.Report:
            prompt += "a report view.";
            break;
        case ViewType.Schedule:
            prompt += "a schedule view.";
            break;
        case ViewType.Section:
            prompt += "a cross section view.";
            break;
        case ViewType.ThreeD:
            prompt += "a 3-D view.";
            break;
        case ViewType.Undefined:
            prompt += "an undefined/unspecified view.";
            break;
        case ViewType.Walkthrough:
            prompt += "a walkthrough view.";
            break;
        default:
            break;
    }

    // Give the user some information
    TaskDialog.Show("Revit",prompt);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub GetViewType(view As Autodesk.Revit.DB.View)
    ' Get the view type of the given view, and format the prompt string
    Dim prompt As [String] = "The view is "

    Select Case view.ViewType
        Case ViewType.AreaPlan
            prompt += "an area view."
            Exit Select
        Case ViewType.CeilingPlan
            prompt += "a reflected ceiling plan view."
            Exit Select
        Case ViewType.ColumnSchedule
            prompt += "a column schedule view."
            Exit Select
        Case ViewType.CostReport
            prompt += "a cost report view."
            Exit Select
        Case ViewType.Detail
            prompt += "a detail view."
            Exit Select
        Case ViewType.DraftingView
            prompt += "a drafting view."
            Exit Select
        Case ViewType.DrawingSheet
            prompt += "a drawing sheet view."
            Exit Select
        Case ViewType.Elevation
            prompt += "an elevation view."
            Exit Select
        Case ViewType.EngineeringPlan
            prompt += "an engineering view."
            Exit Select
        Case ViewType.FloorPlan
            prompt += "afloor plan view."
            Exit Select
        Case ViewType.Internal
            prompt += "Revit's internal view."
            Exit Select
        Case ViewType.Legend
            prompt += "a legend view."
            Exit Select
        Case ViewType.LoadsReport
            prompt += "a loads report view."
            Exit Select
        Case ViewType.PanelSchedule
            prompt += "a panel schedule view."
            Exit Select
        Case ViewType.PresureLossReport
            prompt += "a pressure loss report view."
            Exit Select
        Case ViewType.Rendering
            prompt += "a rendering view."
            Exit Select
        Case ViewType.Report
            prompt += "a report view."
            Exit Select
        Case ViewType.Schedule
            prompt += "a schedule view."
            Exit Select
        Case ViewType.Section
            prompt += "a cross section view."
            Exit Select
        Case ViewType.ThreeD
            prompt += "a 3-D view."
            Exit Select
        Case ViewType.Undefined
            prompt += "an undefined/unspecified view."
            Exit Select
        Case ViewType.Walkthrough
            prompt += "a walkthrough view."
            Exit Select
        Case Else
            Exit Select
    End Select

    ' Give the user some information
    TaskDialog.Show("Revit", prompt)
End Sub
```

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76c639c2-ddce-f010-f81a-bd59e46cc5e1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsInside Method (UV)

---



|  |
| --- |
| [Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the specified point is within this face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public bool IsInside( 	UV point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsInside ( _ 	point As UV _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsInside( 	UV^ point ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     The parameters to be evaluated, in natural parameterization of the face.

#### Return Value

True if point is within this face or on its boundary, otherwise false.

# See Also

[Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)

[IsInside Overload](48a28e26-dd46-5251-c76f-8f2f93d252e9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76c71351-b799-a677-02ce-cee11c2b61f2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetObjectData Method

---



|  |
| --- |
| [InvalidObjectException Class](8092dec2-113a-0823-1a09-a46c11f99fea.htm)   [See Also](#seeAlsoToggle) |

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

[InvalidObjectException Class](8092dec2-113a-0823-1a09-a46c11f99fea.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__76c74081-773e-ec93-f3a9-02389b083f71.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetObjectData Method

---



|  |
| --- |
| [CorruptModelException Class](b1a877a7-6c68-c0e4-25c9-005ee153bc60.htm)   [See Also](#seeAlsoToggle) |

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

[CorruptModelException Class](b1a877a7-6c68-c0e4-25c9-005ee153bc60.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__76c8b986-670c-1d4a-3ae4-776b3eb29ad9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReferenceCurve Property

---



|  |
| --- |
| [HostedSweep Class](e0744068-e808-4547-3743-81be0a4adcbc.htm)   [See Also](#seeAlsoToggle) |

The curve on which the hosted sweep segment is created.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Curve this[ 	Reference targetRef ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ReferenceCurve ( _ 	targetRef As Reference _ ) As Curve 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Curve^ ReferenceCurve[Reference^ targetRef] { 	Curve^ get (Reference^ targetRef); } ``` |

#### Parameters

targetRef
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     Reference of the curve that hosts the object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when regeneration fails. |

# See Also

[HostedSweep Class](e0744068-e808-4547-3743-81be0a4adcbc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76cb7994-3b2c-7165-e55b-f68f7f251466.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CircuitWorksetClosedWarning Property

---



|  |
| --- |
| [BuiltInFailures SystemsFailures Class](b67f74b9-4336-74df-edd9-04f5d08be033.htm)   [See Also](#seeAlsoToggle) |

The workset of the circuit is closed so the circuit path will not be displayed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CircuitWorksetClosedWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CircuitWorksetClosedWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CircuitWorksetClosedWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SystemsFailures Class](b67f74b9-4336-74df-edd9-04f5d08be033.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76cc2368-3903-e988-7323-002985359e5c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDesignElementAndFabricationPartsWithDifferentOffsets Method

---



|  |
| --- |
| [DesignToFabricationConverter Class](b2165e08-c8a4-5674-12ff-d359eba911d4.htm)   [See Also](#seeAlsoToggle) |

Gets the collection of design elements that failed to convert and the associated set of fabrication parts with different offsets.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public IDictionary<ElementId, ISet<ElementId>> GetDesignElementAndFabricationPartsWithDifferentOffsets() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDesignElementAndFabricationPartsWithDifferentOffsets As IDictionary(Of ElementId, ISet(Of ElementId)) ``` |

 

| Visual C++ |
| --- |
| ``` public: IDictionary<ElementId^, ISet<ElementId^>^>^ GetDesignElementAndFabricationPartsWithDifferentOffsets() ``` |

#### Return Value

A map of design element identifiers that were not converted and the associated set fabrication parts left with different offsets.

# Remarks

This set of element identifiers is only available after the  **Convert**  method has been invoked, and returns DesignToFabricationConverterResult::Enum::PartialFailure.

# See Also

[DesignToFabricationConverter Class](b2165e08-c8a4-5674-12ff-d359eba911d4.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)

<!-- Start of Syntax__76cf499a-4a59-9249-8995-e1ab9e629f37.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetVendorId Method

---



|  |
| --- |
| [IExternalServer Interface](91e4af0b-59c0-d640-107a-eebc4d99fa76.htm)   [See Also](#seeAlsoToggle) |

Implement this method to return the id of the vendor of the server.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` string GetVendorId() ``` |

 

| Visual Basic |
| --- |
| ``` Function GetVendorId As String ``` |

 

| Visual C++ |
| --- |
| ``` String^ GetVendorId() ``` |

#### Return Value

Vendor Id of the server.

# Remarks

The Id is expected to be a string consisting of 4 characters.

# See Also

[IExternalServer Interface](91e4af0b-59c0-d640-107a-eebc4d99fa76.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)

<!-- Start of Syntax__76d21b21-dd48-3a31-643e-3869decd8865.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForwardIterator Method

---



|  |
| --- |
| [CitySet Class](9184332e-1167-a3c1-b2c1-58e9409817f3.htm)   [See Also](#seeAlsoToggle) |

Retrieve a forward moving iterator to the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual CitySetIterator ForwardIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ForwardIterator As CitySetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual CitySetIterator^ ForwardIterator() ``` |

#### Return Value

Returns a forward moving iterator to the set.

# See Also

[CitySet Class](9184332e-1167-a3c1-b2c1-58e9409817f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76d4cbc2-c790-4912-c972-aae686d4d6e8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalysisDisplayColorEntry Constructor (Color)

---



|  |
| --- |
| [AnalysisDisplayColorEntry Class](71d66cd5-6dae-22f0-f364-838e13cfbf8e.htm)   [See Also](#seeAlsoToggle) |

Constructs a color entry with no value assigned.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public AnalysisDisplayColorEntry( 	Color color ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	color As Color _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: AnalysisDisplayColorEntry( 	Color^ color ) ``` |

#### Parameters

color
:   Type:  [Autodesk.Revit.DB Color](3735f9b9-d477-09ea-25bd-67f34134595f.htm)    
     Color assigned to the entry.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AnalysisDisplayColorEntry Class](71d66cd5-6dae-22f0-f364-838e13cfbf8e.htm)

[AnalysisDisplayColorEntry Overload](eb5d411d-1102-a4c2-85b7-3fe6a9b3b9b4.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__76d91468-6173-efc2-01e6-c4f76280eae2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FloorsOverlap Property

---



|  |
| --- |
| [BuiltInFailures OverlapFailures Class](b5f85718-fcb7-9396-e706-6d04f0c25c34.htm)   [See Also](#seeAlsoToggle) |

Highlighted floors overlap.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FloorsOverlap { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FloorsOverlap As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FloorsOverlap { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures OverlapFailures Class](b5f85718-fcb7-9396-e706-6d04f0c25c34.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76d95bbc-e2d6-8373-b453-82bab482d0f5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UseDigitGrouping Property

---



|  |
| --- |
| [FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)   [See Also](#seeAlsoToggle) |

Indicates if digit grouping symbols should be displayed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool UseDigitGrouping { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property UseDigitGrouping As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool UseDigitGrouping { 	bool get (); 	void set (bool value); } ``` |

#### Field Value

True if digit grouping symbols should be displayed, false otherwise. The default is false.

# Remarks

When UseDigitGrouping is true, digit grouping symbols (i.e. thousands separators) will be displayed when needed. For example, 123456789.00 may be displayed as 123,456,789.00. The precise display is determined by the DigitGroupingSymbol and DigitGroupingAmount properties of the Units class.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | UseDefault is true in this FormatOptions. |

# See Also

[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76db3e11-fdaa-14f1-58c6-6f66ed70e0bd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ThermalAssetId Property

---



|  |
| --- |
| [Material Class](2ec33007-7a2a-f86a-009b-d4c5d235a307.htm)   [See Also](#seeAlsoToggle) |

The ElementId of the thermal PropertySetElement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public ElementId ThermalAssetId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ThermalAssetId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ThermalAssetId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[Material Class](2ec33007-7a2a-f86a-009b-d4c5d235a307.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76dcb7fb-0b2a-2dcf-2df5-d8c0ac4643f2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidSymbol Method (ForgeTypeId)

---



|  |
| --- |
| [FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)   [See Also](#seeAlsoToggle) |

Checks whether a symbol is valid for the unit in this FormatOptions.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsValidSymbol( 	ForgeTypeId symbolTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidSymbol ( _ 	symbolTypeId As ForgeTypeId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidSymbol( 	ForgeTypeId^ symbolTypeId ) ``` |

#### Parameters

symbolTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     Identifier of the symbol to check.

#### Return Value

True if the symbol is valid, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | UseDefault is true in this FormatOptions. |

# See Also

[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)

[IsValidSymbol Overload](a965e857-57c6-25cb-1622-f2d80425e999.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76e43206-5f28-5e64-e087-46c575327956.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UpDirection Property

---



|  |
| --- |
| [TextElement Class](013e58c3-f3d2-d976-89f0-ff4ff701951d.htm)   [See Also](#seeAlsoToggle) |

Direction along the vertical axis of letters of the text note.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ UpDirection { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property UpDirection As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ UpDirection { 	XYZ^ get (); } ``` |

# Remarks

This vector points up from the base of the letters and is always perpendicular to the base direction. Those two vectors together define the plane of the text.

# See Also

[TextElement Class](013e58c3-f3d2-d976-89f0-ff4ff701951d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76e74eb3-5217-5f99-f781-ef29996eea85.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TypeName Property

---



|  |
| --- |
| [NestedFamilyTypeReference Class](ff71e3b0-4300-7d04-1356-a045b9a90407.htm)   [See Also](#seeAlsoToggle) |

Type of the referenced family

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public string TypeName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property TypeName As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ TypeName { 	String^ get (); } ``` |

# See Also

[NestedFamilyTypeReference Class](ff71e3b0-4300-7d04-1356-a045b9a90407.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76ea2879-bd7e-cf4f-d749-7f0e39a21f64.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FlangeFillet Property

---



|  |
| --- |
| [StructuralSectionGeneralT Class](308dc954-e403-b95c-3f1c-3a9a4c22beaf.htm)   [See Also](#seeAlsoToggle) |

Flange Fillet - fillet radius at the flange end.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public double FlangeFillet { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FlangeFillet As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double FlangeFillet { 	double get (); 	void set (double value); } ``` |

# See Also

[StructuralSectionGeneralT Class](308dc954-e403-b95c-3f1c-3a9a4c22beaf.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__76ebf410-d2e1-c147-536c-5a615938e26d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Origin Property

---



|  |
| --- |
| [ClipPlane Class](eebd15b6-2643-3d82-696b-59ee5618f11b.htm)   [See Also](#seeAlsoToggle) |

The plane's origin.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public XYZ Origin { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Origin As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Origin { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ClipPlane Class](eebd15b6-2643-3d82-696b-59ee5618f11b.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__76ed18a3-be39-71d7-352e-480d821e7221.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GroupCannotSaveWarn Property

---



|  |
| --- |
| [BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)   [See Also](#seeAlsoToggle) |

The group cannot be saved at this time because one of its instances is being edited.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId GroupCannotSaveWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GroupCannotSaveWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ GroupCannotSaveWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76f3c8fd-ae2f-99c8-217d-56e188a92e66.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlasticvinylPattern Property

---



|  |
| --- |
| [PlasticVinyl Class](f2f81383-0340-7868-72f1-a7bb4a4a2eaa.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Relief Pattern" from the "PlasticVinyl" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string PlasticvinylPattern { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PlasticvinylPattern As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ PlasticvinylPattern { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyInteger" with accepted values in the enumerated type "PlasticvinylPatternType".

# See Also

[PlasticVinyl Class](f2f81383-0340-7868-72f1-a7bb4a4a2eaa.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__76f43ff1-42d1-c984-3b47-e5de5097cfa2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurtainGridU Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"U Grid"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CurtainGridU { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CurtainGridU As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CurtainGridU { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76f4ef42-0dc5-8c84-42dc-27d4898b9ec0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetMajorLayoutAsActualSpacing Method

---



|  |
| --- |
| [FabricSheetType Class](892f0ce6-5548-d299-c976-9355ac4109ee.htm)   [See Also](#seeAlsoToggle) |

Sets the major layout pattern as ActualSpacing, while specifying the needed parameters for this pattern.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetMajorLayoutAsActualSpacing( 	double overallWidth, 	double minorStartOverhang, 	double spacing ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetMajorLayoutAsActualSpacing ( _ 	overallWidth As Double, _ 	minorStartOverhang As Double, _ 	spacing As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetMajorLayoutAsActualSpacing( 	double overallWidth,  	double minorStartOverhang,  	double spacing ) ``` |

#### Parameters

overallWidth
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The entire width of the wire sheet in the minor direction.

minorStartOverhang
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The distance from the edge of the sheet to the first wire in the minor direction.

spacing
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The distance between the wires in the major direction.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for overallWidth is not a number -or- The given value for minorStartOverhang is not a number -or- The given value for spacing is not a number -or- The arguments are not consistent, please specify proper input values. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for overallWidth must be greater than 0 and no more than 30000 feet. -or- The given value for minorStartOverhang must be between 0 and 30000 feet. -or- The given value for spacing must be greater than 0 and no more than 30000 feet. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[FabricSheetType Class](892f0ce6-5548-d299-c976-9355ac4109ee.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__76f91359-1f5d-1d3b-e934-bf6a74a08d06.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ClearCutLayerModifiers Method

---



|  |
| --- |
| [ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.htm)   [See Also](#seeAlsoToggle) |

Clears all the cut layer modifiers stored in the layer info.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void ClearCutLayerModifiers() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ClearCutLayerModifiers ``` |

 

| Visual C++ |
| --- |
| ``` public: void ClearCutLayerModifiers() ``` |

# See Also

[ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76fa4e7d-9201-b601-9924-0462e00cd883.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateSheetList Method

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

Creates a sheet list.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ViewSchedule CreateSheetList( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateSheetList ( _ 	document As Document _ ) As ViewSchedule ``` |

 

| Visual C++ |
| --- |
| ``` public: static ViewSchedule^ CreateSheetList( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to which the new schedule will be added.

#### Return Value

The newly created schedule.

# Remarks

A sheet list is a schedule of sheets in the project. It is a schedule of the Sheets category.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__76fd2ea8-1d60-5c8b-43f9-23aa68750200.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddValueString Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Adds a string value to a built-in parameter.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static void AddValueString( 	Element element, 	ElementId builtInParameter, 	string propertyValue ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub AddValueString ( _ 	element As Element, _ 	builtInParameter As ElementId, _ 	propertyValue As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void AddValueString( 	Element^ element,  	ElementId^ builtInParameter,  	String^ propertyValue ) ``` |

#### Parameters

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element.

builtInParameter
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The built-in parameter id.

propertyValue
:   Type:  System String    
     The new value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__77a0815b-a4f1-041c-534b-ed66a72add68.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Name Property

---



|  |
| --- |
| [WireConduitType Class](3c17c9e5-7018-1cf6-4a20-d8059cec370c.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public string Name { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Name As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Name { 	String^ get (); } ``` |

# See Also

[WireConduitType Class](3c17c9e5-7018-1cf6-4a20-d8059cec370c.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__77a31304-1310-12a8-17d4-5fdd817fe270.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetEnumerator Method

---



|  |
| --- |
| [GroundConductorSizeSet Class](c0db891d-23ad-f1d1-0b7f-8e5073aa9bab.htm)   [See Also](#seeAlsoToggle) |

Retrieve a forward moving iterator to the set.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
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

[GroundConductorSizeSet Class](c0db891d-23ad-f1d1-0b7f-8e5073aa9bab.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__77a31a9c-7e57-7818-84a4-1067916c8773.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [ConnectorSetIterator Class](211f670f-72c3-6b6b-24dd-1a784f80a338.htm)   [See Also](#seeAlsoToggle) |

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

[ConnectorSetIterator Class](211f670f-72c3-6b6b-24dd-1a784f80a338.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77a4660e-a59f-1a10-5ab0-38edafa84251.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WaveWaveLenMin Property

---



|  |
| --- |
| [Wave Class](9c0cc26f-f6ae-708e-5612-d3d181058174.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Len Min" from the "Wave" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string WaveWaveLenMin { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WaveWaveLenMin As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ WaveWaveLenMin { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble" within the range of "0, 1000000000".

# See Also

[Wave Class](9c0cc26f-f6ae-708e-5612-d3d181058174.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__77a51362-e601-93b4-9b12-4241073778d4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GBXMLImportOptions Class

---



|  |
| --- |
| [Members](9d4cb70f-d86b-8d2f-e426-082422e254fc.htm)   [See Also](#seeAlsoToggle) |

Import options for Green-Building XML format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class GBXMLImportOptions ``` |

 

| Visual Basic |
| --- |
| ``` Public Class GBXMLImportOptions ``` |

 

| Visual C++ |
| --- |
| ``` public ref class GBXMLImportOptions ``` |

# Remarks

Not used currently. Reserved for future use.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB GBXMLImportOptions

# See Also

[GBXMLImportOptions Members](9d4cb70f-d86b-8d2f-e426-082422e254fc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77a62604-7055-b459-486f-11f917ec922d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAddInNameFromDocument Method

---



|  |
| --- |
| [AddInId Class](31859d69-72c7-03fb-83e1-5c7719dca253.htm)   [See Also](#seeAlsoToggle) |

name of application associated with this ApplicationId First attempts to obtain the name from AddInIds stored in the document. If unsuccessful, attempts to obtain the name from loaded Third Party AddIns.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string GetAddInNameFromDocument( 	Document aDoc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAddInNameFromDocument ( _ 	aDoc As Document _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetAddInNameFromDocument( 	Document^ aDoc ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     target document

#### Return Value

name of application

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |

# See Also

[AddInId Class](31859d69-72c7-03fb-83e1-5c7719dca253.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77a91564-8e22-9050-0048-800dca92a99f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsAttrTreadWidth Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Width"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsAttrTreadWidth { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsAttrTreadWidth As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsAttrTreadWidth { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77aa9939-8f41-1725-80dc-864ca1f7a49c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentPrinting Event

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the DocumentPrinting event to be notified when Revit is just about to print a view or ViewSet of the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<DocumentPrintingEventArgs> DocumentPrinting ``` |

 

| Visual Basic |
| --- |
| ``` Public Event DocumentPrinting As EventHandler(Of DocumentPrintingEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<DocumentPrintingEventArgs^>^ DocumentPrinting { 	void add (EventHandler<DocumentPrintingEventArgs^>^ value); 	void remove (EventHandler<DocumentPrintingEventArgs^>^ value); } ``` |

# Remarks

This event is raised when Revit is just about to print a view or ViewSet of the document.

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Event is cancellable. To cancel it, call the 'Cancel()' method of event's argument to True. Your application is responsible for providing feedback to the user about the reason for the cancellation.

The following API functions are not available for current document during this event:

* All overloads of Autodesk.Revit.DB.Document.Export()
* Autodesk::Revit::DB::Document::Print
* [Print](1ea1e825-8044-7a27-d9b9-ca463443c3b9.htm)  and similar overloads.
* [SubmitPrint](0c9524b7-33b5-8c76-2843-c7024f03e4d7.htm)  and similar overloads.
* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  .
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

After this event, for each view being printed,  [ViewPrinting](941de0b6-a0f9-eb5a-5f25-9aa4d9da699a.htm)  and  [ViewPrinted](ace39293-a976-d22b-4798-42bb8e82b307.htm)  events will be raised. Another event  [DocumentPrinted](8d74cf02-9271-3c6c-00f5-bc7b48d52c56.htm)  will be raised immediately after document printing is finished.

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77ab6680-ae2b-e994-9c65-3b4b9d11d243.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [DuplicateTypeNamesHandlerArgs Class](939b55de-12e5-2117-5fbc-471f8bb009c9.htm)   [See Also](#seeAlsoToggle) |

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

[DuplicateTypeNamesHandlerArgs Class](939b55de-12e5-2117-5fbc-471f8bb009c9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77af495c-e4d7-d143-4d37-6ca9eeea0942.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IfcGuid Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"IfcGUID"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId IfcGuid { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property IfcGuid As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ IfcGuid { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77bad211-6dcf-cb86-c66f-ac25384ccd31.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

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

[CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77bfae79-dd26-2cb7-c20e-eb49a0901975.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MepPipeUpperInvertElevation Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Upper End Invert Elevation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MepPipeUpperInvertElevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MepPipeUpperInvertElevation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MepPipeUpperInvertElevation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77c42cca-7a15-32a2-3a4e-172cb533a022.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GroundConductorNum Property

---



|  |
| --- |
| [Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)   [See Also](#seeAlsoToggle) |

The ground conductor number. Its default value is zero after created.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int GroundConductorNum { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property GroundConductorNum As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int GroundConductorNum { 	int get (); 	void set (int value); } ``` |

# See Also

[Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__77c58c44-0d8d-c10f-b6e7-2be9a25bbb1e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDiscipline Method

---



|  |
| --- |
| [UnitUtils Class](128dd879-fea8-5d7b-1eb2-d64f87753990.htm)   [See Also](#seeAlsoToggle) |

Gets the discipline for a given measurable spec.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId GetDiscipline( 	ForgeTypeId specTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetDiscipline ( _ 	specTypeId As ForgeTypeId _ ) As ForgeTypeId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ForgeTypeId^ GetDiscipline( 	ForgeTypeId^ specTypeId ) ``` |

#### Parameters

specTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     Identifier of the measurable spec.

#### Return Value

Identifier of the discipline.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | specTypeId is not a measurable spec identifier. See UnitUtils.IsMeasurableSpec(ForgeTypeId). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[UnitUtils Class](128dd879-fea8-5d7b-1eb2-d64f87753990.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77ca18ef-783e-9db5-a37a-2d76f637d1a1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ComputeDerivatives Method

---



|  |
| --- |
| [Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)   [See Also](#seeAlsoToggle) |

Returns the first partial derivatives of the underlying surface at the specified point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public Transform ComputeDerivatives( 	UV point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ComputeDerivatives ( _ 	point As UV _ ) As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform^ ComputeDerivatives( 	UV^ point ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     The parameters to be evaluated, in natural parameterization of the face.

#### Return Value

A transformation containing tangent vectors and a normal vector.

# Remarks

The following is the meaning of the transformation members:

* Origin is the point on the face (equivalent to  [Evaluate(UV)](d1219dd7-fc7a-6b12-afce-963d554e947d.htm)  );
* BasisX is the tangent vector along the U coordinate (partial derivative with respect to U).
* BasisY is the tangent vector along the V coordinate (partial derivative with respect to V).
* BasisZ is the underlying surface's normal vector. This is not necessarily aligned with the normal vector pointing out of a solid that contains the face, to get that value use  [ComputeNormal(UV)](15377d5b-d369-2e09-98ef-ca0eb0af86a1.htm)  .

None of the vectors are normalized.

# See Also

[Face Class](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77cd1211-cbc5-1db7-7b05-e64b8e598e59.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionCommonPlasticModulusStrongAxis Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Plastic Modulus strong axis"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralSectionCommonPlasticModulusStrongAxis { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralSectionCommonPlasticModulusStrongAxis As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralSectionCommonPlasticModulusStrongAxis { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77ce5f18-d70d-39a2-d91b-e46bb074282a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanViewViewDir Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"View Direction"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PlanViewViewDir { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PlanViewViewDir As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PlanViewViewDir { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77d59f55-d70a-35b8-aacd-fb66a53223b9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetIntersectingElements Method

---



|  |
| --- |
| [DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)   [See Also](#seeAlsoToggle) |

Set the elements whose intersection with path produces points.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetIntersectingElements( 	ICollection<ElementId> intersectors ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetIntersectingElements ( _ 	intersectors As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetIntersectingElements( 	ICollection<ElementId^>^ intersectors ) ``` |

#### Parameters

intersectors
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Not all intersecting elements in intersectors are valid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77d7ff26-f814-959a-dd64-9906efd5e228.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [KeyBasedTreeEntriesIterator Class](d842419d-d2a9-a839-0944-82f163884362.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [KeyBasedTreeEntriesIterator](d842419d-d2a9-a839-0944-82f163884362.htm)

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

[KeyBasedTreeEntriesIterator Class](d842419d-d2a9-a839-0944-82f163884362.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77db36a1-bf91-e922-1d9d-81929c886944.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WeatherStation Property

---



|  |
| --- |
| [City Class](2ceeb3cd-05a1-02c6-3d95-ef689221acdc.htm)   [See Also](#seeAlsoToggle) |

An identifier for the nearest weather station

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string WeatherStation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property WeatherStation As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ WeatherStation { 	String^ get (); } ``` |

# Remarks

A read only string property that contains an identifier of the nearest weather station.

# See Also

[City Class](2ceeb3cd-05a1-02c6-3d95-ef689221acdc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77dc6e7f-392e-51bd-3b0a-27fcda987357.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetDefaultEntity Method

---



|  |
| --- |
| [DuctFittingAndAccessoryPressureDropData Class](5411567a-c556-61ec-a41b-182d2277d8a5.htm)   [See Also](#seeAlsoToggle) |

Stores the default entity in the data.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetDefaultEntity( 	Entity defaultEntity ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetDefaultEntity ( _ 	defaultEntity As Entity _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetDefaultEntity( 	Entity^ defaultEntity ) ``` |

#### Parameters

defaultEntity
:   Type:  [Autodesk.Revit.DB.ExtensibleStorage Entity](cf17f0e8-33bd-ef95-bf4b-e6298406f29b.htm)    
     The Entity to be stored.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Writing of Entities of this Schema is not allowed to the current add-in. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DuctFittingAndAccessoryPressureDropData Class](5411567a-c556-61ec-a41b-182d2277d8a5.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__77e175b5-7495-7a20-98fc-6aa5706a7687.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StartPoint Property

---



|  |
| --- |
| [LineLoad Class](ee5ec273-350a-1cdb-d136-0c454bb1446a.htm)   [See Also](#seeAlsoToggle) |

Returns the three dimensional location of the start point for the line load.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ StartPoint { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property StartPoint As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ StartPoint { 	XYZ^ get (); } ``` |

# Remarks

The location of the start point is measured in decimal feet.

# See Also

[LineLoad Class](ee5ec273-350a-1cdb-d136-0c454bb1446a.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__77e8c92f-6b48-0f3d-923c-2737a6d6e4ab.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, View, ICollection(ElementId), Int32, XYZ, ArrayAnchorMember)

---



|  |
| --- |
| [LinearArray Class](58e47064-607e-d52b-5930-7e371851a678.htm)   [See Also](#seeAlsoToggle) |

Creates a new linear array element from a set of elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static LinearArray Create( 	Document aDoc, 	View dBView, 	ICollection<ElementId> ids, 	int count, 	XYZ translationToAnchorMember, 	ArrayAnchorMember anchorMember ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	aDoc As Document, _ 	dBView As View, _ 	ids As ICollection(Of ElementId), _ 	count As Integer, _ 	translationToAnchorMember As XYZ, _ 	anchorMember As ArrayAnchorMember _ ) As LinearArray ``` |

 

| Visual C++ |
| --- |
| ``` public: static LinearArray^ Create( 	Document^ aDoc,  	View^ dBView,  	ICollection<ElementId^>^ ids,  	int count,  	XYZ^ translationToAnchorMember,  	ArrayAnchorMember anchorMember ) ``` |

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

The new linear array element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given element id set is empty. -or- One or more elements in ids do not exist in the document. -or- One or more elements in ids is owned by different views and thus cannot be arrayed together. -or- One or more elements in ids is not arrayable. -or- count must be between 2 and 200. -or- The view is invalid for specific view elements array. -or- The translation point vector is invalid to array the element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to create the linear array. |

# See Also

[LinearArray Class](58e47064-607e-d52b-5930-7e371851a678.htm)

[Create Overload](714cd3bc-a955-45b7-09e6-aa7fe9880da0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77ea91bc-36f7-d3bd-5535-66540017a818.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElemCoating Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Coating"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SteelElemCoating { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElemCoating As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SteelElemCoating { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77f23d33-acd6-b2a8-03b0-fba7e65e36a8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextBoxVisibility Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Show Border"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TextBoxVisibility { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextBoxVisibility As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TextBoxVisibility { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77f35dcf-3db3-9db1-50b8-2591b7e8e098.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsWireNeutralModeParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Neutral Size"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsWireNeutralModeParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsWireNeutralModeParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsWireNeutralModeParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77f442ea-1ccc-67fb-c268-dba92c0dda90.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomOutdoorAirInfoParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Outdoor Air Information"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RoomOutdoorAirInfoParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoomOutdoorAirInfoParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RoomOutdoorAirInfoParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77f654b8-0991-b11d-6cc0-20d6b2eaa277.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallNominalThickness Property

---



|  |
| --- |
| [StructuralSectionGeneralR Class](0520949b-2fd0-ca3c-bc98-c259e28d29d1.htm)   [See Also](#seeAlsoToggle) |

Represents wall nominal thickness of rectangle.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public double WallNominalThickness { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property WallNominalThickness As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double WallNominalThickness { 	double get (); 	void set (double value); } ``` |

# Remarks

Nominal is measured real value of profile, should be thicker than designed. In EN standard it is marked as "d". //Need to be verified!!!!!!! In ACI standard it is marked as "d". //Need to be verified!!!!!!!

# See Also

[StructuralSectionGeneralR Class](0520949b-2fd0-ca3c-bc98-c259e28d29d1.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__77f93e08-edf7-e03b-0671-ca59c6301f32.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AssemblyDifferenceConfiguration Class

---



|  |
| --- |
| [Members](002c9b86-ed74-97ef-1b54-0af69e0656a3.htm)   [See Also](#seeAlsoToggle) |

The two assemblies being compared have different spatial configuration

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class AssemblyDifferenceConfiguration : AssemblyDifference ``` |

 

| Visual Basic |
| --- |
| ``` Public Class AssemblyDifferenceConfiguration _ 	Inherits AssemblyDifference ``` |

 

| Visual C++ |
| --- |
| ``` public ref class AssemblyDifferenceConfiguration : public AssemblyDifference ``` |

# Remarks

Assemblies resulting in this difference might be made up of identical elements, but the elements are not arranged in space relative to each other in the same way.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB AssemblyDifference](51d7603f-be85-5d67-eeb1-7cd7a6d199a8.htm)    
  Autodesk.Revit.DB AssemblyDifferenceConfiguration

# See Also

[AssemblyDifferenceConfiguration Members](002c9b86-ed74-97ef-1b54-0af69e0656a3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__77fe7249-7ce9-7f81-0a49-58ae007e4ce8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsPanelScheduleTemplate Method

---



|  |
| --- |
| [PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)   [See Also](#seeAlsoToggle) |

Check if this is a panel schedule template.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsPanelScheduleTemplate() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsPanelScheduleTemplate As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsPanelScheduleTemplate() ``` |

#### Return Value

Check if this is a panel schedule template.

# See Also

[PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__78a38c0a-85c8-5592-1a3d-929f949aeebd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImportScaleTooLarge Property

---



|  |
| --- |
| [BuiltInFailures ImportFailures Class](37a5e9d1-ffe4-363f-2033-1cabbf5634aa.htm)   [See Also](#seeAlsoToggle) |

This scale factor would make the imported object too large. Reverting to the previous scale factor.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ImportScaleTooLarge { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ImportScaleTooLarge As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ImportScaleTooLarge { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ImportFailures Class](37a5e9d1-ffe4-363f-2033-1cabbf5634aa.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78a4fa8a-d5fa-736c-8c98-05073e31a556.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [BalusterPlacement Class](33c016f2-bf39-a852-052f-b1c80b0f1860.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [BalusterPlacement](33c016f2-bf39-a852-052f-b1c80b0f1860.htm)

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

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

[BalusterPlacement Class](33c016f2-bf39-a852-052f-b1c80b0f1860.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__78a9fd54-4d3d-c80c-50ac-a7a835d6ccd6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointElementHostedOnFaceUParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Hosted U Parameter"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PointElementHostedOnFaceUParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PointElementHostedOnFaceUParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PointElementHostedOnFaceUParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78adb5d6-ccbe-861b-6bc1-0c921121f829.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SecondaryHandrailType Property

---



|  |
| --- |
| [RailingType Class](7e7551fe-1772-f2d3-a8b5-58d4bb42a34e.htm)   [See Also](#seeAlsoToggle) |

The type of the secondary handrail.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId SecondaryHandrailType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SecondaryHandrailType As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ SecondaryHandrailType { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The handRailTypeId is not a valid hand rail type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[RailingType Class](7e7551fe-1772-f2d3-a8b5-58d4bb42a34e.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__78b13087-63d8-090e-92ab-024d06717903.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CircuitPathMode Property

---



|  |
| --- |
| [ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)   [See Also](#seeAlsoToggle) |

The circuit path mode of the electrical system.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public ElectricalCircuitPathMode CircuitPathMode { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CircuitPathMode As ElectricalCircuitPathMode 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElectricalCircuitPathMode CircuitPathMode { 	ElectricalCircuitPathMode get (); 	void set (ElectricalCircuitPathMode value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Mechanical Electrical Piping. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The electrical system circuit path does not have customized path, so the CircuitPathMode cannot be set as Custom. |

# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__78bd4d11-0ccd-9065-c316-7225f422fa16.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreaTagType Class

---



|  |
| --- |
| [Members](a17139c3-13c2-dd2d-938e-412f34c9a234.htm)   [See Also](#seeAlsoToggle) |

An object that represents an Area Tag style.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class AreaTagType : FamilySymbol ``` |

 

| Visual Basic |
| --- |
| ``` Public Class AreaTagType _ 	Inherits FamilySymbol ``` |

 

| Visual C++ |
| --- |
| ``` public ref class AreaTagType : public FamilySymbol ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  [Autodesk.Revit.DB InsertableObject](73d870e0-a408-719c-58bd-1fb2ab8f9e5b.htm)    
  [Autodesk.Revit.DB FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)    
  Autodesk.Revit.DB AreaTagType

# See Also

[AreaTagType Members](a17139c3-13c2-dd2d-938e-412f34c9a234.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78c15d1f-7c29-29bf-7b55-e416b21cb16b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadFamilySymbol Method (String, String)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Loads only a specified family type/symbol from a family file into the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool LoadFamilySymbol( 	string filename, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function LoadFamilySymbol ( _ 	filename As String, _ 	name As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool LoadFamilySymbol( 	String^ filename,  	String^ name ) ``` |

#### Parameters

filename
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The fully qualified filename of the Family file, usually ending in .rfa.

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The name of the type/symbol to be loaded, such as "W11x14".

#### Return Value

True if the family type/symbol was loaded successfully into the project, otherwise False.

# Remarks

This function supports loading of types/symbols stored in the family, or those available in the family Type Catalog file.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when filename or name is    a null reference (  Nothing  in Visual Basic)  or empty. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[LoadFamilySymbol Overload](7c99a858-3e0e-e63b-3754-996f98d1bc2f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78c1ea60-254d-0e8b-bd26-c099ea7129d7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetKeys Method

---



|  |
| --- |
| [ExportLinetypeTable Class](136c6197-2f4c-5686-e70c-09cee48b71ad.htm)   [See Also](#seeAlsoToggle) |

Gets all the keys stored in the map.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IList<ExportLinetypeKey> GetKeys() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetKeys As IList(Of ExportLinetypeKey) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ExportLinetypeKey^>^ GetKeys() ``` |

#### Return Value

The keys.

# See Also

[ExportLinetypeTable Class](136c6197-2f4c-5686-e70c-09cee48b71ad.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78c58be5-64f9-fef3-8379-0445640c964f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.SheetFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](c4c42dd1-688c-a0d5-81e9-7331024e138c.htm)   [See Also](#seeAlsoToggle) |

Failures about Sheet.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class SheetFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class SheetFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SheetFailures abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BuiltInFailures SheetFailures

# See Also

[BuiltInFailures SheetFailures Members](c4c42dd1-688c-a0d5-81e9-7331024e138c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78cc4aad-1d3d-587c-6756-e0fdde30d23f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabFittingFailed Property

---



|  |
| --- |
| [BuiltInFailures PipingFailures Class](315ce880-e60a-1af9-bdf9-09ac738260c6.htm)   [See Also](#seeAlsoToggle) |

The Fabrication Fitting was invalid

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FabFittingFailed { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabFittingFailed As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FabFittingFailed { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures PipingFailures Class](315ce880-e60a-1af9-bdf9-09ac738260c6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78cdcbbd-b322-c6e7-1465-29f7cc300fce.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ComponentRotation Property

---



|  |
| --- |
| [DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)   [See Also](#seeAlsoToggle) |

The rotation of the pattern by a multiple of 90 degrees.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ComponentRotation ComponentRotation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ComponentRotation As ComponentRotation 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ComponentRotation ComponentRotation { 	ComponentRotation get (); 	void set (ComponentRotation value); } ``` |

# Remarks

This property has no effect unless a pattern is selected (the ObjectType property is not    a null reference (  Nothing  in Visual Basic)  ).

# See Also

[DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78d0d082-d68d-aa07-2b5e-1e67d5322050.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetWorksharingOptions Method

---



|  |
| --- |
| [SaveAsOptions Class](f8eecf56-8b25-4140-d66e-c87f0d664ee1.htm)   [See Also](#seeAlsoToggle) |

Gets Worksharing options for SaveAs.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public WorksharingSaveAsOptions GetWorksharingOptions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetWorksharingOptions As WorksharingSaveAsOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: WorksharingSaveAsOptions^ GetWorksharingOptions() ``` |

#### Return Value

Defaults to    a null reference (  Nothing  in Visual Basic)  . For a workshared model, if    a null reference (  Nothing  in Visual Basic)  default values for WorksharingSaveAsOptions are used.

# See Also

[SaveAsOptions Class](f8eecf56-8b25-4140-d66e-c87f0d664ee1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78d27a7c-e5eb-6029-2fd4-4287cc84f09d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanModifyDetailLevel Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Check if Detail Level can be modified.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool CanModifyDetailLevel() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanModifyDetailLevel As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanModifyDetailLevel() ``` |

#### Return Value

True if Detail Level can be modified.

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78d4bd05-a40c-57f5-b49c-ee564de352a1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [TransactWithCentralOptions Class](f5da22fa-55ee-9196-cafd-5323d8e9ca0a.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [TransactWithCentralOptions](f5da22fa-55ee-9196-cafd-5323d8e9ca0a.htm)

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

[TransactWithCentralOptions Class](f5da22fa-55ee-9196-cafd-5323d8e9ca0a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78d7a145-5b3c-c82f-6bec-85bb14b00cf5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CrossSection Property

---



|  |
| --- |
| [Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)   [See Also](#seeAlsoToggle) |

Obtain the Wall Cross-section for this wall.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public WallCrossSection CrossSection { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CrossSection As WallCrossSection 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property WallCrossSection CrossSection { 	WallCrossSection get (); 	void set (WallCrossSection value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The current wall does not support the cross section wallCrossSection. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78d92aaf-3be7-4fef-530d-73bf9aa5e64a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HvacRoughness Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Roughness, in discipline HVAC.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId HvacRoughness { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property HvacRoughness As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ HvacRoughness { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78db7785-7069-4511-747e-ea0de2702e8d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCouplerPositionTransform Method

---



|  |
| --- |
| [RebarCoupler Class](af258367-f0c5-e4d3-f863-1733d7bf6b30.htm)   [See Also](#seeAlsoToggle) |

Return a transform representing the relative position of the coupler at index couplerPositionIndex in the set.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public Transform GetCouplerPositionTransform( 	int couplerPositionIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCouplerPositionTransform ( _ 	couplerPositionIndex As Integer _ ) As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform^ GetCouplerPositionTransform( 	int couplerPositionIndex ) ``` |

#### Parameters

couplerPositionIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     An index between 0 and (CouplerQuantity-1).

#### Return Value

Returns a transformation that is composed from : - a translation from (0, 0, 0) to coupler origin - a rotation that will align the coupler with the bar segment on which it stays.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | couplerPositionIndex is not in the range [ 0, CouplerQuantity-1 ]. |

# See Also

[RebarCoupler Class](af258367-f0c5-e4d3-f863-1733d7bf6b30.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__78dbf422-1001-5b4e-2251-a659b1af8e44.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Disconnects Property

---



|  |
| --- |
| [ConfigurationReloadInfo Class](f19d2d1f-191d-ec90-4b07-20c9307bf537.htm)   [See Also](#seeAlsoToggle) |

The number of disconnections caused by the reload.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public int Disconnects { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Disconnects As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int Disconnects { 	int get (); } ``` |

# See Also

[ConfigurationReloadInfo Class](f19d2d1f-191d-ec90-4b07-20c9307bf537.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78dc43d4-3690-ebcf-1841-20b915b56737.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotAddToOptionsWarn Property

---



|  |
| --- |
| [BuiltInFailures DesignOptionFailures Class](306b7ebc-5d5e-e53f-d5e4-9a5da4162068.htm)   [See Also](#seeAlsoToggle) |

Elements can't be added to Option Set

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotAddToOptionsWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotAddToOptionsWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotAddToOptionsWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DesignOptionFailures Class](306b7ebc-5d5e-e53f-d5e4-9a5da4162068.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78e61831-faee-943a-43ef-d4d8822c973f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MassZoneVolume Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Mass Zone Volume"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MassZoneVolume { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MassZoneVolume As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MassZoneVolume { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78ecd40f-36fc-662f-dac8-afc684869f26.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HelpId Property

---



|  |
| --- |
| [DialogBoxData Class](41f22b16-a68b-8c19-53f6-de079feb756c.htm)   [See Also](#seeAlsoToggle) |

An ID that represents the dialog that has been displayed.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int HelpId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HelpId As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int HelpId { 	int get (); } ``` |

# Remarks

Use this ID within your application to key suitable responses for the dialog. Note: this id is not guaranteed to remain stable for different builds of Autodesk Revit.

# See Also

[DialogBoxData Class](41f22b16-a68b-8c19-53f6-de079feb756c.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__78f59d6a-8d6b-cdd9-f045-535e64c007bc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveParameter Method

---



|  |
| --- |
| [RebarShapeDefinition Class](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)   [See Also](#seeAlsoToggle) |

Remove the parameter from the definition.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public void RemoveParameter( 	ElementId paramId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveParameter ( _ 	paramId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveParameter( 	ElementId^ paramId ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of a parameter in the definition.

# Remarks

If the definition does not have the parameter, the method does nothing.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarShapeDefinition Class](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__78f5b5dc-922d-0a67-c3dc-b787bcfb0403.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaxSegmentAngle Property

---



|  |
| --- |
| [Sweep Class](ed383459-badd-2323-4f73-0d94fd76ce0f.htm)   [See Also](#seeAlsoToggle) |

The maximum segment angle of the sweep in radians.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double MaxSegmentAngle { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MaxSegmentAngle As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double MaxSegmentAngle { 	double get (); 	void set (double value); } ``` |

# Remarks

This property is used to retrieve/set the maximum segment angle of the sweep. It is settable only when the trajectory segmentation is enabled.

# See Also

[Sweep Class](ed383459-badd-2323-4f73-0d94fd76ce0f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__78f898b0-8edf-469f-d79e-7e825d9942d7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewScale Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Scale Value 1:"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ViewScale { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewScale As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ViewScale { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79a38981-645b-919d-032e-bf36d47e11f1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanApplyColorFillScheme Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Checks if the id can be applied as the scheme id of specified category to this view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public bool CanApplyColorFillScheme( 	ElementId categoryId, 	ElementId schemeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanApplyColorFillScheme ( _ 	categoryId As ElementId, _ 	schemeId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanApplyColorFillScheme( 	ElementId^ categoryId,  	ElementId^ schemeId ) ``` |

#### Parameters

categoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of category.

schemeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of color fill scheme.

#### Return Value

True if the id can be applied as the scheme id of specified category in this view, false otherwise.

# Remarks

The input scheme id could be InvalidElementId to clear the scheme for the specified category.

Some examples of returnning false:

* The id is not a color fill scheme id.
* The specified category is not supported by this view.
* The category of scheme is not the same as the specified category.
* The view is area plan but the scheme category is not OST\_Areas, or their  [!:Autodesk::Revit::DB::AreaScheme]  are not the same.
* Etc.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79a468db-0482-7674-729f-aafb0ab04152.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### First Property

---



|  |
| --- |
| [VertexPair Class](3f0456e9-59a6-2c68-0f0c-d2355edb9693.htm)   [See Also](#seeAlsoToggle) |

Identifies the first index of VertexPair.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public int First { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property First As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int First { 	int get (); 	void set (int value); } ``` |

# See Also

[VertexPair Class](3f0456e9-59a6-2c68-0f0c-d2355edb9693.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79a85e01-c0c0-9efa-0a91-271b57cdc557.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RegisterService Method (IMultiServerService, ExternalServiceOptions, ExecutionPolicy)

---



|  |
| --- |
| [ExternalServiceRegistry Class](fa14442f-3d47-2c21-467c-6d19e4cc0d9e.htm)   [See Also](#seeAlsoToggle) |

A method to register a multi-server service.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static Guid RegisterService( 	IMultiServerService service, 	ExternalServiceOptions options, 	ExecutionPolicy policy ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function RegisterService ( _ 	service As IMultiServerService, _ 	options As ExternalServiceOptions, _ 	policy As ExecutionPolicy _ ) As Guid ``` |

 

| Visual C++ |
| --- |
| ``` public: static Guid RegisterService( 	IMultiServerService^ service,  	ExternalServiceOptions^ options,  	ExecutionPolicy policy ) ``` |

#### Parameters

service
:   Type:  [Autodesk.Revit.DB.ExternalService IMultiServerService](9704c8c0-2095-37e7-f17c-56d27ff44ed6.htm)    
     An instance of the external service class that implements IMultiServerService interface.

options
:   Type:  [Autodesk.Revit.DB.ExternalService ExternalServiceOptions](80467d42-3f13-de3e-cd06-bf3b43afefe0.htm)    
     Optional settings to control the service's behavior.

policy
:   Type:  [Autodesk.Revit.DB.ExternalService ExecutionPolicy](5234000e-cf74-d7aa-85ff-dcfbed63434b.htm)    
     Specifies how the service handles servers during its execution.

#### Return Value

An execution key to access the service when executing it.

# Remarks

Each service can only be registered once. Revit checks the Id of every service getting registered and throws an exception upon an attempt to register a service with an Id that already exists.

Services need to be registered before Revit ends its initialization. For external applications that means they have to register their services during OnStartup. This will give servers which need to register to services a chance to do so during the ApplicationInitialized event, which is raised after a successfully processing OnStartup routines.

A service can be registered as either recordable or non-recordable. It is expected that a service that is once registered as recordable will always be registered as recordable. Failure to comply with this policy may lead to data loss in some documents when they are opened in a Revit session with the service currently registered as non-recordable.

An application registering a service must specify a policy to follow when executing the service. Once set, the policy remain constant during the Revit session, but a different policy may be used next time, if there is ever a need for such a change. More about the various execution policies can be found in the description of the ExecutionPolicy enumerated type.

A service is supposed to be executed only by the application that registered it. To enforce this requirement, the registering method return an execution key (a Guid) that is required as an argument to ExecuteService methods. If the owner of a service allows executing it by anyone, it needs to register it as a public service (via the option argument). Once registered as public, The access key of the service can be obtained by any application, thus it can also be executed by any application. By default, a service is registered as private.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given service is not a valid implementation of ISingleServerService. -or- The given service does not return valid values from the interface methods. At least one of the Name, VendorId, Description, and ServiceId is either empty or invalid. -or- A service with this Id is either invalid or not unique. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Service cannot be registered because the registry of services has been already closed. All external services must be registered before the ApplicationInitialized event is raised. |

# See Also

[ExternalServiceRegistry Class](fa14442f-3d47-2c21-467c-6d19e4cc0d9e.htm)

[RegisterService Overload](6d690a5d-62c5-958c-842e-620a49421c1c.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)

<!-- Start of Syntax__79a92343-2342-8325-1b51-f12c4fb05481.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FormattedText Class

---



|  |
| --- |
| [Members](e74cf1df-845b-fcd2-01d3-005054467c53.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

FormattedText is used to create, edit and format text in a  [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)  or to query the text and format properties of a  [TextNode](9a06448a-1c82-7fd7-8be7-9113dc1ce86a.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public class FormattedText : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FormattedText _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FormattedText : IDisposable ``` |

# Remarks

An instance of FormattedText can be obtained from a  [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)  (See  **TextNote.GetFormattedText()**  ) or from a  [TextNode](9a06448a-1c82-7fd7-8be7-9113dc1ce86a.htm)  (See  **TextNode.GetFormattedText()**  )

It is also possible to create a new instance of FormattedText and assign it to a  [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)  (See  **TextNote.SetFormattedText()**  ) This will result in a  [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)  with text with the specified formatting applied

Formatted text can be used to:

* Create formatted text for a new  [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)
* Edit, Find and Replace text in an existing  [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)
* Modify formatting of text in an existing  [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)
* Or query the text and formatting a  [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)  or a  [TextNode](9a06448a-1c82-7fd7-8be7-9113dc1ce86a.htm)

Formatted text can be populated with plain text by using its constructor  [FormattedText(String)](86332d2f-1939-4985-f428-24ee8b19072e.htm)  that takes a string, or by using the  [SetPlainText(String)](b2efd1c2-7e1f-2def-f72b-a22066a8b415.htm)  method.

In addition, selected ranges of text can be added, removed, or replaced with the  [SetPlainText(TextRange, String)](ef85472c-c691-77f8-5823-33da6ea43832.htm)  method by specifying a  [TextRange](8a00baaf-8cb8-d9f0-e0a0-eaa5aa16e55e.htm)  .

Use the  [Find(String, Int32, Boolean, Boolean)](79034f02-9ca0-ebe5-8d16-112d674dbdb4.htm)  method to find the location of existing text.

Formatted text can have up to 30,000 characters. All characters, except the linefeed character ('\n'), are allowed. This means that you should not use the 'Environment.NewLine' property, since that includes a linefeed character. Use the carriage return character ('\r') to terminate a paragraph. And use a vertical tab character ('\v') to create a new line without terminating the paragraph.

Formatted text allows for individual characters to be formatted. The following formatting can be applied.

* Bold
* Italic
* Underline
* Superscript/Subscript
* All Caps

Use  [SetBoldStatus(TextRange, Boolean)](fd0eab6d-0808-63ff-3cb0-a014f2adbbd7.htm)  ) ,  [SetItalicStatus(TextRange, Boolean)](310407e6-1244-24cb-c033-e9620068e62e.htm)  ) ,  [SetUnderlineStatus(TextRange, Boolean)](d5f9ca3c-4631-ad4a-5a40-b7103611e254.htm)  ) ,  [SetSuperscriptStatus(TextRange, Boolean)](357540c0-f99c-94da-f3f3-585308c6543f.htm)  ) ,  [SetSubscriptStatus(TextRange, Boolean)](bc2efdbe-7706-0e4d-82ce-39ab7d039c7c.htm)  ) , or  [SetAllCapsStatus(TextRange, Boolean)](03a3a6c3-9195-25a1-abaa-641f00cbc930.htm)  ) to set the character formatting on a range of text.

Use  [GetBoldStatus(TextRange)](654707e3-5575-a8a5-8eaf-e83425f5c50d.htm)  ) ,  [GetItalicStatus(TextRange)](a4df0e88-31d5-4e75-fb17-d68ad22bf89d.htm)  ) ,  [GetUnderlineStatus(TextRange)](0ece8fda-443b-7247-9b1c-4eb493850344.htm)  ) ,  [GetSuperscriptStatus(TextRange)](3ad2a7db-b1c9-ba0e-661e-bb4117e3a538.htm)  ) ,  [GetSubscriptStatus(TextRange)](50803bb1-2ba6-63c5-0ddf-a0bf0f40c58c.htm)  ) , or  [GetAllCapsStatus(TextRange)](0e9f9439-eb01-6844-992a-2128ffddedef.htm)  ) to get the character formatting of a range of text.

Text can be broken up in paragraphs. Paragraphs are terminated by a carriage return character ('\r').

Each paragraph can be indented several levels deep. For each additional level the indentation increments by one tab size. The total indentation is the product of a tab size and the indent level. Use  [SetIndentLevel(TextRange, Int32)](a2e6561d-da40-b701-967f-aadbe6b153f5.htm)  to set the level of indenting up to a maximum indent level that can be obtained from  [GetMaximumIndentLevel](3f77a7ca-54e8-28b5-e1e6-cee57afd13e6.htm)  Use  [GetIndentLevel(TextRange)](2bb008be-f3b5-f0cd-bc1b-6879101ef84a.htm)  to find the indent level of a given range of text.

Note that the tab size is determined by the object that will contain the FormattedText.

In the case of a  [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)  the tab size is a property of the  [TextNoteType](2991b6af-daf6-463d-3796-8b83fdbd344f.htm)  returned from  **TextNote.TextNoteType**  . The tab size can be found by calling the  [Parameter Guid](2e852bc4-46c6-5598-cc45-0eaf38cf8973.htm)  with  [TEXT\_TAB\_SIZE](fb011c91-be7e-f737-28c7-3f1e1917a0e0.htm)  on the  [TextNoteType](2991b6af-daf6-463d-3796-8b83fdbd344f.htm)  obtained from the  [TextNote](ecc1ce1c-d754-96d0-35db-ca2d1d84c57c.htm)

In the case of a  [TextNode](9a06448a-1c82-7fd7-8be7-9113dc1ce86a.htm)  the tab size can be obtained from its  **TabSize**  property

Formatted text can also be used to create numbered or bulleted paragraphs with the  [SetListType(TextRange, ListType)](c0bb9933-9825-a28a-a09c-8b319f089b36.htm)  method.

The following  [ListType](7163554f-3446-22eb-afa4-5490d5df29c8.htm)  options are available:

* [Bullet](7163554f-3446-22eb-afa4-5490d5df29c8.htm)
* [ArabicNumbers](7163554f-3446-22eb-afa4-5490d5df29c8.htm)
* [LowerCaseLetters](7163554f-3446-22eb-afa4-5490d5df29c8.htm)
* [UpperCaseLetters](7163554f-3446-22eb-afa4-5490d5df29c8.htm)

Paragraphs with a  [ListType](7163554f-3446-22eb-afa4-5490d5df29c8.htm)  other than  [None](7163554f-3446-22eb-afa4-5490d5df29c8.htm)  are considered to be 'list' paragraphs. Consecutive list paragraphs with the same indentation level are treated as part of the same list. A list ends when a list paragraph is followed by

* a paragraph that has  [None](7163554f-3446-22eb-afa4-5490d5df29c8.htm)
* or a list paragraph that has a lower indentation level, i.e. is indented less. (See  [GetIndentLevel(TextRange)](2bb008be-f3b5-f0cd-bc1b-6879101ef84a.htm)  )

Note that a list will continue uninterrupted after list paragraphs that have higher indentation level. These paragraphs form a 'sub-list' of the list they interrupt. Sub-lists can have their own sub-sub-lists. The nesting level is only limited by the maximum indent level. Using  [SetIndentLevel(TextRange, Int32)](a2e6561d-da40-b701-967f-aadbe6b153f5.htm)  it is therefore possible to create multi-level lists.

FormattedText will keep lists consistent. That means that list paragraphs will automatically get sequential numbers or letters. It also means that if the list type of one of the paragraphs in a list is changed then that change is propagated to all the paragraphs in that list. Note that this will not affect the list type of any nested sub-lists.

Use a vertical tab character ('\v') to insert a line without a bullet or number. Since this does not end the paragraph this will allow the list to continue to the next paragraph.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void FormatText(TextNote textNote)
{
    // TextNote created with "New sample text"
    FormattedText formatText = textNote.GetFormattedText();

    // italicize "New"
    TextRange range = new TextRange(0, 3);
    formatText.SetItalicStatus(range, true);

    // make "sample" bold
    range = formatText.Find("sample", 0, false, true);
    if (range.Length > 0)
        formatText.SetBoldStatus(range, true);

    // make "text" underlined
    range = formatText.Find("text", 0, false, true);
    if (range.Length > 0)
        formatText.SetUnderlineStatus(range, true);

    // make all text uppercase
    formatText.SetAllCapsStatus(true);

    textNote.SetFormattedText(formatText);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub FormatText(textNote As TextNote)
    ' TextNote created with "New sample text"
    Dim formatText__1 As FormattedText = textNote.GetFormattedText()

    ' italicize "New"
    Dim range As New TextRange(0, 3)
    formatText__1.SetItalicStatus(range, True)

    ' make "sample" bold
    range = formatText__1.Find("sample", 0, False, True)
    If range.Length > 0 Then
        formatText__1.SetBoldStatus(range, True)
    End If

    ' make "text" underlined
    range = formatText__1.Find("text", 0, False, True)
    If range.Length > 0 Then
        formatText__1.SetUnderlineStatus(range, True)
    End If

    ' make all text uppercase
    formatText__1.SetAllCapsStatus(True)

    textNote.SetFormattedText(formatText__1)
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB FormattedText

# See Also

[FormattedText Members](e74cf1df-845b-fcd2-01d3-005054467c53.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79aa07cd-51f9-4ddf-75e0-d5f346197983.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [UpdaterId Class](16a9604f-51bd-ce34-f145-17ae06b7c1cf.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [UpdaterId](16a9604f-51bd-ce34-f145-17ae06b7c1cf.htm)

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

[UpdaterId Class](16a9604f-51bd-ce34-f145-17ae06b7c1cf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79b1cf49-81c6-43b5-391c-a3c29f84edd8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SystemType Property

---



|  |
| --- |
| [ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)   [See Also](#seeAlsoToggle) |

The Electrical System Type of the Electrical System.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElectricalSystemType SystemType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property SystemType As ElectricalSystemType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElectricalSystemType SystemType { 	ElectricalSystemType get (); } ``` |

# Remarks

This property is used to retrieve the Electrical System Type of the Electrical System.

# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__79b61601-f5ee-3cc4-aefe-a6bf6750fc54.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DeleteProfile Method

---



|  |
| --- |
| [Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)   [See Also](#seeAlsoToggle) |

Delete a profile of the form.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void DeleteProfile( 	int profileIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub DeleteProfile ( _ 	profileIndex As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void DeleteProfile( 	int profileIndex ) ``` |

#### Parameters

profileIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index to specify the profile.

# See Also

[Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79b811b5-a7cd-2e6b-bf62-a4942ea57ef9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ZVector Property

---



|  |
| --- |
| [CylindricalHelix Class](fdaa7f4a-e680-8d7e-3a9b-677b082432f5.htm)   [See Also](#seeAlsoToggle) |

The Z direction vector, which is same as the axis direction vector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ ZVector { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ZVector As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ ZVector { 	XYZ^ get (); } ``` |

# See Also

[CylindricalHelix Class](fdaa7f4a-e680-8d7e-3a9b-677b082432f5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79b99ce2-1540-5da8-3f21-2fbb96eb6689.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WireConduitTypeSet Constructor

---



|  |
| --- |
| [WireConduitTypeSet Class](08d0cc98-554e-7f81-cb7c-f827d925de7d.htm)   [See Also](#seeAlsoToggle) |

Initializes a new instance of the  [WireConduitTypeSet](08d0cc98-554e-7f81-cb7c-f827d925de7d.htm)  class

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public WireConduitTypeSet() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: WireConduitTypeSet() ``` |

# See Also

[WireConduitTypeSet Class](08d0cc98-554e-7f81-cb7c-f827d925de7d.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__79baf023-e8b6-dfc2-d598-7d5eb434260a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetCellParamIdAndCategoryId Method (Int32, Int32, ElementId, ElementId)

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Sets a cell's category and parameter Id

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetCellParamIdAndCategoryId( 	int nRow, 	int nCol, 	ElementId paramId, 	ElementId categoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetCellParamIdAndCategoryId ( _ 	nRow As Integer, _ 	nCol As Integer, _ 	paramId As ElementId, _ 	categoryId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetCellParamIdAndCategoryId( 	int nRow,  	int nCol,  	ElementId^ paramId,  	ElementId^ categoryId ) ``` |

#### Parameters

nRow
:   Type:  System Int32

nCol
:   Type:  System Int32

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

categoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given row number nRow is invalid. -or- The given column number nCol is invalid. -or- The paramId or categoryId is not valid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[SetCellParamIdAndCategoryId Overload](0195eb8d-b061-f29a-05cb-0c4eca0cf5c0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79bbfd8e-1226-602b-0355-3a20c6ef3d89.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextNoteLeaderTypes Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Types of text-note leaders

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum TextNoteLeaderTypes ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration TextNoteLeaderTypes ``` |

 

| Visual C++ |
| --- |
| ``` public enum class TextNoteLeaderTypes ``` |

# Members

| Member name | Description |
| --- | --- |
| TNLT\_STRAIGHT\_L | A line leader attached from the left side of a text element |
| TNLT\_STRAIGHT\_R | A line leader attached from the right side of a text element |
| TNLT\_ARC\_L | An arc leader attached from the left side of a text element |
| TNLT\_ARC\_R | An arc leader attached from the right side of a text element |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79bc72c0-378a-d4a5-bcad-56dd30e4dd73.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddCurve Method

---



|  |
| --- |
| [WireframeBuilder Class](ae9e719b-5d13-45c5-22d8-49111edfcfc4.htm)   [See Also](#seeAlsoToggle) |

Add a curve to the shape representation stored in this WireframeBuilder.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void AddCurve( 	Curve GCurve ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddCurve ( _ 	GCurve As Curve _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddCurve( 	Curve^ GCurve ) ``` |

#### Parameters

GCurve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The curve to be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | GCurve is not acceptable for a wireframe shape representation. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[WireframeBuilder Class](ae9e719b-5d13-45c5-22d8-49111edfcfc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79bcd6b3-e336-3599-a3aa-bf49dfe8c82a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsDuctTopElevation Property

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
| ``` public static ForgeTypeId RbsDuctTopElevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsDuctTopElevation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsDuctTopElevation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79bdeb0b-5682-ee6c-8505-8f21579b28eb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EnergyAnalysisMasszoneCoreoffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Perimeter Zone Depth"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId EnergyAnalysisMasszoneCoreoffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property EnergyAnalysisMasszoneCoreoffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ EnergyAnalysisMasszoneCoreoffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79c9d272-1a5d-32f2-33b6-fce3e21dc562.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TestCell Method

---



|  |
| --- |
| [PointCloudFilter Class](ca6f916b-2eba-f8e5-8939-1c063330c886.htm)   [See Also](#seeAlsoToggle) |

Checks whether a given cell, i.e. a box aligned with the XYZ axes, is inside, outside or on the border of the volume of interest.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public int TestCell( 	XYZ min, 	XYZ max ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function TestCell ( _ 	min As XYZ, _ 	max As XYZ _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int TestCell( 	XYZ^ min,  	XYZ^ max ) ``` |

#### Parameters

min
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The lower corner of the cell.

max
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The upper corner of the cell.

#### Return Value

* -1 -- The cell is entirely rejected.
* 0 -- The cell partially belongs to the volume of interest. Use PrepareForCell() and TestPoint() to evaluate individual points.
* 1 -- The cell is fully accepted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PointCloudFilter Class](ca6f916b-2eba-f8e5-8939-1c063330c886.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__79cac0a7-c47c-724d-33f3-e7bc0b3af392.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NoAvailableMatchingConnector Property

---



|  |
| --- |
| [BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)   [See Also](#seeAlsoToggle) |

Cannot add [Element] to Circuit. There is no available connector matching the Type ([Type Name]) for the Circuit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NoAvailableMatchingConnector { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NoAvailableMatchingConnector As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NoAvailableMatchingConnector { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79d10f4e-9ab1-adfb-f89d-c5c754712b23.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCuttingVoidInstances Method

---



|  |
| --- |
| [InstanceVoidCutUtils Class](68b4818a-d737-be1e-0347-ebe305fe3b70.htm)   [See Also](#seeAlsoToggle) |

Return ids of the instances with unattached voids cutting the element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetCuttingVoidInstances( 	Element element ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetCuttingVoidInstances ( _ 	element As Element _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetCuttingVoidInstances( 	Element^ element ) ``` |

#### Parameters

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element being cut

#### Return Value

Ids of instances with unattached voids that cut this element

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[InstanceVoidCutUtils Class](68b4818a-d737-be1e-0347-ebe305fe3b70.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79da5994-50ed-171f-adf2-9a6550c898db.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetHostId Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

The element that contains the rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public void SetHostId( 	Document doc, 	ElementId hostId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetHostId ( _ 	doc As Document, _ 	hostId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetHostId( 	Document^ doc,  	ElementId^ hostId ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing both this element and the host element.

hostId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element that the rebar object belongs to, such as a structural wall, floor, foundation, beam, brace or column. The rebar does not need to be strictly inside the host, but it must be assigned to one host element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | hostId is not a legal Rebar host (see the RebarHostData class). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__79dad9e7-85e8-34ac-6255-12ef9116afa2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IndexBuffer Constructor

---



|  |
| --- |
| [IndexBuffer Class](186f6b15-38c7-cee7-6163-396cfdea43ee.htm)   [See Also](#seeAlsoToggle) |

Constructs the index buffer with the given capacity, measured in short integers.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public IndexBuffer( 	int sizeInShortInts ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	sizeInShortInts As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: IndexBuffer( 	int sizeInShortInts ) ``` |

#### Parameters

sizeInShortInts
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The number of short integers that the buffer can contain.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This IndexBuffer is not available because Revit is not currently rendering. In general, this IndexBuffer must be used in the scope of the RenderScene() callback of IDirectContext3DServer. |

# See Also

[IndexBuffer Class](186f6b15-38c7-cee7-6163-396cfdea43ee.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__79e15a6b-3a5d-3aa1-c13a-5155356c5842.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetOptions Method

---



|  |
| --- |
| [ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)   [See Also](#seeAlsoToggle) |

Gets the collection of named options set by the exporter client.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public IDictionary<string, string> GetOptions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetOptions As IDictionary(Of String, String) ``` |

 

| Visual C++ |
| --- |
| ``` public: IDictionary<String^, String^>^ GetOptions() ``` |

#### Return Value

The collection of named options.

# See Also

[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__79e1f35a-6455-2755-1aeb-afe9f982cf2c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsRuntypeUndersideSurfaceType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Underside Surface": Underside Surface

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsRuntypeUndersideSurfaceType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsRuntypeUndersideSurfaceType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsRuntypeUndersideSurfaceType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79e54362-cc13-8068-99cc-2e7216d5beb6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [GroupSetIterator Class](da2e2718-c83a-f386-ae9c-beca78f9a728.htm)   [See Also](#seeAlsoToggle) |

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

[GroupSetIterator Class](da2e2718-c83a-f386-ae9c-beca78f9a728.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79e692ab-e01d-f723-158a-1951f40aa2b6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SKPImportOptions Class

---



|  |
| --- |
| [Members](9e5f9329-cb48-d600-9fec-1e70271d9707.htm)   [See Also](#seeAlsoToggle) |

The import options used to import SKP format files.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class SKPImportOptions : BaseImportOptions ``` |

 

| Visual Basic |
| --- |
| ``` Public Class SKPImportOptions _ 	Inherits BaseImportOptions ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SKPImportOptions : public BaseImportOptions ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB BaseImportOptions](75898e94-cff4-fb64-c613-9596599444c4.htm)    
  Autodesk.Revit.DB SKPImportOptions

# See Also

[SKPImportOptions Members](9e5f9329-cb48-d600-9fec-1e70271d9707.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79e6f8f6-009a-ea78-58cf-07ee28769a72.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecPanelTotalestloadPowerParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Power Total Estimated Demand"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecPanelTotalestloadPowerParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecPanelTotalestloadPowerParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecPanelTotalestloadPowerParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79e785de-d4e7-9a84-ab8c-eece28c42b1f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSummarySectionHidden Property

---



|  |
| --- |
| [PanelScheduleData Class](d24fcc19-3240-8f07-68ca-ce7b62f7aac3.htm)   [See Also](#seeAlsoToggle) |

True if the user wishes to hide the summary section; setting this value must go through the appropriate update function

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsSummarySectionHidden { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsSummarySectionHidden As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsSummarySectionHidden { 	bool get (); } ``` |

# See Also

[PanelScheduleData Class](d24fcc19-3240-8f07-68ca-ce7b62f7aac3.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__79e88553-e0a3-a2f7-4c6f-958e31313d1c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [SpatialElementBoundarySubface Class](0a8f3677-3320-a8a5-674e-b0d055ac6671.htm)   [See Also](#seeAlsoToggle) |

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

[SpatialElementBoundarySubface Class](0a8f3677-3320-a8a5-674e-b0d055ac6671.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79ea02a9-cc7c-17e7-bedf-bdea40069dc9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewReferencingSheet Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Referencing Sheet"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ViewReferencingSheet { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewReferencingSheet As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ViewReferencingSheet { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79eb0f31-fe7c-16c9-0825-79c73c4f9fff.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [RebarShapeMultiplanarDefinition Class](47a3135c-ce53-c041-f551-0795767eaa41.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
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

[RebarShapeMultiplanarDefinition Class](47a3135c-ce53-c041-f551-0795767eaa41.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__79f2d4c0-afb9-316c-44ac-afb82ec66e05.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralAttachmentEndType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"End Attachment Type"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralAttachmentEndType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralAttachmentEndType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralAttachmentEndType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79f57488-64c6-1630-02a0-b80ceedf510b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BendRadius Property

---



|  |
| --- |
| [RebarBendData Class](027b5619-ad82-74b3-1d78-efe86a1ef96b.htm)   [See Also](#seeAlsoToggle) |

The radius of all fillets, except hook fillets, in the Rebar shape.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double BendRadius { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BendRadius As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double BendRadius { 	double get (); 	void set (double value); } ``` |

# Remarks

Inner radius, not centerline

# See Also

[RebarBendData Class](027b5619-ad82-74b3-1d78-efe86a1ef96b.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__79f5c5cd-1f93-9a7b-e8dc-51ad3ddb4c6a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, ExternalResourceReference, RevitLinkOptions)

---



|  |
| --- |
| [RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)   [See Also](#seeAlsoToggle) |

Creates a new Revit link type from an external resource reference and loads the linked document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static LinkLoadResult Create( 	Document document, 	ExternalResourceReference resourceReference, 	RevitLinkOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	resourceReference As ExternalResourceReference, _ 	options As RevitLinkOptions _ ) As LinkLoadResult ``` |

 

| Visual C++ |
| --- |
| ``` public: static LinkLoadResult^ Create( 	Document^ document,  	ExternalResourceReference^ resourceReference,  	RevitLinkOptions^ options ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to create the Revit link.

resourceReference
:   Type:  [Autodesk.Revit.DB ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.htm)    
     An external resource reference describing the source of the linked Revit document.

options
:   Type:  [Autodesk.Revit.DB RevitLinkOptions](3f710983-5a4d-d515-a633-12b06a419b30.htm)    
     An options class for loading Revit links. The path type information will be ignored.

#### Return Value

An object containing the results of creating and loading the Revit link type. It contains the ElementId of the new link.

# Remarks

This function regenerates the input document.

Only the WorksetConfiguration information in the options argument will be used. The path type information will be ignored.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- The server referenced by the ExternalResourceReference does not exist or does not implement IExternalResourceServer. -or- The server referenced by the ExternalResourceReference cannot support Revit links. -or- The ExternalResourceReference (resourceReference) is not in a format that is supported by its server. -or- The link type referred to by the ExternalResourceReference "resourceReference" already exists in the document. You cannot create another copy of the link type. You can create instances with RevitLinkInstance.Create(), or reload the link using RevitLinkType.Reload(). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Revit cannot customize worksets for this model. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)

[Create Overload](4cdb6058-0ae0-d584-24f7-52b72af617bc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79f73965-9ca2-42d9-8473-b799a01bb961.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProfileId Property

---



|  |
| --- |
| [ContinuousRailType Class](0f4641e3-74e0-0a8e-eb56-fb6f9904b173.htm)   [See Also](#seeAlsoToggle) |

The id of the profile of the rail

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId ProfileId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ProfileId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ProfileId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The profileId is neither a valid element id nor invalidElementId. -or- When setting this property: The profileId is not a valid profile symbol for continuous rail. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ContinuousRailType Class](0f4641e3-74e0-0a8e-eb56-fb6f9904b173.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__79fc794c-dbde-63dc-fdce-01f0a032a07e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundaryZRotationSpring Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Z Rotation - Spring"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BoundaryZRotationSpring { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BoundaryZRotationSpring As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BoundaryZRotationSpring { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__79ffc8b2-8b6a-ee3f-6e76-6ba002128bac.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [SystemZoneData Class](e05367c4-2f7f-2760-a744-c1f7bca68424.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of a system-zone data domain class.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public static SystemZoneData Create() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create As SystemZoneData ``` |

 

| Visual C++ |
| --- |
| ``` public: static SystemZoneData^ Create() ``` |

#### Return Value

The newly created data domain instance.

# See Also

[SystemZoneData Class](e05367c4-2f7f-2760-a744-c1f7bca68424.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__80a92ad0-9f77-fb0d-3858-5cfc2c0f598b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanViewDirection Property

---



|  |
| --- |
| [ViewFamilyType Class](e0edeb6d-1627-3e3f-e386-be182a9dd8cb.htm)   [See Also](#seeAlsoToggle) |

The PlanViewDirection of this view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public PlanViewDirection PlanViewDirection { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PlanViewDirection As PlanViewDirection 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property PlanViewDirection PlanViewDirection { 	PlanViewDirection get (); 	void set (PlanViewDirection value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: PlanViewDirection cannot be set to Undefined |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: View must be a Structural Plan |

# See Also

[ViewFamilyType Class](e0edeb6d-1627-3e3f-e386-be182a9dd8cb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80ac3f63-6383-ba62-380f-0e61b98e8dd7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMinimumNumberOfDigits Method

---



|  |
| --- |
| [NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)   [See Also](#seeAlsoToggle) |

Returns the minimum number of digits to be used for formating the Number parameter of all enumerable elements of the given document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static int GetMinimumNumberOfDigits( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetMinimumNumberOfDigits ( _ 	document As Document _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: static int GetMinimumNumberOfDigits( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document this value is going to be applied to.

#### Return Value

The current number of formatting digits

# Remarks

The number is used by all numbering schemas in the document.

The value can be modified by using the  [SetMinimumNumberOfDigits(Document, Int32)](5b78eda1-9ad6-9c9d-bfe4-bdb6752c262f.htm)  method.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80b41c5d-8532-74bd-4171-b098a970d530.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralElevationAtTop Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Elevation at Top"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralElevationAtTop { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralElevationAtTop As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralElevationAtTop { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80b5319c-2076-8282-51ef-9c79acba41e8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [WaterLoopData Class](2860db31-4947-5332-27c2-fac4caf7cc12.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [WaterLoopData](2860db31-4947-5332-27c2-fac4caf7cc12.htm)

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

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

 IDisposable Dispose

# See Also

[WaterLoopData Class](2860db31-4947-5332-27c2-fac4caf7cc12.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__80ba5187-56f3-855b-8a90-c3c07481f57a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RasterQualityType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing the options for raster quality.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum RasterQualityType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration RasterQualityType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class RasterQualityType ``` |

# Members

| Member name | Description |
| --- | --- |
| Low | The type of Raster Quality is Low. |
| Medium | The type of Raster Quality is Medium. |
| High | The type of Raster Quality is High. |
| Presentation | The type of Raster Quality is Presentation. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80be01c2-73e0-c7d1-6265-46fb900c90cb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationPartCannotChangeTypeBadDimError Property

---



|  |
| --- |
| [BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)   [See Also](#seeAlsoToggle) |

The selected fitting(s) cannot successfully change the type. The newly selected fabrication part may have badly configured dimensions or be constrained due to connected fitting(s). You may try to disconnect the connections on the fitting(s) and try again.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FabricationPartCannotChangeTypeBadDimError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationPartCannotChangeTypeBadDimError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FabricationPartCannotChangeTypeBadDimError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80be14d9-abda-9538-56ac-f198550d11ae.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetExternalDefinitionForElementId Method

---



|  |
| --- |
| [RebarShapeParameters Class](8161950e-3ac7-0f8b-cc9f-2565a2d0afd9.htm)   [See Also](#seeAlsoToggle) |

Seach a DefinitionFile for the ExternalDefinition corresponding to a parameter in a document.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static ExternalDefinition GetExternalDefinitionForElementId( 	Document doc, 	ElementId paramId, 	DefinitionFile definitionFile ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetExternalDefinitionForElementId ( _ 	doc As Document, _ 	paramId As ElementId, _ 	definitionFile As DefinitionFile _ ) As ExternalDefinition ``` |

 

| Visual C++ |
| --- |
| ``` public: static ExternalDefinition^ GetExternalDefinitionForElementId( 	Document^ doc,  	ElementId^ paramId,  	DefinitionFile^ definitionFile ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     A document.

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of a shared parameter in the document.

definitionFile
:   Type:  [Autodesk.Revit.DB DefinitionFile](c074c52e-a483-51ca-476c-55990a06295c.htm)    
     A database of shared parameters.

#### Return Value

The external parameter corresponding to the parameter's ElementId, or null if the Id does not correspond to an external parameter, or the parameter is not in the definition file.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[RebarShapeParameters Class](8161950e-3ac7-0f8b-cc9f-2565a2d0afd9.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__80be3c21-c088-51c7-7d4a-8df7a2554062.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [RebarShapeConstraint Class](21c642f3-7aae-759b-4aac-ff4e2dd77d57.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [RebarShapeConstraint](21c642f3-7aae-759b-4aac-ff4e2dd77d57.htm)

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
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

[RebarShapeConstraint Class](21c642f3-7aae-759b-4aac-ff4e2dd77d57.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__80c6d4cf-d375-5b55-e04a-1a6bd8e43cf5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetValidFamiliesForNoteBlock Method

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

Gets a list of families that can be used for a note block.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetValidFamiliesForNoteBlock( 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetValidFamiliesForNoteBlock ( _ 	document As Document _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetValidFamiliesForNoteBlock( 	Document^ document ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

#### Return Value

The IDs of all valid families.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80cc36e5-c614-fd16-9d75-0879526bb2cb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StationingSurveyFeet Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

US survey feet.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StationingSurveyFeet { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StationingSurveyFeet As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StationingSurveyFeet { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80cccf6d-e10b-8c8b-f536-b3d2e9443a75.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Width Property

---



|  |
| --- |
| [ImageType Class](c6213f81-8dc8-158e-0522-70f87e9bdbb9.htm)   [See Also](#seeAlsoToggle) |

The horizontal size of the image

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public double Width { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Width As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Width { 	double get (); } ``` |

# See Also

[ImageType Class](c6213f81-8dc8-158e-0522-70f87e9bdbb9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80d0b613-3897-a319-ddc6-36ca077cd323.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BorderTopLineStyle Property

---



|  |
| --- |
| [TableCellStyleOverrideOptions Class](ac17323d-f5cf-8a72-34e0-4632173daf52.htm)   [See Also](#seeAlsoToggle) |

Indicates if the border top line style characteristic is overridden.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool BorderTopLineStyle { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BorderTopLineStyle As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool BorderTopLineStyle { 	bool get (); 	void set (bool value); } ``` |

# See Also

[TableCellStyleOverrideOptions Class](ac17323d-f5cf-8a72-34e0-4632173daf52.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80d20187-97ea-f6c0-a3a8-d5545e0b3863.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanViewPlane Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Locations where view range offsets can be specified.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum PlanViewPlane ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration PlanViewPlane ``` |

 

| Visual C++ |
| --- |
| ``` public enum class PlanViewPlane ``` |

# Members

| Member name | Description |
| --- | --- |
| CutPlane | Cut Plane |
| TopClipPlane | Top Clip Plane |
| BottomClipPlane | Bottom Clip Plane |
| ViewDepthPlane | View Depth Plane |
| UnderlayBottom | Underlay Bottom Plane |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80d2b03f-23a5-1357-fe01-9843d79bb483.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ServiceAbbreviation Property

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

The associated service abbreviation for the fabrication service.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public string ServiceAbbreviation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ServiceAbbreviation As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ ServiceAbbreviation { 	String^ get (); } ``` |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80d4fcf9-ada4-3a29-3662-837f9403a358.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaterialAssetParamExternalMaterialId Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"External Material ID"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MaterialAssetParamExternalMaterialId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MaterialAssetParamExternalMaterialId As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MaterialAssetParamExternalMaterialId { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80d7f252-f52e-96cd-7704-58cc40d68957.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [KeyBasedTreeEntriesLoadResults Class](f5208754-8b50-cfff-f2ca-f31a0645fbd5.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [KeyBasedTreeEntriesLoadResults](f5208754-8b50-cfff-f2ca-f31a0645fbd5.htm)

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

[KeyBasedTreeEntriesLoadResults Class](f5208754-8b50-cfff-f2ca-f31a0645fbd5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80d96216-f5fd-0aa7-954b-33b7b0ddcf9b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Rehost Method (SketchPlane, XYZ)

---



|  |
| --- |
| [Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)   [See Also](#seeAlsoToggle) |

Rehost Form to sketch plane

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void Rehost( 	SketchPlane sketchPlane, 	XYZ location ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Rehost ( _ 	sketchPlane As SketchPlane, _ 	location As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Rehost( 	SketchPlane^ sketchPlane,  	XYZ^ location ) ``` |

#### Parameters

sketchPlane
:   Type:  [Autodesk.Revit.DB SketchPlane](ba104029-d175-7e75-caef-667a4281f4af.htm)    
     The sketch plane on which to rehost the form.

location
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The location to which to Rehost the form.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the sketchPlane or location is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when rehosting Form failed. |

# See Also

[Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)

[Rehost Overload](2ec8400f-ad19-2b74-92bc-bad900c5e085.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80db1b02-e36c-1c4e-1788-fd92b0d20a1f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetStatus Method

---



|  |
| --- |
| [TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)   [See Also](#seeAlsoToggle) |

Gets the current status of the transaction group.

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

The current status of the transaction group.

# See Also

[TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80df7346-e018-338f-b41b-b5d95aebd53a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewDetailLevelIsHighInLargeView Property

---



|  |
| --- |
| [BuiltInFailures PerformanceFailures Class](d008a572-b1aa-1e46-0c4e-f760c50776fd.htm)   [See Also](#seeAlsoToggle) |

A large view has view detail level set to medium or coarse. Generation of extraneous details harms performance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ViewDetailLevelIsHighInLargeView { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewDetailLevelIsHighInLargeView As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ViewDetailLevelIsHighInLargeView { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures PerformanceFailures Class](d008a572-b1aa-1e46-0c4e-f760c50776fd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80dfe0b5-6912-6423-b2e8-a2d3b8c13590.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetTaggedGeometry Method

---



|  |
| --- |
| [ExternallyTaggedBRep Class](58a208f6-2ce5-d6cf-d17e-f4968fae5b31.htm)   [See Also](#seeAlsoToggle) |

Returns the externally tagged geometry object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public GeometryObject GetTaggedGeometry( 	ExternalGeometryId externalId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetTaggedGeometry ( _ 	externalId As ExternalGeometryId _ ) As GeometryObject ``` |

 

| Visual C++ |
| --- |
| ``` public: GeometryObject^ GetTaggedGeometry( 	ExternalGeometryId^ externalId ) ``` |

#### Parameters

externalId
:   Type:  [Autodesk.Revit.DB ExternalGeometryId](6074854d-72b6-fa2f-b4ec-df48a33b862b.htm)    
     An external tag that may match a geometry object (i.e face/edge) in this Solid.

#### Return Value

Returns the geometry object that matches the external tag. If no such object is found, this method will return null.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternallyTaggedBRep Class](58a208f6-2ce5-d6cf-d17e-f4968fae5b31.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80e12ef6-3c0b-5912-aea4-71b7c89b0baa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NotAssociatedKeynoteParameter Property

---



|  |
| --- |
| [BuiltInFailures KeynoteFailures Class](d945b1a6-1698-0bdf-d3ca-2c6db1ead693.htm)   [See Also](#seeAlsoToggle) |

Current tag keynoting system uses key value parameter that is not associated with this element category.\nTo resolve, associate parameter with category or change keynoting system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NotAssociatedKeynoteParameter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NotAssociatedKeynoteParameter As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NotAssociatedKeynoteParameter { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures KeynoteFailures Class](d945b1a6-1698-0bdf-d3ca-2c6db1ead693.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80e23fdc-c005-163b-5643-38d84411a73d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Excluding Method

---



|  |
| --- |
| [FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)   [See Also](#seeAlsoToggle) |

Applies an ExclusionFilter to the collector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FilteredElementCollector Excluding( 	ICollection<ElementId> idsToExclude ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Excluding ( _ 	idsToExclude As ICollection(Of ElementId) _ ) As FilteredElementCollector ``` |

 

| Visual C++ |
| --- |
| ``` public: FilteredElementCollector^ Excluding( 	ICollection<ElementId^>^ idsToExclude ) ``` |

#### Parameters

idsToExclude
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ids to exclude from the results.

#### Return Value

A handle to this collector. This is the same collector that has just been modified, returned so you can chain multiple calls together in one line.

# Remarks

Elements passed to this filter will be automatically excluded from the results. If you have an active iterator to this collector it will be stopped by this call.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input collection of ids was empty, or its contents were not valid for iteration. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80e5e8e6-42af-c1b8-6ce1-db598ea166fb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PickPoint Method (String)

---



|  |
| --- |
| [Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)   [See Also](#seeAlsoToggle) |

Prompts the user to pick a point on the active work plane while showing a custom status prompt string.

**Namespace:**   [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ PickPoint( 	string statusPrompt ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function PickPoint ( _ 	statusPrompt As String _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ PickPoint( 	String^ statusPrompt ) ``` |

#### Parameters

statusPrompt
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     Specifies the message shown on the status bar.

#### Return Value

The point picked by user.

Note: if the user cancels the operation (for example, through ESC), the method will throw an OperationCanceledException instance.

# Remarks

Revit users will be permitted to manipulate the Revit view (zooming, panning, and rotating the view), but will not be permitted to click other items in the Revit user interface. Users are not permitted to switch the active view, close the active document or Revit application in the pick session, otherwise an exception will be thrown.

Note: this method must not be called during dynamic update, otherwise ForbiddenForDynamicUpdateException will be thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the argument statusPrompt is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when no work plane set in current view. |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | Thrown when the Revit user cancelled this operation. Thrown when the Revit user tried to switch the active view, close the active document or Revit application when responding to this mode. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | Thrown if this method is called during dynamic update. |

# See Also

[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)

[PickPoint Overload](a1d40214-13d6-2e11-36bb-905d49105168.htm)

[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.htm)

<!-- Start of Syntax__80ea41b0-f274-8e7f-25f8-79f9fdeddb33.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFlags Method (Int32)

---



|  |
| --- |
| [ValueAtPointBase Class](67c49547-b5b9-59ad-8106-65d90886a381.htm)   [See Also](#seeAlsoToggle) |

Sets the flags associated to all measurements to the same value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetFlags( 	int flags ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFlags ( _ 	flags As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFlags( 	int flags ) ``` |

#### Parameters

flags
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Value of flags, uniform for all measurements. Flags values are defined in the enumerated class ValueAtPointFlags and are combined into the int value.

# See Also

[ValueAtPointBase Class](67c49547-b5b9-59ad-8106-65d90886a381.htm)

[SetFlags Overload](dff6d4fa-7c12-ca4e-0439-75b1e4f80b9e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80f24fab-a66b-7bf9-949c-1fbaa360c79d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [Transaction Class](308ebf8d-d96d-4643-cd1d-34fffcea53fd.htm)   [See Also](#seeAlsoToggle) |

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

[Transaction Class](308ebf8d-d96d-4643-cd1d-34fffcea53fd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80f56b2f-2c25-2c70-e2fc-8f9f25a53f3c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### JoistSystemJustificationParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Justification"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId JoistSystemJustificationParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property JoistSystemJustificationParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ JoistSystemJustificationParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80f5ddbd-fdf4-6076-2a06-0cd185b3da78.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateCableTrayConnector Method (Document, Reference, Edge)

---



|  |
| --- |
| [ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)   [See Also](#seeAlsoToggle) |

Create a new cable tray ConnectorElement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static ConnectorElement CreateCableTrayConnector( 	Document document, 	Reference planarFace, 	Edge edge ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateCableTrayConnector ( _ 	document As Document, _ 	planarFace As Reference, _ 	edge As Edge _ ) As ConnectorElement ``` |

 

| Visual C++ |
| --- |
| ``` public: static ConnectorElement^ CreateCableTrayConnector( 	Document^ document,  	Reference^ planarFace,  	Edge^ edge ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to add the connector to.

planarFace
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The planar face to place the connector on.

edge
:   Type:  [Autodesk.Revit.DB Edge](7155ef49-fcd9-c80a-6232-70189a617bcc.htm)    
     One of the edges in the edge loop that defines the connector location on the planar face.

#### Return Value

The cable tray ConnectorElement.

# Remarks

Regenerates the document.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The reference is not a planar face. -or- document is not a family document. -or- Thrown when the edge does not belong to the face. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Connector creation is not allowed in this family. |

# See Also

[ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)

[CreateCableTrayConnector Overload](207247e7-7df9-5164-959e-5ed123a801fd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80f68a76-0ec8-9683-f1c1-9c5d72931aff.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CantMirrorInstWoHost Property

---



|  |
| --- |
| [BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)   [See Also](#seeAlsoToggle) |

Can't mirror an instance without its host.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CantMirrorInstWoHost { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CantMirrorInstWoHost As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CantMirrorInstWoHost { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__80fa3cbc-3cfe-bcfc-ac1f-9487c45f2908.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleHorizontalAlignment Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Horizontal alignment of data in a schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum ScheduleHorizontalAlignment ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ScheduleHorizontalAlignment ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ScheduleHorizontalAlignment ``` |

# Members

| Member name | Description |
| --- | --- |
| Left | Left aligned |
| Center | Center aligned |
| Right | Right aligned |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81a0ba19-cbe5-69b8-2dbf-8b2fc84edafa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImportAdtEntityStructType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Structural Type Name"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ImportAdtEntityStructType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ImportAdtEntityStructType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ImportAdtEntityStructType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81a2d6cb-7f5f-9b27-d5f2-bd410ffc4c28.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewGraphSchedLevelRelativeBaseType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Elevation Base for Levels"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ViewGraphSchedLevelRelativeBaseType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewGraphSchedLevelRelativeBaseType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ViewGraphSchedLevelRelativeBaseType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81a3e90b-f790-88ab-a3dc-22518a81928a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VisGraphicsPointClouds Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"V/G Overrides Point Clouds"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId VisGraphicsPointClouds { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property VisGraphicsPointClouds As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ VisGraphicsPointClouds { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81a72471-bfa6-18ec-db83-911a49c3f4e8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAlmostEqualTo Method (XYZ, Double)

---



|  |
| --- |
| [XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)   [See Also](#seeAlsoToggle) |

Determines whether 2 vectors are the same within the given tolerance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsAlmostEqualTo( 	XYZ source, 	double tolerance ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsAlmostEqualTo ( _ 	source As XYZ, _ 	tolerance As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsAlmostEqualTo( 	XYZ^ source,  	double tolerance ) ``` |

#### Parameters

source
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vector to compare with this vector.

tolerance
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The tolerance for equality check.

#### Return Value

True if the vectors are the same; otherwise, false.

# Remarks

This routine uses an input tolerance to compare two vectors to see if they are almost equivalent. Because it is comparing two vectors the tolerance value is not in length units but instead represents the variation in direction between the vectors. For very small tolerance values it should also be possible to compare two points with this method. To compute the distance between two points for a comparison with a larger allowable difference, use  [DistanceTo(XYZ)](ecbbee02-8f32-d5e9-a565-9c072543ea4f.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when source is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when tolerance is less than 0. |

# See Also

[XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

[IsAlmostEqualTo Overload](dcad6f16-9898-2f6f-1325-5bae45de241a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81aa76f2-38cb-afc3-8ddc-991affadcde7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SummaryShowsVerticalHeaders Property

---



|  |
| --- |
| [PanelScheduleData Class](d24fcc19-3240-8f07-68ca-ce7b62f7aac3.htm)   [See Also](#seeAlsoToggle) |

Shows text in the Load Summary section's headers vertically instead of horizontally

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool SummaryShowsVerticalHeaders { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property SummaryShowsVerticalHeaders As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool SummaryShowsVerticalHeaders { 	bool get (); } ``` |

# Remarks

Setting this value must go through the appropriate update function (updateVerticalHeadersInSection)

# See Also

[PanelScheduleData Class](d24fcc19-3240-8f07-68ca-ce7b62f7aac3.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__81ada6e8-47f1-4ff6-fcb8-907e0a389c7c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SelectionChanged Event

---



|  |
| --- |
| [UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the SelectionChanged event to be notified after the selection was changed.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public event EventHandler<SelectionChangedEventArgs> SelectionChanged ``` |

 

| Visual Basic |
| --- |
| ``` Public Event SelectionChanged As EventHandler(Of SelectionChangedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<SelectionChangedEventArgs^>^ SelectionChanged { 	void add (EventHandler<SelectionChangedEventArgs^>^ value); 	void remove (EventHandler<SelectionChangedEventArgs^>^ value); } ``` |

# Remarks

This event is raised after the selection was changed in the current document. Handlers of this event are forbidden to make modifications to the current document. Handlers of this event are forbidden to change the selection to the current document. It is not allowed to open a new transaction in the active document when handling this event.

# See Also

[UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__81add97d-5d3b-170c-cfdf-01efeeb9a73a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShowImageAsButton Property

---



|  |
| --- |
| [TextBox Class](5cfff6ff-3982-e8f7-a3c8-43d93204d41a.htm)   [See Also](#seeAlsoToggle) |

Gets or sets a value that indicates if the Image set in the text box should be displayed as a clickable button.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool ShowImageAsButton { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ShowImageAsButton As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ShowImageAsButton { 	bool get (); 	void set (bool value); } ``` |

# Remarks

If this property is true, the image will shown as a button inside the textbox. Clicking this button will trigger the EnterPressed event. The default value is false.

# See Also

[TextBox Class](5cfff6ff-3982-e8f7-a3c8-43d93204d41a.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__81b206f9-39bb-ecaf-36e3-3a4c31718972.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidLineStyleIdForFilledRegion Method

---



|  |
| --- |
| [FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the given Id is a valid line style Id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool IsValidLineStyleIdForFilledRegion( 	Document document, 	ElementId lineStyleId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidLineStyleIdForFilledRegion ( _ 	document As Document, _ 	lineStyleId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidLineStyleIdForFilledRegion( 	Document^ document,  	ElementId^ lineStyleId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

lineStyleId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The line style Id.

#### Return Value

True if it is a valid line style Id, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81b2a535-a0a1-7d82-b3c0-ee5fcebd0ab0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LitersPerHour Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Liters per hour.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LitersPerHour { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LitersPerHour As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LitersPerHour { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81b3ac4f-b684-4fac-7bdb-97a75ba12dca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsBaseLevelParam Property

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
| ``` public static ForgeTypeId StairsBaseLevelParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsBaseLevelParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsBaseLevelParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81c2d8f5-462b-8d58-2bd0-061532647f08.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InaccurateDriveCurve Property

---



|  |
| --- |
| [BuiltInFailures InaccurateFailures Class](1cd8eae9-aab1-2808-fbaa-b95bdf9ff3eb.htm)   [See Also](#seeAlsoToggle) |

Element is slightly off axis and may cause inaccuracies.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId InaccurateDriveCurve { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InaccurateDriveCurve As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ InaccurateDriveCurve { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures InaccurateFailures Class](1cd8eae9-aab1-2808-fbaa-b95bdf9ff3eb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81caa3e1-5f0f-5775-3b0b-b7d9349a1464.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OptionElementsDeleted Property

---



|  |
| --- |
| [BuiltInFailures DesignOptionFailures Class](306b7ebc-5d5e-e53f-d5e4-9a5da4162068.htm)   [See Also](#seeAlsoToggle) |

Elements in [option] were deleted

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId OptionElementsDeleted { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property OptionElementsDeleted As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ OptionElementsDeleted { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DesignOptionFailures Class](306b7ebc-5d5e-e53f-d5e4-9a5da4162068.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81cb1798-3dbe-658b-5a04-d97aa2cb4de9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExtensibleStorageFilter Class

---



|  |
| --- |
| [Members](004fe9d1-0b32-4ed3-b8c6-42e0ae00a5a3.htm)   [See Also](#seeAlsoToggle) |

A filter used to filter elements with extensible storage data based on specific Schema id.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class ExtensibleStorageFilter : ElementQuickFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExtensibleStorageFilter _ 	Inherits ElementQuickFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExtensibleStorageFilter : public ElementQuickFilter ``` |

# Remarks

This filter is a quick filter. Quick filters operate only on the ElementRecord, a low-memory class which has a limited interface to read element properties. Elements which are rejected by a quick filter will not be expanded in memory.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  [Autodesk.Revit.DB ElementQuickFilter](ebc95d82-11fc-69f6-2df1-52331dd36443.htm)    
  Autodesk.Revit.DB.ExtensibleStorage ExtensibleStorageFilter

# See Also

[ExtensibleStorageFilter Members](004fe9d1-0b32-4ed3-b8c6-42e0ae00a5a3.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)

<!-- Start of Syntax__81cb7213-47eb-ce6f-cde9-38ce88dcad75.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NotAllowedCableTrayConduitRotation Property

---



|  |
| --- |
| [BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)   [See Also](#seeAlsoToggle) |

Don't allow to rotate a horizontal cable tray/conduit like this

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NotAllowedCableTrayConduitRotation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NotAllowedCableTrayConduitRotation As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NotAllowedCableTrayConduitRotation { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81cbdc7c-9f7f-b454-5669-77ca0514eda7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ColorFillLegend Class

---



|  |
| --- |
| [Members](b8e31474-3699-993e-bdf5-b1681ed0e10d.htm)   [See Also](#seeAlsoToggle) |

Represents color fill legend.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public class ColorFillLegend : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ColorFillLegend _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ColorFillLegend : public Element ``` |

# Remarks

Color fill legend is a 2D annotation element, it can be created through  [Create(Document, ElementId, ElementId, XYZ)](fda03f51-ce31-0cde-a41d-ec0e9885282d.htm)  with specified category of color fill scheme, if there exists a valid color fill scheme activated for the category in the view. After a legend is created, its content and layout will keep consistent with the active color fill scheme of the view. You can adjust its position through  [Origin](b0359d5c-a5f2-dfa6-9804-0d63ea15ad2e.htm)  property, or manually maintain its layout through  [Height](7989267f-da55-4f56-2088-6536d68e4c8e.htm)  property and  [GetColumnWidths](bea0b37a-991b-8ddc-28d7-0bacf0f4181a.htm)  /  [M:Autodesk.Revit.DB.ColorFillLegend.SetColumnWidths(System.Collections.Generic.IList`1{System.Double})]  methods.

Notes:

1. [GetColorFillSchemeId(ElementId)](c504d70c-ab68-2db1-95be-73e821ee3587.htm)  could be used to retrieve the corresponding color fill scheme of this legend, through the  [!:Autodesk::Revit::DB::View::ColorFillCategoryId]  and  [OwnerViewId](174c1adf-0be8-a4b0-41f3-9e3ea1d6b1f1.htm)  properties. Note that there could only exist one active scheme for all spatial categories (rooms, areas, and zones) in one view.
2. Once the height and column widths are explicitly set, they will be fixed even if the contents of the legend change.
3. To retrieve correct height and column widths, it's better to manually retrieve the geometry of legend for nonvisible views. (Because color fill legend is a view specific element.)
4. The value of  [Height](7989267f-da55-4f56-2088-6536d68e4c8e.htm)  property does not contain the line that displays "Calculating...".

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB ColorFillLegend

# See Also

[ColorFillLegend Members](b8e31474-3699-993e-bdf5-b1681ed0e10d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81d0c125-52cf-a81c-5c2a-f02fac4f9da0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternalDataTypeServerFailureResolutionExecutingEventArgs Class

---



|  |
| --- |
| [Members](22f43a41-c5f7-5192-8007-8cb437cedee8.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by the ExternalDataTypeServerFailureResolutionExecuting event.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public class ExternalDataTypeServerFailureResolutionExecutingEventArgs : RevitAPIPreDocEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExternalDataTypeServerFailureResolutionExecutingEventArgs _ 	Inherits RevitAPIPreDocEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExternalDataTypeServerFailureResolutionExecutingEventArgs : public RevitAPIPreDocEventArgs ``` |

# Inheritance Hierarchy

System Object    
  System EventArgs    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPreEventArgs](14097470-c9d9-0143-dc1b-b93a60a460e6.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPreDocEventArgs](ef0073c4-f86b-64b9-12f2-268f4e1b8bbe.htm)    
  Autodesk.Revit.DB.Events ExternalDataTypeServerFailureResolutionExecutingEventArgs

# See Also

[ExternalDataTypeServerFailureResolutionExecutingEventArgs Members](22f43a41-c5f7-5192-8007-8cb437cedee8.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__81d23849-6d6e-9b10-56b4-3bbc9d5d64a7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GrPerHFtSup2InHg Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol gr/(hÂ·ftÂ²Â·inHg), indicating unit Grains per hour square foot inch mercury.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId GrPerHFtSup2InHg { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GrPerHFtSup2InHg As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ GrPerHFtSup2InHg { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81d26278-3a1d-1e9b-90da-9b733c75e9d5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalModelSelector Constructor

---



|  |
| --- |
| [AnalyticalModelSelector Class](d286b023-8822-10ad-6702-53c86a6c9e70.htm)   [See Also](#seeAlsoToggle) |

Creates a selector for the analytical model geometry.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public AnalyticalModelSelector() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: AnalyticalModelSelector() ``` |

# Remarks

This version is useful for single-curve or single-point analytical models. Additionally, this only acts with respect to the entire curve or point.

# See Also

[AnalyticalModelSelector Class](d286b023-8822-10ad-6702-53c86a6c9e70.htm)

[AnalyticalModelSelector Overload](9e76852b-a21f-b2d7-93a3-66b844047368.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__81d30263-8278-d43f-3b1c-d75e4d226648.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OverlappingLines Property

---



|  |
| --- |
| [BuiltInFailures GridChainSketchFailures Class](8840595e-9443-cb55-bfab-882395cb6aa8.htm)   [See Also](#seeAlsoToggle) |

GridChain sketch contains lines which overlap.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId OverlappingLines { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property OverlappingLines As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ OverlappingLines { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GridChainSketchFailures Class](8840595e-9443-cb55-bfab-882395cb6aa8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81d64aca-5b15-956f-fd76-5f3ae00084fe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)   [See Also](#seeAlsoToggle) |

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

[NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81d816a4-758e-e2f1-b953-994837b7a9f3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WoodEarlycolorPerlinProf Property

---



|  |
| --- |
| [AdvancedWood Class](1e8c37ad-69ea-aabc-df91-eda9c7fe54ff.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Profile for earlywood color perlin noise" from the "AdvancedWood" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string WoodEarlycolorPerlinProf { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WoodEarlycolorPerlinProf As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ WoodEarlycolorPerlinProf { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble".

# See Also

[AdvancedWood Class](1e8c37ad-69ea-aabc-df91-eda9c7fe54ff.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__81da6c74-32ea-d386-4035-18bc1a97fb3c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsParallelpipesVerticalNumber Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Vertical Number for parallel pipes"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsParallelpipesVerticalNumber { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsParallelpipesVerticalNumber As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsParallelpipesVerticalNumber { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81db0c0e-c1df-7b1c-736e-04ccb1a4f134.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScaledInnerPerimeter Property

---



|  |
| --- |
| [IFCExtrusionCreationData Class](9447a335-6861-0533-6896-e6ff1fd41761.htm)   [See Also](#seeAlsoToggle) |

The inner perimeter of the extrusion, scaled to the units of export.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double ScaledInnerPerimeter { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ScaledInnerPerimeter As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ScaledInnerPerimeter { 	double get (); 	void set (double value); } ``` |

#### Field Value

This value represents the perimeter of all of the inner curve loops within the area of the extrusion. Zero if the perimeter has never been set on this object.

# See Also

[IFCExtrusionCreationData Class](9447a335-6861-0533-6896-e6ff1fd41761.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__81dd634f-cd45-bb04-4854-daff8ed7777a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DuctPressureDropService Property

---



|  |
| --- |
| [ExternalServices BuiltInExternalServices Class](f189eb3f-7a3a-2891-657a-e18cbf014987.htm)   [See Also](#seeAlsoToggle) |

The external service which permits registration of an alternate implementation for duct pressure drop calculation. To use this service, programmers implement a server class that derives from  IDuctPressureDropServer  .

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public static ExternalServiceId DuctPressureDropService { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DuctPressureDropService As ExternalServiceId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ExternalServiceId^ DuctPressureDropService { 	ExternalServiceId^ get (); } ``` |

# See Also

[ExternalServices BuiltInExternalServices Class](f189eb3f-7a3a-2891-657a-e18cbf014987.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)

<!-- Start of Syntax__81dec13f-8eca-f2eb-bf60-1e206e6d0d98.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DGNImportOptions Class

---



|  |
| --- |
| [Members](f8caf63c-93f6-47c0-30d6-43c4f3643ab3.htm)   [See Also](#seeAlsoToggle) |

The import options used to import DGN format files.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class DGNImportOptions : BaseImportOptions ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DGNImportOptions _ 	Inherits BaseImportOptions ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DGNImportOptions : public BaseImportOptions ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB BaseImportOptions](75898e94-cff4-fb64-c613-9596599444c4.htm)    
  Autodesk.Revit.DB DGNImportOptions

# See Also

[DGNImportOptions Members](f8caf63c-93f6-47c0-30d6-43c4f3643ab3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81e77b23-56b3-1331-7c7a-75bcd3e2ec64.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDone Method

---



|  |
| --- |
| [MacroManagerIterator Class](2e602955-0aaf-f39f-720f-d6269ec8ce26.htm)   [See Also](#seeAlsoToggle) |

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

[MacroManagerIterator Class](2e602955-0aaf-f39f-720f-d6269ec8ce26.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)

<!-- Start of Syntax__81e7b833-bed9-f797-e4ad-9e6df4b0cc12.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Multiply Method

---



|  |
| --- |
| [XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)   [See Also](#seeAlsoToggle) |

Multiplies this vector by the specified value and returns the result.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ Multiply( 	double value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Multiply ( _ 	value As Double _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ Multiply( 	double value ) ``` |

#### Parameters

value
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The value to multiply with this vector.

#### Return Value

The multiplied vector.

# Remarks

The multiplied vector is obtained by multiplying each coordinate of this vector by the specified value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the specified value is an infinite number. |

# See Also

[XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81e80465-626a-5659-5383-25fef813c270.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetProjectGUID Method

---



|  |
| --- |
| [ModelPath Class](40a84c72-e4b8-72ac-2f71-3216c66a11b3.htm)   [See Also](#seeAlsoToggle) |

A GUID identifying the BIM 360 Docs or Autodesk Docs project to which the model is associated.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public Guid GetProjectGUID() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetProjectGUID As Guid ``` |

 

| Visual C++ |
| --- |
| ``` public: Guid GetProjectGUID() ``` |

# See Also

[ModelPath Class](40a84c72-e4b8-72ac-2f71-3216c66a11b3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81e8a4a9-ad56-09e5-bcf8-9801a24dd636.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
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

[AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__81ec301c-4b77-ea17-425d-4a1f716ac538.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DesignReturnAirflow Property

---



|  |
| --- |
| [Space Class](b2c8970e-e554-8d73-06db-b65712c8a2e5.htm)   [See Also](#seeAlsoToggle) |

Get or set the Specified Return Airflow of the Space.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double DesignReturnAirflow { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DesignReturnAirflow As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double DesignReturnAirflow { 	double get (); 	void set (double value); } ``` |

# Remarks

This property is used to get or set the Specified Return Airflow (Unit: CFM) of the Space.

# See Also

[Space Class](b2c8970e-e554-8d73-06db-b65712c8a2e5.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__81ed9da9-d26f-db06-cee0-9d94e323d45c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Illuminance Property

---



|  |
| --- |
| [InitialIlluminanceIntensity Class](d31b6d5f-f002-007b-3e08-e6818727f104.htm)   [See Also](#seeAlsoToggle) |

The illuminance intensity value.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double Illuminance { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Illuminance As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Illuminance { 	double get (); 	void set (double value); } ``` |

#### Field Value

The illuminance value in lx as a numerical value between 0 and 1e+30.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The illuminance value is not valid because it is not between 0 and 1e+30. |

# See Also

[InitialIlluminanceIntensity Class](d31b6d5f-f002-007b-3e08-e6818727f104.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__81faa47c-60f0-c6a5-f46f-e14cff1584f3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IdParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Id"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId IdParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property IdParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ IdParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81fca2c9-ca3c-0f70-366e-8841944bdac7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAlternateUnitsFormatOptions Method

---



|  |
| --- |
| [DimensionType Class](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.htm)   [See Also](#seeAlsoToggle) |

Gets the FormatOptions to optionally override the default settings in the Units class for the alternate units value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FormatOptions GetAlternateUnitsFormatOptions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAlternateUnitsFormatOptions As FormatOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: FormatOptions^ GetAlternateUnitsFormatOptions() ``` |

#### Return Value

A copy of the FormatOptions.

# See Also

[DimensionType Class](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81fcae21-46db-346c-22c1-6dcbf4e7e8f7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NetworkUnderConstrained Property

---



|  |
| --- |
| [BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)   [See Also](#seeAlsoToggle) |

The network is under constrained. You may specify the design flow value in the missing branches, or cap the open ends.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NetworkUnderConstrained { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NetworkUnderConstrained As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NetworkUnderConstrained { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81fcd801-a0da-fa4f-6267-87f515c1998f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathReinAltOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Alternating Bar - Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PathReinAltOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PathReinAltOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PathReinAltOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81fd3daf-ab3d-ae8b-d753-b0d377f64dd5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReferenceArrayIterator Constructor

---



|  |
| --- |
| [ReferenceArrayIterator Class](5b4e4948-c5f0-1e38-d461-7353561774e8.htm)   [See Also](#seeAlsoToggle) |

For Internal Use Only.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ReferenceArrayIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: ReferenceArrayIterator() ``` |

# Remarks

This constructor is exposed to enable support for COM interop only. This object should never be created by the developer.

# See Also

[ReferenceArrayIterator Class](5b4e4948-c5f0-1e38-d461-7353561774e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__81ff0ae2-1df5-6e62-cd94-3c8c31dc92ab.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateFromCenterline Method

---



|  |
| --- |
| [FabricationPartRouteEnd Class](58bd199f-5114-67de-011b-d054a1a4c4d9.htm)   [See Also](#seeAlsoToggle) |

Create fabrication routing end from centreline point on straight element.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static FabricationPartRouteEnd CreateFromCenterline( 	Element element, 	XYZ ptAt ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateFromCenterline ( _ 	element As Element, _ 	ptAt As XYZ _ ) As FabricationPartRouteEnd ``` |

 

| Visual C++ |
| --- |
| ``` public: static FabricationPartRouteEnd^ CreateFromCenterline( 	Element^ element,  	XYZ^ ptAt ) ``` |

#### Parameters

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The straight element that the centerline is on.

ptAt
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     A point along the straight element where the fitting to be cut in should be positioned.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationPartRouteEnd Class](58bd199f-5114-67de-011b-d054a1a4c4d9.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)

<!-- Start of Syntax__82a01138-16c4-8e0c-fd78-2c1b9b0406d7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsAttrRiserMult Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Riser Multiplier"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsAttrRiserMult { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsAttrRiserMult As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsAttrRiserMult { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82a3b2c5-c712-b558-2b4f-825c2e841611.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidFaceReferenceForFaceWall Method

---



|  |
| --- |
| [FaceWall Class](cd76c5c4-4c8d-8101-5ebb-fa1ba4dcf9a1.htm)   [See Also](#seeAlsoToggle) |

Identifies if a reference may be used as the parent of a face wall.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static bool IsValidFaceReferenceForFaceWall( 	Document document, 	Reference faceReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidFaceReferenceForFaceWall ( _ 	document As Document, _ 	faceReference As Reference _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidFaceReferenceForFaceWall( 	Document^ document,  	Reference^ faceReference ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

faceReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The reference.

#### Return Value

True if the reference is valid as a parent to a face wall, false otherwise.

# Remarks

The reference must represent a face of a massing instance, and must be planar, and its normal must not be vertical or horizontal.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FaceWall Class](cd76c5c4-4c8d-8101-5ebb-fa1ba4dcf9a1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82ad5891-a5a5-1405-db0e-5ce7c7aeaf99.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CubicFeetPerMinutePerBritishThermalUnitPerHour Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Cubic feet per minute per British thermal unit per hour.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CubicFeetPerMinutePerBritishThermalUnitPerHour { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CubicFeetPerMinutePerBritishThermalUnitPerHour As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CubicFeetPerMinutePerBritishThermalUnitPerHour { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82ae2419-0650-d52f-f787-9a7dc6d25d04.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureRealWorldOffsetY Property

---



|  |
| --- |
| [Wood Class](945bd0f8-29bb-1294-9d95-7431ef25f4dd.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Offset Y" from the "Wood" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TextureRealWorldOffsetY { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextureRealWorldOffsetY As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TextureRealWorldOffsetY { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDistance".

# See Also

[Wood Class](945bd0f8-29bb-1294-9d95-7431ef25f4dd.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__82af10d1-5ebf-526d-0dbd-e5ea2270f944.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TransferredProjectStandards Event

---



|  |
| --- |
| [UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the TransferredProjectStandards event to be notified after the scope of a Transfer Project Standards operation has been finalized.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017.2

# Syntax

| C# |
| --- |
| ``` public event EventHandler<TransferredProjectStandardsEventArgs> TransferredProjectStandards ``` |

 

| Visual Basic |
| --- |
| ``` Public Event TransferredProjectStandards As EventHandler(Of TransferredProjectStandardsEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<TransferredProjectStandardsEventArgs^>^ TransferredProjectStandards { 	void add (EventHandler<TransferredProjectStandardsEventArgs^>^ value); 	void remove (EventHandler<TransferredProjectStandardsEventArgs^>^ value); } ``` |

# Remarks

This event is raised just after the native Revit items have been transferred, but before the transaction has been committed. An add-in that registered external items in  [TransferringProjectStandards](a7326050-7532-df52-a54a-8acd66a2a8a3.htm)  should subscribe to this event to carry out the transfer of any items that it registered if the user enabled those items for transfer. During the scope of this event, modification is permitted to the target document and modification is not permitted to the source document.

# See Also

[UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__82bbb4bf-7f62-f6f8-bef7-d915db11669d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BottomOffset Property

---



|  |
| --- |
| [Blend Class](6875edf6-f0ba-60bc-f294-21bb689c5994.htm)   [See Also](#seeAlsoToggle) |

The offset of the bottom end of the blend relative to the sketch plane.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double BottomOffset { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BottomOffset As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double BottomOffset { 	double get (); 	void set (double value); } ``` |

# See Also

[Blend Class](6875edf6-f0ba-60bc-f294-21bb689c5994.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82bd14f6-8678-d37c-1848-54a97d2aa7d3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanBeMatchedWithMultipleShapes Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Checks if this Rebar can be matched with multiple Rebar Shapes.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public bool CanBeMatchedWithMultipleShapes() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanBeMatchedWithMultipleShapes As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanBeMatchedWithMultipleShapes() ``` |

#### Return Value

Returns true if this Rebar can be matched with multiple Rebar Shapes, false otherwise.

# Remarks

A Free Form Rebar that has Workshop Instructions set to Bent is considered that can be matched with multiple shapes.

A Free Form Rebar that has Workshop Instructions set to Straight or a Shape Driven Rebar is considered that can be matched with only one shape.

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__82c33025-cb7b-f359-feca-1cb366e6d626.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ContainsKey Method

---



|  |
| --- |
| [ExportLineweightTable Class](5620708e-0c7c-ced6-9887-0237a9229800.htm)   [See Also](#seeAlsoToggle) |

Checks whether a line weight key exists in the table.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool ContainsKey( 	ExportLineweightKey exportLineweightKey ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ContainsKey ( _ 	exportLineweightKey As ExportLineweightKey _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool ContainsKey( 	ExportLineweightKey^ exportLineweightKey ) ``` |

#### Parameters

exportLineweightKey
:   Type:  [Autodesk.Revit.DB ExportLineweightKey](5b3250ab-f70b-6f87-afbf-dd049a64c29e.htm)    
     The export line weight key.

#### Return Value

True if the line weight exists in the table.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportLineweightTable Class](5620708e-0c7c-ced6-9887-0237a9229800.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82c45482-a018-32e4-d8e5-9751e10ffeb9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ParametersMap Property

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Retrieves a map containing all of the parameters that are contained within the element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ParameterMap ParametersMap { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ParametersMap As ParameterMap 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ParameterMap^ ParametersMap { 	ParameterMap^ get (); } ``` |

# Remarks

The Parameters can be rapidly accessed by parameter name as a key. These parameters are displayed in the Element properties dialog in the Autodesk Revit interface. These parameters can be retrieved and set via the parameter objects stored in this map.

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82c469e6-5906-3017-5080-e2d47da138cb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TooShort Property

---



|  |
| --- |
| [BuiltInFailures CurveFailures Class](d8139918-351e-f209-f2bd-439653322d56.htm)   [See Also](#seeAlsoToggle) |

Line is too short.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId TooShort { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TooShort As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ TooShort { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CurveFailures Class](d8139918-351e-f209-f2bd-439653322d56.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82c9eb04-fcec-e129-ffd0-ffed9b6a1650.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurveElemLineAngle Property

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
| ``` public static ForgeTypeId CurveElemLineAngle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CurveElemLineAngle As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CurveElemLineAngle { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82cc661d-89e7-d53e-b5a5-05d2aab397b1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PrepareForCell Method

---



|  |
| --- |
| [PointCloudFilter Class](ca6f916b-2eba-f8e5-8939-1c063330c886.htm)   [See Also](#seeAlsoToggle) |

Informs the filter that a series of points within a given cell is about to be checked.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void PrepareForCell( 	XYZ min, 	XYZ max, 	int numTests ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub PrepareForCell ( _ 	min As XYZ, _ 	max As XYZ, _ 	numTests As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void PrepareForCell( 	XYZ^ min,  	XYZ^ max,  	int numTests ) ``` |

#### Parameters

min
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The lower corner of the cell.

max
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The upper corner of the cell.

numTests
:   Type:  System Int32    
     The engine's estimate of the number of TestPoint() calls it is going to make for this cell.

# Remarks

This is a performance hook that the filter can use to minimize computational work per TestPoint() call within a given cell. The engine should guarantee that all points passed to TestPoint() calls will fall inside the (min, max) box specified here. This promise must be in effect until the next PrepareForCell() call.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PointCloudFilter Class](ca6f916b-2eba-f8e5-8939-1c063330c886.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__82cc8fe6-c6df-43b6-970b-dadb09f1f7c7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PoundForceFeet Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Pound force feet.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PoundForceFeet { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PoundForceFeet As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PoundForceFeet { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82d02113-ab06-48f4-9786-3fa28142e976.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RampAttrLeftBalusterAttachPt Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Left Baluster Location"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RampAttrLeftBalusterAttachPt { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RampAttrLeftBalusterAttachPt As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RampAttrLeftBalusterAttachPt { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82d038e6-9a72-dda8-e0e7-a2b41c3e2640.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReverseIterator Method

---



|  |
| --- |
| [FormArray Class](24506527-802b-2487-919e-14a4a06f60be.htm)   [See Also](#seeAlsoToggle) |

Retrieve a backward moving iterator to the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual FormArrayIterator ReverseIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ReverseIterator As FormArrayIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual FormArrayIterator^ ReverseIterator() ``` |

#### Return Value

Returns a backward moving iterator to the array.

# See Also

[FormArray Class](24506527-802b-2487-919e-14a4a06f60be.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82d48d94-0d91-9c48-efc7-f7d58c3da411.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MarginType Property

---



|  |
| --- |
| [PrintParameters Class](59e6cfe9-b1e8-70c0-814b-ee69c8fca411.htm)   [See Also](#seeAlsoToggle) |

The print margin type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public MarginType MarginType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MarginType As MarginType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property MarginType MarginType { 	MarginType get (); 	void set (MarginType value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the input argument is out of range. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if the PaperPlacement is not Margins type. |

# See Also

[PrintParameters Class](59e6cfe9-b1e8-70c0-814b-ee69c8fca411.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82d6e0c5-f102-ce90-9521-3c2e74fbd495.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundaryValidation Class

---



|  |
| --- |
| [Members](2353c8f1-70aa-b4c9-a50c-48b98c7bb1a5.htm)   [See Also](#seeAlsoToggle) |

Curve loop validators.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public class BoundaryValidation : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class BoundaryValidation _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class BoundaryValidation : IDisposable ``` |

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB BoundaryValidation

# See Also

[BoundaryValidation Members](2353c8f1-70aa-b4c9-a50c-48b98c7bb1a5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82d6f753-6e14-3bd1-1fb2-caa284bf4686.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsParameterModifiable Method

---



|  |
| --- |
| [Subelement Class](2d15bb45-70af-5f84-e899-322742591251.htm)   [See Also](#seeAlsoToggle) |

Checks if given parameter of this subelement is modifiable.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool IsParameterModifiable( 	ElementId parameterId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsParameterModifiable ( _ 	parameterId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsParameterModifiable( 	ElementId^ parameterId ) ``` |

#### Parameters

parameterId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Parameter id.

#### Return Value

True if given parameter of this subelement is modifiable, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Subelement Class](2d15bb45-70af-5f84-e899-322742591251.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82daf5d4-001c-1c0b-e323-b8a8a97bb92d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRelinquishedWorksets Method

---



|  |
| --- |
| [RelinquishedItems Class](50c43bae-6776-ed11-6489-ab4bea85d04f.htm)   [See Also](#seeAlsoToggle) |

The elements that were relinquished by the current user.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ICollection<WorksetId> GetRelinquishedWorksets() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRelinquishedWorksets As ICollection(Of WorksetId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<WorksetId^>^ GetRelinquishedWorksets() ``` |

# See Also

[RelinquishedItems Class](50c43bae-6776-ed11-6489-ab4bea85d04f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82e6e1b8-27c1-e9a1-9bff-06040a6d3c98.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairNotEnoughBoundaryCurvesError Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Stairs require boundaries (chains of one or more Boundary Lines) on each side of the Stair.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId StairNotEnoughBoundaryCurvesError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairNotEnoughBoundaryCurvesError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ StairNotEnoughBoundaryCurvesError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82e737d5-fda4-bc10-6099-88999cd51300.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementTransformUtils Class

---



|  |
| --- |
| [Members](463dc10e-bf30-84ee-70b5-585f8145dff4.htm)   [See Also](#seeAlsoToggle) |

A collection of utilities allowing transformation of elements (e.g. move, rotate, mirror and copy).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static class ElementTransformUtils ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class ElementTransformUtils ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ElementTransformUtils abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ElementTransformUtils

# See Also

[ElementTransformUtils Members](463dc10e-bf30-84ee-70b5-585f8145dff4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82ed0368-6da3-53a3-8c07-4061efd0be56.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LeaderAtachement Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Supported types of vertical attachments of a leader to a text note.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2016   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public enum LeaderAtachement ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration LeaderAtachement ``` |

 

| Visual C++ |
| --- |
| ``` public enum class LeaderAtachement ``` |

# Members

| Member name | Description |
| --- | --- |
| TopLine | Leaders are attached at the position of the top (first) line of the text box, and, unless the text's border is visible, the leader's shoulder line extends all the way to the text, minus the current value of text border offset. |
| Midpoint | Leaders are aligned vertically with the midpoint of the text box and their shoulder line always ends at the box' border regardless of whether the border is visible on not. |
| BottomLine | Leaders are attached at the position of the bottom (last) line of the text box, and, unless the text's border is visible, the leader's shoulder line extends all the way to the text, minus the current value of text border offset. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82f2813b-0c38-d2ac-02d6-0cfb4ba7dd6e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportLineweightTable Constructor

---



|  |
| --- |
| [ExportLineweightTable Class](5620708e-0c7c-ced6-9887-0237a9229800.htm)   [See Also](#seeAlsoToggle) |

Constructs a new ExportLineweightTable with default settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ExportLineweightTable() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: ExportLineweightTable() ``` |

# See Also

[ExportLineweightTable Class](5620708e-0c7c-ced6-9887-0237a9229800.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82f331a5-8933-d7f7-8be7-e8dbad1236c5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsComponentFlipped Property

---



|  |
| --- |
| [DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)   [See Also](#seeAlsoToggle) |

Whether the pattern is flipped.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsComponentFlipped { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsComponentFlipped As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsComponentFlipped { 	bool get (); 	void set (bool value); } ``` |

# Remarks

This property has no effect unless a pattern is selected (the ObjectType property is not    a null reference (  Nothing  in Visual Basic)  ). Changing this flag effectively reflects the component through its XY-plane, which is equivalent to reflecting it through the original surface.

# See Also

[DividedSurface Class](782e1ac7-4e74-9a32-6b03-0a20f7d55217.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82f4580e-0461-e307-1926-d26eb99841d7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, FabricationServiceButton, Double, Double, ElementId)

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Creates a fabrication part element based on button and size.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static FabricationPart Create( 	Document document, 	FabricationServiceButton button, 	double width, 	double depth, 	ElementId levelId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	button As FabricationServiceButton, _ 	width As Double, _ 	depth As Double, _ 	levelId As ElementId _ ) As FabricationPart ``` |

 

| Visual C++ |
| --- |
| ``` public: static FabricationPart^ Create( 	Document^ document,  	FabricationServiceButton^ button,  	double width,  	double depth,  	ElementId^ levelId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

button
:   Type:  [Autodesk.Revit.DB FabricationServiceButton](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)    
     The fabrication service button to use. Matches button condition based on the specified size.

width
:   Type:  System Double    
     The width of the part. Units are in feet (ft).

depth
:   Type:  System Double    
     The depth of the part. Units are in feet (ft). It should be equal to width for round part.

levelId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element identifier associated with the  [Level](577e5d4e-a558-118c-9dea-3b810b061775.htm)  the  [FabricationPart](c9b86162-c105-696a-a919-49a7a7938cc4.htm)  will be created on.

#### Return Value

The new fabrication part.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Fabrication service button contains invalid fittings. -or- Please use FabricationPart.CreateHanger to create fabrication hanger. -or- The ElementId levelId is not a Level. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The fabrication part type does not exist. Reload the service using FabricationConfiguration.LoadServices. -or- failing to match a button condition based on specific size. |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Create Overload](0eac67e8-6cec-11e4-0cfd-cd613f7420c9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82f5703e-2e5f-9156-addf-4dbac824249b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidNonContinuousRailProfile Method

---



|  |
| --- |
| [NonContinuousRailInfo Class](1ba1192c-2cfc-7996-e087-6b515ea4fb15.htm)   [See Also](#seeAlsoToggle) |

Checks whether the input id represents a profile which can be used as the profile of this non-continuous rail.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public bool IsValidNonContinuousRailProfile( 	ElementId profileId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidNonContinuousRailProfile ( _ 	profileId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidNonContinuousRailProfile( 	ElementId^ profileId ) ``` |

#### Parameters

profileId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The profile Id to be checked.

#### Return Value

True if the ElementId refers to a valid NonContinuousRail profile, false otherwise.

# Remarks

[InvalidElementId](08ae8886-6ab3-3ef5-d2e0-0da2ffa7bd2c.htm)  is considered a valid NonContinuousRail profile (the default profile).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[NonContinuousRailInfo Class](1ba1192c-2cfc-7996-e087-6b515ea4fb15.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__82f96572-6f19-95df-38c2-736e4bbafd5a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCData Constructor

---



|  |
| --- |
| [IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.htm)   [See Also](#seeAlsoToggle) |

Creates a copy object.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public IFCData( 	IFCData from ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	from As IFCData _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: IFCData( 	IFCData^ from ) ``` |

#### Parameters

from
:   Type:  [Autodesk.Revit.DB.IFC IFCData](34762033-771a-ebee-bd69-509c55ae78f0.htm)    
     The IFCData object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__82fadee2-5086-ae2e-3e48-648b1bc9039d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpacingLayoutn2 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Layout"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpacingLayoutn2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpacingLayoutn2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpacingLayoutn2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__82fb5b33-008d-586a-8750-4a78864d7939.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationPartSizeMap Constructor (String, Double, Double, Boolean)

---



|  |
| --- |
| [FabricationPartSizeMap Class](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of the FabricationPartSizeMap class.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.2

# Syntax

| C# |
| --- |
| ``` public FabricationPartSizeMap( 	string size, 	double widthDiameter, 	double depth, 	bool isProductList ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	size As String, _ 	widthDiameter As Double, _ 	depth As Double, _ 	isProductList As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: FabricationPartSizeMap( 	String^ size,  	double widthDiameter,  	double depth,  	bool isProductList ) ``` |

#### Parameters

size
:   Type:  System String    
     The size display string for the straight that can be used by the user interface.

widthDiameter
:   Type:  System Double    
     The width or diameter of the straight.

depth
:   Type:  System Double    
     The depth of the straight.

isProductList
:   Type:  System Boolean    
     Set if the straight a product list or not.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationPartSizeMap Class](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.htm)

[FabricationPartSizeMap Overload](0448905d-7f22-4d62-e8f8-05e4d6141056.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)

<!-- Start of Syntax__82fe5634-18f9-b315-9f1b-7e2843792cd3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForceRegenSketch Property

---



|  |
| --- |
| [BuiltInFailures RegenFailures Class](c7726de2-e4f0-8861-8115-0ef9de7935b1.htm)   [See Also](#seeAlsoToggle) |

Regen Sketch

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ForceRegenSketch { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ForceRegenSketch As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ForceRegenSketch { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RegenFailures Class](c7726de2-e4f0-8861-8115-0ef9de7935b1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83a0b23d-f14f-2aa2-6add-83abdb2b47ce.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DeleteSubElement Method

---



|  |
| --- |
| [Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)   [See Also](#seeAlsoToggle) |

Delete a face/edge/curve/vertex of the form, specified by a reference.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void DeleteSubElement( 	Reference subElementReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub DeleteSubElement ( _ 	subElementReference As Reference _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void DeleteSubElement( 	Reference^ subElementReference ) ``` |

#### Parameters

subElementReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The geometry reference of face/edge/curve/vertex

# See Also

[Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83a2812f-af21-6eba-833b-081f0f980377.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IfcApplicationVersion Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"IfcApplicationVersion"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId IfcApplicationVersion { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property IfcApplicationVersion As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ IfcApplicationVersion { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83a42cb4-37dc-d985-ed37-9326b7d06bbd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AllUsersAddinsLocation Property

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

The folder location for .addin files for all users.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public string AllUsersAddinsLocation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property AllUsersAddinsLocation As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ AllUsersAddinsLocation { 	String^ get (); } ``` |

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__83a6f623-33ba-2a01-4620-4146d482d8b0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsShowDownText Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Show Down Text"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsShowDownText { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsShowDownText As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsShowDownText { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83b1ca77-652a-580e-9461-004603675986.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MajorLapSpliceFailure Property

---



|  |
| --- |
| [BuiltInFailures FabricFailures Class](1e10bead-55d2-51cb-dd33-80ed534cb0a8.htm)   [See Also](#seeAlsoToggle) |

The lap splice in the major direction is greater than the half of the overall length.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId MajorLapSpliceFailure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MajorLapSpliceFailure As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ MajorLapSpliceFailure { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FabricFailures Class](1e10bead-55d2-51cb-dd33-80ed534cb0a8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83b3fae4-ef2f-1fda-12a5-6ad78df070b6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarMaximSuffix Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Maxim Suffix"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarMaximSuffix { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarMaximSuffix As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarMaximSuffix { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83b951b2-dadd-ac46-82e6-40003a29403e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEmpty Property

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Checks whether this CompoundStructure is empty.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83b95bbf-6e6d-25ab-053b-441447ac389f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreOptionsValidForTransientDirectShape Method

---



|  |
| --- |
| [DirectShape Class](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.htm)   [See Also](#seeAlsoToggle) |

Validates that the given DirectShapeOptions are allowed if this DirectShape is transient.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool AreOptionsValidForTransientDirectShape( 	DirectShapeOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AreOptionsValidForTransientDirectShape ( _ 	options As DirectShapeOptions _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool AreOptionsValidForTransientDirectShape( 	DirectShapeOptions^ options ) ``` |

#### Parameters

options
:   Type:  [Autodesk.Revit.DB DirectShapeOptions](be2135fc-6e44-0557-3fed-c91306ec2084.htm)    
     The options object.

#### Return Value

True if the DirectShapeOptions are valid; false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShape Class](bfbd137b-c2c2-71bb-6f4a-992d0dcf6ea8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83b9c6ff-4eba-9314-ff97-f607a698a374.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementPhaseStatusFilter Constructor (ElementId, ICollection(ElementOnPhaseStatus), Boolean)

---



|  |
| --- |
| [ElementPhaseStatusFilter Class](7767020a-2564-2c46-689d-59c2abe6e777.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a file to match elements that have a given phase statuses on the input phase, with the option to match all elements that have a phase status other than the input statuses.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementPhaseStatusFilter( 	ElementId phaseId, 	ICollection<ElementOnPhaseStatus> phaseStatuses, 	bool inverted ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	phaseId As ElementId, _ 	phaseStatuses As ICollection(Of ElementOnPhaseStatus), _ 	inverted As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementPhaseStatusFilter( 	ElementId^ phaseId,  	ICollection<ElementOnPhaseStatus>^ phaseStatuses,  	bool inverted ) ``` |

#### Parameters

phaseId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of the phase.

phaseStatuses
:   Type:  System.Collections.Generic ICollection   [ElementOnPhaseStatus](bfc481cc-11c8-de0b-1d71-7b2ffa711780.htm)    
     Target statuses.

inverted
:   Type:  System Boolean    
     True to match all phase statuses other than the input statuses.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElementPhaseStatusFilter Class](7767020a-2564-2c46-689d-59c2abe6e777.htm)

[ElementPhaseStatusFilter Overload](8e99068c-9562-334b-fc5f-65c0e620a131.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83c09b9a-763d-76ad-3d2a-1ac3b987f6f8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElemHoleType Property

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
| ``` public static ForgeTypeId SteelElemHoleType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElemHoleType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SteelElemHoleType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83c20bb5-418e-030d-63b4-7fa6524cd406.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LessThan Operator

---



|  |
| --- |
| [ForgeTypeId Class](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static bool operator <( 	ForgeTypeId lhs, 	ForgeTypeId rhs ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Operator < ( _ 	lhs As ForgeTypeId, _ 	rhs As ForgeTypeId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool operator <( 	ForgeTypeId^ lhs,  	ForgeTypeId^ rhs ) ``` |

#### Parameters

lhs
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)

rhs
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)

# See Also

[ForgeTypeId Class](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83c23e11-64cf-0d4c-1233-d90f69c7de8e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CoordinateSystem Property

---



|  |
| --- |
| [IConnector Interface](d5c02879-947d-d177-9c9a-52f662371da7.htm)   [See Also](#seeAlsoToggle) |

The coordinate system of the connector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` Transform CoordinateSystem { get; } ``` |

 

| Visual Basic |
| --- |
| ``` ReadOnly Property CoordinateSystem As Transform 	Get ``` |

 

| Visual C++ |
| --- |
| ``` property Transform^ CoordinateSystem { 	Transform^ get (); } ``` |

# Remarks

The Z axis of the coordinate system is the normal to the plane of the connector.

# See Also

[IConnector Interface](d5c02879-947d-d177-9c9a-52f662371da7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83ca0005-4722-2b92-21b6-7be74e1b6d8b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [ExportLineweightTableIterator Class](84d255f3-ffc6-5458-1655-f109db371045.htm)   [See Also](#seeAlsoToggle) |

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

[ExportLineweightTableIterator Class](84d255f3-ffc6-5458-1655-f109db371045.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83cc5022-7cbf-1d95-3452-313c14783dc9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LitersPerSecond Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Liters per second.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LitersPerSecond { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LitersPerSecond As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LitersPerSecond { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83cce5df-019e-74e5-e943-f180d7aeef73.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpotSlopePrefix Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Prefix"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpotSlopePrefix { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpotSlopePrefix As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpotSlopePrefix { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83d1ab5e-21c9-3b06-1ac2-59611e91659f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlternateUnitsSuffix Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Alternate Units Suffix"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AlternateUnitsSuffix { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AlternateUnitsSuffix As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AlternateUnitsSuffix { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83db2a29-aa67-8f78-eec1-cc934858523e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsDuctSystemTypeParam Property

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
| ``` public static ForgeTypeId RbsDuctSystemTypeParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsDuctSystemTypeParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsDuctSystemTypeParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83deaccf-a4a8-3e4d-837d-d0fa5d9f8d12.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurveTooShort Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Line is too short.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CurveTooShort { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CurveTooShort As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CurveTooShort { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83dffa17-a810-b1a1-927b-fd18a76aca5a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CouplerTypeInvalid Property

---



|  |
| --- |
| [BuiltInFailures RebarCouplerFailures Class](f1af7139-8dc7-c6de-b703-b01eb95fdff3.htm)   [See Also](#seeAlsoToggle) |

This coupler type does not fit on the selected bar(s). Post error to delete the coupler.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CouplerTypeInvalid { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CouplerTypeInvalid As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CouplerTypeInvalid { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarCouplerFailures Class](f1af7139-8dc7-c6de-b703-b01eb95fdff3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83e01a4d-d51e-42bf-fe18-7c5856fe5c6e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LineColor Property

---



|  |
| --- |
| [MEPSystemType Class](9a14b7f0-1472-4375-c4f0-86f9f2479851.htm)   [See Also](#seeAlsoToggle) |

Indicates the color that should override the line color for all components in the system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public Color LineColor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LineColor As Color 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Color^ LineColor { 	Color^ get (); 	void set (Color^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[MEPSystemType Class](9a14b7f0-1472-4375-c4f0-86f9f2479851.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83e340d0-8c2c-d845-d8d5-2fb6aa64f085.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Curve Property

---



|  |
| --- |
| [Dimension Class](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm)   [See Also](#seeAlsoToggle) |

A curve that represents the dimension line.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Curve Curve { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Curve As Curve 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Curve^ Curve { 	Curve^ get (); } ``` |

# See Also

[Dimension Class](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83e46ea0-5dee-1352-f532-101a3f534de4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MullionTypeSet Class

---



|  |
| --- |
| [Members](e7499fcc-5288-285b-8af8-a9d09e62d46f.htm)   [See Also](#seeAlsoToggle) |

A set that contains mullion types.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class MullionTypeSet : APIObject,  	IEnumerable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class MullionTypeSet _ 	Inherits APIObject _ 	Implements IEnumerable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class MullionTypeSet : public APIObject,  	IEnumerable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB MullionTypeSet

# See Also

[MullionTypeSet Members](e7499fcc-5288-285b-8af8-a9d09e62d46f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83e707a0-aa09-9348-393f-3ec385587327.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProhibitSwitchToIssuedRevision Property

---



|  |
| --- |
| [BuiltInFailures RevisionCloudFailures Class](b102052c-78c1-1c28-486a-8aa5f3165568.htm)   [See Also](#seeAlsoToggle) |

Can't add cloud to an Issued Revision.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ProhibitSwitchToIssuedRevision { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ProhibitSwitchToIssuedRevision As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ProhibitSwitchToIssuedRevision { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RevisionCloudFailures Class](b102052c-78c1-1c28-486a-8aa5f3165568.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83ec5569-bbab-eb7e-f53c-89b176329cee.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointCloudColorSettings Constructor

---



|  |
| --- |
| [PointCloudColorSettings Class](5f7af794-d52e-76a2-c38b-33eed5242484.htm)   [See Also](#seeAlsoToggle) |

Constructs color settings object with default colors.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public PointCloudColorSettings() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: PointCloudColorSettings() ``` |

# See Also

[PointCloudColorSettings Class](5f7af794-d52e-76a2-c38b-33eed5242484.htm)

[PointCloudColorSettings Overload](ec163487-78bf-ffd0-bde5-12823e40f6a3.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__83f2b024-78ad-2f9f-6d17-0e0d33061010.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotDivideCurtainGrid Property

---



|  |
| --- |
| [BuiltInFailures CurtainWallFailures Class](a3d691c9-5f8f-29ca-cfad-fa1d1d66f203.htm)   [See Also](#seeAlsoToggle) |

Can't divide Curtain Grid by Grid Line.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotDivideCurtainGrid { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotDivideCurtainGrid As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotDivideCurtainGrid { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CurtainWallFailures Class](a3d691c9-5f8f-29ca-cfad-fa1d1d66f203.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83f4add7-1c0a-ddfa-b8ab-5be6df0f28a2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Unload Method

---



|  |
| --- |
| [RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)   [See Also](#seeAlsoToggle) |

Unloads the Revit link.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Unload( 	ISaveSharedCoordinatesCallback callback ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Unload ( _ 	callback As ISaveSharedCoordinatesCallback _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Unload( 	ISaveSharedCoordinatesCallback^ callback ) ``` |

#### Parameters

callback
:   Type:  [Autodesk.Revit.DB ISaveSharedCoordinatesCallback](ed4eac2a-d482-7760-2ae7-855611d09c46.htm)    
     A callback indicating what to do if Revit encounters links which have changes in shared coordinates. If    a null reference (  Nothing  in Visual Basic)  , Revit will not save any shared coordinates changes to the link before unloading.

# Remarks

This function regenerates the document.

The document's Undo history will be cleared by this command. As a result, this command and others executed before it cannot be undone. All transaction phases (e.g. transactions transaction groups and sub-transaction) that were explicitly started must be finished prior to calling this method.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | The function is not permitted during dynamic update. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RevitLinkType is not a top-level link. -or- The element "this RevitLinkType" is in a closed workset. -or- Revit could not save shared coordinates changes to the link or one of its nested links. -or- There is a transaction phase left open (such as a transaction, sub-transaction of transaction group) at the time of invoking this method. -or- The document is read-only. It cannot be modified. -or- The document is in an edit mode or is in family mode. -or- Revit cannot link a cloud model to non-cloud model |
| [Autodesk.Revit.Exceptions RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.htm) | Could be for any of the reasons that failed on service side. |
| [Autodesk.Revit.Exceptions RevitServerUnauthenticatedUserException](b9b68e56-c767-4680-a65b-73d268ee8860.htm) | User is not signed in with Autodesk id. |
| [Autodesk.Revit.Exceptions RevitServerUnauthorizedException](9e8c1efc-8719-fe01-f311-cfade7b177ed.htm) | User is not authorized to access the specified cloud model. |

# See Also

[RevitLinkType Class](2204a5ab-6476-df41-116d-23dbe3cb5407.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83f69554-54d6-1632-fb6c-81edf0280d33.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentReloadedLatest Event

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the DocumentReloadedLatestEventArgs event to be notified immediately after Revit has finished reloading a document with central model.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public event EventHandler<DocumentReloadedLatestEventArgs> DocumentReloadedLatest ``` |

 

| Visual Basic |
| --- |
| ``` Public Event DocumentReloadedLatest As EventHandler(Of DocumentReloadedLatestEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<DocumentReloadedLatestEventArgs^>^ DocumentReloadedLatest { 	void add (EventHandler<DocumentReloadedLatestEventArgs^>^ value); 	void remove (EventHandler<DocumentReloadedLatestEventArgs^>^ value); } ``` |

# Remarks

This event is raised immediately after Revit has finished reloading latest changes from a central model. It is raised even when document reloading latest changes from a central model failed or was cancelled (during DocumentReloadingLatest event).

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Check the 'Status' field in event's argument to see whether the action itself was successful or not.

This event is not cancellable, for the process of reloading latest changes from a central model has already been finished.

If the action was not successful, the document may not be modified and new transactions may not be started.

The following API functions are not available for the current document during this event:

* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  .
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__83f822d9-2637-4585-1e28-08f08940e923.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CircularFramingDiameter Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Circular Diameter"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CircularFramingDiameter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CircularFramingDiameter As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CircularFramingDiameter { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83f85da2-200e-1a3f-f879-9778de9ff548.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConceptualConstructionShadeType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

ConceptualConstructionType values for Shades.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public enum ConceptualConstructionShadeType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ConceptualConstructionShadeType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ConceptualConstructionShadeType ``` |

# Members

| Member name | Description |
| --- | --- |
| InvalidShadeTypeConstruction | Invalid value/not set Shade Type Construction |
| BasicShade | Basic Shade |
| NumShadeTypeConstruction | Total Number of Shade Type Constructions |

# See Also

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__83fa4b05-eb78-3db7-3305-8fe8bf56f2a8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StirrupTieBendDiameter Property

---



|  |
| --- |
| [BarTypeDiameterOptions Class](a4f6aef6-f961-7b77-7c4b-6248193c258a.htm)   [See Also](#seeAlsoToggle) |

Represents the stirrup/tie bar and hook bend diameter of the RebarBarType.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

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

# See Also

[BarTypeDiameterOptions Class](a4f6aef6-f961-7b77-7c4b-6248193c258a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83fd26c0-15dc-ac21-a2af-9567438b0605.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsUnitLength Method

---



|  |
| --- |
| [XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)   [See Also](#seeAlsoToggle) |

The boolean value that indicates whether this vector is of unit length.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsUnitLength() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsUnitLength As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsUnitLength() ``` |

# Remarks

A unit length vector has a length of one, and is considered normalized.

# See Also

[XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__83ff5239-509d-7588-3a02-6bf97ffa3df8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportFontKey Constructor (String)

---



|  |
| --- |
| [ExportFontKey Class](bd33456d-7898-f32c-312e-b94af14c0007.htm)   [See Also](#seeAlsoToggle) |

Constructs a new ExportFontKey using an input font name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ExportFontKey( 	string originalFontName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	originalFontName As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ExportFontKey( 	String^ originalFontName ) ``` |

#### Parameters

originalFontName
:   Type:  System String    
     The original font name.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportFontKey Class](bd33456d-7898-f32c-312e-b94af14c0007.htm)

[ExportFontKey Overload](ff73cf2a-8632-5b2b-0b74-c89fa8fe0963.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84a0db17-c3d3-bf8b-e80b-e8d5b419ce1c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProfileSketch Property

---



|  |
| --- |
| [Sweep Class](ed383459-badd-2323-4f73-0d94fd76ce0f.htm)   [See Also](#seeAlsoToggle) |

The profile sketch of the sweep.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Sketch ProfileSketch { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ProfileSketch As Sketch 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Sketch^ ProfileSketch { 	Sketch^ get (); } ``` |

# Remarks

If the profile is not based on sketched curves, this property is    a null reference (  Nothing  in Visual Basic)  .

# See Also

[Sweep Class](ed383459-badd-2323-4f73-0d94fd76ce0f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84a17391-2842-2b65-7e99-21cd00de91f6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsFpSprinklerOrificeSizeParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Orifice Size"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsFpSprinklerOrificeSizeParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsFpSprinklerOrificeSizeParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsFpSprinklerOrificeSizeParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84a5e6ac-480e-cc1e-936c-912f22080c1d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UserHasGraphicOverrides Method

---



|  |
| --- |
| [WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)   [See Also](#seeAlsoToggle) |

Checks whether there are graphic overrides that would apply to elements owned by the given user in the "Individual Owners" display mode.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool UserHasGraphicOverrides( 	string username ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function UserHasGraphicOverrides ( _ 	username As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool UserHasGraphicOverrides( 	String^ username ) ``` |

#### Parameters

username
:   Type:  System String    
     The username to check

#### Return Value

True if there are graphic overrides assigned to the username, false otherwise.

# Remarks

There will always be graphic overrides for all users included in the user table. In addition, there may be other users who have been explicitly assigned overrides.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84a67eb1-4a03-b19f-50ca-47b3dc48097b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MultusegmentRampRiserError Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Ramp can't have multisegment Riser.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId MultusegmentRampRiserError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MultusegmentRampRiserError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ MultusegmentRampRiserError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84a847f0-1601-e65f-170e-d99e1c396373.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsDbgShowRunGeom Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Show Run Geometry"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsDbgShowRunGeom { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsDbgShowRunGeom As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsDbgShowRunGeom { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84b3bac3-82c9-2a9c-a680-588628aaa722.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FailedToRemoveElement Property

---



|  |
| --- |
| [BuiltInFailures ElementFailures Class](efa812cc-5762-0a0c-3c84-6b777337bf71.htm)   [See Also](#seeAlsoToggle) |

Element cannot be removed from the solution. The solution is required to have at least two elements to be valid.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FailedToRemoveElement { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FailedToRemoveElement As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FailedToRemoveElement { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ElementFailures Class](efa812cc-5762-0a0c-3c84-6b777337bf71.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84bd09c5-00dc-2238-1bd4-562e22dbbea5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetValidCategoriesForKeySchedule Method

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

Gets a list of categories that can be used for a key schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetValidCategoriesForKeySchedule() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetValidCategoriesForKeySchedule As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetValidCategoriesForKeySchedule() ``` |

#### Return Value

The IDs of all valid categories.

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84bd650f-9f87-dccb-4dd4-b23ca890b8b9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FunctionId Property

---



|  |
| --- |
| [ApplicationException Class](05012a96-16ea-ace7-6115-b45406dacead.htm)   [See Also](#seeAlsoToggle) |

The information of the function throwing the exception.

**Namespace:**   [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FunctionId FunctionId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property FunctionId As FunctionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property FunctionId^ FunctionId { 	FunctionId^ get (); } ``` |

# See Also

[ApplicationException Class](05012a96-16ea-ace7-6115-b45406dacead.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__84be37b4-0179-39f4-d1ab-01ceff12ae48.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Intersecting Property

---



|  |
| --- |
| [BuiltInFailures PlanRegionFailures Class](eaa8963c-1976-45bc-0d87-581593dbdeb7.htm)   [See Also](#seeAlsoToggle) |

The boundaries of the highlighted Plan Regions overlap.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId Intersecting { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Intersecting As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ Intersecting { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures PlanRegionFailures Class](eaa8963c-1976-45bc-0d87-581593dbdeb7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84c1718f-1a96-d430-32f3-edc4e980c6fc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsVisibleParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Visible"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId IsVisibleParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property IsVisibleParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ IsVisibleParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84c1fdb2-c22e-680e-ca70-060d5998e145.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [BoundingBoxUV Class](e38a0145-4267-0b3f-0718-adb14e34c94e.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [BoundingBoxUV](e38a0145-4267-0b3f-0718-adb14e34c94e.htm)

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

[BoundingBoxUV Class](e38a0145-4267-0b3f-0718-adb14e34c94e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84c4992a-c355-2a2b-23de-606791e00e03.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveTemperatureRatingType Method

---



|  |
| --- |
| [WireMaterialType Class](3d05ec79-0289-c6d1-2a13-7e6b07241afd.htm)   [See Also](#seeAlsoToggle) |

Remove an existing temperature rating type from this material type.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void RemoveTemperatureRatingType( 	TemperatureRatingType temperatureRating ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveTemperatureRatingType ( _ 	temperatureRating As TemperatureRatingType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveTemperatureRatingType( 	TemperatureRatingType^ temperatureRating ) ``` |

#### Parameters

temperatureRating
:   Type:  [Autodesk.Revit.DB.Electrical TemperatureRatingType](fe7e15d7-c31f-b24c-992f-332e54e9a5ba.htm)    
     The temperature rating type to be removed.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The last temperature rating type of project and any one used by a wire type can't be removed. |

# See Also

[WireMaterialType Class](3d05ec79-0289-c6d1-2a13-7e6b07241afd.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__84cfa6b2-460d-9d32-1f6a-55dbbfece098.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarPresentationMode Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Bar presentation mode

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public enum RebarPresentationMode ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration RebarPresentationMode ``` |

 

| Visual C++ |
| --- |
| ``` public enum class RebarPresentationMode ``` |

# Members

| Member name | Description |
| --- | --- |
| All | All bars are presented. |
| FirstLast | The first and last bars are presented. |
| Middle | The middle bar is presented. |
| Select | Selected bars are presented. |

# See Also

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__84d067ae-d08b-1345-55ce-8086c24cc538.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsConnected Property

---



|  |
| --- |
| [Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)   [See Also](#seeAlsoToggle) |

Identifies if the connector is physically connected to a connector on another element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsConnected { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsConnected As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsConnected { 	bool get (); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the connector's type is LogicalConn. |

# See Also

[Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84d0820f-20d2-bda1-5859-f2033a72bb84.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HVACLoadConstructionClass Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Enumerated type listing options for construction class for HVAC analysis.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public enum HVACLoadConstructionClass ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration HVACLoadConstructionClass ``` |

 

| Visual C++ |
| --- |
| ``` public enum class HVACLoadConstructionClass ``` |

# Members

| Member name | Description |
| --- | --- |
| LooseConstruction | A loose construction has an infiltration level of approximately 0.076 cfm/sqft |
| MediumConstruction | A medium construction has an infiltration level of approximately 0.038 cfm/sqft |
| TightConstruction | A tight construction has an infiltration level of approximately 0.019 cfm/sqft |
| NoneConstruction | A none construction has an infiltration level of 0 cfm/sqft |

# See Also

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__84d255f3-ffc6-5458-1655-f109db371045.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportLineweightTableIterator Class

---



|  |
| --- |
| [Members](d5798a1b-afcb-f625-1fda-83ecfeecd999.htm)   [See Also](#seeAlsoToggle) |

An iterator to a set of line weight table.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class ExportLineweightTableIterator : IEnumerator<KeyValuePair<ExportLineweightKey, ExportLineweightInfo>> ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ExportLineweightTableIterator _ 	Implements IEnumerator(Of KeyValuePair(Of ExportLineweightKey, ExportLineweightInfo)) ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ExportLineweightTableIterator : IEnumerator<KeyValuePair<ExportLineweightKey^, ExportLineweightInfo^>> ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ExportLineweightTableIterator

# See Also

[ExportLineweightTableIterator Members](d5798a1b-afcb-f625-1fda-83ecfeecd999.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84d5855c-fba2-b026-ee60-7f2a24b78129.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhaseStatusPresentation Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing the options for element display in a phase filter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum PhaseStatusPresentation ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration PhaseStatusPresentation ``` |

 

| Visual C++ |
| --- |
| ``` public enum class PhaseStatusPresentation ``` |

# Members

| Member name | Description |
| --- | --- |
| DontShow | Don't show elements from the given phase status. |
| ShowByCategory | Show elements from the given phase status by category. |
| ShowOverriden | Show elements from the given phase status by graphics overrides. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84d6967a-63b0-008c-9f03-4ebbcc92e115.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CeramicBump Property

---



|  |
| --- |
| [Ceramic Class](3f990d29-c743-ab3f-0a30-3b0a9b1f14cf.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Type" from the "Ceramic" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string CeramicBump { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CeramicBump As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ CeramicBump { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyInteger" with accepted values in the enumerated type "CeramicBumpType".

# See Also

[Ceramic Class](3f990d29-c743-ab3f-0a30-3b0a9b1f14cf.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__84da3f9b-5587-e060-db8e-cc9dbe1cac48.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsHvacloadWindowCoolingLoadParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Window Cooling Load"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsHvacloadWindowCoolingLoadParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsHvacloadWindowCoolingLoadParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsHvacloadWindowCoolingLoadParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84db8221-5692-ff8f-e5b1-e968a389ed0c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReverseIterator Method

---



|  |
| --- |
| [ReferenceArrayArray Class](b50edc19-b437-2aab-bd03-5d1a0aed4164.htm)   [See Also](#seeAlsoToggle) |

Retrieve a backward moving iterator to the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual ReferenceArrayArrayIterator ReverseIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ReverseIterator As ReferenceArrayArrayIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual ReferenceArrayArrayIterator^ ReverseIterator() ``` |

#### Return Value

Returns a backward moving iterator to the array.

# See Also

[ReferenceArrayArray Class](b50edc19-b437-2aab-bd03-5d1a0aed4164.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84dee1b6-d008-e039-6f06-6e984920228c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PushExportState Method

---



|  |
| --- |
| [ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)   [See Also](#seeAlsoToggle) |

Sets the internal state of the exporter to process the geometry and properties of the input element.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void PushExportState( 	Element Elem, 	GeometryElement GRep ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub PushExportState ( _ 	Elem As Element, _ 	GRep As GeometryElement _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void PushExportState( 	Element^ Elem,  	GeometryElement^ GRep ) ``` |

#### Parameters

Elem
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element.

GRep
:   Type:  [Autodesk.Revit.DB GeometryElement](09eaeb08-58bb-8049-8925-f3a5aa846fdc.htm)    
     The geometry of the element. Optional, can be    a null reference (  Nothing  in Visual Basic)  .

# Remarks

The element will be assigned until PopExportState() is called.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__84e3e931-b085-01b3-3dc2-954234356b8f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Flipped Property

---



|  |
| --- |
| [Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)   [See Also](#seeAlsoToggle) |

Property to test whether the wall orientation is flipped.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

# See Also

[Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84e92ca4-6c6a-af82-454e-1c0b7b145398.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OpenIFCDocument Method (String, IFCImportOptions)

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Opens an IFC document from disk using custom options.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public Document OpenIFCDocument( 	string fileName, 	IFCImportOptions importOptions ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function OpenIFCDocument ( _ 	fileName As String, _ 	importOptions As IFCImportOptions _ ) As Document ``` |

 

| Visual C++ |
| --- |
| ``` public: Document^ OpenIFCDocument( 	String^ fileName,  	IFCImportOptions^ importOptions ) ``` |

#### Parameters

fileName
:   Type:  System String    
     The IFC file to be opened.

importOptions
:   Type:  [Autodesk.Revit.DB.IFC IFCImportOptions](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)    
     The options for this import.

#### Return Value

The newly created document containing the IFC file.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | If 'fileName' is an empty string. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | If the file specified by 'fileName' cannot be found. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | If Revit is missing document templates or if the file cannot be opened. |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[OpenIFCDocument Overload](b7929f76-6c0f-1363-4683-8501a0d582a5.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__84efff3b-dc62-9d0b-997e-d1326c82f438.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationPartDiameterIn Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Main Primary Diameter"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FabricationPartDiameterIn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationPartDiameterIn As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FabricationPartDiameterIn { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84f03bb5-a9b8-581c-631c-6240b4954099.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SchedulableField Class

---



|  |
| --- |
| [Members](ae26ab44-7895-a499-58f8-9563bf2ca1ad.htm)   [See Also](#seeAlsoToggle) |

A non-calculated field eligible to be included in a schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class SchedulableField : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class SchedulableField _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SchedulableField : IDisposable ``` |

# Remarks

The SchedulableField class represents a non-calculated field that is eligible to be included in a schedule. A list of fields that can be included in a schedule can be obtained from ScheduleDefinition.GetSchedulableFields.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB SchedulableField

# See Also

[SchedulableField Members](ae26ab44-7895-a499-58f8-9563bf2ca1ad.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84f0914f-b947-0d23-3d0e-aea92822c5f1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextElementType Class

---



|  |
| --- |
| [Members](4d42ad90-d090-016e-e6c2-32b54a8a9663.htm)   [See Also](#seeAlsoToggle) |

An object that represents a text style.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class TextElementType : LineAndTextAttrSymbol ``` |

 

| Visual Basic |
| --- |
| ``` Public Class TextElementType _ 	Inherits LineAndTextAttrSymbol ``` |

 

| Visual C++ |
| --- |
| ``` public ref class TextElementType : public LineAndTextAttrSymbol ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  [Autodesk.Revit.DB LineAndTextAttrSymbol](1a0a0d23-891b-bf92-6b2b-069704dea9be.htm)    
  Autodesk.Revit.DB TextElementType    
  [Autodesk.Revit.DB TextNoteType](2991b6af-daf6-463d-3796-8b83fdbd344f.htm)

# See Also

[TextElementType Members](4d42ad90-d090-016e-e6c2-32b54a8a9663.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84f4d0e3-ae49-c2f8-d7d3-53d120fe3223.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateViewTemplate Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Creates a new view template instance from this view instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public View CreateViewTemplate() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CreateViewTemplate As View ``` |

 

| Visual C++ |
| --- |
| ``` public: View^ CreateViewTemplate() ``` |

#### Return Value

New view template instance

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The view is not valid for view template creation. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__84f74cd7-56ee-b3e7-2bd7-cfe3afbf9904.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Insert Method

---



|  |
| --- |
| [ExternalApplicationArray Class](5388ad7c-8963-37c7-e021-d0155edccb7a.htm)   [See Also](#seeAlsoToggle) |

Insert the specified item into the array.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual void Insert( 	IExternalApplication item, 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Sub Insert ( _ 	item As IExternalApplication, _ 	index As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Insert( 	IExternalApplication^ item,  	int index ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.UI IExternalApplication](196c8712-71de-03e8-b30d-a9625bd626d2.htm)    
     The item to be inserted into the array.

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The item will be inserted before this index.

#### Return Value

Returns whether the item was inserted into the array.

# See Also

[ExternalApplicationArray Class](5388ad7c-8963-37c7-e021-d0155edccb7a.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__84fd6e14-7c7c-4c71-1067-fcf078d950e7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalMemberForceStartAllNonZero Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"All non 0 forces at start"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnalyticalMemberForceStartAllNonZero { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticalMemberForceStartAllNonZero As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnalyticalMemberForceStartAllNonZero { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85a1df84-025b-4643-0e8a-4385768a4974.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceDepreciationLossFactor Property

---



|  |
| --- |
| [AdvancedLossFactor Class](30e62a9d-eb01-8830-f897-dc8f32b486da.htm)   [See Also](#seeAlsoToggle) |

The surface depreciation loss factor.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double SurfaceDepreciationLossFactor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SurfaceDepreciationLossFactor As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double SurfaceDepreciationLossFactor { 	double get (); 	void set (double value); } ``` |

#### Field Value

The loss factor as a numerical value between 0.0 and 1.0

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The loss factor is not valid because it is not between 0.0 and 1.0. |

# See Also

[AdvancedLossFactor Class](30e62a9d-eb01-8830-f897-dc8f32b486da.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__85a528cd-a15b-263f-5849-6dccb567250b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [DefinitionBindingMapIterator Class](54fa1065-02f7-f4e8-3440-5ec269d422f4.htm)   [See Also](#seeAlsoToggle) |

Retrieves the binding that is the current focus of the iterator.

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

[DefinitionBindingMapIterator Class](54fa1065-02f7-f4e8-3440-5ec269d422f4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85aac403-65ce-356e-2075-a2429a712509.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetAttribute Method (String, String)

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
| ``` public void SetAttribute( 	string name, 	string value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetAttribute ( _ 	name As String, _ 	value As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetAttribute( 	String^ name,  	String^ value ) ``` |

#### Parameters

name
:   Type:  System String    
     The attribute name.

value
:   Type:  System String    
     The value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCAnyHandle Class](8b893943-70fa-94bf-90be-1523d516ecb3.htm)

[SetAttribute Overload](25c11a79-8e0f-5474-cbf5-6a3e7a2821d2.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__85ab1099-34fa-2804-c819-894b2c4e63d1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFunctions Method

---



|  |
| --- |
| [FormulaManager Class](d061dadf-70da-a883-ec12-5cf98ded069e.htm)   [See Also](#seeAlsoToggle) |

Gets list of function names supported by formula engine

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public static IList<string> GetFunctions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetFunctions As IList(Of String) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<String^>^ GetFunctions() ``` |

# See Also

[FormulaManager Class](d061dadf-70da-a883-ec12-5cf98ded069e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85ab2fb1-ac8f-58a7-d24f-cd8ed5990625.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Color Property

---



|  |
| --- |
| [ColorBackgroundSettings Class](f879a275-8244-d98a-50c6-2142fdcca188.htm)   [See Also](#seeAlsoToggle) |

The color of the rendering background.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public Color Color { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Color As Color 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Color^ Color { 	Color^ get (); 	void set (Color^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ColorBackgroundSettings Class](f879a275-8244-d98a-50c6-2142fdcca188.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85ad7768-e581-e529-be17-93c6d0e362d4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [VoltageTypeSetIterator Class](e4da0a34-f75b-2c48-45c4-cd3c82aaba89.htm)   [See Also](#seeAlsoToggle) |

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

[VoltageTypeSetIterator Class](e4da0a34-f75b-2c48-45c4-cd3c82aaba89.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__85af7224-b751-4c40-a5d5-5b4dc757f742.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HookAngle Property

---



|  |
| --- |
| [RebarHookType Class](3c7a78d5-f92b-e58b-e7c9-7927537498fd.htm)   [See Also](#seeAlsoToggle) |

The hook angle, measured in radians. Must be greater than 0 and no more than pi.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double HookAngle { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property HookAngle As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double HookAngle { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for hookAngle is not a number |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: hookAngle must be greater than 0 and no more than pi. |

# See Also

[RebarHookType Class](3c7a78d5-f92b-e58b-e7c9-7927537498fd.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__85af8ba4-7def-183f-a518-ddcccad470ea.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShortCurveInSketch Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

The sketch contains an extremely short line.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ShortCurveInSketch { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ShortCurveInSketch As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ShortCurveInSketch { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85b534b8-dd6c-bc13-7c46-c803c83481e4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImportInstance Class

---



|  |
| --- |
| [Members](fcedeca0-0e52-6a5f-b716-1d92c0fbac62.htm)   [See Also](#seeAlsoToggle) |

An element created during either import or link operation. It is an instance of CADLinkType.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public class ImportInstance : Instance ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ImportInstance _ 	Inherits Instance ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ImportInstance : public Instance ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB Instance](08603dd9-976d-a9fe-add7-2a8450b8006c.htm)    
  Autodesk.Revit.DB ImportInstance

# See Also

[ImportInstance Members](fcedeca0-0e52-6a5f-b716-1d92c0fbac62.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85b944dc-45d9-e99e-392b-1c720042cd78.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ControlledApplication Property

---



|  |
| --- |
| [UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)   [See Also](#seeAlsoToggle) |

Returns the database level ControlledApplication represented by this UI-level ControlledApplication.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ControlledApplication ControlledApplication { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ControlledApplication As ControlledApplication 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ControlledApplication^ ControlledApplication { 	ControlledApplication^ get (); } ``` |

# See Also

[UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__85c0ba1a-0300-82bb-29e9-584a3a525d2f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ColumnHeaders Property

---



|  |
| --- |
| [ViewScheduleExportOptions Class](f0bde7ea-ceab-820d-7c55-b09819f21607.htm)   [See Also](#seeAlsoToggle) |

How to export column headers. Default is MultipleRows.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ExportColumnHeaders ColumnHeaders { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ColumnHeaders As ExportColumnHeaders 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ExportColumnHeaders ColumnHeaders { 	ExportColumnHeaders get (); 	void set (ExportColumnHeaders value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ViewScheduleExportOptions Class](f0bde7ea-ceab-820d-7c55-b09819f21607.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85c18673-c186-4313-a063-9658072de7fa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReuseLocalPlacement Property

---



|  |
| --- |
| [IFCExtrusionCreationData Class](9447a335-6861-0533-6896-e6ff1fd41761.htm)   [See Also](#seeAlsoToggle) |

Allows re-use of local placement when creating a new local placement due to shifting of breps when moving towards the origin.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool ReuseLocalPlacement { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ReuseLocalPlacement As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ReuseLocalPlacement { 	bool get (); 	void set (bool value); } ``` |

# See Also

[IFCExtrusionCreationData Class](9447a335-6861-0533-6896-e6ff1fd41761.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__85c3438b-1946-69a0-fb3b-439109cdd9ef.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalModelTopExtensionMethod Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top Extension Method"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnalyticalModelTopExtensionMethod { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticalModelTopExtensionMethod As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnalyticalModelTopExtensionMethod { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85c395b2-49bd-573d-8a39-8b5414f8148d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LooseCurtainWallData Property

---



|  |
| --- |
| [BuiltInFailures LooseDimensionFailures Class](6e39a26c-cf18-4aa3-9974-e173df435407.htm)   [See Also](#seeAlsoToggle) |

Switching element type to a non-Curtain element Family type. All data about Mullions, Grid Lines, and design units for the Curtain element will be lost.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId LooseCurtainWallData { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LooseCurtainWallData As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ LooseCurtainWallData { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures LooseDimensionFailures Class](6e39a26c-cf18-4aa3-9974-e173df435407.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85c561ea-3683-e83d-5a3c-63a19e8e4f11.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsProductList Property

---



|  |
| --- |
| [FabricationPartSizeMap Class](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.htm)   [See Also](#seeAlsoToggle) |

Are the sizes for a product listed fabrication part.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.2

# Syntax

| C# |
| --- |
| ``` public bool IsProductList { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsProductList As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsProductList { 	bool get (); 	void set (bool value); } ``` |

# See Also

[FabricationPartSizeMap Class](b4be4ccc-ac6d-bb65-ef61-a41713b2916f.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)

<!-- Start of Syntax__85c61cf8-daa1-8aae-76c3-de8f100e9102.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBoundaryFaceInfo Method

---



|  |
| --- |
| [SpatialElementGeometryResults Class](150ca07e-90b0-506f-9b9c-fd39d194a7ea.htm)   [See Also](#seeAlsoToggle) |

Query the spatial element boundary face information with the given face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<SpatialElementBoundarySubface> GetBoundaryFaceInfo( 	Face face ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBoundaryFaceInfo ( _ 	face As Face _ ) As IList(Of SpatialElementBoundarySubface) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<SpatialElementBoundarySubface^>^ GetBoundaryFaceInfo( 	Face^ face ) ``` |

#### Parameters

face
:   Type:  [Autodesk.Revit.DB Face](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)    
     The face from the spatial element's geometry.

#### Return Value

Sub-faces related to the room bounding elements that define the spatial element face. Returns    a null reference (  Nothing  in Visual Basic)  if there is no corresponding boundary information with the given face.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SpatialElementGeometryResults Class](150ca07e-90b0-506f-9b9c-fd39d194a7ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85d170b7-facc-fb3b-22eb-21aabe4754ca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlignmentStationLabelSetOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Alignment Station Label Set Offset": The text is not used directly anywhere in the UI, instead the XAML specifies its own string for the value's label.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AlignmentStationLabelSetOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AlignmentStationLabelSetOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AlignmentStationLabelSetOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85d71c9a-e457-89c9-d17a-b3cbff2277f4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsLandingBaseElevation Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Relative Height": Height

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsLandingBaseElevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsLandingBaseElevation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsLandingBaseElevation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85d83276-ea23-5ad7-440f-667d93fde3c8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralAnalyticalHardPoints Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Use hard-points"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralAnalyticalHardPoints { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralAnalyticalHardPoints As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralAnalyticalHardPoints { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85d968c0-7ffe-dd2a-c7fa-cf339597f0e0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SupportCheckDone Property

---



|  |
| --- |
| [BuiltInFailures AnalyticalModelFailures Class](3633d562-0e24-5cad-ec0f-02e6cc6ad731.htm)   [See Also](#seeAlsoToggle) |

Member support check is complete. No unsupported elements detected.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SupportCheckDone { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SupportCheckDone As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SupportCheckDone { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AnalyticalModelFailures Class](3633d562-0e24-5cad-ec0f-02e6cc6ad731.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85dd2541-33d1-9fc9-4769-73cafd256d3e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ScheduleField](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)

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

[ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85dfcffb-52f5-bbcd-0a36-a3762df94c73.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotKeepAnalyticalAdjustment Property

---



|  |
| --- |
| [BuiltInFailures AnalyticalModelFailures Class](3633d562-0e24-5cad-ec0f-02e6cc6ad731.htm)   [See Also](#seeAlsoToggle) |

Analytical model Adjustment distance exceeds current Adjustment Snapping Distance. To adjust snap settings, go to the Structural Settings Dialog.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotKeepAnalyticalAdjustment { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotKeepAnalyticalAdjustment As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotKeepAnalyticalAdjustment { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AnalyticalModelFailures Class](3633d562-0e24-5cad-ec0f-02e6cc6ad731.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85ebbe3a-1aab-5d70-a076-b25062cf2a4b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TrussElementEnd0Elevation Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Start Level Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TrussElementEnd0Elevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TrussElementEnd0Elevation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TrussElementEnd0Elevation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85ecbce6-1b38-62f3-05e1-d9c65f317f54.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsConnectorDescription Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Connector Description"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsConnectorDescription { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsConnectorDescription As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsConnectorDescription { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85ed78bc-9687-a07d-4d94-5748b16cb970.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Code Property

---



|  |
| --- |
| [FabricationServiceButton Class](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)   [See Also](#seeAlsoToggle) |

The code of the button.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public string Code { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Code As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Code { 	String^ get (); } ``` |

# See Also

[FabricationServiceButton Class](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85ef6496-b0a7-a54f-407b-2fc243485f8c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationOutOfSizeCondition Property

---



|  |
| --- |
| [BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)   [See Also](#seeAlsoToggle) |

The fabrication part size is not within the correct size range for the service button condition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FabricationOutOfSizeCondition { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationOutOfSizeCondition As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FabricationOutOfSizeCondition { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85f2dafa-381e-60fd-2596-8ebb383f149b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRule Method

---



|  |
| --- |
| [RoutingPreferenceManager Class](a8300b97-72a6-beb5-733b-ec4cfea6c472.htm)   [See Also](#seeAlsoToggle) |

Gets the specified rule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public RoutingPreferenceRule GetRule( 	RoutingPreferenceRuleGroupType groupType, 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRule ( _ 	groupType As RoutingPreferenceRuleGroupType, _ 	index As Integer _ ) As RoutingPreferenceRule ``` |

 

| Visual C++ |
| --- |
| ``` public: RoutingPreferenceRule^ GetRule( 	RoutingPreferenceRuleGroupType groupType,  	int index ) ``` |

#### Parameters

groupType
:   Type:  [Autodesk.Revit.DB RoutingPreferenceRuleGroupType](79896fd9-e90c-6561-3bc4-7cefd4692ae5.htm)    
     The routing preference group type from which the rule should be returned.

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The zero-based index where the rule should be returned.

#### Return Value

The rule at the specified group and zero-based index position.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | index is not a valid zero-based index within groupType. -or- Thrown if the index is out of bounds |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[RoutingPreferenceManager Class](a8300b97-72a6-beb5-733b-ec4cfea6c472.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85f3cc07-2cdd-a26e-04e0-6b2a87871d14.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Voltage Property

---



|  |
| --- |
| [AnalyticalTransferSwitchData Class](6029f894-5a16-522b-8759-57b4e3475952.htm)   [See Also](#seeAlsoToggle) |

The voltage value of the electrical analytical transfer switch.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public double Voltage { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Voltage As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Voltage { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The given value for voltage is not a number -or- When setting this property: The given value for voltage is not finite |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for voltage must be positive. |

# See Also

[AnalyticalTransferSwitchData Class](6029f894-5a16-522b-8759-57b4e3475952.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__85f8c0f5-ecc0-82f1-3b18-7d2020ff7626.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsRunWinderBeginWithStraight Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Begin with Straight Run": Winder begin with straight run

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsRunWinderBeginWithStraight { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsRunWinderBeginWithStraight As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsRunWinderBeginWithStraight { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85f924aa-e8c9-a1f6-7c2e-c0934f8c9820.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarSystemBarTypeBottomDirn2 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bottom Minor Bar Type"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarSystemBarTypeBottomDirn2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarSystemBarTypeBottomDirn2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarSystemBarTypeBottomDirn2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__85fbefcc-4e26-dfdd-2f2c-d767978602f9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ParameterValueProvider Constructor

---



|  |
| --- |
| [ParameterValueProvider Class](5978eb2a-4598-f458-1504-80caff09cf7c.htm)   [See Also](#seeAlsoToggle) |

Constructs an instance of ParameterValueProvider.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ParameterValueProvider( 	ElementId parameter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	parameter As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ParameterValueProvider( 	ElementId^ parameter ) ``` |

#### Parameters

parameter
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The parameter used to provide a string, integer, and double-precision, or ElementId value on request for a given element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterValueProvider Class](5978eb2a-4598-f458-1504-80caff09cf7c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86a0df75-ba39-6c56-a11d-62cafb423a0a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReverseIterator Method

---



|  |
| --- |
| [CurtainGridSet Class](adc86636-024c-9035-700f-e7c43442a9f8.htm)   [See Also](#seeAlsoToggle) |

Retrieve a backward moving iterator to the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual CurtainGridSetIterator ReverseIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ReverseIterator As CurtainGridSetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual CurtainGridSetIterator^ ReverseIterator() ``` |

#### Return Value

Returns a backward moving iterator to the set.

# See Also

[CurtainGridSet Class](adc86636-024c-9035-700f-e7c43442a9f8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86a2ffcb-080a-5b95-57ad-c4caa69fafc9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MechanicalEquipmentSetIdParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Mechanical Equipment Set"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MechanicalEquipmentSetIdParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MechanicalEquipmentSetIdParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MechanicalEquipmentSetIdParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86a33da8-dd80-c3e4-be59-bcef78e11e1e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpotElevTickMarkPen Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Leader Arrowhead Line Weight"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpotElevTickMarkPen { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpotElevTickMarkPen As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpotElevTickMarkPen { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86a395f9-c085-a4c3-dd3e-23faa4e7cd3d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateGreaterRule Method (ElementId, Int32)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether integer values from the document are greater than a certain value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateGreaterRule( 	ElementId parameter, 	int value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateGreaterRule ( _ 	parameter As ElementId, _ 	value As Integer _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateGreaterRule( 	ElementId^ parameter,  	int value ) ``` |

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

[CreateGreaterRule Overload](3885f1a1-d26c-a3c3-54e1-81f75c04148a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86a590c3-9481-a823-e944-3bcc6f151328.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Size Property

---



|  |
| --- |
| [CitySet Class](9184332e-1167-a3c1-b2c1-58e9409817f3.htm)   [See Also](#seeAlsoToggle) |

Returns the number of cities that are in the set.

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

[CitySet Class](9184332e-1167-a3c1-b2c1-58e9409817f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86a7e751-11d3-6caa-e876-21ea31413d37.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElemPlateWidth Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Width"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SteelElemPlateWidth { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElemPlateWidth As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SteelElemPlateWidth { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86a8602c-c23f-0170-33b6-04a6e53a8d54.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetOptions Method

---



|  |
| --- |
| [ImporterIFC Class](87327a4b-94fd-5a21-df33-9beb1921cb4d.htm)   [See Also](#seeAlsoToggle) |

Gets the collection of named options set by the importer client.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IDictionary<string, string> GetOptions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetOptions As IDictionary(Of String, String) ``` |

 

| Visual C++ |
| --- |
| ``` public: IDictionary<String^, String^>^ GetOptions() ``` |

#### Return Value

The collection of named options.

# See Also

[ImporterIFC Class](87327a4b-94fd-5a21-df33-9beb1921cb4d.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__86aad3a2-7e1e-eecc-731e-1b31468698c0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Contains Method

---



|  |
| --- |
| [PlanCircuitSet Class](8398c79d-1108-6846-cc0c-b7b2b5c1d026.htm)   [See Also](#seeAlsoToggle) |

Tests for the existence of an item within the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool Contains( 	PlanCircuit item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Contains ( _ 	item As PlanCircuit _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Contains( 	PlanCircuit^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB PlanCircuit](9fdb77cb-c579-1cbd-71de-01f06a18ea3a.htm)    
     The item to be searched for.

#### Return Value

The Contains method returns True if the item is within the set, otherwise False.

# See Also

[PlanCircuitSet Class](8398c79d-1108-6846-cc0c-b7b2b5c1d026.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86ae6440-5226-bf7a-4ca2-100ef3e0d265.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RampDoesntReachOffset Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

The ramp is not long enough to reach the top constraint plus top offset. Change the slope or increase the length of the ramp.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RampDoesntReachOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RampDoesntReachOffset As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RampDoesntReachOffset { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86af03a8-6dc5-c6c5-2ee3-1478f7919574.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceNormal Property

---



|  |
| --- |
| [AdvancedGlazing Class](8f4007d6-eab7-39d3-69b6-18443f9350e5.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Image" from the "AdvancedGlazing" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static string SurfaceNormal { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SurfaceNormal As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ SurfaceNormal { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyReference" and will only contain a reference to a connected image.

# See Also

[AdvancedGlazing Class](8f4007d6-eab7-39d3-69b6-18443f9350e5.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__86b071b1-799e-053c-53c1-a591ea90c8fe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnyPatternIdParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Fill Pattern"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnyPatternIdParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnyPatternIdParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnyPatternIdParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86b16798-b04c-a064-1403-28aff4f23f64.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FramingShapeClassification Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Framing Shape"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FramingShapeClassification { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FramingShapeClassification As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FramingShapeClassification { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86b24b5b-ef47-65e4-8661-bbb62f26a96f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFillPattern Method

---



|  |
| --- |
| [FillPatternElement Class](64ecefd0-f5c4-5cd9-53bd-10a64739257e.htm)   [See Also](#seeAlsoToggle) |

Sets the FillPattern associated to this element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetFillPattern( 	FillPattern newFillPattern ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFillPattern ( _ 	newFillPattern As FillPattern _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFillPattern( 	FillPattern^ newFillPattern ) ``` |

#### Parameters

newFillPattern
:   Type:  [Autodesk.Revit.DB FillPattern](cc546ee9-ba80-c13d-4b74-8c0e2517bc28.htm)    
     The new FillPattern object.

# Remarks

The data stored inside the input FillPattern will be copied into this element. The input FillPattern itself will not be associated with the element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | newFillPattern does not have a valid Target. -or- newFillPattern does not have a valid Name. -or- newFillPattern is a solid fill pattern. -or- newFillPattern contains FillGrids with a zero Offset. -or- The name of the newFillPattern already exists. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The element is the build-in solid fill pattern element and can not be modified. |

# See Also

[FillPatternElement Class](64ecefd0-f5c4-5cd9-53bd-10a64739257e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86b33547-3f92-de80-21ff-21e3cb003e9b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Append Method

---



|  |
| --- |
| [DimensionSegmentArray Class](ea274891-53e6-efbe-6dec-fc2c32636ad2.htm)   [See Also](#seeAlsoToggle) |

Add the item to the end of the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual void Append( 	DimensionSegment item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Sub Append ( _ 	item As DimensionSegment _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Append( 	DimensionSegment^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB DimensionSegment](36b254a0-3dc5-7bdc-d6b4-986e5d82ddbf.htm)    
     The item to be added.

# See Also

[DimensionSegmentArray Class](ea274891-53e6-efbe-6dec-fc2c32636ad2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86b5dde3-bc13-d6d2-a1c8-6bdd79b79ad0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathReinTypen1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Primary Bar - Type"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PathReinTypen1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PathReinTypen1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PathReinTypen1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86bd03c3-b537-87d3-c46c-83d863f5f746.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsWallJoinedToTop Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Checks if wall is joined to top.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool IsWallJoinedToTop( 	Wall wall ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsWallJoinedToTop ( _ 	wall As Wall _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsWallJoinedToTop( 	Wall^ wall ) ``` |

#### Parameters

wall
:   Type:  [Autodesk.Revit.DB Wall](b5891733-c602-12df-beab-da414b58d608.htm)    
     The wall.

#### Return Value

True if wall is joined to top, false if not.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__86bf0125-c816-b2ac-32c1-966685159463.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetValueAsDoubles Method

---



|  |
| --- |
| [AssetPropertyDoubleArray4d Class](1fe933ae-e881-273a-fb8b-c4a7d9e66bc0.htm)   [See Also](#seeAlsoToggle) |

Sets the value of the property.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public void SetValueAsDoubles( 	IList<double> value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetValueAsDoubles ( _ 	value As IList(Of Double) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetValueAsDoubles( 	IList<double>^ value ) ``` |

#### Parameters

value
:   Type:  System.Collections.Generic IList   Double    
     The new value as doubles.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input value is invalid for this AssetPropertyDoubleArray4d property. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The asset property is not editable. |

# See Also

[AssetPropertyDoubleArray4d Class](1fe933ae-e881-273a-fb8b-c4a7d9e66bc0.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__86c163a1-4064-d171-de8d-7ab8ca5e8af5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateAnalysisDisplayStyle Method (Document, String, AnalysisDisplayVectorSettings, AnalysisDisplayColorSettings, AnalysisDisplayLegendSettings)

---



|  |
| --- |
| [AnalysisDisplayStyle Class](927357e1-9874-8b73-72c8-ff2bb78bfa82.htm)   [See Also](#seeAlsoToggle) |

Factory method - creates analysis display style object of type Vectors for the given document.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static AnalysisDisplayStyle CreateAnalysisDisplayStyle( 	Document document, 	string name, 	AnalysisDisplayVectorSettings vectorSettings, 	AnalysisDisplayColorSettings colorSettings, 	AnalysisDisplayLegendSettings legendSettings ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateAnalysisDisplayStyle ( _ 	document As Document, _ 	name As String, _ 	vectorSettings As AnalysisDisplayVectorSettings, _ 	colorSettings As AnalysisDisplayColorSettings, _ 	legendSettings As AnalysisDisplayLegendSettings _ ) As AnalysisDisplayStyle ``` |

 

| Visual C++ |
| --- |
| ``` public: static AnalysisDisplayStyle^ CreateAnalysisDisplayStyle( 	Document^ document,  	String^ name,  	AnalysisDisplayVectorSettings^ vectorSettings,  	AnalysisDisplayColorSettings^ colorSettings,  	AnalysisDisplayLegendSettings^ legendSettings ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document for which analysis display style object is created.

name
:   Type:  System String    
     Name of the analysis display style within the %document%.

vectorSettings
:   Type:  [Autodesk.Revit.DB.Analysis AnalysisDisplayVectorSettings](2e74462f-4216-f6eb-d560-87a1b103e87e.htm)    
     Vector settings for the style.

colorSettings
:   Type:  [Autodesk.Revit.DB.Analysis AnalysisDisplayColorSettings](936b709f-0cf4-c5ab-bfa9-2f4e340f4037.htm)    
     Color settings for the style.

legendSettings
:   Type:  [Autodesk.Revit.DB.Analysis AnalysisDisplayLegendSettings](a0362ecb-2442-6371-7e89-7a9ba66a0466.htm)    
     Legend settings for the style.

#### Return Value

New analysis display style object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | document is a family. -or- name is not unique in document. |

# See Also

[AnalysisDisplayStyle Class](927357e1-9874-8b73-72c8-ff2bb78bfa82.htm)

[CreateAnalysisDisplayStyle Overload](5b69a86f-b18e-e6d0-142a-2ed0343ccb89.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__86c60895-58d3-bd5a-ece2-b4222b1e3834.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CutLineAngle Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Cut Line Angle"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CutLineAngle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CutLineAngle As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CutLineAngle { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86c8a1b4-6ca6-5c1c-635f-f365b5ae9c3c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TotalConnectedCurrent Property

---



|  |
| --- |
| [AnalyticalPowerSourceData Class](844cf629-c023-47a8-55f1-b1d702780658.htm)   [See Also](#seeAlsoToggle) |

The total connected current of the analytical power source.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public double TotalConnectedCurrent { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property TotalConnectedCurrent As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double TotalConnectedCurrent { 	double get (); } ``` |

# See Also

[AnalyticalPowerSourceData Class](844cf629-c023-47a8-55f1-b1d702780658.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__86d288c5-5e53-f462-3098-1073cd425084.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsTopLevel Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top Level": The top level of stairs

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsTopLevel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsTopLevel As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsTopLevel { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86d6662a-fc5b-0027-2167-0f1f70efc923.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetExportFontTable Method

---



|  |
| --- |
| [BaseExportOptions Class](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)   [See Also](#seeAlsoToggle) |

Sets font table to option.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetExportFontTable( 	ExportFontTable fontTable ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetExportFontTable ( _ 	fontTable As ExportFontTable _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetExportFontTable( 	ExportFontTable^ fontTable ) ``` |

#### Parameters

fontTable
:   Type:  [Autodesk.Revit.DB ExportFontTable](b3b4f237-f7f3-ced4-be3d-721f7ac05832.htm)    
     The font table to be set.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[BaseExportOptions Class](d88aaa04-8700-ede2-9a8c-c3ac0d71e68b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86d85e09-e108-3ccd-b515-af3137d91f22.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetObjectData Method

---



|  |
| --- |
| [RegenerationFailedException Class](787bb389-74c2-5ce7-cdd6-32211209ded2.htm)   [See Also](#seeAlsoToggle) |

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

[RegenerationFailedException Class](787bb389-74c2-5ce7-cdd6-32211209ded2.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__86d92fdc-69d4-ce86-5222-8cc2a8073132.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CableTray Class

---



|  |
| --- |
| [Members](bcc7587e-b58e-e6cf-1816-e3acb12f9197.htm)   [See Also](#seeAlsoToggle) |

This class represents a cable tray in Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class CableTray : CableTrayConduitBase ``` |

 

| Visual Basic |
| --- |
| ``` Public Class CableTray _ 	Inherits CableTrayConduitBase ``` |

 

| Visual C++ |
| --- |
| ``` public ref class CableTray : public CableTrayConduitBase ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB HostObject](56a32e0b-df65-a6ba-40bd-8f50a1f31dcd.htm)    
  [Autodesk.Revit.DB MEPCurve](38714847-0f40-7021-aa79-2884c3a02ce2.htm)    
  [Autodesk.Revit.DB.Electrical CableTrayConduitBase](8a5c2986-28de-9e30-cb9f-c6997bff3940.htm)    
  Autodesk.Revit.DB.Electrical CableTray

# See Also

[CableTray Members](bcc7587e-b58e-e6cf-1816-e3acb12f9197.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__86d9d1ba-f873-d678-f5d0-48f37d8d0d76.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [ExportPatternTableIterator Class](1c08a52a-3648-fa5f-c4d2-d42177608496.htm)   [See Also](#seeAlsoToggle) |

Gets the item at the current position of the iterator.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual KeyValuePair<ExportPatternKey, ExportPatternInfo> Current { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property Current As KeyValuePair(Of ExportPatternKey, ExportPatternInfo) 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property KeyValuePair<ExportPatternKey^, ExportPatternInfo^> Current { 	KeyValuePair<ExportPatternKey^, ExportPatternInfo^> get (); } ``` |

#### Implements

 [IEnumerator T Current](http://msdn2.microsoft.com/en-us/library/58e146b7)

# Remarks

There is no current item if the iterator has not started yet or has been done.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | There is no current item in the iterator. |

# See Also

[ExportPatternTableIterator Class](1c08a52a-3648-fa5f-c4d2-d42177608496.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86d9fd32-9b45-d1df-d444-f4d71874e727.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VisibleByDefault Property

---



|  |
| --- |
| [DockablePaneProviderData Class](25c4224d-bc54-f2ed-589d-881a6ccbda87.htm)   [See Also](#seeAlsoToggle) |

Controls the default visibility of the pane upon the first time the pane/plugin is loaded into Revit.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public bool VisibleByDefault { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property VisibleByDefault As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool VisibleByDefault { 	bool get (); 	void set (bool value); } ``` |

# Remarks

By default, panes will be created and shown in the Revit UI when Revit is launched for the first time. Subsequent loads of the Revit UI will determine the visibility of the panes based upon there state at the close of the previous Revit session. Providers can set this to false if they wish there panes to NOT be shown by default.

# See Also

[DockablePaneProviderData Class](25c4224d-bc54-f2ed-589d-881a6ccbda87.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__86dd8bad-9ea7-1486-3882-803a7f2b6a93.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ZoneLevelId Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Level"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ZoneLevelId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ZoneLevelId As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ZoneLevelId { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86ddd37f-36ef-b63e-559c-ae9a916e89ae.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WorksharingDisplay Property

---



|  |
| --- |
| [TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.htm)   [See Also](#seeAlsoToggle) |

The current state of the WorksharingDisplay mode in the associated view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public WorksharingDisplayMode WorksharingDisplay { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property WorksharingDisplay As WorksharingDisplayMode 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property WorksharingDisplayMode WorksharingDisplay { 	WorksharingDisplayMode get (); 	void set (WorksharingDisplayMode value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The WorksharingDisplay mode is either disabled or inapplicable in the associated view. |

# See Also

[TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86e30f63-4894-aed9-c6df-0074cdfa89a7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetParameters Method

---



|  |
| --- |
| [FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)   [See Also](#seeAlsoToggle) |

Gets the parameters associated to family types in order.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IList<FamilyParameter> GetParameters() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetParameters As IList(Of FamilyParameter) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<FamilyParameter^>^ GetParameters() ``` |

#### Return Value

A collection containing all family parameters.

# Remarks

The parameters are family built-in parameters, category built-in parameters and shared parameters associated to the family types.

The collection consists of both visible and invisible parameters associated to the family types.

The parameters are returned in the order in which they appear in the Revit UI within a given group; however, parameters of different groups may be mixed within this output.

Currently the Revit UI order is determined first by group and next by the order of the individual parameters.

# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86e34e2f-3348-3d5c-1a6b-2ea485a1890e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CategorySet Class

---



|  |
| --- |
| [Members](6fb36745-7e17-9e61-faeb-7b734f2998b7.htm)   [See Also](#seeAlsoToggle) |

A set that can contains Category objects.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class CategorySet : APIObject,  	IEnumerable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class CategorySet _ 	Inherits APIObject _ 	Implements IEnumerable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class CategorySet : public APIObject,  	IEnumerable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB CategorySet

# See Also

[CategorySet Members](6fb36745-7e17-9e61-faeb-7b734f2998b7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86eac3b9-d2af-68c8-bdba-f8e8c8d79624.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddBarGeometry Method (CurveLoop)

---



|  |
| --- |
| [RebarCurvesData Class](71996f44-c8f9-7695-ccb9-efae09726c9c.htm)   [See Also](#seeAlsoToggle) |

Adds a new bar to the new rebar geometry. This information is set to the rebar after the API execution is finished successfully.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public RebarFreeFormValidationResult AddBarGeometry( 	CurveLoop curves ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddBarGeometry ( _ 	curves As CurveLoop _ ) As RebarFreeFormValidationResult ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarFreeFormValidationResult AddBarGeometry( 	CurveLoop^ curves ) ``` |

#### Parameters

curves
:   Type:  [Autodesk.Revit.DB CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     Curves describing one bar in the set.

#### Return Value

Returns Success if everything is ok, otherwise the failure reason.

# Remarks

This function can fail due to following reasons:

* CurveLoop is empty.
* CurveLoop contains an unbounded curve.
* A rebar constructed from curves can't be bent according to the bending radius.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Incorrect number of bar geometry for the current layout. |

# See Also

[RebarCurvesData Class](71996f44-c8f9-7695-ccb9-efae09726c9c.htm)

[AddBarGeometry Overload](8c068768-a57c-28fe-80a4-7f22346e46a8.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__86ed7231-000a-3717-86f2-ac1faa69bbfe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBodyRowHeights Method

---



|  |
| --- |
| [ScheduleHeightsOnSheet Class](1af9b0b7-3949-6478-aea8-7e3d04bec24b.htm)   [See Also](#seeAlsoToggle) |

Returns each row's height of schedule body on sheet view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022.1

# Syntax

| C# |
| --- |
| ``` public IList<double> GetBodyRowHeights() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBodyRowHeights As IList(Of Double) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<double>^ GetBodyRowHeights() ``` |

#### Return Value

Each row's height of schedule body on sheet view.

# See Also

[ScheduleHeightsOnSheet Class](1af9b0b7-3949-6478-aea8-7e3d04bec24b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86ef798e-e6b6-941f-c554-b0472374641e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhyMaterialParamExpCoeff3 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Thermal expansion coefficient Z"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PhyMaterialParamExpCoeff3 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PhyMaterialParamExpCoeff3 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PhyMaterialParamExpCoeff3 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86f6c525-1504-f09f-52ab-e16a4da48131.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetGraphicOverrides Method (WorksetId, WorksharingDisplayGraphicSettings)

---



|  |
| --- |
| [WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)   [See Also](#seeAlsoToggle) |

Sets the graphic overrides assigned to elements in a particular user workset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void SetGraphicOverrides( 	WorksetId worksetId, 	WorksharingDisplayGraphicSettings overrides ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetGraphicOverrides ( _ 	worksetId As WorksetId, _ 	overrides As WorksharingDisplayGraphicSettings _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetGraphicOverrides( 	WorksetId^ worksetId,  	WorksharingDisplayGraphicSettings^ overrides ) ``` |

#### Parameters

worksetId
:   Type:  [Autodesk.Revit.DB WorksetId](8bece327-c269-8101-b4c2-38632f593fe6.htm)    
     The workset of interest, which must be a user workset.

overrides
:   Type:  [Autodesk.Revit.DB WorksharingDisplayGraphicSettings](994d2fb5-11cc-6756-155b-d496eedbe800.htm)    
     The desired graphic overrides for this workset.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | worksetId does not correspond to a user workset in the document containing this WorksharingDisplaySettings. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)

[SetGraphicOverrides Overload](d05a245b-367b-7c19-c1d1-857a736e299f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86f8bc8c-b1ec-5540-1941-eab965832488.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReferenceOtherViewUiToggle Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Reference Other View": This is used to determine whether reference other view is enable or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ReferenceOtherViewUiToggle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ReferenceOtherViewUiToggle As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ReferenceOtherViewUiToggle { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86fa0dd0-44f9-59de-4b09-2552124de108.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionCommonHeight Property

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
| ``` public static ForgeTypeId StructuralSectionCommonHeight { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralSectionCommonHeight As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralSectionCommonHeight { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__86fa33e2-d5d1-7b74-13db-7f0f2de389a6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [AreaBasedLoadType Class](2800f280-409f-083d-5b57-127a19344de9.htm)   [See Also](#seeAlsoToggle) |

Creates an area based load type.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public static AreaBasedLoadType Create( 	Document document, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	name As String _ ) As AreaBasedLoadType ``` |

 

| Visual C++ |
| --- |
| ``` public: static AreaBasedLoadType^ Create( 	Document^ document,  	String^ name ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to create the area based load type.

name
:   Type:  System String    
     The name of new area based load type. The actual name may be post-fixed if already exists.

#### Return Value

The newly created area based load type.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- name is an empty string or contains only whitespace. -or- name cannot include prohibited characters, such as "{, }, [, ], |, ;, less-than sign, greater-than sign, ?, `, ~". |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[AreaBasedLoadType Class](2800f280-409f-083d-5b57-127a19344de9.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__86fe2215-c5e3-3d40-031d-59b639048c5c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MepZoneHotwaterLoop Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Heating Hot Water Loop"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MepZoneHotwaterLoop { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MepZoneHotwaterLoop As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MepZoneHotwaterLoop { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87a1e1e2-ee81-1a73-19d7-895b1fa10158.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetCategoryHidden Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Sets if elements of the given category will be visible in this view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetCategoryHidden( 	ElementId categoryId, 	bool hide ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetCategoryHidden ( _ 	categoryId As ElementId, _ 	hide As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetCategoryHidden( 	ElementId^ categoryId,  	bool hide ) ``` |

#### Parameters

categoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ID of the category.

hide
:   Type:  System Boolean    
     True to make elements of this category invisible, false to make them visible.

# Remarks

This affects only if the category is set visible or invisible individually. Other Revit mechanisms may also affect the visibility of elements of this category, including:

* The category classes settings for model categories, annotation categories, import categories or analytical model categories.
* View filters.
* Elements hidden individually in the view.

Thus setting this value may not affect the actual visibility of elements of this category in the view.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | categoryId does not correspond to a Category. -or- Category cannot be hidden. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__87a6e8ff-bf0e-94f3-354f-bb498c335f23.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetValidCategoriesForMaterialTakeoff Method

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

Gets a list of categories that can be used for a material takeoff.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetValidCategoriesForMaterialTakeoff() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetValidCategoriesForMaterialTakeoff As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetValidCategoriesForMaterialTakeoff() ``` |

#### Return Value

The IDs of all valid categories.

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)