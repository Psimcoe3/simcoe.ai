

<!-- Start of combined_102files.md -->



<!-- Start of Syntax__000a344f-d68f-8718-c6e5-72edef5ce04c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForceVector3 Property

---



|  |
| --- |
| [AreaLoad Class](5dc205a9-cafd-911b-6a56-26f2e8bfcdc1.htm)   [See Also](#seeAlsoToggle) |

The force vector applied to the 3rd reference point of the area load, oriented according to OrientTo setting.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public XYZ ForceVector3 { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ForceVector3 As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ ForceVector3 { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

The default force unit is kN/m^2 for metric, and ksf for imperial. Use UnitUtils class methods to convert value from or to internal units.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[AreaLoad Class](5dc205a9-cafd-911b-6a56-26f2e8bfcdc1.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__000ea288-c477-86a8-57e0-764f2e359d5b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NPerMmSup2 Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol N/mmÂ², indicating unit Newtons per square millimeter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId NPerMmSup2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NPerMmSup2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ NPerMmSup2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00a3e500-c61a-4f6a-7a98-7340bef88f4c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ChangePanelType Method

---



|  |
| --- |
| [CurtainGrid Class](5e0d5b7c-aaa1-d299-6fb8-2faa65b1857a.htm)   [See Also](#seeAlsoToggle) |

Change the type of a curtain panel.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Element ChangePanelType( 	Element panel, 	ElementType newSymbol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ChangePanelType ( _ 	panel As Element, _ 	newSymbol As ElementType _ ) As Element ``` |

 

| Visual C++ |
| --- |
| ``` public: Element^ ChangePanelType( 	Element^ panel,  	ElementType^ newSymbol ) ``` |

#### Parameters

panel
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The panel to be changed, it can be a type of  [Panel](ad561307-a19c-9a8a-728d-5646e90b451b.htm)  or  [Wall](b5891733-c602-12df-beab-da414b58d608.htm)  .

newSymbol
:   Type:  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
     The new symbol, it may be of  [PanelType](3a8ad72e-5aa7-8fef-10ba-72041fe47346.htm)  or  [WallType](aa685433-b426-5e4f-bee1-e3487bb59518.htm)  when the panel is hosted in a curtain wall. The new symbol can only be of type  [PanelType](3a8ad72e-5aa7-8fef-10ba-72041fe47346.htm)  if the Panel is hosted in a curtain system.

#### Return Value

If operation succeeds, the modified panel element is returned.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the input symbol can't be used for the panel. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the type change failed. |

# See Also

[CurtainGrid Class](5e0d5b7c-aaa1-d299-6fb8-2faa65b1857a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00a6d114-9937-11c6-f872-d987157a0d41.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExtraCheckBoxText Property

---



|  |
| --- |
| [TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)   [See Also](#seeAlsoToggle) |

ExtraCheckBoxText is used to label the extra checkbox.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public string ExtraCheckBoxText { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExtraCheckBoxText As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ ExtraCheckBoxText { 	String^ get (); 	void set (String^ value); } ``` |

# Remarks

If ExtraCheckBoxText is set, a checkbox with the text will be shown. You can get the response of checkbox by checking the return value of the WasExtraCheckBoxChecked() method.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if the TaskDialog also has EnableMarqueeProgressBar set as the two cannot coincide in the same TaskDialog. |

# See Also

[TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__00aa768a-fca2-172f-e5d4-a4d787803983.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Material Property

---



|  |
| --- |
| [Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)   [See Also](#seeAlsoToggle) |

Retrieves or changes the material of the category.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Material Material { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Material As Material 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Material^ Material { 	Material^ get (); 	void set (Material^ value); } ``` |

#### Field Value

   a null reference (  Nothing  in Visual Basic)  if this category does not have a material.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: material cannot be set for annotation categories. |

# See Also

[Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00abe21f-ebd1-edd7-e05c-4f4515b3cbb7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TrussNotJoinedWebs Property

---



|  |
| --- |
| [BuiltInFailures TrussFailures Class](b56f365f-a6f9-3ed1-8e1a-ebac29099530.htm)   [See Also](#seeAlsoToggle) |

The current edits are causing some webs to disjoin. The truss layout family requires additional constraints to maintain these joins.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId TrussNotJoinedWebs { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TrussNotJoinedWebs As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ TrussNotJoinedWebs { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures TrussFailures Class](b56f365f-a6f9-3ed1-8e1a-ebac29099530.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00ad01bb-55ff-316c-ea47-2019ba2a62c7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [FormArrayIterator Class](41b46034-62c3-0082-667c-537c9ac3c7ab.htm)   [See Also](#seeAlsoToggle) |

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

[FormArrayIterator Class](41b46034-62c3-0082-667c-537c9ac3c7ab.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00af4985-b107-cb1a-8954-b4078a9347ad.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MeshTriangle Class

---



|  |
| --- |
| [Members](200b00e7-e570-266f-2cc1-ecd17d87d972.htm)   [See Also](#seeAlsoToggle) |

One triangle of a mesh.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class MeshTriangle ``` |

 

| Visual Basic |
| --- |
| ``` Public Class MeshTriangle ``` |

 

| Visual C++ |
| --- |
| ``` public ref class MeshTriangle ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB MeshTriangle

# See Also

[MeshTriangle Members](200b00e7-e570-266f-2cc1-ecd17d87d972.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00b45e82-3bd5-b592-66e9-36364628c59b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetEmissiveColor Method

---



|  |
| --- |
| [EffectInstance Class](45b7ef37-46b6-6cf4-2f42-c6f4055a170c.htm)   [See Also](#seeAlsoToggle) |

Sets the emissive color parameter of the effect instance.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetEmissiveColor( 	Color color ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetEmissiveColor ( _ 	color As Color _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetEmissiveColor( 	Color^ color ) ``` |

#### Parameters

color
:   Type:  [Autodesk.Revit.DB Color](3735f9b9-d477-09ea-25bd-67f34134595f.htm)    
     The emissive color value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[EffectInstance Class](45b7ef37-46b6-6cf4-2f42-c6f4055a170c.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__00b47708-0e6b-0bfa-2616-b4ae93c76e53.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [SATExportOptions Class](c0b21f2b-3405-bfc9-2e22-6ff3a6d55c41.htm)   [See Also](#seeAlsoToggle) |

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

[SATExportOptions Class](c0b21f2b-3405-bfc9-2e22-6ff3a6d55c41.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00b5948e-1cb6-4f3b-acc1-9f000e8cc40d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoofType Class

---



|  |
| --- |
| [Members](9e9c34ba-8f13-dcd7-9d21-ba9febf78fbe.htm)   [See Also](#seeAlsoToggle) |

Represents a specific type of roof.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class RoofType : HostObjAttributes ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RoofType _ 	Inherits HostObjAttributes ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RoofType : public HostObjAttributes ``` |

# Remarks

All roof type objects available in the project can be retrieved from the Document object via the RoofTypes property. Every Roof object has a RoofType property that returns a RoofType object representing the type. This same RoofType property can also be used to change the type of the roof by setting it to a different type.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  [Autodesk.Revit.DB HostObjAttributes](a3d349c5-d457-3b56-eec4-c2fa2757c860.htm)    
  Autodesk.Revit.DB RoofType

# See Also

[RoofType Members](9e9c34ba-8f13-dcd7-9d21-ba9febf78fbe.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00b7a1a8-0e12-d02e-7e25-4716baf6dcdc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### JoinType Property

---



|  |
| --- |
| [LocationCurve Class](9dd6eb99-f105-a05f-dc1b-dfde17b8768c.htm)   [See Also](#seeAlsoToggle) |

Get/change the type of the join at the specified end.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public JoinType this[ 	int end ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property JoinType ( _ 	end As Integer _ ) As JoinType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property JoinType JoinType[int end] { 	JoinType get (int end); 	void set (int end, JoinType value); } ``` |

#### Parameters

end
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The end of the location curve driver under question.

# Remarks

This property allows to get join type of wall and concrete beam and to set wall's join type. The new join type is expected to be different from the current one for this end.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The element is neither a wall nor a concrete beam when it tries to get the property. The element is not a wall when it tries to set the property. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | A failure occurred while attempting to set the new type. |

# See Also

[LocationCurve Class](9dd6eb99-f105-a05f-dc1b-dfde17b8768c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00be5894-fe86-6f54-3341-3159c7a88668.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ThermalGradientCoefficientForMoistureCapacity Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Thermal Gradient Coefficient for Moisture Capacity, in discipline Energy.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ThermalGradientCoefficientForMoistureCapacity { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ThermalGradientCoefficientForMoistureCapacity As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ThermalGradientCoefficientForMoistureCapacity { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00bf3073-468d-ab4a-15d4-01196f916437.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEmpty Property

---



|  |
| --- |
| [WireSet Class](44035985-f6a1-72de-ae57-ac08507c8bbb.htm)   [See Also](#seeAlsoToggle) |

Test to see if the set is empty.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
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

If the set is empty then True will be returned, otherwise False.

# See Also

[WireSet Class](44035985-f6a1-72de-ae57-ac08507c8bbb.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__00c06a85-1d38-586a-da53-f9df84288959.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [StructuralSectionsServiceData Class](5bb46529-85cf-18d8-d8ec-9b77c3b78f88.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [StructuralSectionsServiceData](5bb46529-85cf-18d8-d8ec-9b77c3b78f88.htm)

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

[StructuralSectionsServiceData Class](5bb46529-85cf-18d8-d8ec-9b77c3b78f88.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__00c577f1-66ad-2d08-b46a-9bc2b5b344d5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarInternalMultiplanarEndConnector Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"INTERNAL: Multiplanar End Connector"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarInternalMultiplanarEndConnector { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarInternalMultiplanarEndConnector As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarInternalMultiplanarEndConnector { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00cf51d8-dfcd-3bb3-91e8-91b49d0c4f0d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetReferenceCallouts Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Returns element ids of all reference callouts in the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> GetReferenceCallouts() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetReferenceCallouts As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ GetReferenceCallouts() ``` |

#### Return Value

Element ids of all reference callouts in the view.

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00d3f5e9-efac-9d5a-a9d4-2f1f51884106.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecApparentLoadPhase3 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Apparent Load Phase 3"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecApparentLoadPhase3 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecApparentLoadPhase3 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecApparentLoadPhase3 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00d518dd-e22c-a304-ed07-8a0cdadfe640.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PoundsMassPerPoundDegreeFahrenheit Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Pounds mass per pound degree Fahrenheit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PoundsMassPerPoundDegreeFahrenheit { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PoundsMassPerPoundDegreeFahrenheit As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PoundsMassPerPoundDegreeFahrenheit { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00d71deb-c805-5def-2205-87e20bd5de07.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetElementFilterFromRule Method (PerformanceAdviserRuleId, Document)

---



|  |
| --- |
| [PerformanceAdviser Class](f9b0b017-f98f-79a3-ce7b-b1c867bb22f2.htm)   [See Also](#seeAlsoToggle) |

Retrieves a filter to restrict elements to be checked.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementFilter GetElementFilterFromRule( 	PerformanceAdviserRuleId id, 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetElementFilterFromRule ( _ 	id As PerformanceAdviserRuleId, _ 	document As Document _ ) As ElementFilter ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementFilter^ GetElementFilterFromRule( 	PerformanceAdviserRuleId^ id,  	Document^ document ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.DB PerformanceAdviserRuleId](3cd02844-a37b-9a93-e926-7d7f32450839.htm)    
     The rule id to get information for.

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document for which performance problems are being checked.

#### Return Value

The filter to restrict elements to be checked.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PerformanceAdviser Class](f9b0b017-f98f-79a3-ce7b-b1c867bb22f2.htm)

[GetElementFilterFromRule Overload](c2c46d9e-2479-30a0-edb9-8881cbbed4b5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00d7aa1d-bd28-e354-d4b5-c2078722af6e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GeometryPositioning Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Geometric Position"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId GeometryPositioning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GeometryPositioning As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ GeometryPositioning { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00d82cae-806a-8145-5228-bb362c641790.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ValueAtPoint Class

---



|  |
| --- |
| [Members](bf423a60-fcaa-2e9e-b397-91c7e8a44134.htm)   [See Also](#seeAlsoToggle) |

Stores values at one domain point. Each value corresponds to a "measurement" for which this value was calculated.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class ValueAtPoint : ValueAtPointBase ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ValueAtPoint _ 	Inherits ValueAtPointBase ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ValueAtPoint : public ValueAtPointBase ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ValueAtPointBase](67c49547-b5b9-59ad-8106-65d90886a381.htm)    
  Autodesk.Revit.DB.Analysis ValueAtPoint

# See Also

[ValueAtPoint Members](bf423a60-fcaa-2e9e-b397-91c7e8a44134.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__00d90c4f-1946-1069-7887-f12899846481.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BaseEquipment Property

---



|  |
| --- |
| [MEPSystem Class](65946955-8638-fafb-2657-ef7cb7b2941b.htm)   [See Also](#seeAlsoToggle) |

The base panel or equipment of the system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyInstance BaseEquipment { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property BaseEquipment As FamilyInstance 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property FamilyInstance^ BaseEquipment { 	FamilyInstance^ get (); } ``` |

# See Also

[MEPSystem Class](65946955-8638-fafb-2657-ef7cb7b2941b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00e0175c-aa17-1f40-ac65-983d6cdff06c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Erase Method

---



|  |
| --- |
| [SpaceSet Class](ff608354-dee5-99f7-fca3-d8b20ff5733d.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual int Erase( 	Space item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Erase ( _ 	item As Space _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual int Erase( 	Space^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB.Mechanical Space](b2c8970e-e554-8d73-06db-b65712c8a2e5.htm)

# See Also

[SpaceSet Class](ff608354-dee5-99f7-fca3-d8b20ff5733d.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__00e10880-4a18-381a-44fb-51dd1ba226b8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TotalDepth Property

---



|  |
| --- |
| [StairsRunType Class](a76503c0-abd8-0043-883b-134149348542.htm)   [See Also](#seeAlsoToggle) |

The total depth of the stairs run, only available for monolithic stairs run.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double TotalDepth { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property TotalDepth As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double TotalDepth { 	double get (); } ``` |

# See Also

[StairsRunType Class](a76503c0-abd8-0043-883b-134149348542.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__00e4ff47-36d6-4183-57d0-6a1992dd9ffb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRuleDescription Method (Int32)

---



|  |
| --- |
| [PerformanceAdviser Class](f9b0b017-f98f-79a3-ce7b-b1c867bb22f2.htm)   [See Also](#seeAlsoToggle) |

Retrieves the description of the rule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public string GetRuleDescription( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRuleDescription ( _ 	index As Integer _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetRuleDescription( 	int index ) ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The rule index to get information for.

#### Return Value

The description of the rule.

# See Also

[PerformanceAdviser Class](f9b0b017-f98f-79a3-ce7b-b1c867bb22f2.htm)

[GetRuleDescription Overload](1be9f237-63fe-dcbc-adaa-8c08746e15dd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00e8a597-b351-cc16-e236-87095e84d6f6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Transformed Property

---



|  |
| --- |
| [Mesh Class](bf9cd59c-03c3-9e7f-1e2b-6aaf5c425b69.htm)   [See Also](#seeAlsoToggle) |

Transforms this mesh and returns the result.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Mesh this[ 	Transform transform ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Transformed ( _ 	transform As Transform _ ) As Mesh 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Mesh^ Transformed[Transform^ transform] { 	Mesh^ get (Transform^ transform); } ``` |

#### Parameters

transform
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     The transformation used to transform the profile.

#### Return Value

The transformed mesh.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the handle of the specified transformation is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[Mesh Class](bf9cd59c-03c3-9e7f-1e2b-6aaf5c425b69.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00e9b7aa-61b7-ba3a-74ff-d430630566b7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RuleString Property

---



|  |
| --- |
| [FilterStringRule Class](166d75f9-1088-3275-2219-867c1142d8da.htm)   [See Also](#seeAlsoToggle) |

The user-supplied string against which strings from a Revit document will be tested.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string RuleString { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RuleString As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ RuleString { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[FilterStringRule Class](166d75f9-1088-3275-2219-867c1142d8da.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00e9c3c2-c76c-3ae5-8fc9-ab28d0b66187.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Millivolts Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Millivolts.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Millivolts { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Millivolts As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Millivolts { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00ed4d55-4e93-ce8c-5e8a-de4e7d2b2578.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### General Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"General"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId General { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property General As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ General { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00eff26a-414c-e0f0-4849-c815a733d0af.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FailedUpdateCurveChain Property

---



|  |
| --- |
| [BuiltInFailures GeometryFailures Class](6c30543b-4a09-53d0-0867-a2c2c49a4e57.htm)   [See Also](#seeAlsoToggle) |

Failed to update curve chain.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FailedUpdateCurveChain { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FailedUpdateCurveChain As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FailedUpdateCurveChain { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GeometryFailures Class](6c30543b-4a09-53d0-0867-a2c2c49a4e57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00f1c51a-1cae-e6e3-de3c-aa0dc17ce560.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MepCondenserWaterLoop Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Condenser Water Loop"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MepCondenserWaterLoop { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MepCondenserWaterLoop As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MepCondenserWaterLoop { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00f3aeb4-8b39-c3ee-245d-2ddc1c478eb1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BadRailProfile Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

One or more Profile Loops are invalid, probably because of self-intersection.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId BadRailProfile { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BadRailProfile As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ BadRailProfile { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00fd4079-6456-0ad6-69e4-83c098c82414.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurtaingridBeltRatioV Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Belt Measurement"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CurtaingridBeltRatioV { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CurtaingridBeltRatioV As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CurtaingridBeltRatioV { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00fe25ae-0a9e-3c4f-7f9a-3793043497c7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Weight Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Weight, in discipline Structural.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Weight { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Weight As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Weight { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__00feb0be-205e-2c2d-abdf-939d3a672fb5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InfillNoSlopeGlazing Property

---



|  |
| --- |
| [BuiltInFailures InfillFailures Class](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.htm)   [See Also](#seeAlsoToggle) |

Could not change type due to highlighted infilling element. 'Sloped glazing' infills are not allowed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId InfillNoSlopeGlazing { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InfillNoSlopeGlazing As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ InfillNoSlopeGlazing { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures InfillFailures Class](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a088c19-0ec8-fc3c-b14a-25c87b110516.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BtuPerLb Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol BTU/lb, indicating unit British thermal units per pound.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BtuPerLb { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BtuPerLb As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BtuPerLb { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a0a3793-5fce-283d-4953-a137f5593db9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Represents the structural type of a family instance.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public enum StructuralType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration StructuralType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class StructuralType ``` |

# Members

| Member name | Description |
| --- | --- |
| NonStructural | Non-Structural |
| Beam | Structural Beam |
| Brace | Structural Brace |
| Column | Structural Column |
| Footing | Structural Footing |
| UnknownFraming | Unknown Framing |

# See Also

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__0a0dded2-d7d7-9d7e-424d-ffb09051a690.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetIssues Method

---



|  |
| --- |
| [MeshFromGeometryOperationResult Class](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm)   [See Also](#seeAlsoToggle) |

Returns the array of issues encountered while building a mesh.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IList<MeshFromGeometryOperationIssue> GetIssues() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetIssues As IList(Of MeshFromGeometryOperationIssue) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<MeshFromGeometryOperationIssue>^ GetIssues() ``` |

#### Return Value

Array of issues encountered while building a mesh.

# See Also

[MeshFromGeometryOperationResult Class](acca9a2a-6d1d-efd3-3838-218e2a94f52a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a0ebb47-03a3-5fdf-9978-437c8447f102.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetInstanceTransform Method

---



|  |
| --- |
| [ReferenceWithContext Class](fccc2688-a00f-9e3a-26bf-f6d04a58c56c.htm)   [See Also](#seeAlsoToggle) |

Gets the transform of the instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public Transform GetInstanceTransform() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetInstanceTransform As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform^ GetInstanceTransform() ``` |

#### Return Value

The transform of an instance when the reference is returned by FindReferencesWithContextByDirection(XYZ, XYZ, View3D) or ReferenceIntersector.Find(XYZ, XYZ).

# See Also

[ReferenceWithContext Class](fccc2688-a00f-9e3a-26bf-f6d04a58c56c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a0ecf34-db77-997c-c9e3-e631c53fac78.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRequesters Method

---



|  |
| --- |
| [WorksharingTooltipInfo Class](64e2bf53-2787-6cb7-ac29-b73777892ed3.htm)   [See Also](#seeAlsoToggle) |

The ordered list of unique user names of users who have outstanding editing requests for the specified element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<string> GetRequesters() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRequesters As IList(Of String) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<String^>^ GetRequesters() ``` |

#### Return Value

The ordered list of unique user names.

# Remarks

The list is ordered by who placed the earliest request. If the list is empty it means that nobody is currently requesting the specified element.

# See Also

[WorksharingTooltipInfo Class](64e2bf53-2787-6cb7-ac29-b73777892ed3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a0ef591-4f53-5e0c-ce7b-4867b85ac0bb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurrentUser Property

---



|  |
| --- |
| [CentralModelContentionException Class](ad511076-c435-23c1-5720-1205c4ed28b9.htm)   [See Also](#seeAlsoToggle) |

Retrieves current user name.

**Namespace:**   [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public string CurrentUser { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property CurrentUser As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ CurrentUser { 	String^ get (); } ``` |

# See Also

[CentralModelContentionException Class](ad511076-c435-23c1-5720-1205c4ed28b9.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__0a1509c6-70e7-dd42-935f-f7d48af3fc69.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionIshapeBoltSpacingTwoRows Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bolt Spacing Two Rows"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralSectionIshapeBoltSpacingTwoRows { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralSectionIshapeBoltSpacingTwoRows As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralSectionIshapeBoltSpacingTwoRows { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a17ad4e-4a52-a955-c1af-882e2123bf49.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DisplayedStartStation Property

---



|  |
| --- |
| [Alignment Class](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)   [See Also](#seeAlsoToggle) |

Specifies the station at which the alignment's display starts, in Revit internal model units (standard Imperial feet).

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public double DisplayedStartStation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property DisplayedStartStation As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double DisplayedStartStation { 	double get (); } ``` |

# Remarks

This station is within the alignment's geometric definition range (  [StartStation](e3cf3a39-2fd0-f651-3366-f71a15fb5615.htm)  ,  [EndStation](cbfe6749-6c31-dcd3-e111-15fb2c04f042.htm)  ).

# See Also

[Alignment Class](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)

<!-- Start of Syntax__0a185ddd-e618-7b5b-ba1d-6d659ae79d7d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasStructuralDeck Property

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Checks if the compound structure has a structural deck.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool HasStructuralDeck { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HasStructuralDeck As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool HasStructuralDeck { 	bool get (); } ``` |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a19b743-8512-da8b-006d-cd703987310d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewId Property

---



|  |
| --- |
| [CADLinkOptions Class](a5d5d78c-cc65-c7a5-0bc8-4413156a2114.htm)   [See Also](#seeAlsoToggle) |

The id of the view to use as the link's reference view, if the reference view has been deleted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public ElementId ViewId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ViewId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ViewId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[CADLinkOptions Class](a5d5d78c-cc65-c7a5-0bc8-4413156a2114.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a1bf574-4e96-369c-e76f-f46f50d7fa8b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ActualReturnAirflow Property

---



|  |
| --- |
| [Space Class](b2c8970e-e554-8d73-06db-b65712c8a2e5.htm)   [See Also](#seeAlsoToggle) |

Get the Actual Return Airflow of the Space.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public double ActualReturnAirflow { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ActualReturnAirflow As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ActualReturnAirflow { 	double get (); } ``` |

# Remarks

This property is used to get the Actual Return Airflow (Unit: CFM) of the Space.

# See Also

[Space Class](b2c8970e-e554-8d73-06db-b65712c8a2e5.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__0a1bf912-867b-9e65-f34a-0ebd8432a364.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CantileverLength Property

---



|  |
| --- |
| [StructuralSectionConcreteCross Class](e4ff1053-b04d-bd05-9cdd-f1dc33412bb2.htm)   [See Also](#seeAlsoToggle) |

Flange cantilever length.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public double CantileverLength { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CantileverLength As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double CantileverLength { 	double get (); 	void set (double value); } ``` |

# See Also

[StructuralSectionConcreteCross Class](e4ff1053-b04d-bd05-9cdd-f1dc33412bb2.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__0a1cd042-dfeb-5a5f-734e-0b91d6a9e8dc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetHookOffsetLength Method

---



|  |
| --- |
| [RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)   [See Also](#seeAlsoToggle) |

Identifies the hook offset length for a hook type

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public double GetHookOffsetLength( 	ElementId hookId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetHookOffsetLength ( _ 	hookId As ElementId _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetHookOffsetLength( 	ElementId^ hookId ) ``` |

#### Parameters

hookId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     id of the hook type

#### Return Value

The hook offset length for a hook type

# Remarks

If the AutoCalcHookLengths property is turned off, the default hook offset length will be returned

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | the rebar hook type id hookId is not valid -or- the hook specified by id hookId doesn't have valid offset length -or- The element hookId does not exist in the document containing this RebarBarType -or- the hook specified by id hookId doesn't have valid default offset length |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document containing this RebarBarType is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The element is a member of a loaded family. -or- The element is a member of a group type that is not being edited. -or- hookId is a member of a loaded family. -or- hookId is a member of a group type that is not being edited. |

# See Also

[RebarBarType Class](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__0a1fbe9f-4945-3950-21ec-403d18a5668b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [ParameterSetIterator Class](389eba07-4d2d-a26f-0a61-aae5054a669a.htm)   [See Also](#seeAlsoToggle) |

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

[ParameterSetIterator Class](389eba07-4d2d-a26f-0a61-aae5054a669a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a204b72-b358-c603-109a-76a212571a63.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ClearCoverOther Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Rebar Cover - Other Faces"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ClearCoverOther { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ClearCoverOther As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ClearCoverOther { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a20cdd6-6e44-bc77-a4c3-2d35470ba911.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpatialElementTag Class

---



|  |
| --- |
| [Members](52d8b265-4527-674a-3101-1749a606e1ac.htm)   [See Also](#seeAlsoToggle) |

A tag attached to a SpatialElement (room, space or area) in Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public class SpatialElementTag : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class SpatialElementTag _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SpatialElementTag : public Element ``` |

# Remarks

SpatialElementTag is the base class for RoomTag, SpaceTag and AreaTag. Zone tag is not derived from SpatialElementTag. See  [IndependentTag](e52073e2-9d98-6fb5-eb43-288cf9ed2e28.htm)  for more information.

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB SpatialElementTag    
  [Autodesk.Revit.DB.Architecture RoomTag](3593ae3b-3046-4fd1-ced3-ce1368e3adb3.htm)    
  [Autodesk.Revit.DB AreaTag](8bbf0942-d7ce-02f0-8e07-aaa6e7aff169.htm)    
  [Autodesk.Revit.DB.Mechanical SpaceTag](ef54adf0-d922-e041-0e8c-34cff3ebdb8f.htm)

# See Also

[SpatialElementTag Members](52d8b265-4527-674a-3101-1749a606e1ac.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a227101-3cee-9f7f-87fb-f86757c22fc1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetRodLength Method

---



|  |
| --- |
| [FabricationRodInfo Class](b52fe314-2639-a697-cf97-b3e4824818f8.htm)   [See Also](#seeAlsoToggle) |

Set the rod length of the hanger for the specified rod index, excluding top extension. The hanger must not be set to be auto-hosted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool SetRodLength( 	int rodIndex, 	double newLength ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetRodLength ( _ 	rodIndex As Integer, _ 	newLength As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool SetRodLength( 	int rodIndex,  	double newLength ) ``` |

#### Parameters

rodIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The rod index.

newLength
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)

#### Return Value

returns true if it worked.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the index rodIndex is should be in range of rod count. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The rod length cannot be set because the hanger is set to automatically host to other elements. |

# See Also

[FabricationRodInfo Class](b52fe314-2639-a697-cf97-b3e4824818f8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a31d088-f05a-a306-3b8d-8a1a9ba9b764.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ContourLabelsRelativeBase Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Relative Base"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ContourLabelsRelativeBase { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ContourLabelsRelativeBase As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ContourLabelsRelativeBase { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a3484ab-9df4-6efc-cd16-23d23db4220c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCopyRevolveAxisWarn Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

The axis cannot be copied.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCopyRevolveAxisWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCopyRevolveAxisWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCopyRevolveAxisWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a36101d-7ce2-c7b5-7e94-ae2b824d10c4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDetailed Method

---



|  |
| --- |
| [StructuralConnectionHandlerType Class](e948a909-1b00-8789-6302-b46015c9cb47.htm)   [See Also](#seeAlsoToggle) |

Checks if StructuralConnectionHandlerType is detailed.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public bool IsDetailed() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsDetailed As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsDetailed() ``` |

#### Return Value

True if StructuralConnectionHandlerType is detailed.

# See Also

[StructuralConnectionHandlerType Class](e948a909-1b00-8789-6302-b46015c9cb47.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__0a36b1c4-f112-38f6-7b14-d572ea11584b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LocationPoint Class

---



|  |
| --- |
| [Members](e1071a1b-b98e-5875-2e13-b673e2b9fef6.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Provides location functionality for all elements that have a single insertion point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class LocationPoint : Location ``` |

 

| Visual Basic |
| --- |
| ``` Public Class LocationPoint _ 	Inherits Location ``` |

 

| Visual C++ |
| --- |
| ``` public ref class LocationPoint : public Location ``` |

# Remarks

The location point objects adds additional functionality to its base location object class. This includes setting the elements location to a specific point and retrieving its rotation around its insertion point. Inplace families do not have a single insertion point and therefore do not have meaningful LocationPoint data.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
void LocationInformation(LocationPoint position)
{
    String prompt = "The selected column location information:";
    prompt += "\nPoint:  (" + position.Point.X + ", "
            + position.Point.Y + ", " + position.Point.Z + ")";
    prompt += "\nRotation: " + position.Rotation;

    TaskDialog.Show("Revit",prompt);
}

bool LocationRotate(Autodesk.Revit.ApplicationServices.Application application, Autodesk.Revit.DB.Element element)
{
    bool rotated = false;
    LocationPoint location = element.Location as LocationPoint;

    if (null != location)
    {
        XYZ aa = location.Point;
        XYZ cc = new XYZ(aa.X, aa.Y, aa.Z + 10);
        Line axis = Line.CreateBound(aa,cc);
        rotated = location.Rotate(axis, Math.PI / 2.0);
    }

    return rotated;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub LocationInformation(position As LocationPoint)
    Dim prompt As [String] = "The selected column location information:"
    prompt += vbLf & "Point:  (" & Convert.ToString(position.Point.X) & ", " & Convert.ToString(position.Point.Y) & ", " & Convert.ToString(position.Point.Z) & ")"
    prompt += vbLf & "Rotation: " & Convert.ToString(position.Rotation)

    TaskDialog.Show("Revit", prompt)
End Sub

Private Function LocationRotate(application As Autodesk.Revit.ApplicationServices.Application, element As Autodesk.Revit.DB.Element) As Boolean
    Dim rotated As Boolean = False
    Dim location As LocationPoint = TryCast(element.Location, LocationPoint)

    If location IsNot Nothing Then
        Dim aa As XYZ = location.Point
        Dim cc As New XYZ(aa.X, aa.Y, aa.Z + 10)
        Dim axis As Line = Line.CreateBound(aa, cc)
        rotated = location.Rotate(axis, Math.PI / 2.0)
    End If

    Return rotated
End Function
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  [Autodesk.Revit.DB Location](3dbe57e5-fdea-5bf9-c715-52653f56073f.htm)    
  Autodesk.Revit.DB LocationPoint

# See Also

[LocationPoint Members](e1071a1b-b98e-5875-2e13-b673e2b9fef6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a370e32-eaba-785e-7e1f-9330929525fc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShape Class

---



|  |
| --- |
| [Members](f4ae417f-20df-e18e-79bd-6f31f835aa91.htm)   [See Also](#seeAlsoToggle) |

RebarShape specifies the shape type for a Rebar instance.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public class RebarShape : ElementType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RebarShape _ 	Inherits ElementType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RebarShape : public ElementType ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  Autodesk.Revit.DB.Structure RebarShape

# See Also

[RebarShape Members](f4ae417f-20df-e18e-79bd-6f31f835aa91.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__0a3a6e91-2521-e6b5-e614-741928b5e302.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCLink Property

---



|  |
| --- |
| [ExternalResourceTypes BuiltInExternalResourceTypes Class](3f1b13ff-0488-0a46-b646-21c2e29398e7.htm)   [See Also](#seeAlsoToggle) |

An external resource type representing IFC links.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public static ExternalResourceType IFCLink { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property IFCLink As ExternalResourceType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ExternalResourceType^ IFCLink { 	ExternalResourceType^ get (); } ``` |

# See Also

[ExternalResourceTypes BuiltInExternalResourceTypes Class](3f1b13ff-0488-0a46-b646-21c2e29398e7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a3d3bee-957a-45e0-3779-b1b924a0ce0f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewExported Event

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the ViewExported event to be notified immediately after Revit has finished exporting a view of the document.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public event EventHandler<ViewExportedEventArgs> ViewExported ``` |

 

| Visual Basic |
| --- |
| ``` Public Event ViewExported As EventHandler(Of ViewExportedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<ViewExportedEventArgs^>^ ViewExported { 	void add (EventHandler<ViewExportedEventArgs^>^ value); 	void remove (EventHandler<ViewExportedEventArgs^>^ value); } ``` |

# Remarks

This event is raised immediately after Revit has finished exporting a view of the document. It is raised only during accelerated export jobs, in which views are exported in parallel using a background process. Accelerated export only occurs when exporting to DWF formats and not combining views into a single file.

It is raised even when view exporting failed.

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Check the 'Status' field in event's argument to see whether the action was successful or not.

This event is not cancellable, for the process of view exporting has already been finished.

If the action was not successful, the document may not be modified and new transactions may not be started.

The following API functions are not available for the current document during this event:

* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__0a3f6fee-4ab4-ee50-9eb7-11837da1492b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LineWidth Property

---



|  |
| --- |
| [LineProperties Class](baddd6a0-35a8-c547-2566-ae7846799856.htm)   [See Also](#seeAlsoToggle) |

The current width (thickness) of the pen stroke when drawing lines/curves.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public double LineWidth { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property LineWidth As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double LineWidth { 	double get (); } ``` |

# See Also

[LineProperties Class](baddd6a0-35a8-c547-2566-ae7846799856.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a43e43f-fc15-d257-b159-dc76aedc2743.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDistributionPath Method

---



|  |
| --- |
| [RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)   [See Also](#seeAlsoToggle) |

The distribution path of a rebar set.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public Line GetDistributionPath() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDistributionPath As Line ``` |

 

| Visual C++ |
| --- |
| ``` public: Line^ GetDistributionPath() ``` |

#### Return Value

A line beginning at (0, 0, 0) and representing the direction and length of the set.

# See Also

[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__0a44918c-6c12-8a93-0cf2-6f764f369921.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurtainPanelNotBelongsToElement Property

---



|  |
| --- |
| [BuiltInFailures CurtainGridFamilyFailures Class](35e77e14-b020-50ef-133f-1c029c28429e.htm)   [See Also](#seeAlsoToggle) |

Curtain element Panel doesn't belong to Curtain element. In merging, you must select the version of a Curtain element that has had Panels added to it.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CurtainPanelNotBelongsToElement { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CurtainPanelNotBelongsToElement As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CurtainPanelNotBelongsToElement { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CurtainGridFamilyFailures Class](35e77e14-b020-50ef-133f-1c029c28429e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a486c45-b571-e8ce-e2a6-c2c95465acf4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FloorParamSpanDirection Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Span Direction"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FloorParamSpanDirection { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FloorParamSpanDirection As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FloorParamSpanDirection { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a4a49d3-d226-efb1-9eaf-1998f78b34c6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WireDiameter Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Wire Diameter, in discipline Electrical.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId WireDiameter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WireDiameter As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ WireDiameter { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a4aabb3-f684-0800-7bf5-31540831593f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RefersToExternalResourceReference Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Determines whether this Element uses external resources associated with a specified external resource type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool RefersToExternalResourceReference( 	ExternalResourceType resourceType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function RefersToExternalResourceReference ( _ 	resourceType As ExternalResourceType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool RefersToExternalResourceReference( 	ExternalResourceType^ resourceType ) ``` |

#### Parameters

resourceType
:   Type:  [Autodesk.Revit.DB ExternalResourceType](3fbd8c3c-1fa9-1f70-044e-b9e92f025a5e.htm)    
     The desired external resource type.

#### Return Value

Returns true if this Element uses external resources associated with the specified external resource type; otherwise, false.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a4ab95f-13d6-0789-ce75-2c28dd06a219.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PipingTemperature Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Temperature, in discipline Piping.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PipingTemperature { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PipingTemperature As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PipingTemperature { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a4ac474-2d59-3ab3-0ebd-7f04a8c20b72.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [ReinforcementAbbreviationTag Class](bf71dcbf-bb5b-07db-9711-e901b109b8e2.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
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

[ReinforcementAbbreviationTag Class](bf71dcbf-bb5b-07db-9711-e901b109b8e2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__0a538386-e10f-be9d-ba3b-c81093006256.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApparentLoad Property

---



|  |
| --- |
| [AreaBasedLoadData Class](10433e6e-e655-db35-54a9-cc8034cff631.htm)   [See Also](#seeAlsoToggle) |

The electrical apparent load of the area based load.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public double ApparentLoad { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ApparentLoad As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ApparentLoad { 	double get (); } ``` |

# See Also

[AreaBasedLoadData Class](10433e6e-e655-db35-54a9-cc8034cff631.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__0a54d7c6-4951-e153-faba-b46dadb5c5c1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddBendVariableRadius Method

---



|  |
| --- |
| [RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)   [See Also](#seeAlsoToggle) |

Specify a variable-radius bend.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void AddBendVariableRadius( 	int vertexIndex, 	RebarShapeVertexTurn turn, 	RebarShapeBendAngle angle, 	ElementId paramId, 	bool measureIncludingBarThickness ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddBendVariableRadius ( _ 	vertexIndex As Integer, _ 	turn As RebarShapeVertexTurn, _ 	angle As RebarShapeBendAngle, _ 	paramId As ElementId, _ 	measureIncludingBarThickness As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddBendVariableRadius( 	int vertexIndex,  	RebarShapeVertexTurn turn,  	RebarShapeBendAngle angle,  	ElementId^ paramId,  	bool measureIncludingBarThickness ) ``` |

#### Parameters

vertexIndex
:   Type:  System Int32    
     Index of the vertex (1 to NumberOfVertices - 2).

turn
:   Type:  [Autodesk.Revit.DB.Structure RebarShapeVertexTurn](a59971ec-c31f-a05e-e2d7-65882e23a21f.htm)    
     Specify turn direction (RebarShapeVertexTurn::Left or RebarShapeVertexTurn::Right).

angle
:   Type:  [Autodesk.Revit.DB.Structure RebarShapeBendAngle](176a9649-853e-f173-c108-d6722fcd5b61.htm)    
     Specify whether the bend is acute, obtuse, etc.

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of a parameter driving the radius.

measureIncludingBarThickness
:   Type:  System Boolean    
     If true, the radius is measured to the outside of the bend; if false, it is measured to the inside.

# Remarks

You must add a bend between each two segments.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | vertexIndex is not between 0 and NumberOfVertices. -or- paramId is not the id of a shared parameter in the current document, or its unit type is not UT\_Reinforcement\_Length or UT\_Angle. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__0a595a4e-97f1-9385-bafd-a0debe50f468.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [DesignToFabricationConverter Class](b2165e08-c8a4-5674-12ff-d359eba911d4.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [DesignToFabricationConverter](b2165e08-c8a4-5674-12ff-d359eba911d4.htm)

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

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

[DesignToFabricationConverter Class](b2165e08-c8a4-5674-12ff-d359eba911d4.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)

<!-- Start of Syntax__0a5aeba4-1900-a774-a9f3-7496696abe3e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPointLineZone Method (UV)

---



|  |
| --- |
| [FillGrid Class](6dfc3e2f-c869-d06e-876e-49c4007f7e59.htm)   [See Also](#seeAlsoToggle) |

Gets the index of fill grid line closest to the input 2d point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public int GetPointLineZone( 	UV point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPointLineZone ( _ 	point As UV _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int GetPointLineZone( 	UV^ point ) ``` |

#### Parameters

point
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     Input point.

#### Return Value

The index of fill grid line.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FillGrid Class](6dfc3e2f-c869-d06e-876e-49c4007f7e59.htm)

[GetPointLineZone Overload](3bbe339f-c7f0-a266-c698-2bb03e0f2e3e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a5baed4-452e-8416-0ad9-8c64744166c9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Contains Method

---



|  |
| --- |
| [ParameterSet Class](6e6e8667-ebe2-0c60-c180-9d8000cff598.htm)   [See Also](#seeAlsoToggle) |

Tests for the existence of a parameter within the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool Contains( 	Parameter item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Contains ( _ 	item As Parameter _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Contains( 	Parameter^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB Parameter](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)    
     The parameter to be searched for.

#### Return Value

The Contains method returns True if the parameter is within the set, otherwise False.

# See Also

[ParameterSet Class](6e6e8667-ebe2-0c60-c180-9d8000cff598.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a5c5449-f9f7-48d4-3e85-f96e1dd89f0a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [DocumentDifference Class](856189a3-0160-8609-8e6b-df23ea369e43.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [DocumentDifference](856189a3-0160-8609-8e6b-df23ea369e43.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

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

[DocumentDifference Class](856189a3-0160-8609-8e6b-df23ea369e43.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a5e9adf-e909-91c7-b307-9e4418e8732b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [TextNoteOptions Class](b0fd6ef8-a0ef-9cf4-5bc2-8cd65f81f648.htm)   [See Also](#seeAlsoToggle) |

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

[TextNoteOptions Class](b0fd6ef8-a0ef-9cf4-5bc2-8cd65f81f648.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a68f628-9ef8-8c2e-3075-e3730b35fbb9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsADirectContext3DHandleCategory Method

---



|  |
| --- |
| [DirectContext3DDocumentUtils Class](f30693d6-532f-6de8-25d9-6fd23337cb2e.htm)   [See Also](#seeAlsoToggle) |

Checks whether the provided category ID is one of the categories used by DirectContext3D handle elements.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static bool IsADirectContext3DHandleCategory( 	ElementId categoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsADirectContext3DHandleCategory ( _ 	categoryId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsADirectContext3DHandleCategory( 	ElementId^ categoryId ) ``` |

#### Parameters

categoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The category ID to check.

#### Return Value

True, if the category is valid for DirectContext3D handle elements, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectContext3DDocumentUtils Class](f30693d6-532f-6de8-25d9-6fd23337cb2e.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__0a69fdd3-8c45-d097-19c2-fb07a6a8f5cf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BentFabricBendDirection Property

---



|  |
| --- |
| [FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)   [See Also](#seeAlsoToggle) |

Specifies which wire direction of the fabric sheet is bent.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public BentFabricBendDirection BentFabricBendDirection { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BentFabricBendDirection As BentFabricBendDirection 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property BentFabricBendDirection BentFabricBendDirection { 	BentFabricBendDirection get (); 	void set (BentFabricBendDirection value); } ``` |

# Remarks

This parameter applies only to bent fabric sheets.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: the data-setting method is not applicable to fabric sheets that are flat |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidObjectException](8092dec2-113a-0823-1a09-a46c11f99fea.htm) | When setting this property: The data-setting method is not applicable to fabric sheets that are flat. |

# See Also

[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__0a6d155e-6ef1-7215-f8f1-c1d8203797ee.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpatialFieldManager Class

---



|  |
| --- |
| [Members](f9619c41-0e3a-0182-b130-8c73ac0aa546.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Exposes all API for an external analysis application. Its primary role is creation, deletion and modification of SpatialFieldElement elements.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class SpatialFieldManager : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class SpatialFieldManager _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SpatialFieldManager : public Element ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
Document doc = commandData.Application.ActiveUIDocument.Document;
UIDocument uiDoc = commandData.Application.ActiveUIDocument;

SpatialFieldManager sfm = SpatialFieldManager.GetSpatialFieldManager(doc.ActiveView);
if (null == sfm)
{
    sfm = SpatialFieldManager.CreateSpatialFieldManager(doc.ActiveView, 1);
}
Reference reference = uiDoc.Selection.PickObject(ObjectType.Face, "Select a face");
int idx = sfm.AddSpatialFieldPrimitive(reference);

Face face = doc.GetElement(reference).GetGeometryObjectFromReference(reference) as Face;

IList<UV> uvPts = new List<UV>();
BoundingBoxUV bb = face.GetBoundingBox();
UV min = bb.Min;
UV max = bb.Max;
uvPts.Add(new UV(min.U,min.V));
uvPts.Add(new UV(max.U,max.V));

FieldDomainPointsByUV pnts = new FieldDomainPointsByUV(uvPts);

List<double> doubleList = new List<double>();
IList<ValueAtPoint> valList = new List<ValueAtPoint>();
doubleList.Add(0);
valList.Add(new ValueAtPoint(doubleList));
doubleList.Clear();
doubleList.Add(10);
valList.Add(new ValueAtPoint(doubleList));

FieldValues vals = new FieldValues(valList);
AnalysisResultSchema resultSchema = new AnalysisResultSchema("Schema Name", "Description");
int schemaIndex = sfm.RegisterResult(resultSchema);
sfm.UpdateSpatialFieldPrimitive(idx, pnts, vals, schemaIndex);
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Dim doc As Document = commandData.Application.ActiveUIDocument.Document
Dim uiDoc As UIDocument = commandData.Application.ActiveUIDocument

Dim sfm As SpatialFieldManager = SpatialFieldManager.GetSpatialFieldManager(doc.ActiveView)
If sfm Is Nothing Then
    sfm = SpatialFieldManager.CreateSpatialFieldManager(doc.ActiveView, 1)
End If
Dim reference As Reference = uiDoc.Selection.PickObject(ObjectType.Face, "Select a face")
Dim idx As Integer = sfm.AddSpatialFieldPrimitive(reference)

Dim face As Face = TryCast(doc.GetElement(reference).GetGeometryObjectFromReference(reference), Face)

Dim uvPts As IList(Of UV) = New List(Of UV)()
Dim bb As BoundingBoxUV = face.GetBoundingBox()
Dim min As UV = bb.Min
Dim max As UV = bb.Max
uvPts.Add(New UV(min.U, min.V))
uvPts.Add(New UV(max.U, max.V))

Dim pnts As New FieldDomainPointsByUV(uvPts)

Dim doubleList As New List(Of Double)()
Dim valList As IList(Of ValueAtPoint) = New List(Of ValueAtPoint)()
doubleList.Add(0)
valList.Add(New ValueAtPoint(doubleList))
doubleList.Clear()
doubleList.Add(10)
valList.Add(New ValueAtPoint(doubleList))

Dim vals As New FieldValues(valList)
Dim resultSchema As New AnalysisResultSchema("Schema Name", "Description")
Dim schemaIndex As Integer = sfm.RegisterResult(resultSchema)
sfm.UpdateSpatialFieldPrimitive(idx, pnts, vals, schemaIndex)
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB.Analysis SpatialFieldManager

# See Also

[SpatialFieldManager Members](f9619c41-0e3a-0182-b130-8c73ac0aa546.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__0a713eab-1202-249e-cfb3-a9f7796be443.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetParameterFormula Method

---



|  |
| --- |
| [RebarShapeDefinition Class](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)   [See Also](#seeAlsoToggle) |

Return the parameter's formula, if one is associated with it.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public string GetParameterFormula( 	ElementId paramId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetParameterFormula ( _ 	paramId As ElementId _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetParameterFormula( 	ElementId^ paramId ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of a parameter in the definition.

#### Return Value

The formula, or an empty string if there is no formula for the parameter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This RebarShapeDefinition does not have a value for the parameter paramId. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarShapeDefinition Class](bb1f59be-c95e-a45b-8d2b-8121df179676.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__0a718766-52de-fe93-064a-d0369f5260f9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhyMaterialParamBending Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bending"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PhyMaterialParamBending { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PhyMaterialParamBending As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PhyMaterialParamBending { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a72e0ea-0523-bbc5-493b-771027a346aa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LiquidViscosity Property

---



|  |
| --- |
| [ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)   [See Also](#seeAlsoToggle) |

The liquid viscosity of the asset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double LiquidViscosity { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LiquidViscosity As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double LiquidViscosity { 	double get (); 	void set (double value); } ``` |

# Remarks

Values are in kilograms per feet-second (kg/(ft Â· s)) and must be non-negative.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for liquidViscosity must be non-negative. |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | When setting this property: the asset must be liquid to set this property. |

# See Also

[ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a793259-e84b-8695-d8f7-5d703e383168.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PoundsForcePerSquareFoot Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Pounds force per square foot.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PoundsForcePerSquareFoot { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PoundsForcePerSquareFoot As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PoundsForcePerSquareFoot { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a80d27c-a959-a712-6298-de5410502ed8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetConnections Method

---



|  |
| --- |
| [StairsLanding Class](cae109cd-bc50-6c36-300e-35d3457c0982.htm)   [See Also](#seeAlsoToggle) |

Returns information about the connections in which the stairs landing participates.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public IList<StairsComponentConnection> GetConnections() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetConnections As IList(Of StairsComponentConnection) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<StairsComponentConnection^>^ GetConnections() ``` |

#### Return Value

The connections in which the stairs landing participates.

# See Also

[StairsLanding Class](cae109cd-bc50-6c36-300e-35d3457c0982.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__0a848656-aa5e-e17e-5464-044a7d47f061.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [IFCFile Class](6f327830-5053-cf5d-c50e-2f5ab037b0b5.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [IFCFile](6f327830-5053-cf5d-c50e-2f5ab037b0b5.htm)

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

[IFCFile Class](6f327830-5053-cf5d-c50e-2f5ab037b0b5.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__0a89ca78-ca34-93fa-4fa7-71883a535497.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AppendSequence Method

---



|  |
| --- |
| [NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)   [See Also](#seeAlsoToggle) |

Appends all elements of one numbering sequence to the end of another sequence.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void AppendSequence( 	string fromPartition, 	string toPartition ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AppendSequence ( _ 	fromPartition As String, _ 	toPartition As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AppendSequence( 	String^ fromPartition,  	String^ toPartition ) ``` |

#### Parameters

fromPartition
:   Type:  System String    
     Name of the partition that determines which numbering sequence to append. The sequence must exist already, otherwise an exception will be thrown.

toPartition
:   Type:  System String    
     Name of a partition into which the source sequence is going to be appended. The sequence must exist already, otherwise an exception will be thrown.

# Remarks

All numbers assigned to elements in the target sequence remain the same, but numbers in the source sequence (the one getting appended) will change. Elements that match elements in the target sequence will get the same numbers assigned. Remaining elements will get consecutive numbers in the creation order of the elements starting with the next highest number available in the target sequence.

This operation modifies the Partition parameter of all elements in the sequence that is getting appended. Therefore, all its elements must be accessible for editing, otherwise this operation will fail.

Elements can be appended only to a sequence that already exists. In order to reassign elements of one sequence to a partition that does not exist yet, use either the  [MoveSequence](9ae38f60-e76f-5bd7-1d71-bd57cf06f641.htm)  or  MergeSequences  methods.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The sequence fromPartition does not exist in the schema. -or- The sequence toPartition does not exist in the schema. -or- Given partition names fromPartition and toPartition must be different. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Either the schema or its document cannot be modified at present. -or- Thrown if there is an element that cannot have new value of the NUMBER\_PARTITION\_PARAM parameter assigned. It may be an indication that the element is not free to be edited at present. |

# See Also

[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a8b7c58-406d-b801-5921-8b23568806be.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetViewRange Method

---



|  |
| --- |
| [ViewPlan Class](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)   [See Also](#seeAlsoToggle) |

Gets the view range.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public PlanViewRange GetViewRange() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetViewRange As PlanViewRange ``` |

 

| Visual C++ |
| --- |
| ``` public: PlanViewRange^ GetViewRange() ``` |

#### Return Value

The view range.

# See Also

[ViewPlan Class](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a8bfec9-c0a9-ddcf-2ac6-5af5d7d622c1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForwardIterator Method

---



|  |
| --- |
| [SlabShapeCreaseArray Class](dbb7004c-920c-74ce-bde2-834d46b0c132.htm)   [See Also](#seeAlsoToggle) |

Retrieve a forward moving iterator to the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual SlabShapeCreaseArrayIterator ForwardIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ForwardIterator As SlabShapeCreaseArrayIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual SlabShapeCreaseArrayIterator^ ForwardIterator() ``` |

#### Return Value

Returns a forward moving iterator to the array.

# See Also

[SlabShapeCreaseArray Class](dbb7004c-920c-74ce-bde2-834d46b0c132.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a8f3677-3320-a8a5-674e-b0d055ac6671.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpatialElementBoundarySubface Class

---



|  |
| --- |
| [Members](31b85cd6-c98d-f8e1-5c9d-d15a1330d6f6.htm)   [See Also](#seeAlsoToggle) |

SpatialElementBoundarySubface represents the geometry boundary information of spatial element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class SpatialElementBoundarySubface : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class SpatialElementBoundarySubface _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SpatialElementBoundarySubface : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB SpatialElementBoundarySubface

# See Also

[SpatialElementBoundarySubface Members](31b85cd6-c98d-f8e1-5c9d-d15a1330d6f6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a905433-bd87-58d5-903b-344c47ad2519.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewAreaBoundaryLine Method

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [See Also](#seeAlsoToggle) |

Creates a new boundary line as an Area border.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ModelCurve NewAreaBoundaryLine( 	SketchPlane sketchPlane, 	Curve geometryCurve, 	ViewPlan areaView ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewAreaBoundaryLine ( _ 	sketchPlane As SketchPlane, _ 	geometryCurve As Curve, _ 	areaView As ViewPlan _ ) As ModelCurve ``` |

 

| Visual C++ |
| --- |
| ``` public: ModelCurve^ NewAreaBoundaryLine( 	SketchPlane^ sketchPlane,  	Curve^ geometryCurve,  	ViewPlan^ areaView ) ``` |

#### Parameters

sketchPlane
:   Type:  [Autodesk.Revit.DB SketchPlane](ba104029-d175-7e75-caef-667a4281f4af.htm)    
     The sketch plane.

geometryCurve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The geometry curve on which the boundary line are

areaView
:   Type:  [Autodesk.Revit.DB ViewPlan](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)    
     The View for the new Area

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the sketch plane does not exist in the given document. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the area view does not exist in the given document. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__0a9379ea-9d8e-1380-e69b-a259c09608cc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetSourceElementIds Method

---



|  |
| --- |
| [PartMaker Class](ec5be0eb-bf10-0f05-83a4-77daa2cfb0fd.htm)   [See Also](#seeAlsoToggle) |

Set the source elements for the PartMaker.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetSourceElementIds( 	ICollection<ElementId> sourceElementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetSourceElementIds ( _ 	sourceElementIds As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetSourceElementIds( 	ICollection<ElementId^>^ sourceElementIds ) ``` |

#### Parameters

sourceElementIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Elements to be the sources for this PartMaker.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One or more element ids was not permitted to be a source for this PartMaker Elements should be Parts that have no PartMaker yet |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartMaker Class](ec5be0eb-bf10-0f05-83a4-77daa2cfb0fd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a94dad4-55d7-fa94-45df-022ce30b9805.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MustReplacePanels Property

---



|  |
| --- |
| [BuiltInFailures CurtainWallFailures Class](a3d691c9-5f8f-29ca-cfad-fa1d1d66f203.htm)   [See Also](#seeAlsoToggle) |

Missing Curtain Panels will be replaced with System Panels to complete command.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId MustReplacePanels { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MustReplacePanels As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ MustReplacePanels { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CurtainWallFailures Class](a3d691c9-5f8f-29ca-cfad-fa1d1d66f203.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a9cbf71-3df2-595e-5522-2e4e9b019fd0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RailPathCloseLoopForExtensionWarning Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

The rail path is closed at the start and end path point for extension creation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RailPathCloseLoopForExtensionWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RailPathCloseLoopForExtensionWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RailPathCloseLoopForExtensionWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0a9df754-4dc0-e5c0-b7f1-73bed8e4e192.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [BindingMap Class](4ce777fb-ab30-6d15-d019-5b430223ac62.htm)   [See Also](#seeAlsoToggle) |

This method is used to remove all the items in the map.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public override void Clear() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Sub Clear ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Clear() override ``` |

# Remarks

The method Clear inherited from base class is not permitted for this class. A Autodesk::Revit::Exceptions::InvalidOperationException will be thrown.

# See Also

[BindingMap Class](4ce777fb-ab30-6d15-d019-5b430223ac62.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0aa38eaf-be9c-3dd9-f0e4-621847cfcb63.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Orientation Property

---



|  |
| --- |
| [Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)   [See Also](#seeAlsoToggle) |

The normal vector projected from the exterior side of the wall.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ Orientation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Orientation As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Orientation { 	XYZ^ get (); } ``` |

# See Also

[Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0aa4039d-4d7d-fc7c-224e-b09a3b853980.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StartPercentage Property

---



|  |
| --- |
| [ViewDisplayDepthCueing Class](3acdcd08-f0f1-f23b-94a2-90d1f4ca0eaf.htm)   [See Also](#seeAlsoToggle) |

The start percentage defines where depth cueing starts. Values between 0 and 100.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public int StartPercentage { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property StartPercentage As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int StartPercentage { 	int get (); } ``` |

# See Also

[ViewDisplayDepthCueing Class](3acdcd08-f0f1-f23b-94a2-90d1f4ca0eaf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0aa90e49-871d-89e5-4af0-c20472df9729.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BaseEquipmentConnector Property

---



|  |
| --- |
| [MechanicalSystem Class](ef83dd58-07d6-4f9a-8dc6-f4b1fd8246d2.htm)   [See Also](#seeAlsoToggle) |

The connector within the base equipment which is used to connect with the system.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Connector BaseEquipmentConnector { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BaseEquipmentConnector As Connector 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Connector^ BaseEquipmentConnector { 	Connector^ get (); 	void set (Connector^ value); } ``` |

# Remarks

Assigning    a null reference (  Nothing  in Visual Basic)  to the base equipment connector will disconnect the base equipment from the system.

# Remarks

Setting this property will regenerate the document even in manual regeneration mode.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when assigning a connector which is used in a system, or when the connector's owner is not of type 'mechanical equipment'. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the set operation failed. |

# See Also

[MechanicalSystem Class](ef83dd58-07d6-4f9a-8dc6-f4b1fd8246d2.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__0aabc992-1723-9f78-aff7-ef9760f8a64b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetHookOrientation Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Returns the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public RebarHookOrientation GetHookOrientation( 	int iEnd ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetHookOrientation ( _ 	iEnd As Integer _ ) As RebarHookOrientation ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarHookOrientation GetHookOrientation( 	int iEnd ) ``` |

#### Parameters

iEnd
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     0 for the start hook, 1 for the end hook.

#### Return Value

Value = Right: The hook is on your right as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up." Value = Left: The hook is on your left as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up."

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | iEnd must be 0 or 1. |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__0ab1f8d7-489c-ac18-d262-be359377e523.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanFilterByGlobalParameters Method

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Checks whether a field can be used with a global parameter-based filter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public bool CanFilterByGlobalParameters( 	ScheduleFieldId fieldId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanFilterByGlobalParameters ( _ 	fieldId As ScheduleFieldId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanFilterByGlobalParameters( 	ScheduleFieldId^ fieldId ) ``` |

#### Parameters

fieldId
:   Type:  [Autodesk.Revit.DB ScheduleFieldId](e437cc01-b976-fe8a-225a-1a0024171fae.htm)    
     The ID of the field to check.

#### Return Value

True if the field can be used with a global parameter-based filter, false otherwise.

# Remarks

The global parameter-based filter types are IsAsociatedWith, IsNotAssociatedWith.

Only parameters which have a compatible type with at least one existing global parameter can be filtered.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | fieldId is not the ID of a field in this ScheduleDefinition. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0abe0739-691f-f229-6d5f-bea73b20a698.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLockCallback Method

---



|  |
| --- |
| [TransactWithCentralOptions Class](f5da22fa-55ee-9196-cafd-5323d8e9ca0a.htm)   [See Also](#seeAlsoToggle) |

Sets or resets a callback object that would allow an external application to change Revit's default behavior of endlessly waiting and repeatedly trying to lock a central model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetLockCallback( 	ICentralLockedCallback lockCallback ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLockCallback ( _ 	lockCallback As ICentralLockedCallback _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLockCallback( 	ICentralLockedCallback^ lockCallback ) ``` |

#### Parameters

lockCallback
:   Type:  [Autodesk.Revit.DB ICentralLockedCallback](ed94c7da-d506-5d51-d261-306c3a2a69a6.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TransactWithCentralOptions Class](f5da22fa-55ee-9196-cafd-5323d8e9ca0a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__0ac1f229-14e3-6039-22f1-1d6b40a000de.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AcceptableName Method

---



|  |
| --- |
| [SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)   [See Also](#seeAlsoToggle) |

Checks whether a string is an acceptable name for a Schema or a Field.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool AcceptableName( 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AcceptableName ( _ 	name As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool AcceptableName( 	String^ name ) ``` |

#### Parameters

name
:   Type:  System String    
     The string to check.

#### Return Value

True if the name is acceptable.

# Remarks

For interoperability, names are required to be usable as C++ identifiers. The allowable characters are ASCII letters, numbers (except the first character) and underscore. The length must be between 1 and 247 characters.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)

<!-- Start of Syntax__0ac40648-62a9-23ab-c95d-1883f5fb2ac3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasBinding Property

---



|  |
| --- |
| [RevitCommandId Class](0fb2f851-f469-f739-d6ee-89b40b25c4a2.htm)   [See Also](#seeAlsoToggle) |

Indicates whether a replacement of either the Execute or CanExecute events (or both) have been applied to this command.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool HasBinding { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HasBinding As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool HasBinding { 	bool get (); } ``` |

# Remarks

This will not indicate if one or more applications have subscribed to the BeforeExecuted event, as this event is not limited to a single subscriber.

# See Also

[RevitCommandId Class](0fb2f851-f469-f739-d6ee-89b40b25c4a2.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__0ac86739-54ac-ff78-dfc7-bd4dc7404b45.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsEnergyAnalysisProjectPhaseParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Project Phase"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsEnergyAnalysisProjectPhaseParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsEnergyAnalysisProjectPhaseParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsEnergyAnalysisProjectPhaseParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of combined_178files.md -->



<!-- Start of Syntax__01a64599-8558-c473-ea8f-fe7544138453.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetSolidInView Method

---



|  |
| --- |
| [RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)   [See Also](#seeAlsoToggle) |

Sets this RebarContainer element is shown as solid in the given 3D view.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` [ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit. The RebarContainer will always be shown solidly in 3D views with Fine level of detail. To change this, you can override the detail level of view for Structural Rebar category.")] public void SetSolidInView( 	View3D view, 	bool solid ) ``` |

 

| Visual Basic |
| --- |
| ``` <ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit. The RebarContainer will always be shown solidly in 3D views with Fine level of detail. To change this, you can override the detail level of view for Structural Rebar category.")> _ Public Sub SetSolidInView ( _ 	view As View3D, _ 	solid As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` [ObsoleteAttribute(L"This method is deprecated in Revit 2023 and may be removed in a later version of Revit. The RebarContainer will always be shown solidly in 3D views with Fine level of detail. To change this, you can override the detail level of view for Structural Rebar category.")] public: void SetSolidInView( 	View3D^ view,  	bool solid ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View3D](d795a238-fc24-1875-e64f-a2bef56ae949.htm)    
     The 3D view element

solid
:   Type:  System Boolean    
     True if this RebarContainer element is shown as solid in the given 3D view, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | This rebar container element doesn't have valid visibility data. |

# See Also

[RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__01a9de26-22cb-039c-2fa0-044ebbc900a0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EnergyAnalysisBuildingOperatingSchedule Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Building Operating Schedule"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId EnergyAnalysisBuildingOperatingSchedule { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property EnergyAnalysisBuildingOperatingSchedule As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ EnergyAnalysisBuildingOperatingSchedule { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01aa60d3-974f-b718-452e-a5e51b7d1b72.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CantMakeFillets Property

---



|  |
| --- |
| [BuiltInFailures RebarFailures Class](2d5565b1-8ddd-7e13-0eb1-8537eb342225.htm)   [See Also](#seeAlsoToggle) |

The bar cannot be bent in that shape. Check the bending diameter and the bar type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CantMakeFillets { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CantMakeFillets As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CantMakeFillets { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarFailures Class](2d5565b1-8ddd-7e13-0eb1-8537eb342225.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01abdb4e-e919-6d6e-94b9-8f66390e145c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpaceResolutionOutOfRange Property

---



|  |
| --- |
| [BuiltInFailures EnergyAnalysisFailures Class](8b9bfa39-1c9b-5cb0-14f1-0f49e2f8828a.htm)   [See Also](#seeAlsoToggle) |

Voxel size is out of range.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SpaceResolutionOutOfRange { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpaceResolutionOutOfRange As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SpaceResolutionOutOfRange { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures EnergyAnalysisFailures Class](8b9bfa39-1c9b-5cb0-14f1-0f49e2f8828a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01ace328-75ec-0fa9-d4a0-708136bbaaaa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallId Property

---



|  |
| --- |
| [WallFoundation Class](29a6e040-a36e-2a0c-5339-c69aa7776301.htm)   [See Also](#seeAlsoToggle) |

Returns the id of the host wall.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public ElementId WallId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property WallId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ WallId { 	ElementId^ get (); } ``` |

# See Also

[WallFoundation Class](29a6e040-a36e-2a0c-5339-c69aa7776301.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01b08561-f396-1475-6e90-05c2e9f41d48.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadTypeBase Class

---



|  |
| --- |
| [Members](ee5d78a9-d9bc-6336-0922-090b046ba908.htm)   [See Also](#seeAlsoToggle) |

An object that represents a Load type.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class LoadTypeBase : ElementType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class LoadTypeBase _ 	Inherits ElementType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class LoadTypeBase : public ElementType ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  Autodesk.Revit.DB.Structure LoadTypeBase    
  [Autodesk.Revit.DB.Structure AreaLoadType](eb4b548c-059a-d0d7-2431-8203c29dfebd.htm)    
  [Autodesk.Revit.DB.Structure LineLoadType](b9172085-e7bf-a23f-834c-7a5448ee39d4.htm)    
  [Autodesk.Revit.DB.Structure PointLoadType](c7b52498-80ca-1da6-bba4-d13744847e5d.htm)

# See Also

[LoadTypeBase Members](ee5d78a9-d9bc-6336-0922-090b046ba908.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__01b4cdc2-28af-d6e6-acfb-32cb1a86ffb5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecCircuitNumberOfElementsParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Number of Elements"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecCircuitNumberOfElementsParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecCircuitNumberOfElementsParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecCircuitNumberOfElementsParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01b7b190-a203-ea9f-c8a7-b114bb6baea8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CommonTintColor Property

---



|  |
| --- |
| [Ceramic Class](3f990d29-c743-ab3f-0a30-3b0a9b1f14cf.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Tint Color" from the "Ceramic" schema.

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

[Ceramic Class](3f990d29-c743-ab3f-0a30-3b0a9b1f14cf.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__01b8a908-533e-35f5-bc08-925af05cd218.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LbForceDashFtPerFt Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol lb-ft/ft, indicating unit Pound force feet per foot.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LbForceDashFtPerFt { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LbForceDashFtPerFt As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LbForceDashFtPerFt { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01c1c4b6-fc91-0651-3312-4d988073433a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Status Property

---



|  |
| --- |
| [RevitAPIPostEventArgs Class](93554f52-0145-3454-5697-3f1015e46434.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the action associated with this event succeeded, failed, or was cancelled (by an API event handler).

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public RevitAPIEventStatus Status { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Status As RevitAPIEventStatus 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property RevitAPIEventStatus Status { 	RevitAPIEventStatus get (); } ``` |

# See Also

[RevitAPIPostEventArgs Class](93554f52-0145-3454-5697-3f1015e46434.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__01c61fb6-104d-d594-0365-b493bb0165b5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetUnderlineStatus Method (Boolean)

---



|  |
| --- |
| [FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)   [See Also](#seeAlsoToggle) |

Sets the characters in the entire text to be underlined or not underlined.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetUnderlineStatus( 	bool isUnderlined ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetUnderlineStatus ( _ 	isUnderlined As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetUnderlineStatus( 	bool isUnderlined ) ``` |

#### Parameters

isUnderlined
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     The desired underline status of characters in the entire text. True to set underlined, false to set not underlined.

# See Also

[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)

[SetUnderlineStatus Overload](f40e89f5-a18e-16c4-0bad-4521d4cfaea2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01c64409-346b-5d8c-757c-28fde44938c4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Contains Method

---



|  |
| --- |
| [MacroManager Class](49eb4b8a-ae13-95e7-fef4-11347bbb67d3.htm)   [See Also](#seeAlsoToggle) |

Indicates the given module is a member of this collection.

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPIMacros  (in RevitAPIMacros.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool Contains( 	MacroModule module ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Contains ( _ 	module As MacroModule _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Contains( 	MacroModule^ module ) ``` |

#### Parameters

module
:   Type:  [Autodesk.Revit.DB.Macros MacroModule](d604a3cb-4f41-78a8-6353-270c566ac661.htm)    
     The module.

#### Return Value

Returns true if the given module is a member of this collection, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MacroManager Class](49eb4b8a-ae13-95e7-fef4-11347bbb67d3.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)

<!-- Start of Syntax__01c6bd32-cdd9-2407-311c-3e510493c7a2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PartMakerSplitterProfileFlipAlong Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Profile Along Flip"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PartMakerSplitterProfileFlipAlong { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PartMakerSplitterProfileFlipAlong As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PartMakerSplitterProfileFlipAlong { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01c7235f-cf9a-5d38-ed5f-c60b975643d8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMassDataElementIdForZoneFaceReference Method

---



|  |
| --- |
| [MassZone Class](da242463-3097-290a-9c10-afdf54d96649.htm)   [See Also](#seeAlsoToggle) |

MassZone faces come from faces of MassEnergyAnalyticalModel, and those faces have MassSurfaceData or MassLevelData elements associated with them.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementId GetMassDataElementIdForZoneFaceReference( 	Reference referenceOfZone ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMassDataElementIdForZoneFaceReference ( _ 	referenceOfZone As Reference _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetMassDataElementIdForZoneFaceReference( 	Reference^ referenceOfZone ) ``` |

#### Parameters

referenceOfZone
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     Reference to face of the MassZone to get data element for.

#### Return Value

Id of MassSurfaceData or MassLevelData element.

# Remarks

This element will contain the properties associated with the MassEnergyAnalyticalModel face or MassLevelData that the MassZone Face is derived from.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input Reference is not a face Reference of this MassZone. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MassZone Class](da242463-3097-290a-9c10-afdf54d96649.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__01cddc01-b348-3c51-d2ad-c61ac64c6da4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateRotation Method

---



|  |
| --- |
| [Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)   [See Also](#seeAlsoToggle) |

Creates a transform that represents a rotation about the given axis at (0, 0, 0).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static Transform CreateRotation( 	XYZ axis, 	double angle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateRotation ( _ 	axis As XYZ, _ 	angle As Double _ ) As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: static Transform^ CreateRotation( 	XYZ^ axis,  	double angle ) ``` |

#### Parameters

axis
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The rotation axis.

angle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The angle.

#### Return Value

The new transform.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for angle is not finite |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | axis has zero length. |

# See Also

[Transform Class](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01d600ff-427e-76a4-81b2-4b708acd40ff.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotPasteInViewError Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

Cannot paste the contents into %1!s! view. Attempt to paste into an appropriate view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotPasteInViewError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotPasteInViewError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotPasteInViewError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01e7c70f-9458-128f-b6bc-84acfd658dc5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Transform Method

---



|  |
| --- |
| [CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)   [See Also](#seeAlsoToggle) |

Transforms this curve loop and all of its component curves by the supplied transformation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void Transform( 	Transform transform ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Transform ( _ 	transform As Transform _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Transform( 	Transform^ transform ) ``` |

#### Parameters

transform
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     The transformation.

# Remarks

The modified CurveLoop is guaranteed to be valid with all consituent curves contiguous (assuming that the curves were contiguous in the input curve loop).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | transform is not conformal. -or- transform has a scale that is negative or zero. |

# See Also

[CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01e960f6-9041-e2e7-9c9b-87fceee9a7b1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SecondaryHandrailLateralOffset Property

---



|  |
| --- |
| [RailingType Class](7e7551fe-1772-f2d3-a8b5-58d4bb42a34e.htm)   [See Also](#seeAlsoToggle) |

The lateral offset of the secondary handrail.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double SecondaryHandrailLateralOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property SecondaryHandrailLateralOffset As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double SecondaryHandrailLateralOffset { 	double get (); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The rail has no secondary hand rail. |

# See Also

[RailingType Class](7e7551fe-1772-f2d3-a8b5-58d4bb42a34e.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__01ed99e3-ee07-3c39-1fbc-5d2dc13f2ba9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RailingSystemTopRailTypesParam Property

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
| ``` public static ForgeTypeId RailingSystemTopRailTypesParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RailingSystemTopRailTypesParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RailingSystemTopRailTypesParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01ee11a5-bc7d-dc85-892d-66382052badf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsUpdaterRegistered Method (UpdaterId, Document)

---



|  |
| --- |
| [UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.htm)   [See Also](#seeAlsoToggle) |

Checks whether updater with the given id is registered in a document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool IsUpdaterRegistered( 	UpdaterId id, 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsUpdaterRegistered ( _ 	id As UpdaterId, _ 	document As Document _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsUpdaterRegistered( 	UpdaterId^ id,  	Document^ document ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.DB UpdaterId](16a9604f-51bd-ce34-f145-17ae06b7c1cf.htm)    
     Id of the updater being tested.

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document in which this updater is tested whether it's registered or not.

#### Return Value

Returns True if the updater is registered in the given document.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[UpdaterRegistry Class](4f24f516-5274-1420-f255-458c0af5d318.htm)

[IsUpdaterRegistered Overload](62e89fa9-b9e6-41ab-8cfd-9bc6d0b6b6a0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01f11dff-0195-b6fe-d617-2d475357017e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Description Property

---



|  |
| --- |
| [AnalysisResultSchema Class](90969170-ac45-68e6-2527-f6fba5b3f7ae.htm)   [See Also](#seeAlsoToggle) |

Description of analysis result in view

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public string Description { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Description As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Description { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[AnalysisResultSchema Class](90969170-ac45-68e6-2527-f6fba5b3f7ae.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__01fbf5d9-6fa7-6483-6a1c-5cf439f27dc7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SlabShapeVertices Property

---



|  |
| --- |
| [SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)   [See Also](#seeAlsoToggle) |

All of the vertices that can be edited.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public SlabShapeVertexArray SlabShapeVertices { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property SlabShapeVertices As SlabShapeVertexArray 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property SlabShapeVertexArray^ SlabShapeVertices { 	SlabShapeVertexArray^ get (); } ``` |

# See Also

[SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__01ffb388-9936-9186-90f2-ddc7facb9ff9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Density Property

---



|  |
| --- |
| [ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)   [See Also](#seeAlsoToggle) |

The density of the asset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double Density { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Density As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Density { 	double get (); 	void set (double value); } ``` |

# Remarks

Values are in kilograms per cubed feet (kg/ftÂ³) and must be non-negative.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for density must be non-negative. |

# See Also

[ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a0878c8-6662-eca6-0450-b67401f43736.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ZoneUseOutsideAirPerPersonParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Use Outside Air Per Person"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ZoneUseOutsideAirPerPersonParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ZoneUseOutsideAirPerPersonParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ZoneUseOutsideAirPerPersonParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a0a0d23-891b-bf92-6b2b-069704dea9be.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LineAndTextAttrSymbol Class

---



|  |
| --- |
| [Members](35fb06d9-cbc3-600b-67e4-0812f7a653de.htm)   [See Also](#seeAlsoToggle) |

An object that represents a dimension style.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class LineAndTextAttrSymbol : ElementType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class LineAndTextAttrSymbol _ 	Inherits ElementType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class LineAndTextAttrSymbol : public ElementType ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  Autodesk.Revit.DB LineAndTextAttrSymbol    
  [Autodesk.Revit.DB FilledRegionType](850ae173-379b-bfd6-7295-3950ccc229ca.htm)    
  [Autodesk.Revit.DB GridType](f53d7c74-a843-4bdb-b9d9-584b7abbf668.htm)    
  [Autodesk.Revit.DB LevelType](dea94d1d-f327-c5f3-3597-09774189cb9b.htm)    
  [Autodesk.Revit.DB TextElementType](84f0914f-b947-0d23-3d0e-aea92822c5f1.htm)

# See Also

[LineAndTextAttrSymbol Members](35fb06d9-cbc3-600b-67e4-0812f7a653de.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a0b276f-37f0-e800-e1a7-ecf4446c414f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BeforeExecuted Event

---



|  |
| --- |
| [AddInCommandBinding Class](a457ac93-b849-d962-8719-2b3910358b04.htm)   [See Also](#seeAlsoToggle) |

Occurs before the command associated with this AddInCommandBinding executes.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public event EventHandler<BeforeExecutedEventArgs> BeforeExecuted ``` |

 

| Visual Basic |
| --- |
| ``` Public Event BeforeExecuted As EventHandler(Of BeforeExecutedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<BeforeExecutedEventArgs^>^ BeforeExecuted { 	void add (EventHandler<BeforeExecutedEventArgs^>^ value); 	void remove (EventHandler<BeforeExecutedEventArgs^>^ value); } ``` |

# See Also

[AddInCommandBinding Class](a457ac93-b849-d962-8719-2b3910358b04.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__1a0bb277-6f31-b344-bbcc-e5593826ae54.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewFlexPipe Method (Connector, IList(XYZ), FlexPipeType)

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [See Also](#seeAlsoToggle) |

Adds a new flexible pipe into the document, using a connector, point array and pipe type.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FlexPipe NewFlexPipe( 	Connector connector, 	IList<XYZ> points, 	FlexPipeType pipeType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewFlexPipe ( _ 	connector As Connector, _ 	points As IList(Of XYZ), _ 	pipeType As FlexPipeType _ ) As FlexPipe ``` |

 

| Visual C++ |
| --- |
| ``` public: FlexPipe^ NewFlexPipe( 	Connector^ connector,  	IList<XYZ^>^ points,  	FlexPipeType^ pipeType ) ``` |

#### Parameters

connector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The connector to be connected to the flexible pipe, including the end points.

points
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The point array indicating the path of the flexible pipe.

pipeType
:   Type:  [Autodesk.Revit.DB.Plumbing FlexPipeType](89da057e-f826-1f1e-dd71-9df4ce7f38cf.htm)    
     The type of the flexible pipe.

#### Return Value

If creation was successful then a new flexible pipe is returned, otherwise an exception with failure information will be thrown.

# Remarks

If the connector is a fitting or equipment connector of the correct domain, and if the connector's direction matches the direction of the flexible pipe to be created, the connectors will be automatically connected. A transition fitting will be added at the connector(s) if necessary. If the connector's type, domain, does not match the one of the input connector, no connection will be established.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument connector or points is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the flexible pipe cannot be created or regenerate fails. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the flexible pipe type does not exist in the given document. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[NewFlexPipe Overload](f60f5fa9-8394-3b80-99e1-90fcb98fb154.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__1a11b798-70a9-60fc-a116-1fc10d6788ad.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ContinuousFootingBottomHeel Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bottom Heel Length"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ContinuousFootingBottomHeel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ContinuousFootingBottomHeel As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ContinuousFootingBottomHeel { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a14a55b-ae8c-4cca-de65-51e2a1d24c9c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ResolveFailures Method

---



|  |
| --- |
| [FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)   [See Also](#seeAlsoToggle) |

Resolves one or more failures using last set failure resolution type for each of the failures. If failure resolution type was not set for some of failures, default failure resolution type will be used.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void ResolveFailures( 	IList<FailureMessageAccessor> failures ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ResolveFailures ( _ 	failures As IList(Of FailureMessageAccessor) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ResolveFailures( 	IList<FailureMessageAccessor^>^ failures ) ``` |

#### Parameters

failures
:   Type:  System.Collections.Generic IList   [FailureMessageAccessor](753477d8-b720-97a0-26f5-439d49de418c.htm)    
     The accessors to the failures to be resolved.

# Remarks

After execution of the failure resolutions the failures will not be removed from the document automatically. To prevent failure from being delivered to the user, failures (pre)processor should return ProceedWithCommit. It will cause failures to be regenerated and failure resolution process to be restarted. If attempt to resolve failure was not successful, and the same failure is present on repetitive calls of the failures (pre)processor, the preprocessor code should take care to attempt a different resolution the next time the failure appears, to avoid an infinite loop.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Default resolution of one of the failures is not permitted or not applicable. -or- One of the failures was already attempted to resolve twice with that resolution type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailuresAccessor is inactive (is used outside of failures processing). -or- Resolution of failures is not permitted in the current state of the document. |

# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a1ca698-adf9-d982-b30b-5a5d1af6a7e0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AdditionalElementsRequired Property

---



|  |
| --- |
| [BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)   [See Also](#seeAlsoToggle) |

Grouping the selected elements requires that additional element(s) also be grouped. [Description] To satisfy the grouping requirement, these additional element(s) will be automatically added to the group as well.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId AdditionalElementsRequired { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AdditionalElementsRequired As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ AdditionalElementsRequired { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a22bfd6-bb08-c368-f981-d02151986b5c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Export2DIncludingAnnotationObjects Property

---



|  |
| --- |
| [CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)   [See Also](#seeAlsoToggle) |

This flag sets the exporter of 2D views to either include or exclude output of annotation objects when the model is being processed by the export context.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public bool Export2DIncludingAnnotationObjects { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Export2DIncludingAnnotationObjects As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool Export2DIncludingAnnotationObjects { 	bool get (); 	void set (bool value); } ``` |

# Remarks

A convenient way of determining whether an element category is annotation is using  [!:Autodesk::Revit::DB::Category::CategoryType]  .

# See Also

[CustomExporter Class](d2437433-9183-cbb1-1c67-dedd86db5b5a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a24ee05-1057-4638-0b15-1a0f0ef0c21d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFailureMessages Method (FailureSeverity)

---



|  |
| --- |
| [FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)   [See Also](#seeAlsoToggle) |

Provides access to the individual failure messages if a given severity currently posted in the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public IList<FailureMessageAccessor> GetFailureMessages( 	FailureSeverity severity ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFailureMessages ( _ 	severity As FailureSeverity _ ) As IList(Of FailureMessageAccessor) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<FailureMessageAccessor^>^ GetFailureMessages( 	FailureSeverity severity ) ``` |

#### Parameters

severity
:   Type:  [Autodesk.Revit.DB FailureSeverity](d0cdffe3-22c5-b764-8090-5104f044b000.htm)    
     The failure severity for which failure messages are requested. If the requested severity is None, an empty collection is returned.

#### Return Value

Accessors to the individual failure messages of a given severity posted in the document.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailuresAccessor is inactive (is used outside of failures processing). |

# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)

[GetFailureMessages Overload](1e53e7f7-fee4-1bf4-ec76-9d5e67274aad.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a28171e-8460-d849-4e7d-9a306a22cd6e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetExternalResourceReferenceExpanded Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Gets the collection of ExternalResourceReference associated with a specified external resource type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public IList<ExternalResourceReference> GetExternalResourceReferenceExpanded( 	ExternalResourceType resourceType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetExternalResourceReferenceExpanded ( _ 	resourceType As ExternalResourceType _ ) As IList(Of ExternalResourceReference) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ExternalResourceReference^>^ GetExternalResourceReferenceExpanded( 	ExternalResourceType^ resourceType ) ``` |

#### Parameters

resourceType
:   Type:  [Autodesk.Revit.DB ExternalResourceType](3fbd8c3c-1fa9-1f70-044e-b9e92f025a5e.htm)    
     The desired external resource type.

#### Return Value

The collection of the ExternalResourceReference associated with a specified external resource type.

# Remarks

Use this API for an element which has multiple external resource references under a specified type, e.g., AppearanceAssetElement. See also:  [!:Autodesk::Revit::DB::Element::getExternalResourceReference]  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This Element does not use a resource reference for the specified resource type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a291c40-65d6-cae1-a69c-e60ef026645a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SharedCoords Property

---



|  |
| --- |
| [ACADExportOptions Class](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)   [See Also](#seeAlsoToggle) |

True to use the shared coordinate system's origin, false to use the project origin. Default value is false.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool SharedCoords { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SharedCoords As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool SharedCoords { 	bool get (); 	void set (bool value); } ``` |

# See Also

[ACADExportOptions Class](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a2bec33-499d-2850-ba65-0e9b3bf70656.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DormerCutProblem Property

---



|  |
| --- |
| [BuiltInFailures CutFailures Class](6bec436a-fefb-b90c-454f-ce494f3b06c5.htm)   [See Also](#seeAlsoToggle) |

Dormer Opening Cut is not fully defined. Cut was not performed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DormerCutProblem { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DormerCutProblem As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DormerCutProblem { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CutFailures Class](6bec436a-fefb-b90c-454f-ce494f3b06c5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a3bc9f7-528e-0c50-e7e5-ed24890a3e6f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CorrectionFactorSet Constructor

---



|  |
| --- |
| [CorrectionFactorSet Class](2a56bd02-5b0a-4455-8193-6b6384d42835.htm)   [See Also](#seeAlsoToggle) |

Initializes a new instance of the  [CorrectionFactorSet](2a56bd02-5b0a-4455-8193-6b6384d42835.htm)  class

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public CorrectionFactorSet() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: CorrectionFactorSet() ``` |

# See Also

[CorrectionFactorSet Class](2a56bd02-5b0a-4455-8193-6b6384d42835.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__1a3bd77e-f671-8d1a-d9d5-dbf61389f240.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurrentUserAddinsLocation Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

The folder location for .addin files for the current user.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public string CurrentUserAddinsLocation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property CurrentUserAddinsLocation As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ CurrentUserAddinsLocation { 	String^ get (); } ``` |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__1a3e7b93-8d83-ad16-f9a4-6cefb3ea4fcf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [WorksetTable Class](9ffa5fc8-e6a5-17d6-590e-8ecbfd7b85fb.htm)   [See Also](#seeAlsoToggle) |

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

[WorksetTable Class](9ffa5fc8-e6a5-17d6-590e-8ecbfd7b85fb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a427b4b-7e21-2bc2-911f-2be09d61a0cb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FractionalInches Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Fractional inches.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FractionalInches { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FractionalInches As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FractionalInches { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a43c153-cbaf-f89b-d298-93c6ff7d0ae0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLineWeight Method

---



|  |
| --- |
| [Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)   [See Also](#seeAlsoToggle) |

Sets the line weight for the given graphics style type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetLineWeight( 	int lineWeight, 	GraphicsStyleType graphicsStyleType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLineWeight ( _ 	lineWeight As Integer, _ 	graphicsStyleType As GraphicsStyleType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLineWeight( 	int lineWeight,  	GraphicsStyleType graphicsStyleType ) ``` |

#### Parameters

lineWeight
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

graphicsStyleType
:   Type:  [Autodesk.Revit.DB GraphicsStyleType](60a5cce6-2cdc-dd63-e737-f584582ceeca.htm)    
     The type of graphics style.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the input argument-"lineWeight" or "graphicsStyleType"-is out of range. |

# See Also

[Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a44f5bf-0f28-e1f6-0085-e35bec49d5c6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectionInputPointInfo Class

---



|  |
| --- |
| [Members](fbe0dd8d-89d3-e0d1-f611-366e29034c40.htm)   [See Also](#seeAlsoToggle) |

An object that holds description information about a connection input point

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public class ConnectionInputPointInfo : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ConnectionInputPointInfo _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ConnectionInputPointInfo : IDisposable ``` |

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB.Structure ConnectionInputPointInfo

# See Also

[ConnectionInputPointInfo Members](fbe0dd8d-89d3-e0d1-f611-366e29034c40.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__1a494d8c-0734-ea7a-3a93-b603374dc32f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Inequality Operator

---



|  |
| --- |
| [ScheduleFieldId Class](e437cc01-b976-fe8a-225a-1a0024171fae.htm)   [See Also](#seeAlsoToggle) |

Determines whether two ScheduleFieldId are different.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static bool operator !=( 	ScheduleFieldId first, 	ScheduleFieldId second ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Operator <> ( _ 	first As ScheduleFieldId, _ 	second As ScheduleFieldId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool operator !=( 	ScheduleFieldId^ first,  	ScheduleFieldId^ second ) ``` |

#### Parameters

first
:   Type:  [Autodesk.Revit.DB ScheduleFieldId](e437cc01-b976-fe8a-225a-1a0024171fae.htm)    
     The first ScheduleFieldId.

second
:   Type:  [Autodesk.Revit.DB ScheduleFieldId](e437cc01-b976-fe8a-225a-1a0024171fae.htm)    
     The second ScheduleFieldId.

#### Return Value

True if the ScheduleFieldId are different, otherwise false.

# See Also

[ScheduleFieldId Class](e437cc01-b976-fe8a-225a-1a0024171fae.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a49f909-b046-97da-57b2-f22b44fa55aa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsRouteAnalysisEnabled Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Checks whether or not route analysis is enabled, and enable or disable it.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public bool IsRouteAnalysisEnabled { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsRouteAnalysisEnabled As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsRouteAnalysisEnabled { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The current product type is not ProductType.Revit and discipline controls are not enabled. |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__1a4a3b83-48a5-1b11-36df-5381ee769971.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsPipeSizeFormattedParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Size"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsPipeSizeFormattedParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsPipeSizeFormattedParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsPipeSizeFormattedParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a4b4bbb-060d-1f42-fbb2-ab85081f8e7f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCheckoutStatus Method (Document, ElementId)

---



|  |
| --- |
| [WorksharingUtils Class](ae7857a0-4e9b-f9c1-84c7-8b250af68068.htm)   [See Also](#seeAlsoToggle) |

Gets the ownership status of an element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static CheckoutStatus GetCheckoutStatus( 	Document document, 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetCheckoutStatus ( _ 	document As Document, _ 	elementId As ElementId _ ) As CheckoutStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: static CheckoutStatus GetCheckoutStatus( 	Document^ document,  	ElementId^ elementId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the element.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the element.

#### Return Value

A summary of whether the element is unowned, owned by the current user, or owned by another user.

# Remarks

This method returns a locally cached value which may not be up to date with the current state of the element in the central. Because of this, the return value is suitable for reporting to an interactive user (e.g. via a mechanism similar to Worksharing display mode), but cannot be considered a reliable indication of whether the element can be immediately edited by the application. Also, the return value may not be dependable in the middle of a local transaction. See the remarks on  [WorksharingUtils](ae7857a0-4e9b-f9c1-84c7-8b250af68068.htm)  for more details.

For performance reasons, the model is not validated to be workshared, and the element id is also not validated; the element will not be expanded.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[WorksharingUtils Class](ae7857a0-4e9b-f9c1-84c7-8b250af68068.htm)

[GetCheckoutStatus Overload](c0c14d7d-d3a3-eeb7-9e21-fbf84597e5fb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a4f77d8-811c-b5e8-ca73-9f7ba14c73d0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SlantedColumnTopExtension Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top Extension"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SlantedColumnTopExtension { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SlantedColumnTopExtension As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SlantedColumnTopExtension { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a510aef-63f6-4d32-c0ff-a8071f5e23b8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ClosedShell Property

---



|  |
| --- |
| [Room Class](75c9d2c7-a402-ea8b-9e7c-f8bc3510bbd5.htm)   [See Also](#seeAlsoToggle) |

Return the closedShell of the Room.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public GeometryElement ClosedShell { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ClosedShell As GeometryElement 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property GeometryElement^ ClosedShell { 	GeometryElement^ get (); } ``` |

# See Also

[Room Class](75c9d2c7-a402-ea8b-9e7c-f8bc3510bbd5.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__1a51df6e-9081-7616-eb5e-d6c29d74284d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PoundsMassPerCubicFoot Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Pounds mass per cubic foot.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PoundsMassPerCubicFoot { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PoundsMassPerCubicFoot As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PoundsMassPerCubicFoot { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a531067-c312-8532-4517-c5a0a3df75cb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalLinkReleaseRotationX Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"X Rotation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnalyticalLinkReleaseRotationX { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticalLinkReleaseRotationX As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnalyticalLinkReleaseRotationX { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a58fd7b-e423-87bf-5978-c5ca93ae8949.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetEntries Method

---



|  |
| --- |
| [KeyBasedTreeEntriesLoadContent Class](c612ce53-9774-8d74-28fc-5918c6491576.htm)   [See Also](#seeAlsoToggle) |

Gets a copy of KeyBasedTreeEntries object owned by this KeyBasedTreeEntriesLoadContent object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public KeyBasedTreeEntries GetEntries() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetEntries As KeyBasedTreeEntries ``` |

 

| Visual C++ |
| --- |
| ``` public: KeyBasedTreeEntries^ GetEntries() ``` |

#### Return Value

A copy of KeyBasedTreeEntries object owned by this KeyBasedTreeEntriesLoadContent object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The KeyBasedTreeEntries object owned by this KeyBasedTreeEntriesLoadContent object is not built yet. The information about this KeyBasedTreeEntries object is not available. |

# See Also

[KeyBasedTreeEntriesLoadContent Class](c612ce53-9774-8d74-28fc-5918c6491576.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a5ac6c8-8a2e-0772-652d-7584e465c1d5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShowGraphicalWarningElectricalDisconnects Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Whether or not to show the graphical warnings for Electrical disconnects.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool ShowGraphicalWarningElectricalDisconnects { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ShowGraphicalWarningElectricalDisconnects As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ShowGraphicalWarningElectricalDisconnects { 	bool get (); 	void set (bool value); } ``` |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__1a5cd3ae-ee5e-ee99-961a-89a0f4d59c3b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RotateConnectedTap Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Rotates a connected fabrication tap by the specified angles about the primary and secondary axis.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016 Subscription Release

# Syntax

| C# |
| --- |
| ``` public static void RotateConnectedTap( 	Document doc, 	FabricationPart tap, 	double primaryAxisRotateBy, 	double secondaryAxisRotateBy ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub RotateConnectedTap ( _ 	doc As Document, _ 	tap As FabricationPart, _ 	primaryAxisRotateBy As Double, _ 	secondaryAxisRotateBy As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void RotateConnectedTap( 	Document^ doc,  	FabricationPart^ tap,  	double primaryAxisRotateBy,  	double secondaryAxisRotateBy ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

tap
:   Type:  [Autodesk.Revit.DB FabricationPart](c9b86162-c105-696a-a919-49a7a7938cc4.htm)    
     The connected fabrication part tap to rotate.

primaryAxisRotateBy
:   Type:  System Double    
     The primary axis rotation angle in radians to rotate by.

secondaryAxisRotateBy
:   Type:  System Double    
     The secondary axis rotation angle in radians to rotate by.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Is not connected as a fabrication part tap. -or- tap cannot be rotated about the primary axis by the specified angle: primaryAxisRotateBy -or- tap cannot be rotated about the secondary axis by the specified angle: secondaryAxisRotateBy |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a5ce82b-7509-7045-dca8-558f1ec98cb2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaterialBelongTo Property

---



|  |
| --- |
| [GroundConductorSize Class](922e6d1c-9bde-70c5-774b-a04a941003c1.htm)   [See Also](#seeAlsoToggle) |

Get the material type which include this ground conductor size information.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public WireMaterialType MaterialBelongTo { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property MaterialBelongTo As WireMaterialType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property WireMaterialType^ MaterialBelongTo { 	WireMaterialType^ get (); } ``` |

# See Also

[GroundConductorSize Class](922e6d1c-9bde-70c5-774b-a04a941003c1.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__1a5e2d9b-4a85-b268-1c60-169bf8a187cb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GeomStepFailed Property

---



|  |
| --- |
| [BuiltInFailures RegenFailures Class](c7726de2-e4f0-8861-8115-0ef9de7935b1.htm)   [See Also](#seeAlsoToggle) |

Can't rebuild geometry.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId GeomStepFailed { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GeomStepFailed As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ GeomStepFailed { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RegenFailures Class](c7726de2-e4f0-8861-8115-0ef9de7935b1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a63ad2e-0958-eebf-c8bd-ef3cf4fdd5f1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [TessellatedFace Class](6b007c37-6c87-50c5-8cf3-c3c68aa130ae.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [TessellatedFace](6b007c37-6c87-50c5-8cf3-c3c68aa130ae.htm)

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

[TessellatedFace Class](6b007c37-6c87-50c5-8cf3-c3c68aa130ae.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a6f1360-fc61-d312-43aa-7d95ea5032d1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PatternId Property

---



|  |
| --- |
| [LineProperties Class](baddd6a0-35a8-c547-2566-ae7846799856.htm)   [See Also](#seeAlsoToggle) |

Id of the current Line pattern element used when drawing lines/curves.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public ElementId PatternId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property PatternId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ PatternId { 	ElementId^ get (); } ``` |

# See Also

[LineProperties Class](baddd6a0-35a8-c547-2566-ae7846799856.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a70967c-2d0b-c5a0-60e6-a7cd079f6d61.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhyMaterialParamExpCoeffn2 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Thermal Expansion Coefficient 2"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PhyMaterialParamExpCoeffn2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PhyMaterialParamExpCoeffn2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PhyMaterialParamExpCoeffn2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a7448dd-27de-79c5-f4d4-fa5dc8c7157a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DesignHVACLoadperArea Property

---



|  |
| --- |
| [Space Class](b2c8970e-e554-8d73-06db-b65712c8a2e5.htm)   [See Also](#seeAlsoToggle) |

Get or set the Design HVAC Load per Area of the Space.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double DesignHVACLoadperArea { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DesignHVACLoadperArea As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double DesignHVACLoadperArea { 	double get (); 	void set (double value); } ``` |

# Remarks

This property is used to get or set the Design HVAC Load per Area (Unit: W/ft2) of the Space.

# See Also

[Space Class](b2c8970e-e554-8d73-06db-b65712c8a2e5.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__1a79abbd-a072-2e11-1405-06252915fd9e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRemovedUsers Method

---



|  |
| --- |
| [WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)   [See Also](#seeAlsoToggle) |

Returns the set of users who have been explicitly removed from the settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ICollection<string> GetRemovedUsers() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRemovedUsers As ICollection(Of String) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<String^>^ GetRemovedUsers() ``` |

#### Return Value

Users who have been explicitly removed from the list.

# See Also

[WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a7a5434-600b-9921-1ba0-bab9d90061f0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCopyNoAttachedParentWarn Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

Attached Detail Group can't be copied without its Model Group

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCopyNoAttachedParentWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCopyNoAttachedParentWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCopyNoAttachedParentWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a7af0e5-a3ff-e906-9263-db38de011f1b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MultiReferenceAnnotationDimensionStyle Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Dimension Style"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MultiReferenceAnnotationDimensionStyle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MultiReferenceAnnotationDimensionStyle As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MultiReferenceAnnotationDimensionStyle { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a7b2093-a251-21ae-a225-1a456da5d73b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [IndexStream Class](9c300586-7f1f-41db-270b-797d6ad967d8.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [IndexStream](9c300586-7f1f-41db-270b-797d6ad967d8.htm)

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
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

[IndexStream Class](9c300586-7f1f-41db-270b-797d6ad967d8.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__1a7d76ec-3042-cb83-cb8f-8c521398c843.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ListNames Method

---



|  |
| --- |
| [ExportDGNSettings Class](3df10700-a305-dba7-fc4a-5afb5387256c.htm)   [See Also](#seeAlsoToggle) |

Returns a list of names of dgn export settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static IList<string> ListNames( 	Document aDoc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ListNames ( _ 	aDoc As Document _ ) As IList(Of String) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<String^>^ ListNames( 	Document^ aDoc ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     A Revit document to retrieve names from

#### Return Value

An array of strings representing names of predefined setups.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportDGNSettings Class](3df10700-a305-dba7-fc4a-5afb5387256c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a840a92-5e60-2b5c-003a-039ef8c26486.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OpaqueF0 Property

---



|  |
| --- |
| [AdvancedOpaque Class](e8a19a97-fc76-71ad-c713-f2a62415475f.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Specular reflectance" from the "AdvancedOpaque" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string OpaqueF0 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property OpaqueF0 As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ OpaqueF0 { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble". This property allows a connected asset.

# See Also

[AdvancedOpaque Class](e8a19a97-fc76-71ad-c713-f2a62415475f.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__1a855734-c230-30ee-8d74-33617eb7bc3f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddOverride Method (ElementId, Int32)

---



|  |
| --- |
| [RebarContainerParameterManager Class](a0e5db38-c482-7232-df45-b0cdbcebac7d.htm)   [See Also](#seeAlsoToggle) |

Adds an override for the given parameter as its value will be displayed for the Rebar Container element.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void AddOverride( 	ElementId paramId, 	int value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddOverride ( _ 	paramId As ElementId, _ 	value As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddOverride( 	ElementId^ paramId,  	int value ) ``` |

#### Parameters

paramId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the parameter

value
:   Type:  System Int32    
     The override value of the parameter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | paramId is not the id of a parameter in the current document, or its value type is not integer. -or- paramId is not a Rebar Container parameter |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarContainerParameterManager Class](a0e5db38-c482-7232-df45-b0cdbcebac7d.htm)

[AddOverride Overload](d64341c8-f3b8-f22b-a178-707fd3040127.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__1a8c7baa-0653-8d1b-06f4-c3bd4cd5953f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDistance Method

---



|  |
| --- |
| [Alignment Class](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)   [See Also](#seeAlsoToggle) |

Calculates the relative distance along the alignment between two stations based on their alignment distances according to Revit Internal Origin Coordinate Base. The distance may be positive or negative depending on the relative positions of the input stations on the alignment.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public double GetDistance( 	double fromStation, 	double toStation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDistance ( _ 	fromStation As Double, _ 	toStation As Double _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetDistance( 	double fromStation,  	double toStation ) ``` |

#### Parameters

fromStation
:   Type:  System Double    
     The displayed alignment station from which 2D length is to be calculated, in Revit internal model units (standard Imperial feet).

toStation
:   Type:  System Double    
     The displayed alignment station to which 2D length is to be calculated, in Revit internal model units (standard Imperial feet).

#### Return Value

Distance (positive or negative) along the alignment between two stations. The sign of the distance depends on the relative positions of the input stations on the alignment.

# See Also

[Alignment Class](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)

<!-- Start of Syntax__1a8dbc43-88f6-8087-1607-7b01d61f4560.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAllHandles Method

---



|  |
| --- |
| [RebarConstraintsManager Class](32fe1ec6-ddb3-feac-f18c-8683b054f639.htm)   [See Also](#seeAlsoToggle) |

Gets all RebarConstrainedHandles of this bar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public IList<RebarConstrainedHandle> GetAllHandles() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAllHandles As IList(Of RebarConstrainedHandle) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<RebarConstrainedHandle^>^ GetAllHandles() ``` |

#### Return Value

All RebarConstrainedHandle objects will be returned, regardless of whether there are constraints associated to them.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The RebarConstraintsManager does not manage a valid Rebar element. |

# See Also

[RebarConstraintsManager Class](32fe1ec6-ddb3-feac-f18c-8683b054f639.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__1a92dabe-8532-07af-377d-f894ce9993bd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SuccessToConvertLine Property

---



|  |
| --- |
| [BuiltInFailures GeometryFailures Class](6c30543b-4a09-53d0-0867-a2c2c49a4e57.htm)   [See Also](#seeAlsoToggle) |

Success to convert lines

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SuccessToConvertLine { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SuccessToConvertLine As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SuccessToConvertLine { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GeometryFailures Class](6c30543b-4a09-53d0-0867-a2c2c49a4e57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a9439b4-d23d-6d6d-6ff2-999ffc8952a9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Count Property

---



|  |
| --- |
| [ExportPatternTable Class](3e87bc0e-e04b-f76a-2b06-82e951b5aec2.htm)   [See Also](#seeAlsoToggle) |

Count of the items contained in the collection.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public int Count { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Count As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int Count { 	int get (); } ``` |

# See Also

[ExportPatternTable Class](3e87bc0e-e04b-f76a-2b06-82e951b5aec2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a9453cc-db8c-bbcf-dd6c-5380b809df09.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsUnobscuredInView Method

---



|  |
| --- |
| [RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)   [See Also](#seeAlsoToggle) |

Checks if this rebar container element is shown unobscured in a view.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool IsUnobscuredInView( 	View view ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsUnobscuredInView ( _ 	view As View _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsUnobscuredInView( 	View^ view ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view element

#### Return Value

True if rebar is shown unobscured, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | This rebar container element doesn't have valid visibility data. |

# See Also

[RebarContainer Class](61979a57-facc-d97a-7a35-ee04eed59156.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__1a969227-e826-316a-7cef-a0d2beb2b948.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanUseHookType Method

---



|  |
| --- |
| [RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)   [See Also](#seeAlsoToggle) |

Checks if the specified RebarHookType id is of a valid RebarHookType for the Rebar's RebarBarType

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool CanUseHookType( 	ElementId proposedHookId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanUseHookType ( _ 	proposedHookId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanUseHookType( 	ElementId^ proposedHookId ) ``` |

#### Parameters

proposedHookId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The Id of the RebarHookType

#### Return Value

Returns true if the id is of a valid RebarHookType for the Rebar element.

# Remarks

Also, checks that the Style of the Hook matches that of the Rebar's RebarShape

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__1a973af7-5f14-26b4-25e8-af69fc6f0901.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RuledFace Class

---



|  |
| --- |
| [Members](83f4ea16-e2b8-ba1f-94a7-81c87a99908e.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

A ruled face of a 3d solid or open shell.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public class RuledFace : Face ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RuledFace _ 	Inherits Face ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RuledFace : public Face ``` |

# Remarks

A ruled surface is created by sweeping a line between two profile curves or between a curve and a point (a point and a curve). For details on the parameterization, refer to the documentation for  [RuledSurface](9a33fec9-bbcd-f035-3194-cf36122b6cc6.htm)  .

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void GetRuledFaceInfo(Face face)
{
    RuledFace ruledFace = face as RuledFace;
    if (null != ruledFace)
    {
        Curve curve = ruledFace.get_Curve(0);
        XYZ point = ruledFace.get_Point(0);
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub GetRuledFaceInfo(face As Face)
    Dim ruledFace As RuledFace = TryCast(face, RuledFace)
    If ruledFace IsNot Nothing Then
        Dim curve As Curve = ruledFace.Curve(0)
        Dim point As XYZ = ruledFace.Point(0)
    End If
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
  [Autodesk.Revit.DB Face](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)    
  Autodesk.Revit.DB RuledFace

# See Also

[RuledFace Members](83f4ea16-e2b8-ba1f-94a7-81c87a99908e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a97e079-901e-56e0-252d-2b030d04e595.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ACAPreference Property

---



|  |
| --- |
| [ACADExportOptions Class](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)   [See Also](#seeAlsoToggle) |

The preferred way to generate geometry of ACA objects. Default value is ACAObjectPreference.Object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ACAObjectPreference ACAPreference { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ACAPreference As ACAObjectPreference 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ACAObjectPreference ACAPreference { 	ACAObjectPreference get (); 	void set (ACAObjectPreference value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ACADExportOptions Class](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1a9f4976-57aa-09bd-c844-5409f6b96545.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Profile1FlippedHor Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Profile Is Flipped"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Profile1FlippedHor { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Profile1FlippedHor As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Profile1FlippedHor { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1aa02476-e696-53aa-0627-d2e3373ca598.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CmSup2PerM Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol cmÂ²/m, indicating unit Square centimeters per meter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CmSup2PerM { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CmSup2PerM As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CmSup2PerM { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1aa0ce6b-68d1-6643-9491-4b9328cf53e0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UseHatchBackgroundColor Property

---



|  |
| --- |
| [ACADExportOptions Class](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)   [See Also](#seeAlsoToggle) |

Indicates if hatch background color will be used or not. default value is false.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool UseHatchBackgroundColor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property UseHatchBackgroundColor As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool UseHatchBackgroundColor { 	bool get (); 	void set (bool value); } ``` |

# See Also

[ACADExportOptions Class](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1aa202a8-bc28-bd00-e00b-3ea339d83ac1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProjectionLinePatternId Property

---



|  |
| --- |
| [OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)   [See Also](#seeAlsoToggle) |

Id of the projection surface line pattern.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ElementId ProjectionLinePatternId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ProjectionLinePatternId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ProjectionLinePatternId { 	ElementId^ get (); } ``` |

# See Also

[OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1aa22fcc-b6ce-4287-bb31-07a06dfb8e26.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpacingLengthVert Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Spacing"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpacingLengthVert { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpacingLengthVert As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpacingLengthVert { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1aa3160e-1ef5-273b-f480-f171f15fa555.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document)

---



|  |
| --- |
| [EndTreatmentType Class](107f2dd4-7a92-e67e-0b79-a1c8c87dbf35.htm)   [See Also](#seeAlsoToggle) |

Creates a new EndTreatmentType in a document.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static EndTreatmentType Create( 	Document doc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	doc As Document _ ) As EndTreatmentType ``` |

 

| Visual C++ |
| --- |
| ``` public: static EndTreatmentType^ Create( 	Document^ doc ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[EndTreatmentType Class](107f2dd4-7a92-e67e-0b79-a1c8c87dbf35.htm)

[Create Overload](bfa0b5ed-b4e3-dcba-67f9-7ea73bf408b2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__1aa44a28-c45d-d77b-ced8-3b5cd5e582f3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DockableFrameFocusChangedEventArgs Class

---



|  |
| --- |
| [Members](87df5245-6d2f-2e36-cd22-3215baa3ce18.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by the DockableFrameActivatedChanged event.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class DockableFrameFocusChangedEventArgs : RevitAPISingleEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DockableFrameFocusChangedEventArgs _ 	Inherits RevitAPISingleEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DockableFrameFocusChangedEventArgs : public RevitAPISingleEventArgs ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPISingleEventArgs](446fa3c6-4f35-47f4-e8c2-e5235c321836.htm)    
  Autodesk.Revit.UI.Events DockableFrameFocusChangedEventArgs

# See Also

[DockableFrameFocusChangedEventArgs Members](87df5245-6d2f-2e36-cd22-3215baa3ce18.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__1aa4db18-1cac-878e-506c-12a9aad40fa0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureRealWorldOffsetX Property

---



|  |
| --- |
| [Noise Class](71c2801a-771b-97ce-3ef4-4c4e0904c5ec.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Offset X" from the "Noise" schema.

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

[Noise Class](71c2801a-771b-97ce-3ef4-4c4e0904c5ec.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__1aa957da-e64f-1d7c-37c5-e90801091e0f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DegreeR Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol Â°R, indicating unit Rankine.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DegreeR { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DegreeR As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DegreeR { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1ab4fea6-0712-146f-5bde-3a7f491de1bd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StoryAboveDeleted Property

---



|  |
| --- |
| [BuiltInFailures LevelFailures Class](fda0bd98-2636-3483-fb7e-de406b1bd252.htm)   [See Also](#seeAlsoToggle) |

The level set as the Story Above for these levels is being deleted. This change will cause these levels to revert to the default Story Above.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId StoryAboveDeleted { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StoryAboveDeleted As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ StoryAboveDeleted { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures LevelFailures Class](fda0bd98-2636-3483-fb7e-de406b1bd252.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1ab56927-b127-3041-fc23-24740bf3e514.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceAreaPerUnitLength Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Surface Area per Unit Length, in discipline Structural.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SurfaceAreaPerUnitLength { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SurfaceAreaPerUnitLength As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SurfaceAreaPerUnitLength { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1ab6dbfe-4927-3cc9-79a6-946391fec593.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyCategoryPseudoParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Category"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FamilyCategoryPseudoParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FamilyCategoryPseudoParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FamilyCategoryPseudoParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1abba00e-5078-e3ef-8f29-a7ed7583a697.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AllModelTypeComments Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Type Comments"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AllModelTypeComments { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AllModelTypeComments As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AllModelTypeComments { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1abbb31d-1bff-4d17-6b1c-e67c2e5c6c6a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalMemberForceEndAllNonZero Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"All non 0 forces at end"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnalyticalMemberForceEndAllNonZero { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticalMemberForceEndAllNonZero As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnalyticalMemberForceEndAllNonZero { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1abd367a-a574-025b-28ae-997e6f6d7a4d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SweepBaseVertOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Vertical Profile Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SweepBaseVertOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SweepBaseVertOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SweepBaseVertOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1abdb114-4582-ffc5-0a0c-bf3a1b30f8c2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DefaultPathOfTravelCalculationGUID Property

---



|  |
| --- |
| [PathOfTravelCalculationServerIds Class](0f801901-9d39-e079-f12c-aa90fc0124d8.htm)   [See Also](#seeAlsoToggle) |

GUID to represent the default calculation server id.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public static Guid DefaultPathOfTravelCalculationGUID { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DefaultPathOfTravelCalculationGUID As Guid 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property Guid DefaultPathOfTravelCalculationGUID { 	Guid get (); } ``` |

# See Also

[PathOfTravelCalculationServerIds Class](0f801901-9d39-e079-f12c-aa90fc0124d8.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__1ac57ab3-92a9-392e-41f6-25c43dbd9e15.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CombinableElementArrayIterator Constructor

---



|  |
| --- |
| [CombinableElementArrayIterator Class](20ec8352-e767-2eff-609f-c71f19806631.htm)   [See Also](#seeAlsoToggle) |

For Internal Use Only.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public CombinableElementArrayIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: CombinableElementArrayIterator() ``` |

# Remarks

This constructor is exposed to enable support for COM interop only. This object should never be created by the developer.

# See Also

[CombinableElementArrayIterator Class](20ec8352-e767-2eff-609f-c71f19806631.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1ac62d1b-f9cd-39c4-cc04-1527c315e4a8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBasicIEnumerator Method

---



|  |
| --- |
| [ExportPatternTable Class](3e87bc0e-e04b-f76a-2b06-82e951b5aec2.htm)   [See Also](#seeAlsoToggle) |

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

[ExportPatternTable Class](3e87bc0e-e04b-f76a-2b06-82e951b5aec2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1ac8b262-9085-07e9-cef6-85377e8c70f3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetOpenUIViews Method

---



|  |
| --- |
| [UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)   [See Also](#seeAlsoToggle) |

Get a list of all open view windows in the Revit user interface.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IList<UIView> GetOpenUIViews() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetOpenUIViews As IList(Of UIView) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<UIView^>^ GetOpenUIViews() ``` |

# Remarks

A sheet view with an activated viewport will return the view associated with the activated viewport, not the sheet view.

# See Also

[UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__1acafee6-95e0-50dd-2e46-8951e9405311.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Language Property

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

The language used in the current session of Revit.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public LanguageType Language { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Language As LanguageType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property LanguageType Language { 	LanguageType get (); } ``` |

# Remarks

Use this property to determine the language used by Revit; this can allow your application to load the appropriate resources.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__1acb725b-4a86-160b-6fe9-acb84cb14ca7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadAreaForceFz2 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Fz 2"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LoadAreaForceFz2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoadAreaForceFz2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LoadAreaForceFz2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1acf54fa-2304-396b-8f4b-077cda826b6f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddFilter Method

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Adds a new filter at the end of the list.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void AddFilter( 	ScheduleFilter filter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddFilter ( _ 	filter As ScheduleFilter _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddFilter( 	ScheduleFilter^ filter ) ``` |

#### Parameters

filter
:   Type:  [Autodesk.Revit.DB ScheduleFilter](a5dfec9f-1efd-b507-d079-eabcbf5032f8.htm)    
     The filter to add.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public static void AddFilterToSchedule(ViewSchedule schedule, ElementId levelId)
{
    // Find level field
    ScheduleDefinition definition = schedule.Definition;

    ScheduleField levelField = FindField(schedule, BuiltInParameter.ROOM_LEVEL_ID);

    // Add filter
    using (Transaction t = new Transaction(schedule.Document, "Add filter"))
    {
        t.Start();

        // If field not present, add it
        if (levelField == null)
        {
            levelField = definition.AddField(ScheduleFieldType.Instance, new ElementId(BuiltInParameter.ROOM_LEVEL_ID));
        }

        // Set field to hidden
        levelField.IsHidden = true;
        ScheduleFilter filter = new ScheduleFilter(levelField.FieldId, ScheduleFilterType.Equal, levelId);
        definition.AddFilter(filter);

        t.Commit();
    }
}

/// <summary>
/// Finds an existing ScheduleField matching the given parameter
/// </summary>
/// <param name="schedule"></param>
/// <param name="paramEnum"></param>
/// <returns></returns>
public static ScheduleField FindField(ViewSchedule schedule, BuiltInParameter paramEnum)
{
    ScheduleDefinition definition = schedule.Definition;
    ScheduleField foundField = null;
    ElementId paramId = new ElementId(paramEnum);

    foreach (ScheduleFieldId fieldId in definition.GetFieldOrder())
    {
        foundField = definition.GetField(fieldId);
        if (foundField.ParameterId == paramId)
        {
            return foundField;
        }
    }

    return null;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Shared Sub AddFilterToSchedule(schedule As ViewSchedule, levelId As ElementId)
    ' Find level field
    Dim definition As ScheduleDefinition = schedule.Definition

    Dim levelField As ScheduleField = FindField(schedule, BuiltInParameter.ROOM_LEVEL_ID)

    ' Add filter
    Using t As New Transaction(schedule.Document, "Add filter")
        t.Start()

        ' If field not present, add it
        If levelField Is Nothing Then
            levelField = definition.AddField(ScheduleFieldType.Instance, New ElementId(BuiltInParameter.ROOM_LEVEL_ID))
        End If

        ' Set field to hidden
        levelField.IsHidden = True
        Dim filter As New ScheduleFilter(levelField.FieldId, ScheduleFilterType.Equal, levelId)
        definition.AddFilter(filter)

        t.Commit()
    End Using
End Sub

' <summary>
' Finds an existing ScheduleField matching the given parameter
' </summary>
' <param name="schedule"></param>
' <param name="paramEnum"></param>
' <returns></returns>
Public Shared Function FindField(schedule As ViewSchedule, paramEnum As BuiltInParameter) As ScheduleField
    Dim definition As ScheduleDefinition = schedule.Definition
    Dim foundField As ScheduleField = Nothing
    Dim paramId As New ElementId(paramEnum)

    For Each fieldId As ScheduleFieldId In definition.GetFieldOrder()
        foundField = definition.GetField(fieldId)
        If foundField.ParameterId = paramId Then
            Return foundField
        End If
    Next

    Return Nothing
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The field ID is not the ID of a field in this ScheduleDefinition. -or- The field and filter type cannot be used to filter this ScheduleDefinition. -or- The filter value is not valid for the field and filter type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This ScheduleDefinition does not support filters. -or- The resulting filter count would be greater than 8. |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1ad157f4-c5f6-e0ce-5636-1482b237bbe2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoveNext Method

---



|  |
| --- |
| [IntersectionResultArrayIterator Class](87690604-accc-59bb-3b4e-a70c1f40ec0c.htm)   [See Also](#seeAlsoToggle) |

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

[IntersectionResultArrayIterator Class](87690604-accc-59bb-3b4e-a70c1f40ec0c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1ad21401-acd6-a49b-f0f4-006e01aa813f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Item Property

---



|  |
| --- |
| [SlabShapeVertexArray Class](ce947cf3-a5a8-43d7-49c7-3a1961ad7407.htm)   [See Also](#seeAlsoToggle) |

Gets or sets an item at a specified index within the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual SlabShapeVertex this[ 	int index ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Property Item ( _ 	index As Integer _ ) As SlabShapeVertex 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property SlabShapeVertex^ Item[int index] { 	SlabShapeVertex^ get (int index); 	void set (int index, SlabShapeVertex^ value); } ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the item to be set or retrieved.

#### Return Value

Returns the object at the specified index.

# See Also

[SlabShapeVertexArray Class](ce947cf3-a5a8-43d7-49c7-3a1961ad7407.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1ad3e0c9-8ea6-49dc-62d4-40b67aad1f9b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GraphicDisplayOptionsModel Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Model Display"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId GraphicDisplayOptionsModel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GraphicDisplayOptionsModel As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ GraphicDisplayOptionsModel { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1ad55a62-8551-c892-e5a9-c700a8580a32.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Insert Method

---



|  |
| --- |
| [WireConduitTypeSet Class](08d0cc98-554e-7f81-cb7c-f827d925de7d.htm)   [See Also](#seeAlsoToggle) |

Insert the specified conduit type into the set.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool Insert( 	WireConduitType item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Insert ( _ 	item As WireConduitType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Insert( 	WireConduitType^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB.Electrical WireConduitType](3c17c9e5-7018-1cf6-4a20-d8059cec370c.htm)    
     The conduit type to be inserted into the set.

#### Return Value

Returns whether the conduit type was inserted into the set.

# See Also

[WireConduitTypeSet Class](08d0cc98-554e-7f81-cb7c-f827d925de7d.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__1ad95fb2-c693-47b3-e826-c726fd1a09b9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FillPatternTarget Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The type of the fill pattern.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public enum FillPatternTarget ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration FillPatternTarget ``` |

 

| Visual C++ |
| --- |
| ``` public enum class FillPatternTarget ``` |

# Members

| Member name | Description |
| --- | --- |
| Drafting | Represents a material in symbolic form. |
| Model | Represents an actual element appearance on a building. |
| None |  |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1ad9af61-0201-e6c6-86ec-37311996d7e0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CeramicBumpType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The enumerated type representing the permitted values for the asset property "CeramicBump" from the "Ceramic" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public enum CeramicBumpType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration CeramicBumpType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class CeramicBumpType ``` |

# Members

| Member name | Description |
| --- | --- |
| None |  |
| Wavy |  |
| Custom |  |

# See Also

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__1ade3356-8405-4d06-f004-79fc11026786.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EvaluateOnFace Method

---



|  |
| --- |
| [Edge Class](7155ef49-fcd9-c80a-6232-70189a617bcc.htm)   [See Also](#seeAlsoToggle) |

Evaluates a parameter on the edge to produce UV coordinates on the face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public UV EvaluateOnFace( 	double param, 	Face face ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function EvaluateOnFace ( _ 	param As Double, _ 	face As Face _ ) As UV ``` |

 

| Visual C++ |
| --- |
| ``` public: UV^ EvaluateOnFace( 	double param,  	Face^ face ) ``` |

#### Parameters

param
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The parameter to be evaluated, in [0,1].

face
:   Type:  [Autodesk.Revit.DB Face](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)    
     The face on which to perform the evaluation. Must belong to the edge.

# See Also

[Edge Class](7155ef49-fcd9-c80a-6232-70189a617bcc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1ae103ff-960e-a5e7-7a4f-c7c561ca5a3f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HostedSweepType Class

---



|  |
| --- |
| [Members](b9081e37-fd2e-f963-e7cc-381cbe667851.htm)   [See Also](#seeAlsoToggle) |

An object that represents the attributes for sweep host objects in Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class HostedSweepType : HostObjAttributes ``` |

 

| Visual Basic |
| --- |
| ``` Public Class HostedSweepType _ 	Inherits HostObjAttributes ``` |

 

| Visual C++ |
| --- |
| ``` public ref class HostedSweepType : public HostObjAttributes ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  [Autodesk.Revit.DB HostObjAttributes](a3d349c5-d457-3b56-eec4-c2fa2757c860.htm)    
  Autodesk.Revit.DB HostedSweepType    
  [Autodesk.Revit.DB.Architecture FasciaType](ed44fcab-1425-b04f-d4eb-16d948f00375.htm)    
  [Autodesk.Revit.DB.Architecture GutterType](572b736f-1533-b759-7a9e-55ed1ff2709b.htm)    
  [Autodesk.Revit.DB SlabEdgeType](0f6f73b4-26b9-044e-590c-ef65a1210db8.htm)

# See Also

[HostedSweepType Members](b9081e37-fd2e-f963-e7cc-381cbe667851.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1af90084-8c60-caf5-47f8-0756bdc83125.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EdgeHostedPointToBeUnhosted Property

---



|  |
| --- |
| [BuiltInFailures PointFailures Class](b1b1f464-16e5-fd74-9350-a0e4b0397b9b.htm)   [See Also](#seeAlsoToggle) |

A point element in a family was hosted on an edge outside its family and the edge no longer exists. The point will remain placed but with no host.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId EdgeHostedPointToBeUnhosted { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property EdgeHostedPointToBeUnhosted As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ EdgeHostedPointToBeUnhosted { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures PointFailures Class](b1b1f464-16e5-fd74-9350-a0e4b0397b9b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1af9b0b7-3949-6478-aea8-7e3d04bec24b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleHeightsOnSheet Class

---



|  |
| --- |
| [Members](46431bc3-0afa-406d-df0b-a608c3b6c9f7.htm)   [See Also](#seeAlsoToggle) |

Heights information of a schedule on sheet.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022.1

# Syntax

| C# |
| --- |
| ``` public class ScheduleHeightsOnSheet : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ScheduleHeightsOnSheet _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ScheduleHeightsOnSheet : IDisposable ``` |

# Remarks

This class returns the heights of schedule title, column header and each body row on sheet view.

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB ScheduleHeightsOnSheet

# See Also

[ScheduleHeightsOnSheet Members](46431bc3-0afa-406d-df0b-a608c3b6c9f7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1affa01f-14eb-d62e-28a4-b7e91dfb096e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LbMassPerLbDegreeF Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol lb/(lbÂ·Â°F), indicating unit Pounds mass per pound degree Fahrenheit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LbMassPerLbDegreeF { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LbMassPerLbDegreeF As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LbMassPerLbDegreeF { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1affa941-d61f-a554-e457-43cc819becd0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DimStyleDimLineSnapDist Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Dimension Line Snap Distance"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DimStyleDimLineSnapDist { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DimStyleDimLineSnapDist As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DimStyleDimLineSnapDist { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b044c80-e60b-3495-2960-5c14a172097d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NotBentSharedFamily Property

---



|  |
| --- |
| [BuiltInFailures BendFailures Class](0c504e8d-3d3b-0f84-e5e1-a6e47fdcf232.htm)   [See Also](#seeAlsoToggle) |

While making curved beam type "[Type Name]" Shared Family Instances were not created

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NotBentSharedFamily { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NotBentSharedFamily As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NotBentSharedFamily { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures BendFailures Class](0c504e8d-3d3b-0f84-e5e1-a6e47fdcf232.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b05e7b9-25c3-ae4b-79de-72373c408248.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LayoutRuleFixedDistance Constructor

---



|  |
| --- |
| [LayoutRuleFixedDistance Class](a2910330-3b62-58d3-0f1a-e322ec4fb32c.htm)   [See Also](#seeAlsoToggle) |

Constructor of LayoutRuleFixedDistance. Create LayoutRuleFixedDistance with the values passed in.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public LayoutRuleFixedDistance( 	double spacing, 	BeamSystemJustifyType justifyType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	spacing As Double, _ 	justifyType As BeamSystemJustifyType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: LayoutRuleFixedDistance( 	double spacing,  	BeamSystemJustifyType justifyType ) ``` |

#### Parameters

spacing
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The value of spacing must be between 0 and 30000.

justifyType
:   Type:  [Autodesk.Revit.DB BeamSystemJustifyType](2ab9e284-9fd9-eaac-ae59-c550fdcce372.htm)    
     The type of the justification, it's corresponding to the items in the element properties dialog.

# See Also

[LayoutRuleFixedDistance Class](a2910330-3b62-58d3-0f1a-e322ec4fb32c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b07da0b-f7cf-95e1-a7b2-585b72177edd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [EdgeArrayArray Class](7f25fe6f-a427-7ac3-6753-2dec37fb058c.htm)   [See Also](#seeAlsoToggle) |

Removes every edge array from the array, rendering it empty.

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

[EdgeArrayArray Class](7f25fe6f-a427-7ac3-6753-2dec37fb058c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b0bcd96-994a-1ddd-2584-112cfc13aaa6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Insert Method

---



|  |
| --- |
| [ElementSet Class](48b47759-c441-ded2-5d8c-5c541c3eab01.htm)   [See Also](#seeAlsoToggle) |

Insert the specified element into the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool Insert( 	Element item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Insert ( _ 	item As Element _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Insert( 	Element^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element to be inserted into the set.

#### Return Value

Returns whether the element was inserted into the set.

# See Also

[ElementSet Class](48b47759-c441-ded2-5d8c-5c541c3eab01.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b0df884-d8d4-e55f-f940-6c96fbea125b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewOrganizationId Property

---



|  |
| --- |
| [InSessionViewSheetSet Class](61a44d58-c862-5fb6-6a06-dd3d3abac585.htm)   [See Also](#seeAlsoToggle) |

[ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)  to the  [BrowserOrganization](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)  for non-sheet views.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual ElementId ViewOrganizationId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Property ViewOrganizationId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property ElementId^ ViewOrganizationId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

#### Implements

 [IViewSheetSet ViewOrganizationId](cab190d0-c36b-4bdb-1259-93241c94fd58.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the  [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)  does not reference to  [BrowserOrganization](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)  , or the target type of  [BrowserOrganization](4fd57c3f-6127-efd9-f79e-70ad3e5dc1cc.htm)  is incompatible. |

# See Also

[InSessionViewSheetSet Class](61a44d58-c862-5fb6-6a06-dd3d3abac585.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b0f0c45-6b21-b2a2-b2cb-2e07393cbbb7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsRunBottomElevation Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Relative Base Height": Relative height to stairs bottom elevation

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsRunBottomElevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsRunBottomElevation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsRunBottomElevation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b0fea7f-4fd0-bee4-cc1b-773b13b2e36b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetKnotsV Method

---



|  |
| --- |
| [NurbsSurfaceData Class](7d65dbde-8aac-7d7d-e811-a6c91a541de4.htm)   [See Also](#seeAlsoToggle) |

Get the list of knots in the v-direction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public IList<double> GetKnotsV() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetKnotsV As IList(Of Double) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<double>^ GetKnotsV() ``` |

# See Also

[NurbsSurfaceData Class](7d65dbde-8aac-7d7d-e811-a6c91a541de4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b10e0d0-d2e9-d157-db30-a29a809a5021.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeParamStartHookTanLen Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Start Tangent Hook Length"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarShapeParamStartHookTanLen { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarShapeParamStartHookTanLen As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarShapeParamStartHookTanLen { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b1127c1-56aa-6338-c532-40904b878fd6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PreheatCoilType Property

---



|  |
| --- |
| [AirSystemData Class](4a7c39a1-cd35-4828-97b7-f70cbd3fdab8.htm)   [See Also](#seeAlsoToggle) |

The preheat coil type. Note this property change would reset the preheat water loop.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public AirHeatingCoilType PreheatCoilType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PreheatCoilType As AirHeatingCoilType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property AirHeatingCoilType PreheatCoilType { 	AirHeatingCoilType get (); 	void set (AirHeatingCoilType value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[AirSystemData Class](4a7c39a1-cd35-4828-97b7-f70cbd3fdab8.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__1b12b26e-d988-4115-c2b7-eb7a582a8dbe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForwardIterator Method

---



|  |
| --- |
| [CombinableElementArray Class](dc5f6afb-a30d-dc82-fcd3-340eff1685c7.htm)   [See Also](#seeAlsoToggle) |

Retrieve a forward moving iterator to the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual CombinableElementArrayIterator ForwardIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ForwardIterator As CombinableElementArrayIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual CombinableElementArrayIterator^ ForwardIterator() ``` |

#### Return Value

Returns a forward moving iterator to the array.

# See Also

[CombinableElementArray Class](dc5f6afb-a30d-dc82-fcd3-340eff1685c7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b1413fd-1358-709b-77a8-e383d6c1301e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Import Method (String, DWGImportOptions, View, ElementId)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Imports a DWG or DXF file to the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool Import( 	string file, 	DWGImportOptions options, 	View pDBView, 	out ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Import ( _ 	file As String, _ 	options As DWGImportOptions, _ 	pDBView As View, _ 	<OutAttribute> ByRef elementId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Import( 	String^ file,  	DWGImportOptions^ options,  	View^ pDBView,  	[OutAttribute] ElementId^% elementId ) ``` |

#### Parameters

file
:   Type:  System String    
     Full path of the file to import. File must exist and must be a valid DWG or DXF file.

options
:   Type:  [Autodesk.Revit.DB DWGImportOptions](fcba2c30-7e6d-9ab7-8378-f4c6d5de06bf.htm)    
     Various options applicable to the DWG or DXF format. If    a null reference (  Nothing  in Visual Basic)  , all options will be set to their respective default values.

pDBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     View used to aid placement of the imported file. If the options specify ThisViewOnly, this argument is required and the imported file will only be visible in the specified view. If the options specify center-to-center placement, this argument is required and the imported file will be placed in the center of the specified view. Otherwise, this view is used to obtain a base level to associate with the imported file. If not specified, an existing view will be chosen instead and may open a view or associate the imported file to an arbitrary level.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)   %    
     The id of imported instance after a successful import.

#### Return Value

True if successful, otherwise False.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Not a valid file for DWG import (.dwg and .dxf files are valid). -or- ThisViewOnly cannot be true when importing a DWG|DGN drawing into a 3D view. -or- The provided view is not valid for the options provided. -or- One or more strings describing layer selection is invalid or empty. -or- The line weights are not valid; either it contains an invalid number of line weights, or a line weight outside the valid range. -or- The scale is not valid as a CustomScale for use during import. -or- NullOrEmpty -or- The view is not printable. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The given file does not exist. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Import is temporarily disabled. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |
| [Autodesk.Revit.Exceptions OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The DWG Import/Link module is not available in the installed Revit. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Import Overload](05c3dbe2-fe7e-c293-761d-b11f356a011b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b142373-5069-d110-9aab-22328e7e7c4d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadAttrAreaForceScaleFactor Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Area force scale"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LoadAttrAreaForceScaleFactor { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoadAttrAreaForceScaleFactor As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LoadAttrAreaForceScaleFactor { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b1517e8-b244-e249-9f01-e6137b40c886.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetInterpolatingCurves Method

---



|  |
| --- |
| [ReferencePoint Class](b4b9baeb-2ec5-a2e1-1420-37f593d36aa4.htm)   [See Also](#seeAlsoToggle) |

The set of CurveByPoints elements that interpolate a ReferencePoint.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public CurveByPointsArray GetInterpolatingCurves() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetInterpolatingCurves As CurveByPointsArray ``` |

 

| Visual C++ |
| --- |
| ``` public: CurveByPointsArray^ GetInterpolatingCurves() ``` |

# Remarks

A CurveByPoints is in the  GetInterpolatingCurves  array if and only if the ReferencePoint is in the Points array of  [CurveByPoints](2df7ab39-1ac0-5803-79fa-b23a959bf8f2.htm)  .

# See Also

[ReferencePoint Class](b4b9baeb-2ec5-a2e1-1420-37f593d36aa4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b15a741-d1a0-e791-5d93-d59773ecc137.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsWorksetVisible Method

---



|  |
| --- |
| [WorksetDefaultVisibilitySettings Class](8a6f0949-069b-4b83-380c-f6582ef37a40.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the workset is visible by default.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsWorksetVisible( 	WorksetId worksetId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsWorksetVisible ( _ 	worksetId As WorksetId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsWorksetVisible( 	WorksetId^ worksetId ) ``` |

#### Parameters

worksetId
:   Type:  [Autodesk.Revit.DB WorksetId](8bece327-c269-8101-b4c2-38632f593fe6.htm)    
     Id of the workset.

#### Return Value

Whether the workset is visible by default.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | There is no workset with this Id in the document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | WorksetDefaultVisibilitySettings is not applicable to family documents. |

# See Also

[WorksetDefaultVisibilitySettings Class](8a6f0949-069b-4b83-380c-f6582ef37a40.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b1a9194-d048-7d41-eb53-94b9201e2a9b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsTypeNameValidForCustomConnection Method

---



|  |
| --- |
| [StructuralConnectionHandlerType Class](e948a909-1b00-8789-6302-b46015c9cb47.htm)   [See Also](#seeAlsoToggle) |

Validates if the input name matches the criteria of StructuralConnectionHandlerType name. Name must be unique among other existing StructuralConnectionHandlerTypes and cannot contain any of the following characters: new line, {}[];`~\\/:\*?";<>| or any of the non-printable characters.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static bool IsTypeNameValidForCustomConnection( 	Document document, 	string typeName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsTypeNameValidForCustomConnection ( _ 	document As Document, _ 	typeName As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsTypeNameValidForCustomConnection( 	Document^ document,  	String^ typeName ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document.

typeName
:   Type:  System String    
     The StructuralConnectionHandlerType name to validate.

#### Return Value

True if the input name matches the criteria of StructuralConnectionHandlerType name.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[StructuralConnectionHandlerType Class](e948a909-1b00-8789-6302-b46015c9cb47.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__1b2182eb-3d56-7b65-70bc-f904f236266a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DWFImageQuality Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing possible image quality for DWF Export.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum DWFImageQuality ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration DWFImageQuality ``` |

 

| Visual C++ |
| --- |
| ``` public enum class DWFImageQuality ``` |

# Members

| Member name | Description |
| --- | --- |
| Default |  |
| Low |  |
| Medium |  |
| High |  |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b232f70-c5c3-dbe4-5a93-4555710a0944.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Kcal Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol kcal, indicating unit Kilocalories.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Kcal { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Kcal As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Kcal { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b268ee5-d666-03fd-e41c-f92f487fe45e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [FamilySizeTableErrorInfo Class](5912d43c-de68-a783-d8dd-1526ef9edb02.htm)   [See Also](#seeAlsoToggle) |

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

[FamilySizeTableErrorInfo Class](5912d43c-de68-a783-d8dd-1526ef9edb02.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b26e9f8-64d3-91a1-5296-4addc9516f9e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpaceCarpetingParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Carpeting"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpaceCarpetingParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpaceCarpetingParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpaceCarpetingParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b297ba5-692b-1011-5ffa-c5286c0e2798.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarGeometryType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Geometry"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarGeometryType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarGeometryType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarGeometryType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b324b35-0617-b47c-8d05-5af63e72cd7c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OriginalElementTypeId Property

---



|  |
| --- |
| [ElementTypeDuplicatedEventArgs Class](7ec2ef50-ea02-2e47-a854-490d00285cd1.htm)   [See Also](#seeAlsoToggle) |

The id of the element type that is duplicated.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public ElementId OriginalElementTypeId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property OriginalElementTypeId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ OriginalElementTypeId { 	ElementId^ get (); } ``` |

# See Also

[ElementTypeDuplicatedEventArgs Class](7ec2ef50-ea02-2e47-a854-490d00285cd1.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__1b33c047-c22a-48b0-c33c-db67cd7253d4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImportSymbolName Property

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
| ``` public static ForgeTypeId ImportSymbolName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ImportSymbolName As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ImportSymbolName { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b39a6a8-e775-d37b-99d5-e93165f350bb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HeadingOrientation Property

---



|  |
| --- |
| [ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)   [See Also](#seeAlsoToggle) |

The orientation of the column heading text.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ScheduleHeadingOrientation HeadingOrientation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property HeadingOrientation As ScheduleHeadingOrientation 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ScheduleHeadingOrientation HeadingOrientation { 	ScheduleHeadingOrientation get (); 	void set (ScheduleHeadingOrientation value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b3aab39-84c9-7592-7be2-060c68e1d276.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForwardIterator Method

---



|  |
| --- |
| [EdgeArrayArray Class](7f25fe6f-a427-7ac3-6753-2dec37fb058c.htm)   [See Also](#seeAlsoToggle) |

Retrieve a forward moving iterator to the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual EdgeArrayArrayIterator ForwardIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ForwardIterator As EdgeArrayArrayIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual EdgeArrayArrayIterator^ ForwardIterator() ``` |

#### Return Value

Returns a forward moving iterator to the array.

# See Also

[EdgeArrayArray Class](7f25fe6f-a427-7ac3-6753-2dec37fb058c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b4084c5-7adc-12fb-054b-ca639f4f3a07.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PreviewControl Constructor

---



|  |
| --- |
| [PreviewControl Class](50112279-5c9d-0351-bbd1-698e76be9e36.htm)   [See Also](#seeAlsoToggle) |

Constructs a preview control.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public PreviewControl( 	Document document, 	ElementId viewId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	document As Document, _ 	viewId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: PreviewControl( 	Document^ document,  	ElementId^ viewId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

viewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The view id want to browse in this control.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when dbDocument or viewId is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the given document is a linked document or the given viewId is invalid or the view is a schedule or other non-graphical view such as schedule views or the project browser view. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when there is an active preview control already. |

# See Also

[PreviewControl Class](50112279-5c9d-0351-bbd1-698e76be9e36.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__1b41a9db-a87a-accb-96e5-4d11647876ab.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ImportOptions3DM Constructor (ImportOptions3DM)

---



|  |
| --- |
| [ImportOptions3DM Class](72310605-e939-bc8c-c790-642da4cc02cb.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of ImportOptions3DM as a copy of the provided import options.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public ImportOptions3DM( 	ImportOptions3DM option ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	option As ImportOptions3DM _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ImportOptions3DM( 	ImportOptions3DM^ option ) ``` |

#### Parameters

option
:   Type:  [Autodesk.Revit.DB ImportOptions3DM](72310605-e939-bc8c-c790-642da4cc02cb.htm)    
     The 3DM import options to be copied.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ImportOptions3DM Class](72310605-e939-bc8c-c790-642da4cc02cb.htm)

[ImportOptions3DM Overload](c4450a10-130f-cc67-c513-e22bb8ea89a1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b4309e7-bdf4-807a-a13a-6dcef6a94b50.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FillColor Property

---



|  |
| --- |
| [MEPSystemType Class](9a14b7f0-1472-4375-c4f0-86f9f2479851.htm)   [See Also](#seeAlsoToggle) |

Indicates the color that should override the fill color for all components in the system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public Color FillColor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FillColor As Color 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Color^ FillColor { 	Color^ get (); 	void set (Color^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[MEPSystemType Class](9a14b7f0-1472-4375-c4f0-86f9f2479851.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b458b40-b9a1-c706-7754-186ec0dd719c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpacingJustification Property

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
| ``` public static ForgeTypeId SpacingJustification { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpacingJustification As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpacingJustification { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b474262-8b56-a5f0-9ecb-ffe07afd8732.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DisjoinedSolidsInInPlaceFamily Property

---



|  |
| --- |
| [BuiltInFailures PerformanceFailures Class](d008a572-b1aa-1e46-0c4e-f760c50776fd.htm)   [See Also](#seeAlsoToggle) |

In-place family contains multiple disjoined solids. Consider splitting in several in-place families.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DisjoinedSolidsInInPlaceFamily { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DisjoinedSolidsInInPlaceFamily As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DisjoinedSolidsInInPlaceFamily { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures PerformanceFailures Class](d008a572-b1aa-1e46-0c4e-f760c50776fd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b4bd623-6155-0659-e3eb-440d9449605a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyFreeinstDefaultElevation Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Default Elevation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FamilyFreeinstDefaultElevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FamilyFreeinstDefaultElevation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FamilyFreeinstDefaultElevation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b4c0c9b-020d-6791-d0cb-3592bd2c8480.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DefaultConstructionMassOpening Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Mass Opening"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DefaultConstructionMassOpening { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DefaultConstructionMassOpening As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DefaultConstructionMassOpening { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b4cc73b-dc00-0439-5480-fd7979b1e106.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPointAtStation Method

---



|  |
| --- |
| [Alignment Class](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)   [See Also](#seeAlsoToggle) |

Calculates the model point for a given alignment station.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public XYZ GetPointAtStation( 	double station ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPointAtStation ( _ 	station As Double _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetPointAtStation( 	double station ) ``` |

#### Parameters

station
:   Type:  System Double    
     The alignment station for which to calculate the point, in Revit internal model units (standard Imperial feet).

#### Return Value

The model point at the given alignment station.

# See Also

[Alignment Class](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)

<!-- Start of Syntax__1b4edf8f-bddc-1a2b-f093-af6c2a966cdb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuildingPadNoSurface Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

A Pad can't extend beyond the edge of a Toposurface.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId BuildingPadNoSurface { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BuildingPadNoSurface As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ BuildingPadNoSurface { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b58d735-f0b4-8f13-52a1-b25e1329cfe6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpatialFieldMgrResultsVisibility Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Results Visibility"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpatialFieldMgrResultsVisibility { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpatialFieldMgrResultsVisibility As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpatialFieldMgrResultsVisibility { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b5a0a22-2613-64de-ce7b-b8b9dcff4dd2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PropertySegmentNS Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"N/S"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PropertySegmentNS { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PropertySegmentNS As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PropertySegmentNS { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b5bca46-3a87-5c13-7e49-f1d2524548a0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RotationalPointSpringCoefficient Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Rotational Point Spring Coefficient, in discipline Structural.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RotationalPointSpringCoefficient { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RotationalPointSpringCoefficient As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RotationalPointSpringCoefficient { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b5d6569-0550-4113-f8d1-3cc94201c5a4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumberOfCurves Method

---



|  |
| --- |
| [CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)   [See Also](#seeAlsoToggle) |

Returns the number of curves in the curve loop.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2019.1

# Syntax

| C# |
| --- |
| ``` public int NumberOfCurves() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NumberOfCurves As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int NumberOfCurves() ``` |

#### Return Value

The number of curves in the curve loop.

# See Also

[CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b5f2a55-5ea2-e468-b887-7f3c98aa6e85.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Schedule Property

---



|  |
| --- |
| [ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)   [See Also](#seeAlsoToggle) |

The schedule that this field belongs to.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ViewSchedule Schedule { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Schedule As ViewSchedule 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ViewSchedule^ Schedule { 	ViewSchedule^ get (); } ``` |

# See Also

[ScheduleField Class](3d6b0eb5-ed36-278d-a5df-38b6d600e876.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b6161d1-42da-1365-f796-382f297730da.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
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

[Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b626235-f4b5-cb31-28fe-fbe27353979a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetUnits Method

---



|  |
| --- |
| [PipeFittingAndAccessoryPressureDropUIData Class](6dcc2335-c5a0-2122-82ed-566efa781f41.htm)   [See Also](#seeAlsoToggle) |

Gets units.

**Namespace:**   [Autodesk.Revit.UI.Plumbing](a4cc3644-f568-6568-9c2f-dcdb6eafdf6b.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public Units GetUnits() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetUnits As Units ``` |

 

| Visual C++ |
| --- |
| ``` public: Units^ GetUnits() ``` |

#### Return Value

The Units object.

# See Also

[PipeFittingAndAccessoryPressureDropUIData Class](6dcc2335-c5a0-2122-82ed-566efa781f41.htm)

[Autodesk.Revit.UI.Plumbing Namespace](a4cc3644-f568-6568-9c2f-dcdb6eafdf6b.htm)

<!-- Start of Syntax__1b662e5b-b564-c828-f47b-0d6fe38b6973.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomCalculatedSupplyAirflowParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Calculated Supply Airflow"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RoomCalculatedSupplyAirflowParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoomCalculatedSupplyAirflowParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RoomCalculatedSupplyAirflowParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b67db3c-93cd-4bdd-8b8c-8828a28304b7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementView Property

---



|  |
| --- |
| [DockablePanes BuiltInDockablePanes Class](03b7f98b-7e0d-8fa6-052c-f9192ff86ca8.htm)   [See Also](#seeAlsoToggle) |

The element view pane.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static DockablePaneId ElementView { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ElementView As DockablePaneId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property DockablePaneId^ ElementView { 	DockablePaneId^ get (); } ``` |

# See Also

[DockablePanes BuiltInDockablePanes Class](03b7f98b-7e0d-8fa6-052c-f9192ff86ca8.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__1b6aa6c7-35a8-46cf-8e05-efa5665f8f5d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAnalyticalPropertyData Method

---



|  |
| --- |
| [ElectricalAnalyticalNode Class](562d1f7d-c9df-bee5-4659-4f8607ee4333.htm)   [See Also](#seeAlsoToggle) |

Gets the electrical analytical node property data,    a null reference (  Nothing  in Visual Basic)  if not available.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public AnalyticalDistributionNodePropertyData GetAnalyticalPropertyData() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAnalyticalPropertyData As AnalyticalDistributionNodePropertyData ``` |

 

| Visual C++ |
| --- |
| ``` public: AnalyticalDistributionNodePropertyData^ GetAnalyticalPropertyData() ``` |

#### Return Value

The electrical analytical node property data.

# Remarks

These types have special data:

* Bus
* TransferSwitch
* EquipmentLoad

# See Also

[ElectricalAnalyticalNode Class](562d1f7d-c9df-bee5-4659-4f8607ee4333.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__1b6b85a0-b51e-9f82-cfa7-6db4cda9f884.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddSpace Method

---



|  |
| --- |
| [IFCProductWrapper Class](368d2c50-1258-32a9-00ed-cc41059a6694.htm)   [See Also](#seeAlsoToggle) |

Adds an IfcSpace handle to associate with the IfcProduct in this wrapper.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void AddSpace( 	IFCAnyHandle spaceHandle, 	IFCLevelInfo pLevelInfo, 	IFCExtrusionCreationData pParams, 	bool relateToLevel ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddSpace ( _ 	spaceHandle As IFCAnyHandle, _ 	pLevelInfo As IFCLevelInfo, _ 	pParams As IFCExtrusionCreationData, _ 	relateToLevel As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddSpace( 	IFCAnyHandle^ spaceHandle,  	IFCLevelInfo^ pLevelInfo,  	IFCExtrusionCreationData^ pParams,  	bool relateToLevel ) ``` |

#### Parameters

spaceHandle
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)    
     The IfcSpace handle.

pLevelInfo
:   Type:  [Autodesk.Revit.DB.IFC IFCLevelInfo](9f287338-fe0c-383b-58be-39105d704a9f.htm)    
     Information on the associated level.

pParams
:   Type:  [Autodesk.Revit.DB.IFC IFCExtrusionCreationData](9447a335-6861-0533-6896-e6ff1fd41761.htm)    
     The extrusion creation data associated with the given space. Optional, can be    a null reference (  Nothing  in Visual Basic)  .

relateToLevel
:   Type:  System Boolean    
     True to relate the space to the level, false otherwise.

# Remarks

If the IFCLevelInfo is not provided, and relateToLevel to true, the handle will be associated to the building handle.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCProductWrapper Class](368d2c50-1258-32a9-00ed-cc41059a6694.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__1b6c908c-b65c-8e75-80ac-cbe4a7d8eec4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadCaseNature Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Nature"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LoadCaseNature { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoadCaseNature As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LoadCaseNature { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b74c240-55f5-c1ab-1e78-57bba4090a66.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetInputPoints Method

---



|  |
| --- |
| [StructuralConnectionHandler Class](78653026-36f1-6ab3-f2c0-728692c99b3c.htm)   [See Also](#seeAlsoToggle) |

Returns a list of additional points defining certain connections.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public IList<ConnectionInputPoint> GetInputPoints() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetInputPoints As IList(Of ConnectionInputPoint) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ConnectionInputPoint^>^ GetInputPoints() ``` |

# See Also

[StructuralConnectionHandler Class](78653026-36f1-6ab3-f2c0-728692c99b3c.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__1b765ccd-d60b-21f9-122e-1d2f27fdb1a5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SectionAttrHeadTag Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Section Head"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SectionAttrHeadTag { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SectionAttrHeadTag As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SectionAttrHeadTag { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b77356c-e92b-e151-f8c9-727b3e2b8934.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SweepProfile Class

---



|  |
| --- |
| [Members](1918f6b7-7c78-4b3d-9d2b-3030d4504550.htm)   [See Also](#seeAlsoToggle) |

Represents a profile for sweep or swept blend elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class SweepProfile : APIObject ``` |

 

| Visual Basic |
| --- |
| ``` Public Class SweepProfile _ 	Inherits APIObject ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SweepProfile : public APIObject ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB SweepProfile    
  [Autodesk.Revit.DB CurveLoopsProfile](e841c265-7932-3a99-ea0d-a8865e21ca05.htm)    
  [Autodesk.Revit.DB FamilySymbolProfile](9a0976ad-9366-4139-43f1-95e9f3918622.htm)

# See Also

[SweepProfile Members](1918f6b7-7c78-4b3d-9d2b-3030d4504550.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b777386-42a0-6a34-2c79-1290186b79a0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreCoordinationModelHandlesHidden Property

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Indicates if Coordination Model handles are currently hidden in the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool AreCoordinationModelHandlesHidden { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AreCoordinationModelHandlesHidden As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool AreCoordinationModelHandlesHidden { 	bool get (); 	void set (bool value); } ``` |

#### Field Value

True if Coordination Model handles are currently hidden in the view, false otherwise.

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b7b2326-764f-b601-799c-13cabe495b37.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DialogType Property

---



|  |
| --- |
| [MessageBoxShowingEventArgs Class](aa1b432c-e9b9-b528-aa3b-60514aaea2a3.htm)   [See Also](#seeAlsoToggle) |

An integer that describes the standard Windows type of the dialog box.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public int DialogType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property DialogType As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int DialogType { 	int get (); } ``` |

# See Also

[MessageBoxShowingEventArgs Class](aa1b432c-e9b9-b528-aa3b-60514aaea2a3.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__1b7bfbea-9f67-ef97-9469-98cd063c33a8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsFlippedOnFace Method (Face)

---



|  |
| --- |
| [Edge Class](7155ef49-fcd9-c80a-6232-70189a617bcc.htm)   [See Also](#seeAlsoToggle) |

Determines if this edge's topological direction on the Face is opposite to its parametric direction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public bool IsFlippedOnFace( 	Face face ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsFlippedOnFace ( _ 	face As Face _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsFlippedOnFace( 	Face^ face ) ``` |

#### Parameters

face
:   Type:  [Autodesk.Revit.DB Face](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)    
     The face with respect to which the direction is considered. Must belong to the edge.

#### Return Value

true if this edge's topological direction on the Face is opposite to its parametric direction, false if the topological direction agrees with the parametric direction.

# Remarks

Outer edge loops on a Face are oriented counter-clockwise with respect to the Face's orientation, and inner loops are oriented clockwise. The topological direction of an edge on a face means the direction in which the edge's loop is being traversed.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the specified face is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the specified face is not one of the faces for this edge. |

# See Also

[Edge Class](7155ef49-fcd9-c80a-6232-70189a617bcc.htm)

[IsFlippedOnFace Overload](7524789f-8226-a9c3-b105-9985e0ea9174.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b7c6e26-f9b9-8fd8-14bd-84280f1b6586.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ThermalExpansionCoefficient Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Thermal Expansion Coefficient, in discipline Structural.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ThermalExpansionCoefficient { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ThermalExpansionCoefficient As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ThermalExpansionCoefficient { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b8038e0-fb86-0869-27ba-4f7b136693fc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecLoadClassification Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Load Classification"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecLoadClassification { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecLoadClassification As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecLoadClassification { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b8323a9-dd24-c818-e74c-e29b346000d3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetElementsWithOpenConnector Method

---



|  |
| --- |
| [DesignToFabricationConverter Class](b2165e08-c8a4-5674-12ff-d359eba911d4.htm)   [See Also](#seeAlsoToggle) |

Gets the set of fabrication part or MEP design element identifiers with open connectors, caused by fittings failing to convert.

**Namespace:**   [Autodesk.Revit.DB.Fabrication](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public ISet<ElementId> GetElementsWithOpenConnector() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetElementsWithOpenConnector As ISet(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ISet<ElementId^>^ GetElementsWithOpenConnector() ``` |

# Remarks

This set of element identifiers is only available after the  **Convert**  method has been invoked, and returns DesignToFabricationConverterResult::Enum::PartialFailure.

# See Also

[DesignToFabricationConverter Class](b2165e08-c8a4-5674-12ff-d359eba911d4.htm)

[Autodesk.Revit.DB.Fabrication Namespace](49e74a25-7ea1-efa6-548a-a3c3d0655e43.htm)

<!-- Start of Syntax__1b83b0df-b3dc-e5c5-5933-579b1ba877bf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathReinHookTypen1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Primary Bar - Start Hook Type"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PathReinHookTypen1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PathReinHookTypen1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PathReinHookTypen1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b876c5c-c873-7347-efb9-280fa827b325.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsShapeImporterAvailable Method

---



|  |
| --- |
| [OptionalFunctionalityUtils Class](98d35b3b-34ec-4105-f7c5-16e9215b6b52.htm)   [See Also](#seeAlsoToggle) |

Checks whether the ShapeImporter functionality is available in the installed Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static bool IsShapeImporterAvailable() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsShapeImporterAvailable As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsShapeImporterAvailable() ``` |

#### Return Value

True if the ShapeImporter functionality is available in the installed Revit.

# See Also

[OptionalFunctionalityUtils Class](98d35b3b-34ec-4105-f7c5-16e9215b6b52.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b88a5e9-03ee-2a20-652d-f68586776dda.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, ElementId, XYZ, XYZ, LineLoadType)

---



|  |
| --- |
| [LineLoad Class](ee5ec273-350a-1cdb-d136-0c454bb1446a.htm)   [See Also](#seeAlsoToggle) |

Creates a new hosted line load within the project.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public static LineLoad Create( 	Document aDoc, 	ElementId hostElemId, 	XYZ forceVector1, 	XYZ momentVector1, 	LineLoadType symbol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	aDoc As Document, _ 	hostElemId As ElementId, _ 	forceVector1 As XYZ, _ 	momentVector1 As XYZ, _ 	symbol As LineLoadType _ ) As LineLoad ``` |

 

| Visual C++ |
| --- |
| ``` public: static LineLoad^ Create( 	Document^ aDoc,  	ElementId^ hostElemId,  	XYZ^ forceVector1,  	XYZ^ momentVector1,  	LineLoadType^ symbol ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document to which new line load will be added.

hostElemId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The analytical host element for the line Load.

forceVector1
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The applied 3d force vector.

momentVector1
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The applied 3d moment vector.

symbol
:   Type:  [Autodesk.Revit.DB.Structure LineLoadType](b9172085-e7bf-a23f-834c-7a5448ee39d4.htm)    
     The symbol of the LineLoad. Set    a null reference (  Nothing  in Visual Basic)  to use default type.

#### Return Value

If successful, returns the newly created LineLoad,    a null reference (  Nothing  in Visual Basic)  otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element hostElemId does not exist in the document -or- hostElemId is not permitted for this type of load. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | Thrown when all force and moment vectors are equal zero. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if type could not be set for newly created line load. |

# See Also

[LineLoad Class](ee5ec273-350a-1cdb-d136-0c454bb1446a.htm)

[Create Overload](c02b26f5-fbdd-3cdc-70ad-c872f19c405d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__1b89233e-8ab3-90ec-394d-e9795a8a5a94.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WhileLoadingFamilyShared Property

---



|  |
| --- |
| [BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)   [See Also](#seeAlsoToggle) |

While loading shared family '[Family Name]' from family '[Family Name]': [Description]

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId WhileLoadingFamilyShared { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WhileLoadingFamilyShared As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ WhileLoadingFamilyShared { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b8931c8-fc7c-f31f-d586-de7606b50b8c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### KipPerIn Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol kip/in, indicating unit Kips per inch.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId KipPerIn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property KipPerIn As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ KipPerIn { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b89a389-2422-bd9c-d141-e230d2b2f16e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CabletrayMinbendmultiplierParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bend Radius Multiplier"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CabletrayMinbendmultiplierParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CabletrayMinbendmultiplierParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CabletrayMinbendmultiplierParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b8afc56-1985-8459-0626-3fa73114c4c3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsVisibleByDefault Property

---



|  |
| --- |
| [Workset Class](aa8f7f05-16c7-2fbf-5004-d819a1fd0b6d.htm)   [See Also](#seeAlsoToggle) |

Whether the workset is visible by default.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsVisibleByDefault { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsVisibleByDefault As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsVisibleByDefault { 	bool get (); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | WorksetDefaultVisibilitySettings is not applicable to family documents. |

# See Also

[Workset Class](aa8f7f05-16c7-2fbf-5004-d819a1fd0b6d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b8cf1f1-2b87-2aa4-1811-58f4b49372a6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ExternalDefinition Class](a3e84415-b88e-a8e0-4e11-64795d92da0e.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ExternalDefinition](a3e84415-b88e-a8e0-4e11-64795d92da0e.htm)

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

[ExternalDefinition Class](a3e84415-b88e-a8e0-4e11-64795d92da0e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b8db332-20c8-47e7-4457-b83dfcddb43c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsTriserTreadNumber Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Tread Number": Count the sequential number of tread in the stair.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsTriserTreadNumber { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsTriserTreadNumber As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsTriserTreadNumber { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b92c153-4c3a-9ca3-5cff-fee65b5b77de.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DivideVolumesProfilesEdgeMatchForWidthAll Property

---



|  |
| --- |
| [BuiltInFailures DPartFailures Class](60230c02-eb7e-98f0-38c8-8da51b5109a8.htm)   [See Also](#seeAlsoToggle) |

Division family cannot be used with the selected edge condition for all widths of hosts

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DivideVolumesProfilesEdgeMatchForWidthAll { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DivideVolumesProfilesEdgeMatchForWidthAll As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DivideVolumesProfilesEdgeMatchForWidthAll { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DPartFailures Class](60230c02-eb7e-98f0-38c8-8da51b5109a8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b94d1ce-863e-9b5e-bb10-a82ddca75b47.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureRealWorldOffsetX Property

---



|  |
| --- |
| [Wave Class](9c0cc26f-f6ae-708e-5612-d3d181058174.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Offset X" from the "Wave" schema.

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

[Wave Class](9c0cc26f-f6ae-708e-5612-d3d181058174.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__1b9538a9-a76b-0a40-2aed-e02f6974a43a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Export Method (String, String, NavisworksExportOptions)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Exports a Revit project to the Navisworks .nwc format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Export( 	string folder, 	string name, 	NavisworksExportOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Export ( _ 	folder As String, _ 	name As String, _ 	options As NavisworksExportOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Export( 	String^ folder,  	String^ name,  	NavisworksExportOptions^ options ) ``` |

#### Parameters

folder
:   Type:  System String    
     The name of the folder for the exported file.

name
:   Type:  System String    
     The name of the exported file. If it doesn't end in '.nwc', this extension will be added automatically.

options
:   Type:  [Autodesk.Revit.DB NavisworksExportOptions](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)    
     Options which control the contents of the export.

# Remarks

This is an optional functionality that does not have to be installed. The method "OptionalFunctionalityUtils.isNavisworksExporterAvailable()" can be called to check if the exporter is present.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | NullOrEmpty -or- Contains invalid characters. -or- The input options were not valid. Check the exception message for specific details. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Export is temporarily disabled. -or- Exporting is not allowed in the current application mode. |
| [Autodesk.Revit.Exceptions InvalidPathArgumentException](3f3c93a6-008b-f9de-40d4-5cd99bb32b34.htm) | The folder does not exist. |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | The export operation is cancelled in event handler. |
| [Autodesk.Revit.Exceptions OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | A Navisworks Exporter is not available in the installed Revit. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Export Overload](2f535342-ee41-86f9-0022-92ba1f65112d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b9a5edf-d0dc-ce3b-cedd-75c01e431bac.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RectangleLightShape Class

---



|  |
| --- |
| [Members](544012d5-0f2f-fbe7-af52-bc8984d2a5db.htm)   [See Also](#seeAlsoToggle) |

This class encapsulates a rectangle light shape.

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class RectangleLightShape : LightShape ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RectangleLightShape _ 	Inherits LightShape ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RectangleLightShape : public LightShape ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB.Lighting LightShape](6fc9d0d9-21ac-9192-0178-115be3a48dc7.htm)    
  Autodesk.Revit.DB.Lighting RectangleLightShape

# See Also

[RectangleLightShape Members](544012d5-0f2f-fbe7-af52-bc8984d2a5db.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__1b9b02cf-8fca-84b7-d80e-ed4b32277826.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DistanceTo Method

---



|  |
| --- |
| [UV Class](1724be37-059b-91ff-aa74-d1508082f76d.htm)   [See Also](#seeAlsoToggle) |

Returns the distance from this 2-D point to the specified 2-D point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double DistanceTo( 	UV source ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function DistanceTo ( _ 	source As UV _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double DistanceTo( 	UV^ source ) ``` |

#### Parameters

source
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     The specified point.

#### Return Value

The real number equal to the distance between the two points.

# Remarks

The distance between the two points is equal to the length of the vector that joins the two points.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when source is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[UV Class](1724be37-059b-91ff-aa74-d1508082f76d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b9cdb90-85ba-424a-3df0-33cab7d066f6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LabelLineLength Property

---



|  |
| --- |
| [Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.htm)   [See Also](#seeAlsoToggle) |

The length of the viewport label line in sheet space, measured in feet.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public double LabelLineLength { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LabelLineLength As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double LabelLineLength { 	double get (); 	void set (double value); } ``` |

# Remarks

It can be negative. The sign depends on the direction of the label line.

# See Also

[Viewport Class](5991dc40-234a-4835-cc06-07524d2e61a4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__1b9d23db-b700-1f02-e02e-77ac73e7d667.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PrimitiveType Property

---



|  |
| --- |
| [IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.htm)   [See Also](#seeAlsoToggle) |

The primitive data type.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public IFCDataPrimitiveType PrimitiveType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PrimitiveType As IFCDataPrimitiveType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property IFCDataPrimitiveType PrimitiveType { 	IFCDataPrimitiveType get (); 	void set (IFCDataPrimitiveType value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__1b9deb4d-aff3-1b12-8061-cc983d68040b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [EdgeArray Class](7069d0a1-fc52-a347-e0d8-6de1f40797d3.htm)   [See Also](#seeAlsoToggle) |

Removes every edge from the array, rendering it empty.

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

[EdgeArray Class](7069d0a1-fc52-a347-e0d8-6de1f40797d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)