

<!-- Start of Syntax__0003f9f7-1be6-9bcb-212a-d38767d01e10.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaxRange Property

---



|  |
| --- |
| [ElectricalDemandFactorValue Class](54de7c5a-916a-291e-5b9c-08ebce5a8ab0.htm)   [See Also](#seeAlsoToggle) |

The maximum range for this demand factor value. For example, objects 1 to 3 can have 100% demand factor. In the example above, the maximum range will be 3.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public double MaxRange { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MaxRange As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double MaxRange { 	double get (); 	void set (double value); } ``` |

# See Also

[ElectricalDemandFactorValue Class](54de7c5a-916a-291e-5b9c-08ebce5a8ab0.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__003adb28-a381-05f5-6490-e80ecc13b4fe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetGlobal3DDirectionHandles Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Sets the handles representing the cardinal directions in 3D.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static void SetGlobal3DDirectionHandles( 	bool positive, 	IFCAnyHandle xDir, 	IFCAnyHandle yDir, 	IFCAnyHandle zDir ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SetGlobal3DDirectionHandles ( _ 	positive As Boolean, _ 	xDir As IFCAnyHandle, _ 	yDir As IFCAnyHandle, _ 	zDir As IFCAnyHandle _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SetGlobal3DDirectionHandles( 	bool positive,  	IFCAnyHandle^ xDir,  	IFCAnyHandle^ yDir,  	IFCAnyHandle^ zDir ) ``` |

#### Parameters

positive
:   Type:  System Boolean    
     True if the handles returned should be in the positive direction, false if the handles should be in the negative direction.

xDir
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)    
     The X direction handle.

yDir
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)    
     The Y direction handle.

zDir
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)    
     The Z direction handle.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__003c6560-b317-aee4-349a-9a2161c45704.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [LightFamily Class](53ebee14-8d6f-28ac-f44e-1e7bd906c7d8.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [LightFamily](53ebee14-8d6f-28ac-f44e-1e7bd906c7d8.htm)

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

[LightFamily Class](53ebee14-8d6f-28ac-f44e-1e7bd906c7d8.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__003d9e36-c831-af50-c7e8-182f11464680.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Rotation Property

---



|  |
| --- |
| [TextNoteOptions Class](b0fd6ef8-a0ef-9cf4-5bc2-8cd65f81f648.htm)   [See Also](#seeAlsoToggle) |

Base line angle of a text note, in radians.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public double Rotation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Rotation As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Rotation { 	double get (); 	void set (double value); } ``` |

# Remarks

Default value is 0.0.

# See Also

[TextNoteOptions Class](b0fd6ef8-a0ef-9cf4-5bc2-8cd65f81f648.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__003db3a7-789a-dc15-222d-fe0eae1e559c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCreateGroup Property

---



|  |
| --- |
| [BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)   [See Also](#seeAlsoToggle) |

Cannot create group of these elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCreateGroup { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCreateGroup As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCreateGroup { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03a2609a-7777-f049-5013-c90eaa7054a2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ListNames Method

---



|  |
| --- |
| [ExportDWGSettings Class](a17fc52f-f67a-9763-e52f-29f867106908.htm)   [See Also](#seeAlsoToggle) |

Returns a list of names of dwg/dxf export settings.

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
     A Revit document to retrieve names from.

#### Return Value

An array of strings representing names of predefined setups.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportDWGSettings Class](a17fc52f-f67a-9763-e52f-29f867106908.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03a3a6c3-9195-25a1-abaa-641f00cbc930.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetAllCapsStatus Method (TextRange, Boolean)

---



|  |
| --- |
| [FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)   [See Also](#seeAlsoToggle) |

Sets the characters in a given text range to be in all caps or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetAllCapsStatus( 	TextRange textRange, 	bool isAllCaps ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetAllCapsStatus ( _ 	textRange As TextRange, _ 	isAllCaps As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetAllCapsStatus( 	TextRange^ textRange,  	bool isAllCaps ) ``` |

#### Parameters

textRange
:   Type:  [Autodesk.Revit.DB TextRange](8a00baaf-8cb8-d9f0-e0a0-eaa5aa16e55e.htm)    
     The given text range.

isAllCaps
:   Type:  System Boolean    
     The desired all caps status of characters in the given text range. True will render all characters in all caps. False will revert the characters back to their original mixed case.

# Remarks

Removing the all caps status will revert the characters back to their original case. It will not make them lower case.

The given text range should not be empty.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This text range is empty. -or- This start index of this text range is not within the text range identifying the entire text. -or- The end of this text range is not within the text range identifying the entire text. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)

[SetAllCapsStatus Overload](abf2e346-79c9-8128-926e-1fbf6af65c5d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03a44256-4123-6916-bbf3-39013a3cf238.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ValueParsingOptions Class](5e3782ee-a1ed-593d-8180-37ebf36eda83.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ValueParsingOptions](5e3782ee-a1ed-593d-8180-37ebf36eda83.htm)

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

[ValueParsingOptions Class](5e3782ee-a1ed-593d-8180-37ebf36eda83.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03a8b9ea-a778-0598-72b6-e79c41ce881e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetObjectData Method

---



|  |
| --- |
| [DisabledDisciplineException Class](3693dcdf-67fb-0128-3be8-cad150e9498e.htm)   [See Also](#seeAlsoToggle) |

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

[DisabledDisciplineException Class](3693dcdf-67fb-0128-3be8-cad150e9498e.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__03b391a2-c9ca-f501-28cb-f109966df57f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetExportLineweightInfo Method

---



|  |
| --- |
| [ExportLineweightTable Class](5620708e-0c7c-ced6-9887-0237a9229800.htm)   [See Also](#seeAlsoToggle) |

Gets a copy of the ExportLineweightInfo corresponding to the given ExportLineweightKey.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public ExportLineweightInfo GetExportLineweightInfo( 	ExportLineweightKey exportLineweightKey ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetExportLineweightInfo ( _ 	exportLineweightKey As ExportLineweightKey _ ) As ExportLineweightInfo ``` |

 

| Visual C++ |
| --- |
| ``` public: ExportLineweightInfo^ GetExportLineweightInfo( 	ExportLineweightKey^ exportLineweightKey ) ``` |

#### Parameters

exportLineweightKey
:   Type:  [Autodesk.Revit.DB ExportLineweightKey](5b3250ab-f70b-6f87-afbf-dd049a64c29e.htm)    
     The export line weight Key.

#### Return Value

Returns the line weight info for this key.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | An entry with the given key is not present in the table. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportLineweightTable Class](5620708e-0c7c-ced6-9887-0237a9229800.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03b7f98b-7e0d-8fa6-052c-f9192ff86ca8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DockablePanes.BuiltInDockablePanes Class

---



|  |
| --- |
| [DockablePanes Class](a6e4943e-8a76-92f6-81d3-1d467a1aa701.htm)   [Members](1fa5cdf1-2abb-1782-47a4-a5bef46d4793.htm)   [See Also](#seeAlsoToggle) |

A collection of ids of the dockable panes provided by Revit.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static class BuiltInDockablePanes ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class BuiltInDockablePanes ``` |

 

| Visual C++ |
| --- |
| ``` public ref class BuiltInDockablePanes abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.UI DockablePanes BuiltInDockablePanes

# See Also

[DockablePanes BuiltInDockablePanes Members](1fa5cdf1-2abb-1782-47a4-a5bef46d4793.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__03b804b3-3c30-56cb-a29b-92676a276798.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BasepointElevationParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Elev"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BasepointElevationParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BasepointElevationParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BasepointElevationParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03b8e2af-4445-39ed-f7b0-da9f3df942ef.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewFamilyInstanceCreationData Method (FamilySymbol, IList(XYZ))

---



|  |
| --- |
| [Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)   [See Also](#seeAlsoToggle) |

Creates an object which wraps the arguments of NewFamilyInstance() for batch creation.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyInstanceCreationData NewFamilyInstanceCreationData( 	FamilySymbol symbol, 	IList<XYZ> adaptivePoints ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewFamilyInstanceCreationData ( _ 	symbol As FamilySymbol, _ 	adaptivePoints As IList(Of XYZ) _ ) As FamilyInstanceCreationData ``` |

 

| Visual C++ |
| --- |
| ``` public: FamilyInstanceCreationData^ NewFamilyInstanceCreationData( 	FamilySymbol^ symbol,  	IList<XYZ^>^ adaptivePoints ) ``` |

#### Parameters

symbol
:   Type:  [Autodesk.Revit.DB FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)    
     A FamilySymbol object that represents the type of the instance that is to be inserted.

adaptivePoints
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The adaptive point location where the adaptive instance is to be placed.

# See Also

[Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)

[NewFamilyInstanceCreationData Overload](8f899df7-9949-9839-35f7-4092a6e70e20.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__03bb8e45-f73a-9ae5-eebb-cf84f3c0704f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionZprofileBottomFlangeLength Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bottom Flange Length"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralSectionZprofileBottomFlangeLength { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralSectionZprofileBottomFlangeLength As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralSectionZprofileBottomFlangeLength { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03bbec45-65f4-7770-1278-2f16e1d101b5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Flipped Property

---



|  |
| --- |
| [DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)   [See Also](#seeAlsoToggle) |

If the divided path is flipped the nodes are numbered in the reverse order. It also switches the ends from which beginningIndent and endIndent are measured from.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
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

# See Also

[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03c03f81-fe2c-aa3c-28a6-a07f1fb3588e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Erase Method

---



|  |
| --- |
| [ConnectorSet Class](a9821fc1-54cf-5f69-13a9-25d506ecb048.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual int Erase( 	Connector item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Erase ( _ 	item As Connector _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual int Erase( 	Connector^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)

# See Also

[ConnectorSet Class](a9821fc1-54cf-5f69-13a9-25d506ecb048.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03c0742a-15ba-d46d-8cd7-5c5a1fb63a6c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Visible Property

---



|  |
| --- |
| [RibbonItem Class](79225f03-1633-3722-15b0-752c91a3740d.htm)   [See Also](#seeAlsoToggle) |

Gets or sets a value indicating whether the item is visible.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

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

# Remarks

When the Visible property is set to false, the item won't be displayed on Ribbon.

# See Also

[RibbonItem Class](79225f03-1633-3722-15b0-752c91a3740d.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__03c0f25f-d24a-1635-7554-82bbf6775986.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetColorOptions Method

---



|  |
| --- |
| [ColorOptions Class](1ca57d8c-b970-83b4-c5ce-9e39464e5cc2.htm)   [See Also](#seeAlsoToggle) |

Returns the current Revit instance's ColorOptions.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public static ColorOptions GetColorOptions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetColorOptions As ColorOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: static ColorOptions^ GetColorOptions() ``` |

#### Return Value

The ColorOptions for the current Revit instance.

# See Also

[ColorOptions Class](1ca57d8c-b970-83b4-c5ce-9e39464e5cc2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03c126de-1985-bb64-28b3-cc4c3c391591.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShowDownText Property

---



|  |
| --- |
| [StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)   [See Also](#seeAlsoToggle) |

Represents whether show stairs down text or not.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool ShowDownText { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ShowDownText As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ShowDownText { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The type of this stairs path is not automatic up/down direction. |

# See Also

[StairsPath Class](ed5913d6-1219-9c7c-7e52-317dd58d7cd3.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__03c31b18-947a-5860-7278-da0cd8949e52.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotComputeRailElevation Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Can't compute elevation profile for one or more Rails

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotComputeRailElevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotComputeRailElevation As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotComputeRailElevation { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03c48a42-726d-2ca7-64ae-79b851820fd1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DigitGroupingAmount Property

---



|  |
| --- |
| [Units Class](89d89465-897f-4105-b935-27edf67aab3e.htm)   [See Also](#seeAlsoToggle) |

The number of digits in each group when numbers are formatted with digit grouping.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public DigitGroupingAmount DigitGroupingAmount { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DigitGroupingAmount As DigitGroupingAmount 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property DigitGroupingAmount DigitGroupingAmount { 	DigitGroupingAmount get (); 	void set (DigitGroupingAmount value); } ``` |

#### Field Value

The number of digits in each group. The default is Three.

# Remarks

This setting only has an effect when the UseDigitGrouping property is set to true in the FormatOptions object for the unit type being formatted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[Units Class](89d89465-897f-4105-b935-27edf67aab3e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03c63432-97f5-6efe-dee9-bad80fff548b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateGreaterRule Method (ElementId, Double, Double)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether double-precision values from the document are greater than a certain value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateGreaterRule( 	ElementId parameter, 	double value, 	double epsilon ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateGreaterRule ( _ 	parameter As ElementId, _ 	value As Double, _ 	epsilon As Double _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateGreaterRule( 	ElementId^ parameter,  	double value,  	double epsilon ) ``` |

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

# Remarks

Values greater than  *value*  but within  *epsilon*  are considered equal, not greater.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for value is not finite -or- The given value for value is not a number -or- The given value for epsilon is not finite -or- The given value for epsilon is not a number |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)

[CreateGreaterRule Overload](3885f1a1-d26c-a3c3-54e1-81f75c04148a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03c9e112-1fb3-5e42-1114-e99555cd1bfd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasSameType Method

---



|  |
| --- |
| [PanelScheduleTemplate Class](cf7e5cbb-7df4-ae55-8178-f449827b5752.htm)   [See Also](#seeAlsoToggle) |

Checks if given template has the same panel schedule type with this template.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool HasSameType( 	PanelScheduleTemplate otherTemplate ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function HasSameType ( _ 	otherTemplate As PanelScheduleTemplate _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool HasSameType( 	PanelScheduleTemplate^ otherTemplate ) ``` |

#### Parameters

otherTemplate
:   Type:  [Autodesk.Revit.DB.Electrical PanelScheduleTemplate](cf7e5cbb-7df4-ae55-8178-f449827b5752.htm)    
     The given template to check.

#### Return Value

True if the given template has the same panel schedule type with this template, false otherwise.

# Remarks

The panel schedule type is the enum type of PanelScheduleType class (Branch, switchboard, data etc.)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PanelScheduleTemplate Class](cf7e5cbb-7df4-ae55-8178-f449827b5752.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__03ca1f74-2bd8-a93c-ddf8-377e5a337c6c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreSolidsEqual Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Determines whether two solids are identical, potentially offset from each other.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool AreSolidsEqual( 	Solid first, 	Solid second, 	out Transform trf ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function AreSolidsEqual ( _ 	first As Solid, _ 	second As Solid, _ 	<OutAttribute> ByRef trf As Transform _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool AreSolidsEqual( 	Solid^ first,  	Solid^ second,  	[OutAttribute] Transform^% trf ) ``` |

#### Parameters

first
:   Type:  [Autodesk.Revit.DB Solid](7a3b5ac1-c66d-9f81-a11d-9bcd4e026295.htm)    
     The first solid.

second
:   Type:  [Autodesk.Revit.DB Solid](7a3b5ac1-c66d-9f81-a11d-9bcd4e026295.htm)    
     The second solid

trf
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)   %    
     The offset transform

#### Return Value

True if they are identical, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__03ced8e5-beb5-1582-b43c-5a97b937578c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [SynchronizeWithCentralOptions Class](96eaf3af-971d-da6d-a857-88d6e602ffd4.htm)   [See Also](#seeAlsoToggle) |

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

[SynchronizeWithCentralOptions Class](96eaf3af-971d-da6d-a857-88d6e602ffd4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03cf479f-e57d-4fd5-79e6-557b274a7489.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PostWarning Method

---



|  |
| --- |
| [PerformanceAdviser Class](f9b0b017-f98f-79a3-ce7b-b1c867bb22f2.htm)   [See Also](#seeAlsoToggle) |

Reports a problem detected during execution of a rule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public void PostWarning( 	FailureMessage message ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub PostWarning ( _ 	message As FailureMessage _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void PostWarning( 	FailureMessage^ message ) ``` |

#### Parameters

message
:   Type:  [Autodesk.Revit.DB FailureMessage](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)    
     Warning describing the problem detected by a rule.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The message must have severity "warning". |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Performance advisor is not executing rules. |

# See Also

[PerformanceAdviser Class](f9b0b017-f98f-79a3-ce7b-b1c867bb22f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03d57de0-5d90-09fd-1ba8-7f71d2300639.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotDrawSingularSlantedWallError Property

---



|  |
| --- |
| [BuiltInFailures CreationFailures Class](62f22d53-ffd1-5c31-12c2-9bf34a79f079.htm)   [See Also](#seeAlsoToggle) |

Cannot create wall - it would intersect itself. Reduce the wall's height or slant.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotDrawSingularSlantedWallError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotDrawSingularSlantedWallError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotDrawSingularSlantedWallError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CreationFailures Class](62f22d53-ffd1-5c31-12c2-9bf34a79f079.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03da0af3-6e92-5117-143f-3f4cb3b98e24.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Append Method

---



|  |
| --- |
| [PhaseArray Class](a60fcff7-0295-3297-8784-ed09da99351a.htm)   [See Also](#seeAlsoToggle) |

Add the phase to the end of the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual void Append( 	Phase item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Sub Append ( _ 	item As Phase _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Append( 	Phase^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB Phase](ab01f390-a8e8-c21c-b2d0-6dd21056cdec.htm)    
     The phase to be added.

# See Also

[PhaseArray Class](a60fcff7-0295-3297-8784-ed09da99351a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03e28341-f219-8090-b3cf-df6ce44b3e47.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PanelMismatchDistSysWhenCircuitAssigned Property

---



|  |
| --- |
| [BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)   [See Also](#seeAlsoToggle) |

The selected circuit was added to panel [Element], but the distribution system for the panel does not match the power connector definition on the panel.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId PanelMismatchDistSysWhenCircuitAssigned { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PanelMismatchDistSysWhenCircuitAssigned As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ PanelMismatchDistSysWhenCircuitAssigned { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03e3b3d9-40bc-dda4-4d48-bf5fdc4b324d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [AnalyticalModelSelector Class](d286b023-8822-10ad-6702-53c86a6c9e70.htm)   [See Also](#seeAlsoToggle) |

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

[AnalyticalModelSelector Class](d286b023-8822-10ad-6702-53c86a6c9e70.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__03e4b6e9-9ae0-5b00-3b55-a14ad8323ebb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WeatherStationName Property

---



|  |
| --- |
| [SiteLocation Class](9d71159d-514c-c1b3-8673-5c0e7f28b688.htm)   [See Also](#seeAlsoToggle) |

The name of the weather station at the site location.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014 UR2

# Syntax

| C# |
| --- |
| ``` public string WeatherStationName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property WeatherStationName As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ WeatherStationName { 	String^ get (); } ``` |

# See Also

[SiteLocation Class](9d71159d-514c-c1b3-8673-5c0e7f28b688.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03e7af77-1c61-bc87-95d9-daa5d2ae8d23.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointAdaptiveOrientationType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Orients to"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PointAdaptiveOrientationType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PointAdaptiveOrientationType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PointAdaptiveOrientationType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03e84698-d122-594b-b436-4932f9ff49c6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, IList(Curve), Level, XYZ, Boolean)

---



|  |
| --- |
| [BeamSystem Class](6c5c1bd2-8456-5ec9-c53e-0bd3f604ad06.htm)   [See Also](#seeAlsoToggle) |

Creates a new BeamSystem with specified profile curves.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static BeamSystem Create( 	Document document, 	IList<Curve> profile, 	Level level, 	XYZ direction, 	bool is3d ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	profile As IList(Of Curve), _ 	level As Level, _ 	direction As XYZ, _ 	is3d As Boolean _ ) As BeamSystem ``` |

 

| Visual C++ |
| --- |
| ``` public: static BeamSystem^ Create( 	Document^ document,  	IList<Curve^>^ profile,  	Level^ level,  	XYZ^ direction,  	bool is3d ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which the new BeamSystem is created.

profile
:   Type:  System.Collections.Generic IList   [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The profile of the BeamSystem.

level
:   Type:  [Autodesk.Revit.DB Level](577e5d4e-a558-118c-9dea-3b810b061775.htm)    
     The level on which the BeamSystem is to be created. The work-plane of the BeamSystem will be the sketch plane associated with the Level. If there is no current sketch plane associated with the level yet, we will create a default one.

direction
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The direction is the direction of the BeamSystem.

is3d
:   Type:  System Boolean    
     Whether the BeamSystem is 3D. If the BeamSystem is 3D, the sketchPlane must be a level, otherwise an exception will be thrown.

#### Return Value

If successful, a new BeamSystem object will be returned.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input profile contains at least one helical curve and is not supported for this operation. -or- The input level does not have associated plan view. -or- The plan view associated with the input level is not valid. -or- Can not get valid sketch plane from the input level. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[BeamSystem Class](6c5c1bd2-8456-5ec9-c53e-0bd3f604ad06.htm)

[Create Overload](38e7211c-d61b-01fb-7c66-0fca146684a2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03ebe88a-a645-59c1-bde1-eb64a227e35f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarSystemAddlBottomOffset Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Additional Bottom Cover Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarSystemAddlBottomOffset { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarSystemAddlBottomOffset As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarSystemAddlBottomOffset { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03ee5975-6d93-f6d1-0c6f-ab31c0331f34.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDefault Property

---



|  |
| --- |
| [Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)   [See Also](#seeAlsoToggle) |

Indicates if the railing is the default one that system generates.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

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

[Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__03f088cc-a35b-74af-24f0-24399a9370b1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceArea Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Surface Area"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SurfaceArea { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SurfaceArea As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SurfaceArea { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03f1bce3-dd39-9deb-c732-db82474cb40b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCVersion Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing available IFC file versions into which a file may be exported.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public enum IFCVersion ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration IFCVersion ``` |

 

| Visual C++ |
| --- |
| ``` public enum class IFCVersion ``` |

# Members

| Member name | Description |
| --- | --- |
| Default | The Autodesk Revit application's default export format. Note that this may change as the defaults change in the Revit user interface. |
| IFCBCA | IFC BCA file format. This is a certified variant of IFC 2x2 used for submitting files to the Singapore BCA ePlan Check Server. |
| IFC2x2 | IFC 2x2 file format. |
| IFC2x3 | IFC 2x3 file format. |
| IFCCOBIE | IFC GSA COBIE 2010 file format. This is a variant of IFC 2x3 used for submitting files that are COBIE 2010-complaint. |
| IFC2x3CV2 | IFC 2x3 Coordination View 2.0 file format. This is a variant of IFC 2x3 used for exporting files using the Coordination View 2.0 model view. |
| IFC4 | IFC 4 file format. |
| IFC2x3FM | IFC2x3 Extended FM Handover View |
| IFC4RV | IFC4 Reference View |
| IFC4DTV | IFC4 Design Transfer View |
| IFC2x3BFM | IFC2x3 Basic FM Handover View |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__03f384b6-7a50-15c9-aed0-ab39d18c6b52.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SillHeight Property

---



|  |
| --- |
| [MassSurfaceData Class](69fcb13c-6443-d1c2-29d5-08adc1261afd.htm)   [See Also](#seeAlsoToggle) |

The height above the level where the bottoms of auto-generated windows will be located.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double SillHeight { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SillHeight As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double SillHeight { 	double get (); 	void set (double value); } ``` |

# Remarks

Will be accurate unless the target glazing percentage cannot be achieved using this height. In that case, the sillHeight will be ignored and windows will be created below this height.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The sill height is less than zero. |

# See Also

[MassSurfaceData Class](69fcb13c-6443-d1c2-29d5-08adc1261afd.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__065e52f3-c115-160a-c681-51e5a78e956b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsDataPanelSchedule Property

---



|  |
| --- |
| [PanelScheduleTemplate Class](cf7e5cbb-7df4-ae55-8178-f449827b5752.htm)   [See Also](#seeAlsoToggle) |

Checks to see if this object is data panel schedule template element.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsDataPanelSchedule { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsDataPanelSchedule As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsDataPanelSchedule { 	bool get (); } ``` |

# See Also

[PanelScheduleTemplate Class](cf7e5cbb-7df4-ae55-8178-f449827b5752.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__066be9de-edf8-4d48-c80f-f289e85866c4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceName Property

---



|  |
| --- |
| [EnergyAnalysisSurface Class](72ef40eb-20ae-d7ef-0ab5-8c52ddd4b813.htm)   [See Also](#seeAlsoToggle) |

The unique name identifier for this surface.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public string SurfaceName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property SurfaceName As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ SurfaceName { 	String^ get (); } ``` |

# Remarks

Surface and Opening elements get an Name element assigned according to the below described schema:

(Orientation)(Space#)[(Other space#)](Exposure)(Type)-(sequence number)[Opening Type+#]

Sample: N-101-102-E-W-O-77

* N = Orientation [N/NE/E/SE/S/SW/W/NW/N/T/B/X] (every surface within the sector of 22.5 degrees from the north vector gets the letter N etc) (horizontal surfaces facing upwards get the letter T for top, downwards B for bottom) (shading surfaces get the letter X for differentiation).
* 101 = Space number.
* 102 = Other space number.
* E = Exposure - exterior/interior/underground [E/I/U].
* W = Type [W/C/R/F] (Wall, Roof, Ceiling, Floor, Shade) (every surface type has it's letter W-Wall R-Roof C-Ceiling F-Floor S-Shade).
* O = Opening Type [W/D/O] (Window, Door, Opening) (every opening type has it's letter W-Window D-Door O-Opening).
* 77 = sequence number.

Sample surface names:

* N-101-E-W-84 North facing Exterior Wall #84 in space 101.
* N-101-E-W-84-D-1 Door #1 in North facing Exterior Wall #84 in space 101.
* E-101-102-I-W-92 Vertical Interior Wall #92 between space 101 and 102.
* T-101-E-R-141 Top facing Exterior Roof #141 in space 101.
* B-101-201-I-F-88 Bottom facing Interior Floor #88 between space 101 and 201.
* X-73 Shade #73.

# See Also

[EnergyAnalysisSurface Class](72ef40eb-20ae-d7ef-0ab5-8c52ddd4b813.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__066eb6e5-eba3-0885-d4a8-da1ade8722cc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InchesPerSecondSquared Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Inches per second squared.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId InchesPerSecondSquared { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InchesPerSecondSquared As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ InchesPerSecondSquared { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__067e75f2-193d-f347-94ca-601173767605.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Index Property

---



|  |
| --- |
| [DuctFittingAndAccessoryConnectorData Class](ffb25c4f-cd7a-bd51-8f78-3107a0955fc9.htm)   [See Also](#seeAlsoToggle) |

return the index of this connector

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public int Index { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Index As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int Index { 	int get (); } ``` |

# See Also

[DuctFittingAndAccessoryConnectorData Class](ffb25c4f-cd7a-bd51-8f78-3107a0955fc9.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__068a23bd-bc73-2090-f607-ea1b5e4612dd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MassSubCategoryId Property

---



|  |
| --- |
| [ConceptualSurfaceType Class](b79ddf97-2888-ceda-a2c4-222dab08163e.htm)   [See Also](#seeAlsoToggle) |

The mass subcategory id of the ConceptualSurfaceType.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementId MassSubCategoryId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property MassSubCategoryId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ MassSubCategoryId { 	ElementId^ get (); } ``` |

# See Also

[ConceptualSurfaceType Class](b79ddf97-2888-ceda-a2c4-222dab08163e.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__068a4e61-858f-e6cd-256b-1fee54a8c49a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExtensibleStorageFilter Constructor

---



|  |
| --- |
| [ExtensibleStorageFilter Class](81cb1798-3dbe-658b-5a04-d97aa2cb4de9.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to match elements with extensible storage data based on specific Schema id.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ExtensibleStorageFilter( 	Guid schemaGuid ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	schemaGuid As Guid _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ExtensibleStorageFilter( 	Guid schemaGuid ) ``` |

#### Parameters

schemaGuid
:   Type:  [System Guid](http://msdn2.microsoft.com/en-us/library/cey1zx63)    
     Schema id used to filter elements with extensible storage data

# See Also

[ExtensibleStorageFilter Class](81cb1798-3dbe-658b-5a04-d97aa2cb4de9.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)

<!-- Start of Syntax__068d7bed-c2cf-4ad1-9a30-73b3d9d7a649.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecLoadsummaryLoadclassificationParam Property

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
| ``` public static ForgeTypeId RbsElecLoadsummaryLoadclassificationParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecLoadsummaryLoadclassificationParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecLoadsummaryLoadclassificationParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__069c7b48-6de8-cc34-ff95-65ac7db08f66.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RailingCurvesNotSplitRamp Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

The slope of this railing will not parallel the ramp at landings. To get a parallel railing, split the railing sketch at the ends of landings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RailingCurvesNotSplitRamp { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RailingCurvesNotSplitRamp As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RailingCurvesNotSplitRamp { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__070a03d1-c33d-fc17-324e-60f727fcfb3c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetScans Method

---



|  |
| --- |
| [PointCloudInstance Class](d17686cb-b8c5-bee5-44d3-0311d27678e0.htm)   [See Also](#seeAlsoToggle) |

Returns array of scan names.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public IList<string> GetScans() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetScans As IList(Of String) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<String^>^ GetScans() ``` |

#### Return Value

Resulting array of scan names.

# See Also

[PointCloudInstance Class](d17686cb-b8c5-bee5-44d3-0311d27678e0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__070af608-cb1e-43d5-f3ca-6d53150f9dbb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Action Property

---



|  |
| --- |
| [IFCImportOptions Class](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)   [See Also](#seeAlsoToggle) |

The action of the import.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IFCImportAction Action { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Action As IFCImportAction 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property IFCImportAction Action { 	IFCImportAction get (); 	void set (IFCImportAction value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[IFCImportOptions Class](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__070c2d73-9a6d-3840-b149-b82bb87d4ed3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewAreaBoundaryConditions Method (Reference, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double)

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new Area BoundaryConditions element on a reference.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public BoundaryConditions NewAreaBoundaryConditions( 	Reference reference, 	TranslationRotationValue X_Translation, 	double X_TranslationSpringModulus, 	TranslationRotationValue Y_Translation, 	double Y_TranslationSpringModulus, 	TranslationRotationValue Z_Translation, 	double Z_TranslationSpringModulus ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewAreaBoundaryConditions ( _ 	reference As Reference, _ 	X_Translation As TranslationRotationValue, _ 	X_TranslationSpringModulus As Double, _ 	Y_Translation As TranslationRotationValue, _ 	Y_TranslationSpringModulus As Double, _ 	Z_Translation As TranslationRotationValue, _ 	Z_TranslationSpringModulus As Double _ ) As BoundaryConditions ``` |

 

| Visual C++ |
| --- |
| ``` public: BoundaryConditions^ NewAreaBoundaryConditions( 	Reference^ reference,  	TranslationRotationValue X_Translation,  	double X_TranslationSpringModulus,  	TranslationRotationValue Y_Translation,  	double Y_TranslationSpringModulus,  	TranslationRotationValue Z_Translation,  	double Z_TranslationSpringModulus ) ``` |

#### Parameters

reference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The Geometry reference obtained from a Wall, Slab or Slab Foundation.

X\_Translation
:   Type:  [Autodesk.Revit.DB.Structure TranslationRotationValue](0b6cf7fa-b211-2f21-98a0-4f4e0fe2ca0e.htm)    
     A value indicating the X axis translation option.

X\_TranslationSpringModulus
:   Type:  System Double    
     Translation Spring Modulus for X axis. Ignored if X\_Translation is not "Spring".

Y\_Translation
:   Type:  [Autodesk.Revit.DB.Structure TranslationRotationValue](0b6cf7fa-b211-2f21-98a0-4f4e0fe2ca0e.htm)    
     A value indicating the Y axis translation option.

Y\_TranslationSpringModulus
:   Type:  System Double    
     Translation Spring Modulus for Y axis. Ignored if Y\_Translation is not "Spring".

Z\_Translation
:   Type:  [Autodesk.Revit.DB.Structure TranslationRotationValue](0b6cf7fa-b211-2f21-98a0-4f4e0fe2ca0e.htm)    
     A value indicating the Z axis translation option.

Z\_TranslationSpringModulus
:   Type:  System Double    
     Translation Spring Modulus for Z axis. Ignored if Z\_Translation is not "Spring".

#### Return Value

If successful, NewAreaBoundaryConditions returns an object for the newly created BoundaryConditions with the BoundaryType = 2 - "Area".    a null reference (  Nothing  in Visual Basic)  is returned if the operation fails.

# Remarks

This method will only function with the Autodesk Revit Structure application.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
bool CreateAreaConditionWithReference(AnalyticalPanel wall, Autodesk.Revit.Creation.Document docCreation)
{
   // Get the Geometry reference to the wall
   Reference profileReference = null;
   if (null == wall)
   {
      return false; // the profile reference can't be retrieved.
   }

   // loop through the curves of the wall and get the first one as a reference
   foreach (Curve curve in wall.GetOuterContour())
   {
      AnalyticalModelSelector selector = new AnalyticalModelSelector(curve);

      profileReference = wall.GetReference(selector);
      if (null != profileReference)
      {
         break;
      }
   }
   BoundaryConditions condition = null;
   // Create the Area Boundary Conditions if we have a profileReference
   if (null != profileReference)
   {
      // Create Area Boundary Conditions with profile reference.
      condition = docCreation.NewAreaBoundaryConditions(profileReference, TranslationRotationValue.Fixed, 0,
                                                                          TranslationRotationValue.Fixed, 0,
                                                                          TranslationRotationValue.Fixed, 0);
   }
   return (null != condition);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Function CreateAreaConditionWithReference(wall As Wall, docCreation As Autodesk.Revit.Creation.Document) As Boolean
   ' Get the Geometry reference to the wall
   Dim profileReference As Reference = Nothing
   Dim document As Document = wall.Document
   Dim analytical As Autodesk.Revit.DB.Structure.AnalyticalPanel = Nothing
   Dim relManager As Autodesk.Revit.DB.Structure.AnalyticalToPhysicalAssociationManager = Autodesk.Revit.DB.Structure.AnalyticalToPhysicalAssociationManager.GetAnalyticalToPhysicalAssociationManager(document)

   If (relManager Is Nothing) Then
      Return False
   End If

   Dim counterpartId As ElementId = relManager.GetAssociatedElementId(wall.Id)
   If (counterpartId Is Nothing) Then
      Return False
   End If

   analytical = document.GetElement(counterpartId)
   If analytical Is Nothing Then
      ' the profile reference can't be retrieved.
      Return False
   End If

   ' loop through the curves of the wall and get the first one as a reference
   For Each curve As Curve In analytical.GetOuterContour().ToList()
      profileReference = curve.Reference
      If profileReference IsNot Nothing Then
         Exit For
      End If
   Next

   Dim condition As BoundaryConditions = Nothing
   ' Create the Area Boundary Conditions if we have a profileReference
   If profileReference IsNot Nothing Then
      ' Create Area Boundary Conditions with profile reference.
      condition = docCreation.NewAreaBoundaryConditions(profileReference, TranslationRotationValue.Fixed, 0, TranslationRotationValue.Fixed, 0, TranslationRotationValue.Fixed,
              0)
   End If
   Return (condition IsNot Nothing)
End Function
```

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[NewAreaBoundaryConditions Overload](935e002a-ac38-a936-6f06-3a16689b4c3a.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__070dab89-fd61-a3b2-8111-57c63430ab9a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### KgPerM Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol kg/m, indicating unit Kilograms per meter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId KgPerM { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property KgPerM As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ KgPerM { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__071adb98-310b-3b6a-acc2-e98d9c94771f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSelectedElementIds Method

---



|  |
| --- |
| [NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)   [See Also](#seeAlsoToggle) |

Returns the element ids of the elements to export. Empty by default.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> GetSelectedElementIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSelectedElementIds As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ GetSelectedElementIds() ``` |

# See Also

[NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__071ca21c-4867-72cf-d0ce-c412efe248c5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RungSpace Property

---



|  |
| --- |
| [CableTray Class](86d92fdc-69d4-ce86-5222-8cc2a8073132.htm)   [See Also](#seeAlsoToggle) |

Distance between two rungs for the ladder cable tray.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double RungSpace { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RungSpace As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double RungSpace { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The rung space value should be at least equal to or larger than rang width which is 1 inch. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[CableTray Class](86d92fdc-69d4-ce86-5222-8cc2a8073132.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__071d17b9-da93-a2b9-6435-4f886da3759a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RadiansPerSecond Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Radians per second.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RadiansPerSecond { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RadiansPerSecond As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RadiansPerSecond { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__071f6ca9-f243-4655-924c-7beb881b100f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clone Method

---



|  |
| --- |
| [Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)   [See Also](#seeAlsoToggle) |

Returns a copy of this curve.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Curve Clone() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Clone As Curve ``` |

 

| Visual C++ |
| --- |
| ``` public: Curve^ Clone() ``` |

#### Return Value

A copy of this curve.

# See Also

[Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f06036b-8970-0638-470d-379ebd30b46e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsMasking Property

---



|  |
| --- |
| [FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.htm)   [See Also](#seeAlsoToggle) |

Indicates whether this element is a 'Filled Region or a 'Masking Region'.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsMasking { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsMasking As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsMasking { 	bool get (); } ``` |

# See Also

[FilledRegion Class](3685651c-a789-3550-f6bb-7c1decc29079.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f060c6b-ec06-aced-2898-7fcd1bf2f522.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [TransmissionData Class](d78d1e9c-1cee-1336-88d5-b605dacd077d.htm)   [See Also](#seeAlsoToggle) |

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

[TransmissionData Class](d78d1e9c-1cee-1336-88d5-b605dacd077d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f099ebb-ef3b-4502-835f-349a10efb04b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectPipePlaceholdersAtCross Method (Document, Connector, Connector, Connector, Connector)

---



|  |
| --- |
| [PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.htm)   [See Also](#seeAlsoToggle) |

Connects placeholders that looks like Cross connection.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool ConnectPipePlaceholdersAtCross( 	Document document, 	Connector connector1, 	Connector connector2, 	Connector connector3, 	Connector connector4 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ConnectPipePlaceholdersAtCross ( _ 	document As Document, _ 	connector1 As Connector, _ 	connector2 As Connector, _ 	connector3 As Connector, _ 	connector4 As Connector _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ConnectPipePlaceholdersAtCross( 	Document^ document,  	Connector^ connector1,  	Connector^ connector2,  	Connector^ connector3,  	Connector^ connector4 ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

connector1
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The first end connector of placeholder to be connected to the second.

connector2
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The second end connector of placeholder to be connected to the first.

connector3
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The third end connector of placeholder to be connected to the forth.

connector4
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The fourth end connector of placeholder to be connected to the third.

#### Return Value

True if connection succeeds, false otherwise.

# Remarks

The placeholders may or may not have physical connection. However a) The ends of four connectors should intersect at same point; b) the first and second placeholders should be collinear each other; c) the third and fourth placeholders should be collinear each other and d) the third and fourth should have intersection with first or second placeholder. If connection fails, the placeholders cannot be physically connected.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The owner of connector is not pipe placeholder. -or- The owners of connectors belong to different types of system. -or- The curves of connector1 and connector2 are not collinear or either the connecto1 or connector2 is not connector of curve end. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.htm)

[ConnectPipePlaceholdersAtCross Overload](7635724a-038c-577c-fbf5-f00e365ffded.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__2f170ed9-52a0-88a1-f972-f237859ee8bf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetTransparency Method

---



|  |
| --- |
| [ColorWithTransparency Class](b68f80e1-5ea0-a485-ec3e-7dd077043230.htm)   [See Also](#seeAlsoToggle) |

get transparency

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public uint GetTransparency() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetTransparency As UInteger ``` |

 

| Visual C++ |
| --- |
| ``` public: unsigned int GetTransparency() ``` |

#### Return Value

transparency

# See Also

[ColorWithTransparency Class](b68f80e1-5ea0-a485-ec3e-7dd077043230.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f223fde-0e7c-fce5-e68f-3c1ca6a6b6c1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### JoinGeometry Method

---



|  |
| --- |
| [JoinGeometryUtils Class](c45b6484-3efd-1d81-0b47-ba678857fff1.htm)   [See Also](#seeAlsoToggle) |

Creates clean joins between two elements that share a common face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static void JoinGeometry( 	Document document, 	Element firstElement, 	Element secondElement ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub JoinGeometry ( _ 	document As Document, _ 	firstElement As Element, _ 	secondElement As Element _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void JoinGeometry( 	Document^ document,  	Element^ firstElement,  	Element^ secondElement ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the two elements.

firstElement
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The first element to be joined.

secondElement
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The second element to be joined. This element must not be joined to the first element.

# Remarks

The visible edge between joined elements is removed. The joined elements then share the same line weight and fill pattern. This functionality is not available for family documents.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- The element firstElement was not found in the given document. -or- The element secondElement was not found in the given document. -or- The elements are already joined. -or- The elements cannot be joined. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Please remove or add segments on curtain grids instead of joining or unjoining geometry of the panels. |

# See Also

[JoinGeometryUtils Class](c45b6484-3efd-1d81-0b47-ba678857fff1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f270626-e056-8b73-c3d1-640fdf3a9f98.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RailingSystemSegmentVGrid Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"V Grid"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RailingSystemSegmentVGrid { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RailingSystemSegmentVGrid As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RailingSystemSegmentVGrid { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f291187-825d-fb60-cd4a-33280dce91e4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetDeckEmbeddingType Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Sets the deck embedding type to use for the specified structural deck.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetDeckEmbeddingType( 	int layerIdx, 	StructDeckEmbeddingType embedType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetDeckEmbeddingType ( _ 	layerIdx As Integer, _ 	embedType As StructDeckEmbeddingType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetDeckEmbeddingType( 	int layerIdx,  	StructDeckEmbeddingType embedType ) ``` |

#### Parameters

layerIdx
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index of a layer in the CompoundStructure.

embedType
:   Type:  [Autodesk.Revit.DB StructDeckEmbeddingType](2cc96ee3-bb7b-26e8-271c-25975dbc9fc4.htm)    
     The embedding type to be used by the specified layer if it is a structural deck.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The layer is not a structural deck. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. -or- A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f301670-4ef0-22ee-9e3b-1541b33edba2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportExtrudedSlabOpenings Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static void ExportExtrudedSlabOpenings( 	ExporterIFC exporterIFC, 	Element pElem, 	IFCLevelInfo levelInfo, 	IFCAnyHandle localPlacementAny, 	IList<IFCAnyHandle> elementSlabAnyArr, 	IList<IList<CurveLoop>> extrusionLoops, 	Plane plane, 	IFCProductWrapper pWrapper ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub ExportExtrudedSlabOpenings ( _ 	exporterIFC As ExporterIFC, _ 	pElem As Element, _ 	levelInfo As IFCLevelInfo, _ 	localPlacementAny As IFCAnyHandle, _ 	elementSlabAnyArr As IList(Of IFCAnyHandle), _ 	extrusionLoops As IList(Of IList(Of CurveLoop)), _ 	plane As Plane, _ 	pWrapper As IFCProductWrapper _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void ExportExtrudedSlabOpenings( 	ExporterIFC^ exporterIFC,  	Element^ pElem,  	IFCLevelInfo^ levelInfo,  	IFCAnyHandle^ localPlacementAny,  	IList<IFCAnyHandle^>^ elementSlabAnyArr,  	IList<IList<CurveLoop^>^>^ extrusionLoops,  	Plane^ plane,  	IFCProductWrapper^ pWrapper ) ``` |

#### Parameters

exporterIFC
:   Type:  [Autodesk.Revit.DB.IFC ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.htm)

pElem
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

levelInfo
:   Type:  [Autodesk.Revit.DB.IFC IFCLevelInfo](9f287338-fe0c-383b-58be-39105d704a9f.htm)

localPlacementAny
:   Type:  [Autodesk.Revit.DB.IFC IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)

elementSlabAnyArr
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [IFCAnyHandle](8b893943-70fa-94bf-90be-1523d516ecb3.htm)

extrusionLoops
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

plane
:   Type:  [Autodesk.Revit.DB Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)

pWrapper
:   Type:  [Autodesk.Revit.DB.IFC IFCProductWrapper](368d2c50-1258-32a9-00ed-cc41059a6694.htm)

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__2f336e46-1aa3-1a9a-9482-f8587aed1a86.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFlangeThicknessInQuarterWidth Method

---



|  |
| --- |
| [StructuralSectionGeneralT Class](308dc954-e403-b95c-3f1c-3a9a4c22beaf.htm)   [See Also](#seeAlsoToggle) |

Returns thickness of flange measured in the 0.25 \* width, sometimes used for sections with width <= 300 mm.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public double GetFlangeThicknessInQuarterWidth() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFlangeThicknessInQuarterWidth As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetFlangeThicknessInQuarterWidth() ``` |

# See Also

[StructuralSectionGeneralT Class](308dc954-e403-b95c-3f1c-3a9a4c22beaf.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__2f346b3e-3cf6-f529-80f1-15a33f406519.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [PhaseFilter Class](3236c80e-48be-f657-951f-70490a43f065.htm)   [See Also](#seeAlsoToggle) |

Creates a new phase filter with default status presentation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static PhaseFilter Create( 	Document document, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	name As String _ ) As PhaseFilter ``` |

 

| Visual C++ |
| --- |
| ``` public: static PhaseFilter^ Create( 	Document^ document,  	String^ name ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

name
:   Type:  System String    
     The name.

#### Return Value

The newly created phase filter.

# Remarks

The default status presentation is ShowByCategory for New status, and ShowOverriden for Existing, Demolished and Temporary statuses.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | name is already in use. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PhaseFilter Class](3236c80e-48be-f657-951f-70490a43f065.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f362523-5fa1-fa99-cd88-fb3cf70a3602.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Insert Method

---



|  |
| --- |
| [AssetSet Class](b76daaec-4e96-af6c-336f-7ad9eba6ac82.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool Insert( 	Asset item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Insert ( _ 	item As Asset _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Insert( 	Asset^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB.Visual Asset](598e104b-b6ec-9ebe-7a93-ec96b8cbeba9.htm)

# See Also

[AssetSet Class](b76daaec-4e96-af6c-336f-7ad9eba6ac82.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__2f372d5c-9de2-0c8e-80fc-19292bac58e3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlertColor Property

---



|  |
| --- |
| [ColorOptions Class](1ca57d8c-b970-83b4-c5ce-9e39464e5cc2.htm)   [See Also](#seeAlsoToggle) |

The color used to highlight elements when a special alert is required.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public Color AlertColor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AlertColor As Color 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Color^ AlertColor { 	Color^ get (); 	void set (Color^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ColorOptions Class](1ca57d8c-b970-83b4-c5ce-9e39464e5cc2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f414a57-3e73-8453-4e27-b19eb4f599d4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DpartShapeModified Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Shape is modified"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DpartShapeModified { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DpartShapeModified As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DpartShapeModified { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f446ef4-c568-8081-a33c-2bc0e6291484.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetResolutionCaption Method

---



|  |
| --- |
| [FailureDefinitionAccessor Class](2abf9897-5ebf-a3bc-d40f-46632b0159fc.htm)   [See Also](#seeAlsoToggle) |

Retrieves the caption for a specific resolution type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string GetResolutionCaption( 	FailureResolutionType type ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetResolutionCaption ( _ 	type As FailureResolutionType _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetResolutionCaption( 	FailureResolutionType type ) ``` |

#### Parameters

type
:   Type:  [Autodesk.Revit.DB FailureResolutionType](786e6422-f66d-5320-99f9-e530819e50a1.htm)    
     The resolution type.

#### Return Value

The caption of the resolution.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Resolution of the type is not applicable to the failure. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The FailureDefinitionAccessor has not been properly initialized. -or- FailureDefinition does not have any resolutions. |

# See Also

[FailureDefinitionAccessor Class](2abf9897-5ebf-a3bc-d40f-46632b0159fc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f46508b-4646-b32e-e391-0f1cbf733243.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Insert Method

---



|  |
| --- |
| [SlabShapeVertexArray Class](ce947cf3-a5a8-43d7-49c7-3a1961ad7407.htm)   [See Also](#seeAlsoToggle) |

Insert the specified item into the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual void Insert( 	SlabShapeVertex item, 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Sub Insert ( _ 	item As SlabShapeVertex, _ 	index As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Insert( 	SlabShapeVertex^ item,  	int index ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB SlabShapeVertex](8c022b91-723f-045d-3024-8cb037a41acc.htm)    
     The item to be inserted into the array.

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The item will be inserted before this index.

#### Return Value

Returns whether the item was inserted into the array.

# See Also

[SlabShapeVertexArray Class](ce947cf3-a5a8-43d7-49c7-3a1961ad7407.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f482b62-410e-2db9-b6b9-c64abedcbc4c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentSaved Event

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the DocumentSaved event to be notified immediately after Revit has finished saving a document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
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

This event is raised immediately after Revit has finished saving a document. Note that the first save of a newly created document will raise  [DocumentSavedAs](7ace570d-870f-be20-e493-e80ffa27f454.htm)  rather than the DocumentSaved event. It is raised even when document saving failed or was cancelled (during DocumentSaving event).

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Check the 'Status' property in event's argument to see whether the action itself was successful or not.

This event is not cancellable, for the process of saving document has already been finished.

The following API functions are not available for the current document during this event:

* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  .
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f488ba7-d289-aaef-ae8d-156e5a564142.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundaryYRotationFixed Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Y Rotation - Fixed"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BoundaryYRotationFixed { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BoundaryYRotationFixed As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BoundaryYRotationFixed { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f5031a2-f07c-761d-2f88-c16674b070a7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StretchAndFit Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Stretch the fabrication part from the specified connector and fit to the target routing end.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static FabricationPartFitResult StretchAndFit( 	Document document, 	Connector stretchConnector, 	FabricationPartRouteEnd target, 	out ISet<ElementId> newPartIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function StretchAndFit ( _ 	document As Document, _ 	stretchConnector As Connector, _ 	target As FabricationPartRouteEnd, _ 	<OutAttribute> ByRef newPartIds As ISet(Of ElementId) _ ) As FabricationPartFitResult ``` |

 

| Visual C++ |
| --- |
| ``` public: static FabricationPartFitResult StretchAndFit( 	Document^ document,  	Connector^ stretchConnector,  	FabricationPartRouteEnd^ target,  	[OutAttribute] ISet<ElementId^>^% newPartIds ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to perform the stretch and fit.

stretchConnector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The connector of the fabrication part to be stretched.

target
:   Type:  [Autodesk.Revit.DB.Fabrication FabricationPartRouteEnd](58bd199f-5114-67de-011b-d054a1a4c4d9.htm)    
     The target routing end to align and fit to.

newPartIds
:   Type:  System.Collections.Generic ISet   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)   %    
     New fabrication part element identifiers.

#### Return Value

Returns FabricationPartFitResult::Success if successful.

# Remarks

Cannot stretch and fit fabrication part straight, tap or hanger.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Connector does not belong to a fabrication part with a valid fabrication service. -or- Connector is connected. -or- Connector belongs to a fabrication part straight, tap or hanger. -or- routing end is valid to route to. -or- stretch target end type must be a supported type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | fabrication part is not connected at one end only. -or- cannot stretch fabrication part to a different service. |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f52924c-8851-6512-c2b0-28205a799c21.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetValue Method (Int32)

---



|  |
| --- |
| [ScheduleFilter Class](a5dfec9f-1efd-b507-d079-eabcbf5032f8.htm)   [See Also](#seeAlsoToggle) |

Set the filter value to an integer.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetValue( 	int value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetValue ( _ 	value As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetValue( 	int value ) ``` |

#### Parameters

value
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The filter value.

# See Also

[ScheduleFilter Class](a5dfec9f-1efd-b507-d079-eabcbf5032f8.htm)

[SetValue Overload](ea4c058c-08df-494d-3521-dccfed636c3d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f59330d-a69d-a78b-e364-f22b087960ef.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HideCategoriesTemporary Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Set multiple categories to be temporarily hidden in the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void HideCategoriesTemporary( 	ICollection<ElementId> elementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub HideCategoriesTemporary ( _ 	elementIds As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void HideCategoriesTemporary( 	ICollection<ElementId^>^ elementIds ) ``` |

#### Parameters

elementIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Ids of the categories to be hidden

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Some elements in elementIds do not correspond to a Category. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f61c3d3-efc3-4858-1f18-e89fa2048a12.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Percentage Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Percentage.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Percentage { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Percentage As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Percentage { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f687142-fdc9-f422-c904-c7705bec7331.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CategoryId2 Property

---



|  |
| --- |
| [AssemblyMemberDifferentCategory Class](e244624d-2bdb-ded8-dfcc-255259880dc6.htm)   [See Also](#seeAlsoToggle) |

Category id of the second assembly member

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementId CategoryId2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property CategoryId2 As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ CategoryId2 { 	ElementId^ get (); } ``` |

# See Also

[AssemblyMemberDifferentCategory Class](e244624d-2bdb-ded8-dfcc-255259880dc6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f706aa4-5138-e192-b928-9a3388ab7b60.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Value Property

---



|  |
| --- |
| [ElementIdParameterValue Class](7de25c99-4f85-ef1d-7f64-74092f963c98.htm)   [See Also](#seeAlsoToggle) |

The stored value

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public ElementId Value { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Value As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ Value { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ElementIdParameterValue Class](7de25c99-4f85-ef1d-7f64-74092f963c98.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f707487-817c-d648-4b99-559f9000f123.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateElevationMarker Method

---



|  |
| --- |
| [ElevationMarker Class](ca59d2f7-4cd0-d13d-22a0-c153ac8310d4.htm)   [See Also](#seeAlsoToggle) |

Creates a new ElevationMarker.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ElevationMarker CreateElevationMarker( 	Document document, 	ElementId viewFamilyTypeId, 	XYZ origin, 	int initialViewScale ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateElevationMarker ( _ 	document As Document, _ 	viewFamilyTypeId As ElementId, _ 	origin As XYZ, _ 	initialViewScale As Integer _ ) As ElevationMarker ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElevationMarker^ CreateElevationMarker( 	Document^ document,  	ElementId^ viewFamilyTypeId,  	XYZ^ origin,  	int initialViewScale ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to which the new ElevationMarker will be added.

viewFamilyTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     This ViewFamilyType will be used by all elevations hosted on the new ElevationMarker.

origin
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The desired origin for the ElevationMarker.

initialViewScale
:   Type:  System Int32    
     This view scale will be automatically applied to new elevations created on the ElevationMarker. The scale is the ratio of true model size to paper size.

#### Return Value

The new ElevationMarker.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This view family type is not appropriate for ElevationMarkers. -or- The denominator X of the view scale 1/X must be in the range 1 to 24,000. -or- Elevation view creation is not allowed in this family. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElevationMarker Class](ca59d2f7-4cd0-d13d-22a0-c153ac8310d4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f712219-70a9-76f0-6f10-36ea98f72a14.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPartCustomDataReal Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Set the custom data real value for the specified custom data.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void SetPartCustomDataReal( 	int customId, 	double value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetPartCustomDataReal ( _ 	customId As Integer, _ 	value As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetPartCustomDataReal( 	int customId,  	double value ) ``` |

#### Parameters

customId
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The identifier of the custom data field to set.

value
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The real value of the custom data. If the data is not a real type the value will be parsed according to the fabrication confifuration rules.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The custom data does not exist on the part. |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f7248a7-de59-7352-e8ed-38dfc386b5ab.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UpperRange Property

---



|  |
| --- |
| [ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)   [See Also](#seeAlsoToggle) |

Upper part of progress bar range - will be any non-zero number

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public int UpperRange { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property UpperRange As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int UpperRange { 	int get (); } ``` |

# See Also

[ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__2f79fff4-9773-471a-83f8-5636459bdbe5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StringParameterValue Class

---



|  |
| --- |
| [Members](867a09bc-428b-adfa-023b-1f03f169863b.htm)   [See Also](#seeAlsoToggle) |

A class that holds a String value of a parameter element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public class StringParameterValue : ParameterValue ``` |

 

| Visual Basic |
| --- |
| ``` Public Class StringParameterValue _ 	Inherits ParameterValue ``` |

 

| Visual C++ |
| --- |
| ``` public ref class StringParameterValue : public ParameterValue ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ParameterValue](366521ef-ecc2-c3e3-feb5-81b3bbd8df0c.htm)    
  Autodesk.Revit.DB StringParameterValue

# See Also

[StringParameterValue Members](867a09bc-428b-adfa-023b-1f03f169863b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f83a170-9a16-20b2-a726-6718b5cf196b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DimLabel Property

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
| ``` public static ForgeTypeId DimLabel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DimLabel As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DimLabel { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f85517f-3076-bd03-5e3a-9eb708b77ca9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsInMultistoryExceedTopConstraint Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Stairs in MultistoryStairs after adjusting still exceed the top constraint.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId StairsInMultistoryExceedTopConstraint { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsInMultistoryExceedTopConstraint As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ StairsInMultistoryExceedTopConstraint { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f8676a8-5b07-cbd7-e364-826719ab97ca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBoundingBox Method

---



|  |
| --- |
| [GeometryElement Class](09eaeb08-58bb-8049-8925-f3a5aa846fdc.htm)   [See Also](#seeAlsoToggle) |

Retrieves a box that encloses the geometry element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public BoundingBoxXYZ GetBoundingBox() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBoundingBox As BoundingBoxXYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: BoundingBoxXYZ^ GetBoundingBox() ``` |

#### Return Value

The bounding box.

# See Also

[GeometryElement Class](09eaeb08-58bb-8049-8925-f3a5aa846fdc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f888fc9-ecf5-25d3-ba0e-06351c07609b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetOuterContour Method

---



|  |
| --- |
| [AnalyticalSurfaceBase Class](9cad2b9c-a5d2-f434-2d9a-3c9183a55ada.htm)   [See Also](#seeAlsoToggle) |

Returns the Curve Loop that defines the geometry of the Analytical Surface element.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public CurveLoop GetOuterContour() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetOuterContour As CurveLoop ``` |

 

| Visual C++ |
| --- |
| ``` public: CurveLoop^ GetOuterContour() ``` |

#### Return Value

CurveLoop associated with Analytical Surface element.

# See Also

[AnalyticalSurfaceBase Class](9cad2b9c-a5d2-f434-2d9a-3c9183a55ada.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__2f9010d5-2f50-5df3-03e1-50658f74e030.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReleaseConditions Constructor (Boolean, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean)

---



|  |
| --- |
| [ReleaseConditions Class](f742770e-6b65-f237-5851-ccdf16cfc1b5.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of ReleaseConditions.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public ReleaseConditions( 	bool start, 	bool fx, 	bool fy, 	bool fz, 	bool mx, 	bool my, 	bool mz ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	start As Boolean, _ 	fx As Boolean, _ 	fy As Boolean, _ 	fz As Boolean, _ 	mx As Boolean, _ 	my As Boolean, _ 	mz As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ReleaseConditions( 	bool start,  	bool fx,  	bool fy,  	bool fz,  	bool mx,  	bool my,  	bool mz ) ``` |

#### Parameters

start
:   Type:  System Boolean    
     The position on analytical element. True for start, false for end.

fx
:   Type:  System Boolean    
     Fx of the release type.

fy
:   Type:  System Boolean    
     Fy of the release type.

fz
:   Type:  System Boolean    
     Fz of the release type.

mx
:   Type:  System Boolean    
     Mx of the release type.

my
:   Type:  System Boolean    
     My of the release type.

mz
:   Type:  System Boolean

# See Also

[ReleaseConditions Class](f742770e-6b65-f237-5851-ccdf16cfc1b5.htm)

[ReleaseConditions Overload](d0d81781-b683-ba87-9c1d-074417bcdb7a.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__2f9126ea-17e4-c221-40f8-e430dfae5262.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceDataSource Property

---



|  |
| --- |
| [MassSurfaceData Class](69fcb13c-6443-d1c2-29d5-08adc1261afd.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the MassSurfaceData properties are driven by the EnergyDataSettings of the Document or are overridden for the surface.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public MassSurfaceDataSource SurfaceDataSource { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SurfaceDataSource As MassSurfaceDataSource 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property MassSurfaceDataSource SurfaceDataSource { 	MassSurfaceDataSource get (); 	void set (MassSurfaceDataSource value); } ``` |

# Remarks

The Construction property is not governed by this setting and has a separate value to indicate if it is to be synchronized with EnergyDataSettings.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The surface data source does not fall within an appropriate range. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[MassSurfaceData Class](69fcb13c-6443-d1c2-29d5-08adc1261afd.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__2f91a9f3-7f69-72f9-08d6-a2d71dfb33db.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Parameter Property (BuiltInParameter)

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Retrieves a parameter from the element given a parameter id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Parameter this[ 	BuiltInParameter parameterId ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Parameter ( _ 	parameterId As BuiltInParameter _ ) As Parameter 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Parameter^ Parameter[BuiltInParameter parameterId] { 	Parameter^ get (BuiltInParameter parameterId); } ``` |

#### Parameters

parameterId
:   Type:  [Autodesk.Revit.DB BuiltInParameter](fb011c91-be7e-f737-28c7-3f1e1917a0e0.htm)    
     The built in parameter id of the parameter to be retrieved.

# Remarks

Parameters are a generic form of data storage within elements. The parameters are visible through the Autodesk Revit user interface in the Element Properties dialog. This method uses a built in parameter id to access the parameter. Autodesk Revit has a large number of built in parameters that are available via an enumerated type.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public Parameter FindWithBuiltinParameterID(Wall wall)
{
    //Use the WALL_BASE_OFFSET paramametId
    // to get the base offset parameter of the wall.
    BuiltInParameter paraIndex = BuiltInParameter.WALL_BASE_OFFSET;
    Parameter parameter = wall.get_Parameter(paraIndex);

    return parameter;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Function FindWithBuiltinParameterID(wall As Wall) As Parameter
    'Use the WALL_BASE_OFFSET paramametId
    ' to get the base offset parameter of the wall.
    Dim paraIndex As BuiltInParameter = BuiltInParameter.WALL_BASE_OFFSET
    Dim parameter As Parameter = wall.Parameter(paraIndex)

    Return parameter
End Function
```

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Parameter Overload](a742d71a-b415-9e99-2978-abd3b5bae7f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f926f7e-f816-6933-a125-53c856a25d8c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsPipingAnalysisEnabled Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Checks whether or not piping analysis is enabled, and enable or disable it.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsPipingAnalysisEnabled { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsPipingAnalysisEnabled As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsPipingAnalysisEnabled { 	bool get (); 	void set (bool value); } ``` |

# Remarks

Enabling piping analysis will not take effect unless the piping discipline is also enabled.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The current product type is not ProductType.Revit and discipline controls are not enabled. |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__2f9290d2-e879-2e12-bfbf-ffd054c7364f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnableToTransformElement Property

---



|  |
| --- |
| [BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)   [See Also](#seeAlsoToggle) |

Attempted an invalid element rotate, mirror, or move.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId UnableToTransformElement { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property UnableToTransformElement As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ UnableToTransformElement { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f92b4ae-afdc-6342-7a6f-96329238b1f4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MechanicalEquipmentSetBeingDeleted Property

---



|  |
| --- |
| [BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)   [See Also](#seeAlsoToggle) |

The mechanical equipment set was deleted because it no longer contained any members.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId MechanicalEquipmentSetBeingDeleted { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MechanicalEquipmentSetBeingDeleted As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ MechanicalEquipmentSetBeingDeleted { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f93dd88-baac-8e61-377e-b937f3faaff6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCurvesInView Method

---



|  |
| --- |
| [DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)   [See Also](#seeAlsoToggle) |

Gets a collection of curves representing the DatumPlane element in the given view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public IList<Curve> GetCurvesInView( 	DatumExtentType extentMode, 	View view ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCurvesInView ( _ 	extentMode As DatumExtentType, _ 	view As View _ ) As IList(Of Curve) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Curve^>^ GetCurvesInView( 	DatumExtentType extentMode,  	View^ view ) ``` |

#### Parameters

extentMode
:   Type:  [Autodesk.Revit.DB DatumExtentType](7a968bc3-1860-6a8b-6f3a-2b23b80a56a5.htm)    
     The extent type.

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view.

#### Return Value

The curves.

# Remarks

Curves returned for Model extents can be different than curves returned for View-specific extents (2d extents) in the given view. In some cases, such as an arc grid in a section view, there will be two identical curves but offset from one another.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The datum plane cannot be visible in the view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f93df68-e5de-f0de-dad1-1b84a18f476d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UserCancelled Property

---



|  |
| --- |
| [BuiltInFailures RegenFailures Class](c7726de2-e4f0-8861-8115-0ef9de7935b1.htm)   [See Also](#seeAlsoToggle) |

Operation is cancelled by the user.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId UserCancelled { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property UserCancelled As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ UserCancelled { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RegenFailures Class](c7726de2-e4f0-8861-8115-0ef9de7935b1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2f9772ee-a2ba-8b07-d480-5cef37a23edf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDefaultRepeatingReferenceSource Method

---



|  |
| --- |
| [RepeatingReferenceSource Class](c1a3887e-0272-7dcb-bed3-85c807ec39a0.htm)   [See Also](#seeAlsoToggle) |

Returns the default repeating reference source for a given element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static RepeatingReferenceSource GetDefaultRepeatingReferenceSource( 	Document document, 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetDefaultRepeatingReferenceSource ( _ 	document As Document, _ 	elementId As ElementId _ ) As RepeatingReferenceSource ``` |

 

| Visual C++ |
| --- |
| ``` public: static RepeatingReferenceSource^ GetDefaultRepeatingReferenceSource( 	Document^ document,  	ElementId^ elementId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document that contains the element.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the element.

#### Return Value

The default repeating reference source of the given element.

# Remarks

The element must support repeating references. Use HasRepeatingReferenceSource() to find out whether an element has any repeating references.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element elementId does not exist in the document -or- The element does not have any repeating reference sources. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RepeatingReferenceSource Class](c1a3887e-0272-7dcb-bed3-85c807ec39a0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fa1b23e-fa0a-65c5-d8fd-3850c55051f7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OpenLoopError Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Lines must be in closed loops. The highlighted lines are open on one end.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId OpenLoopError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property OpenLoopError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ OpenLoopError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fa5cdff-3d4c-a479-fbc6-f2bae9c06884.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForceVector1 Property

---



|  |
| --- |
| [AreaLoad Class](5dc205a9-cafd-911b-6a56-26f2e8bfcdc1.htm)   [See Also](#seeAlsoToggle) |

The force vector applied to the 1st reference point of the area load, oriented according to OrientTo setting.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public XYZ ForceVector1 { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ForceVector1 As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ ForceVector1 { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

The default force unit is kN/m^2 for metric, and ksf for imperial. Use UnitUtils class methods to convert value from or to internal units.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[AreaLoad Class](5dc205a9-cafd-911b-6a56-26f2e8bfcdc1.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__2fa7d011-c5db-3863-af69-59b06d0a38a9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetValues Method

---



|  |
| --- |
| [ExportLayerTable Class](e68ce1c7-a922-d1b7-53bb-f832a4bad273.htm)   [See Also](#seeAlsoToggle) |

Returns all the values stored in the map.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public IList<ExportLayerInfo> GetValues() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetValues As IList(Of ExportLayerInfo) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ExportLayerInfo^>^ GetValues() ``` |

#### Return Value

Return the info array.

# See Also

[ExportLayerTable Class](e68ce1c7-a922-d1b7-53bb-f832a4bad273.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fa855ba-6a1a-b0af-8079-10415ff7e2d3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IDuplicateTypeNamesHandler Interface

---



|  |
| --- |
| [Members](849445d0-c87a-7e91-df43-41daf2605640.htm)   [See Also](#seeAlsoToggle) |

An interface for custom handlers of duplicate type names encountered during a paste operation. When the destination document contains types that have the same names as the types being copied, but different internals, a decision must be made on how to proceed - whether to cancel the operation or continue, but only copy types with unique names.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public interface IDuplicateTypeNamesHandler ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IDuplicateTypeNamesHandler ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IDuplicateTypeNamesHandler ``` |

# See Also

[IDuplicateTypeNamesHandler Members](849445d0-c87a-7e91-df43-41daf2605640.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fa98df9-0384-e3a6-65f9-a4529b87ed36.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddSeparator Method

---



|  |
| --- |
| [RibbonPanel Class](544c0af7-6124-4f64-a25d-46e81ac5300f.htm)   [See Also](#seeAlsoToggle) |

Adds a new Separator to the panel.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void AddSeparator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddSeparator ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddSeparator() ``` |

# Remarks

The separator won't be shown if there are no items already added to the panel.

# See Also

[RibbonPanel Class](544c0af7-6124-4f64-a25d-46e81ac5300f.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__2fae60e5-94e0-4fb5-60d3-3b7ce4dd3e51.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsHVACSystemTypeId Method

---



|  |
| --- |
| [FlexDuct Class](39e3bd3a-8304-7785-dd10-4043aa0d7da4.htm)   [See Also](#seeAlsoToggle) |

Checks if given type is valid HVAC system type.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool IsHVACSystemTypeId( 	Document document, 	ElementId systemTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsHVACSystemTypeId ( _ 	document As Document, _ 	systemTypeId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsHVACSystemTypeId( 	Document^ document,  	ElementId^ systemTypeId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

systemTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     ElementId of the HVAC system type to check.

#### Return Value

True if the given systemTypeId is the HVAC system type, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FlexDuct Class](39e3bd3a-8304-7785-dd10-4043aa0d7da4.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__2faf0cca-a05a-45dc-d7e4-e61443a53623.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ParentId Property

---



|  |
| --- |
| [DisplacementElement Class](08113547-eaaa-5ec1-5ff1-de609fe7c29c.htm)   [See Also](#seeAlsoToggle) |

The element id of the parent DisplacementElement. This DisplacementElement's relative transform will be concatenated with the absolute transform of its parent.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ElementId ParentId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ParentId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ParentId { 	ElementId^ get (); } ``` |

# See Also

[DisplacementElement Class](08113547-eaaa-5ec1-5ff1-de609fe7c29c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fb3c757-0555-d2ba-2cd2-9399bf238735.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsCurveValidInView Method

---



|  |
| --- |
| [DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)   [See Also](#seeAlsoToggle) |

Checks if the curve is valid to be as the extents for the datum plane in a view. The curve must be bound and coincident with the original one of the datum plane.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool IsCurveValidInView( 	DatumExtentType extentMode, 	View view, 	Curve curve ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsCurveValidInView ( _ 	extentMode As DatumExtentType, _ 	view As View, _ 	curve As Curve _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsCurveValidInView( 	DatumExtentType extentMode,  	View^ view,  	Curve^ curve ) ``` |

#### Parameters

extentMode
:   Type:  [Autodesk.Revit.DB DatumExtentType](7a968bc3-1860-6a8b-6f3a-2b23b80a56a5.htm)    
     The extent type.

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view.

curve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The curve.

#### Return Value

True if it is valid, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[DatumPlane Class](3e0a6725-ee40-c4d5-839f-b7720c1fe2af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fba2f22-8d88-8b2c-c75e-8908223ec20c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UpdateMultiple Method (Document, IList(ElementId))

---



|  |
| --- |
| [PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)   [See Also](#seeAlsoToggle) |

Updates the specified paths of travel by recalculating each path using their original start and end points.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public static int UpdateMultiple( 	Document adoc, 	IList<ElementId> elementsToUpdate ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function UpdateMultiple ( _ 	adoc As Document, _ 	elementsToUpdate As IList(Of ElementId) _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: static int UpdateMultiple( 	Document^ adoc,  	IList<ElementId^>^ elementsToUpdate ) ``` |

#### Parameters

adoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document of elements to be updated.

elementsToUpdate
:   Type:  System.Collections.Generic IList   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The list of  [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)  of the paths to update.

#### Return Value

number of successfully updated elements

# Remarks

For unsuccessfully updated elements, Revit will post warnings.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This functionality is not available in Revit LT. |

# See Also

[PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)

[UpdateMultiple Overload](7d6c08a5-abd4-84bb-7865-706dfb1a91c5.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__2fc2d211-38de-6e5d-473d-8e72b8529ed2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotPasteModelPlusViewSpecificElementsIntoView Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

Cannot paste view-specific model plus into view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotPasteModelPlusViewSpecificElementsIntoView { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotPasteModelPlusViewSpecificElementsIntoView As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotPasteModelPlusViewSpecificElementsIntoView { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fc35e00-cdf2-8368-e6a6-032725492cbe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ModelUpdatesStatus Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Indicates whether an element in the current model has additional user changes in the central model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public enum ModelUpdatesStatus ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ModelUpdatesStatus ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ModelUpdatesStatus ``` |

# Members

| Member name | Description |
| --- | --- |
| CurrentWithCentral | The element has no additional changes in the central model. |
| NotYetInCentral | The element is new in the current model and has not been saved to the central model. Note that this status will apply to newly created elements even if they are created in the central model. |
| DeletedInCentral | The element has been deleted in the central model. |
| UpdatedInCentral | The element has additional user changes in the central model. A reload latest will be required before it can be modified in the current model. |

# Remarks

Note that this status only indicates that the element has user changes in the central model. A user change is typically an action specifically taken by a user. Making a user change to an element requires that the user making the change reload all other user changes made to the element in the central model. Making a user change also causes the element to be checked out to the current user so other users will not be able to make user changes to the same element.

Elements can also be modified by system changes. A system change is one which is done automatically by Revit to fully update the model after a user change occurs. Users may make changes to an element in their local model even if the element contains additional system changes in the central model.

Example: Suppose Alice and Bob are working on the same model. Alice moves a wall which contains windows. Then Alice synchronizes with the central file. The wall was explicitly changed by Alice and so it will report as "UpdatedInCentral" in Bob's model. Bob would have to reload latest before he could make user changes to that wall. In contrast, Revit automatically moved the windows with the wall, so the windows do not contain any user changes. The windows would therefore report "CurrentWithCentral" and Bob would be allowed to modify them in his local model without reloading latest.

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fc830c4-3e81-5a83-a110-d4e0f13cade3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PrimaryUnits Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Primary Units"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PrimaryUnits { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PrimaryUnits As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PrimaryUnits { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fca6a21-4a1c-01d3-5e05-7f47d60931e8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Ksf Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol ksf, indicating unit Kips per square foot.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Ksf { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Ksf As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Ksf { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fcc3896-28ea-38ea-7cd5-becbe575d4db.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FaceWallComplexType Property

---



|  |
| --- |
| [BuiltInFailures WallFailures Class](22d82d7e-a7d6-c096-991c-728df0b2d61c.htm)   [See Also](#seeAlsoToggle) |

Vertically compound wall type features sweeps, reveals, or split layers are not supported on non-vertical face. Consider using a simplified type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FaceWallComplexType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FaceWallComplexType As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FaceWallComplexType { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures WallFailures Class](22d82d7e-a7d6-c096-991c-728df0b2d61c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fce0630-0135-1c5f-a2ac-4f6e211a9c61.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetConditionImage Method

---



|  |
| --- |
| [FabricationServiceButton Class](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)   [See Also](#seeAlsoToggle) |

Gets the image for the specified fabrication service button condition.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public virtual Bitmap GetConditionImage( 	int condition ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function GetConditionImage ( _ 	condition As Integer _ ) As Bitmap ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual Bitmap^ GetConditionImage( 	int condition ) ``` |

#### Parameters

condition
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The condition index.

#### Return Value

System.Drawing.Bitmap represents the fabrication service button image.    a null reference (  Nothing  in Visual Basic)  if there is no preview image.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the index condition is not larger or equal to 0 and less than ConditionCount |

# See Also

[FabricationServiceButton Class](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fd1fab5-247f-4ec9-4bc9-9840c1b6eab8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Tier Property

---



|  |
| --- |
| [EnergyAnalysisDetailModel Class](858aed23-8a94-a70a-c1fc-ca03523e2f02.htm)   [See Also](#seeAlsoToggle) |

Level of computation for energy analysis model.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public EnergyAnalysisDetailModelTier Tier { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Tier As EnergyAnalysisDetailModelTier 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property EnergyAnalysisDetailModelTier Tier { 	EnergyAnalysisDetailModelTier get (); } ``` |

# See Also

[EnergyAnalysisDetailModel Class](858aed23-8a94-a70a-c1fc-ca03523e2f02.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__2fd26edf-b1f8-905b-e5d7-b56eaa2a2eeb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SaveAsCloudModel Method (Guid, Guid, String, String)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Saves current non-workshared or workshared model as a cloud model or workshared cloud model in BIM 360 Docs or Autodesk Docs.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public void SaveAsCloudModel( 	Guid accountId, 	Guid projectId, 	string folderId, 	string modelName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SaveAsCloudModel ( _ 	accountId As Guid, _ 	projectId As Guid, _ 	folderId As String, _ 	modelName As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SaveAsCloudModel( 	Guid accountId,  	Guid projectId,  	String^ folderId,  	String^ modelName ) ``` |

#### Parameters

accountId
:   Type:  System Guid    
     The BIM 360 Docs or Autodesk Docs account Id. You can use one of the following methods to get this Id:

    * If you get the hub Id with Forge Data Management API, remove the prefix "b." of the Id string and convert the rest to a Guid.
    * If you get the account Id with Forge BIM 360 Docs or Autodesk Docs API, just convert the Id string to a Guid.

projectId
:   Type:  System Guid    
     The BIM 360 Docs or Autodesk Docs project Id. You can use one of the following methods to get this Id:

    * If you get the project Id with Forge Data Management API, remove the prefix "b." of the Id string and convert the rest to a Guid.
    * If you get the project Id with Forge BIM 360 Docs or Autodesk Docs API, just convert the Id string to a Guid.

folderId
:   Type:  System String    
     Folder identity in BIM 360 Docs or Autodesk Docs to save the model. You can use one of the following methods to get this Id:

    * The folder Id string from Forge Data Management API.
    * The folder Id string from Forge BIM 360 Docs or Autodesk Docs API.

modelName
:   Type:  System String    
     Model name in BIM 360 Docs or Autodesk Docs to save the model.

# Remarks

Assumes that user is currently signed in BIM 360 Docs or Autodesk Docs and has access to Autodesk cloud services. This operation will create a model on cloud and then create a local cache of the cloud model. This method cannot be used when current document is already in cloud.

You can use one of the following methods to save a local model as a workshared cloud model in BIM 360 Docs or Autodesk Docs.

* If the local model is a workshared model, then it will be a workshared cloud model after you use this method successfully.
* If the local model is a non-workshared model, you can enable the workset with  [EnableWorksharing(String, String)](7c29717e-1d8c-4e02-20ad-65c53ea8eaaa.htm)  and then save as a workshared cloud model.
* If the local model is a non-workshared model, and you have already saved it as a non-workshared cloud model in BIM 360 Docs or Autodesk Docs, you can still enable the workset with  [EnableCloudWorksharing](4146e816-565e-85d8-ce94-93ec505a0924.htm)  to convert it to a workshared cloud model.

You cannot save a local workshared model as a non-workshared cloud model in BIM 360 Docs or Autodesk Docs.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | folderId is an empty string. -or- modelName is an empty string. -or- The input file name "modelName" does not represent a valid file name. -or- Thrown when the input BIM 360 Docs or Autodesk Docs account Id or project Id is invalid or unmatched. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | SaveAs may not be called during dynamic update. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Saving is not allowed in the current application mode. -or- This Document is not a project document. -or- This Document is in an edit mode. -or- This Document is not a primary document, it is a linked document. -or- SaveAs is temporarily disabled. -or- This Document is a cloud model, cannot be saved as a cloud model. -or- There is a transaction phase left open (such as a transaction, sub-transaction of transaction group) at the time of invoking this method. |
| [Autodesk.Revit.Exceptions RevitServerCommunicationException](a0003d89-0113-6623-65da-0db5c568bfb6.htm) | Could be for any of the reasons related to network. |
| [Autodesk.Revit.Exceptions RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.htm) | Could be for any of the reasons that saveAs fails with RevitServerInternalException. |
| [Autodesk.Revit.Exceptions RevitServerModelAlreadyExistsException](a3ed0157-0a46-0b62-62db-08112e1645bd.htm) | Failed due to there is a model with the same name already exists at the specified location. |
| [Autodesk.Revit.Exceptions RevitServerModelNameBreaksConventionException](ec0e702a-f076-1b44-4277-feefd39045d4.htm) | Failed due to the model name is breaking project naming convention. |
| [Autodesk.Revit.Exceptions RevitServerUnauthenticatedUserException](b9b68e56-c767-4680-a65b-73d268ee8860.htm) | User is not signed in with Autodesk id. |
| [Autodesk.Revit.Exceptions RevitServerUnauthorizedException](9e8c1efc-8719-fe01-f311-cfade7b177ed.htm) | You don't have the entitlement to perform the operation to this this Document. -or- User is not authorized to access the specified cloud project. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fd2a61a-bb02-1f15-f23b-cc8016aeb142.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Contains Method

---



|  |
| --- |
| [GeomCombinationSet Class](854ed2aa-bd22-3352-383f-7a5230f154e5.htm)   [See Also](#seeAlsoToggle) |

Tests for the existence of an GeomCombination within the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool Contains( 	GeomCombination item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Contains ( _ 	item As GeomCombination _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Contains( 	GeomCombination^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB GeomCombination](75501cfa-a83b-0acf-c446-b368551da6c4.htm)    
     The element to be searched for.

#### Return Value

The Contains method returns True if the GeomCombination is within the set, otherwise False.

# See Also

[GeomCombinationSet Class](854ed2aa-bd22-3352-383f-7a5230f154e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fd54bc7-83ec-bc69-4e97-74482d420f54.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsRailingHeightShiftVal Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Landing Height Adjustment"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsRailingHeightShiftVal { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsRailingHeightShiftVal As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsRailingHeightShiftVal { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fdabf9d-39d6-5739-9d28-6ceca0ecf2f5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (XYZ, XYZ, Curve, Double, Double)

---



|  |
| --- |
| [RevolvedSurface Class](ce0b47e0-2b24-61f5-1434-87fe3ff70390.htm)   [See Also](#seeAlsoToggle) |

Creates a Surface object coincident with the surface of revolution defined by an axis, a profile curve, and start and end angles of revolution.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static Surface Create( 	XYZ axisBasePoint, 	XYZ axisDirection, 	Curve profileCurve, 	double startAngle, 	double endAngle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	axisBasePoint As XYZ, _ 	axisDirection As XYZ, _ 	profileCurve As Curve, _ 	startAngle As Double, _ 	endAngle As Double _ ) As Surface ``` |

 

| Visual C++ |
| --- |
| ``` public: static Surface^ Create( 	XYZ^ axisBasePoint,  	XYZ^ axisDirection,  	Curve^ profileCurve,  	double startAngle,  	double endAngle ) ``` |

#### Parameters

axisBasePoint
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The base point of the axis of revolution. Expected to lie within the Revit design limits  [IsWithinLengthLimits(XYZ)](ac2171af-4250-8a30-faa7-4d7030d29a03.htm)  .

axisDirection
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The direction of the axis.

profileCurve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     The profile curve, which should satisfy the following conditions:

    * It is bounded and non-degenerate.
    * It is co-planar with the axis of revolution.
    * It lies on only one side of the axis.
    * Only the end points of the profile curve can touch the axis.

startAngle
:   Type:  System Double    
     Start angle of rotation. The angles are measured around the axis of revolution, using the right-hand rule. The profile curve is at the zero angle.

endAngle
:   Type:  System Double    
     End angle of rotation. Start angle must be less than end angle and their difference must be less than or equal to two times PI.

#### Return Value

The created surface. Note that this surface may not be of type RevolvedSurface.

# Remarks

The returned surface may not be of type RevolvedSurface - this function will create a surface of the simplest possible type (Plane, Cylinder, etc.) that can be used to represent the required surface of revolution. Given that the surface may be simplified, this function does not guarantee any particular parameterization of the surface.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input point lies outside of Revit design limits. -or- The input profile curve is not valid to create a surface revolution around the given axis. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | axisDirection has zero length. |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | Start angle must be less than end angle and their difference must be less than or equal to two times PI. |

# See Also

[RevolvedSurface Class](ce0b47e0-2b24-61f5-1434-87fe3ff70390.htm)

[Create Overload](a52396a7-ee6e-72a9-4f67-0202a1ea17e0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fe0ab1a-cde7-bcc7-307e-b2dba452bda5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConstantHeightNotParallel Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Constant-height-defining lines must be parallel.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ConstantHeightNotParallel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ConstantHeightNotParallel As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ConstantHeightNotParallel { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fe3b885-64ad-58e9-d585-2c544c3ec92b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ErrorInFamilyResolved Property

---



|  |
| --- |
| [BuiltInFailures GeneralFailures Class](d4679f32-45d9-bec2-e0ff-168c3aee6de9.htm)   [See Also](#seeAlsoToggle) |

An error occurred in family "[Name]" and was automatically resolved. Please review changes made to the family.\nError Information:\n"[Text]"\nError Resolution: [Resolution]

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ErrorInFamilyResolved { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ErrorInFamilyResolved As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ErrorInFamilyResolved { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GeneralFailures Class](d4679f32-45d9-bec2-e0ff-168c3aee6de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fe5f0c1-c4c7-ea97-541c-5ee61b397dce.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WorksetConfigurationOption Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

A collection of options used to initialize a WorksetConfiguration.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public enum WorksetConfigurationOption ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration WorksetConfigurationOption ``` |

 

| Visual C++ |
| --- |
| ``` public enum class WorksetConfigurationOption ``` |

# Members

| Member name | Description |
| --- | --- |
| OpenAllWorksets | Open all user-created worksets by default. Additional open requests will be ignored for this type of configuration. |
| CloseAllWorksets | Close all user-created worksets by default. Additional close requests will be ignored for this type of configuration. |
| OpenLastViewed | Close all user-created worksets by default, but open last viewed worksets. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fe87e81-da51-e784-8169-6991a17b4669.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCellFormatOptions Method (Int32, Int32, Document)

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

Returns a cell's FormatOptions and if no FormatOptions exists for this cell, it would come from the column, or the row, or the section.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public FormatOptions GetCellFormatOptions( 	int nRow, 	int nCol, 	Document ccda ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCellFormatOptions ( _ 	nRow As Integer, _ 	nCol As Integer, _ 	ccda As Document _ ) As FormatOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: FormatOptions^ GetCellFormatOptions( 	int nRow,  	int nCol,  	Document^ ccda ) ``` |

#### Parameters

nRow
:   Type:  System Int32

nCol
:   Type:  System Int32

ccda
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given row number nRow is invalid. -or- The given column number nCol is invalid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[GetCellFormatOptions Overload](ec9bdc85-6227-0c41-9ce2-8709a98c9776.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fe8dd3a-06f6-42f0-52c6-49e83c2c28f2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPointElementReference Method

---



|  |
| --- |
| [ReferencePoint Class](b4b9baeb-2ec5-a2e1-1420-37f593d36aa4.htm)   [See Also](#seeAlsoToggle) |

Change the rule for computing the location of the ReferencePoint relative to other elements in the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetPointElementReference( 	PointElementReference pointElementReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetPointElementReference ( _ 	pointElementReference As PointElementReference _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetPointElementReference( 	PointElementReference^ pointElementReference ) ``` |

#### Parameters

pointElementReference
:   Type:  [Autodesk.Revit.DB PointElementReference](f1548185-45ba-c1c6-8bde-4f9bb0669026.htm)    
     An object specifying a rule for the location and orientation of a ReferencePoint. (Note: The ReferencePoint object does not store the pointElementReference object after this call.)

# Remarks

pointElementReference may be    a null reference (  Nothing  in Visual Basic)  , in which case the ReferencePoint does not follow any other element. When Reference is changed from    a null reference (  Nothing  in Visual Basic)  to a non-null value, the point moves and rotates to the prescribed location and orientation. Where the coordinate system has some freedom, it will remain as close to the old orientation as possible. When the reference is set to    a null reference (  Nothing  in Visual Basic)  , the point does not move or rotate.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when Reference is set to a non-null object, and the ReferencePoint is unable to move to the new reference. |

# See Also

[ReferencePoint Class](b4b9baeb-2ec5-a2e1-1420-37f593d36aa4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fe9cd03-06c1-37a5-bbe8-406c2db0d0ea.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FilterStringGreaterOrEqual Constructor

---



|  |
| --- |
| [FilterStringGreaterOrEqual Class](43ce5f90-7e85-96b2-e9e6-18b493e9a22e.htm)   [See Also](#seeAlsoToggle) |

Constructs an instance of FilterStringGreaterOrEqual.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FilterStringGreaterOrEqual() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: FilterStringGreaterOrEqual() ``` |

# See Also

[FilterStringGreaterOrEqual Class](43ce5f90-7e85-96b2-e9e6-18b493e9a22e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fea1615-56df-d26c-6bef-c073ff8157c5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Length Property

---



|  |
| --- |
| [FabricationAncillaryUsage Class](558a5a38-b4d8-84ed-3260-3253db661a62.htm)   [See Also](#seeAlsoToggle) |

Length of required ancillaries.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public double Length { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Length As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Length { 	double get (); } ``` |

# See Also

[FabricationAncillaryUsage Class](558a5a38-b4d8-84ed-3260-3253db661a62.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2fef9f31-7da8-ffa8-c01d-a16e553e2167.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFromRebarShape Method

---



|  |
| --- |
| [RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)   [See Also](#seeAlsoToggle) |

Set an instance of a RebarContainerItem element, as an instance of a RebarShape. The instance will have the default shape parameters from the RebarShape, and its location is based on the bounding box of the shape in the shape definition. Hooks are removed from the shape before computing its bounding box. If appropriate hooks can be found in the document, they will be assigned arbitrarily.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void SetFromRebarShape( 	RebarShape rebarShape, 	RebarBarType barType, 	XYZ origin, 	XYZ xVec, 	XYZ yVec ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFromRebarShape ( _ 	rebarShape As RebarShape, _ 	barType As RebarBarType, _ 	origin As XYZ, _ 	xVec As XYZ, _ 	yVec As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFromRebarShape( 	RebarShape^ rebarShape,  	RebarBarType^ barType,  	XYZ^ origin,  	XYZ^ xVec,  	XYZ^ yVec ) ``` |

#### Parameters

rebarShape
:   Type:  [Autodesk.Revit.DB.Structure RebarShape](0a370e32-eaba-785e-7e1f-9330929525fc.htm)    
     A RebarShape element that defines the shape of the rebar.

barType
:   Type:  [Autodesk.Revit.DB.Structure RebarBarType](467b44cc-54e7-3ecf-07e1-ad15d05fe800.htm)    
     A RebarBarType element that defines bar diameter, bend radius and material of the rebar.

origin
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The lower-left corner of the shape's bounding box will be placed at this point in the project.

xVec
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The x-axis in the shape definition will be mapped to this direction in the project.

yVec
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The y-axis in the shape definition will be mapped to this direction in the project.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rebarShape has End Treatments |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | xVec has zero length. -or- yVec has zero length. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__2ff87911-3c17-babc-781d-e2c68e62d4e9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExtensionUtility Property

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [See Also](#seeAlsoToggle) |

Property to check whether the instance can be extended and return the interface for extension operation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IExtension ExtensionUtility { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ExtensionUtility As IExtension 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property IExtension^ ExtensionUtility { 	IExtension^ get (); } ``` |

# Remarks

If the family instance can not support extension operation, it returns    a null reference (  Nothing  in Visual Basic)

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2ffad006-1ef9-8224-bd1e-a0cfcc533d29.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MultiReferenceAnnotationOptions Constructor

---



|  |
| --- |
| [MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)   [See Also](#seeAlsoToggle) |

Create an instance of Multi-Reference Annotation Options set with default values.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public MultiReferenceAnnotationOptions( 	MultiReferenceAnnotationType multiReferenceAnnotationType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	multiReferenceAnnotationType As MultiReferenceAnnotationType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: MultiReferenceAnnotationOptions( 	MultiReferenceAnnotationType^ multiReferenceAnnotationType ) ``` |

#### Parameters

multiReferenceAnnotationType
:   Type:  [Autodesk.Revit.DB MultiReferenceAnnotationType](046b4d91-40b3-4dd0-be1b-635fb30956c2.htm)    
     The MultiReferenceAnnotationType to be used by the new MultiReferenceAnnotation.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MultiReferenceAnnotationOptions Class](2e081b6c-38fd-4f03-a372-0dfa841e6248.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__2ffb2cbc-6ab4-c486-b683-96483f33df78.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CentralModelAlreadyExistsException Class

---



|  |
| --- |
| [Members](65b2f6b4-af4d-870a-9a80-ab08a7180f6b.htm)   [See Also](#seeAlsoToggle) |

Exception is thrown when the central model already exists at the specified location.

**Namespace:**   [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` [SerializableAttribute] public class CentralModelAlreadyExistsException : CentralModelException ``` |

 

| Visual Basic |
| --- |
| ``` <SerializableAttribute> _ Public Class CentralModelAlreadyExistsException _ 	Inherits CentralModelException ``` |

 

| Visual C++ |
| --- |
| ``` [SerializableAttribute] public ref class CentralModelAlreadyExistsException : public CentralModelException ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)    
  [Autodesk.Revit.Exceptions ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.htm)    
  [Autodesk.Revit.Exceptions CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.htm)    
  Autodesk.Revit.Exceptions CentralModelAlreadyExistsException

# See Also

[CentralModelAlreadyExistsException Members](65b2f6b4-af4d-870a-9a80-ab08a7180f6b.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)

<!-- Start of Syntax__2ffc0a97-bafa-9890-5c93-41ad61bd4fbf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlasticvinylBumpMap Property

---



|  |
| --- |
| [PlasticVinyl Class](f2f81383-0340-7868-72f1-a7bb4a4a2eaa.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Image" from the "PlasticVinyl" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string PlasticvinylBumpMap { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PlasticvinylBumpMap As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ PlasticvinylBumpMap { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyReference" and will only contain a reference to a connected image.

# See Also

[PlasticVinyl Class](f2f81383-0340-7868-72f1-a7bb4a4a2eaa.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3a023d35-faa0-39e5-fc77-824a65216c50.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TopographyLinkPath Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Saved Path"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TopographyLinkPath { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TopographyLinkPath As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TopographyLinkPath { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a03430e-0baa-d9ca-a887-97d8d00498ec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CloudPoint Constructor

---



|  |
| --- |
| [CloudPoint Structure](c780514e-fc08-e055-bda4-c4fe455c13d3.htm)   [See Also](#seeAlsoToggle) |

Creates a new cloud point.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public CloudPoint( 	float x, 	float y, 	float z, 	int color ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	x As Single, _ 	y As Single, _ 	z As Single, _ 	color As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: CloudPoint( 	float x,  	float y,  	float z,  	int color ) ``` |

#### Parameters

x
:   Type:  [System Single](http://msdn2.microsoft.com/en-us/library/3www918f)    
     The X coordinate.

y
:   Type:  [System Single](http://msdn2.microsoft.com/en-us/library/3www918f)    
     The Y coordinate.

z
:   Type:  [System Single](http://msdn2.microsoft.com/en-us/library/3www918f)    
     The Z coordinate.

color
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The color.

# See Also

[CloudPoint Structure](c780514e-fc08-e055-bda4-c4fe455c13d3.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__3a08f29a-8b2c-0e66-f863-03e04099f371.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionLProfileWithLips Class

---



|  |
| --- |
| [Members](9d68a554-1fc6-c633-e875-05dc9b96c899.htm)   [See Also](#seeAlsoToggle) |

Defines parameters for L Profile with lips structural section.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public class StructuralSectionLProfileWithLips : StructuralSectionGeneralLA ``` |

 

| Visual Basic |
| --- |
| ``` Public Class StructuralSectionLProfileWithLips _ 	Inherits StructuralSectionGeneralLA ``` |

 

| Visual C++ |
| --- |
| ``` public ref class StructuralSectionLProfileWithLips : public StructuralSectionGeneralLA ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSection](65b59d7d-bd7b-c71b-7159-dfc506a912ee.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionRectangular](fc038108-6279-839c-285b-effe342b4491.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionColdFormed](f77557fc-2bc9-e1f9-5984-57cbbe93508a.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionGeneralLA](ac8289f3-7267-03b2-450a-df1a50ccc844.htm)    
  Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionLProfileWithLips

# See Also

[StructuralSectionLProfileWithLips Members](9d68a554-1fc6-c633-e875-05dc9b96c899.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__3a11aaf5-d512-bdd6-a1ab-cdc236887556.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TooManyElementsToCheckout Property

---



|  |
| --- |
| [BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)   [See Also](#seeAlsoToggle) |

Too many elements were attempted to be marked as editable, prompt user to mark workset(s) editable instead

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId TooManyElementsToCheckout { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TooManyElementsToCheckout As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ TooManyElementsToCheckout { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a161382-e2bc-e5af-09fb-494107f37b47.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VoltageIsOutOfRange Property

---



|  |
| --- |
| [BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)   [See Also](#seeAlsoToggle) |

Cannot assign or add [Element] to Circuit. The Voltage ([Voltage Value]) for the Circuit is out of range for the Line to Ground Voltage for [Element] (The Line to Ground Voltage is specified in the assigned Distribution System)."

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId VoltageIsOutOfRange { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property VoltageIsOutOfRange As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ VoltageIsOutOfRange { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a190829-9269-0e56-8b9b-a53b89de35a6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSingleConnectedAsset Method

---



|  |
| --- |
| [AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Gets the single connected asset attached to this asset property, if it exists.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public Asset GetSingleConnectedAsset() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSingleConnectedAsset As Asset ``` |

 

| Visual C++ |
| --- |
| ``` public: Asset^ GetSingleConnectedAsset() ``` |

#### Return Value

The connected asset, or    a null reference (  Nothing  in Visual Basic)  if there is no connected asset.

# Remarks

Throws if there is more than one connected asset.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void SetBumpmapBitmap(Material material, String bumpmapImageFilepath)
{
   ElementId appearanceAssetId = material.AppearanceAssetId;

   AppearanceAssetElement assetElem = material.Document.GetElement(appearanceAssetId) as AppearanceAssetElement;

   using (Transaction t = new Transaction(material.Document, "Change material bumpmap bitmap"))
   {
      t.Start();

      using (AppearanceAssetEditScope editScope = new AppearanceAssetEditScope(assetElem.Document))
      {
         Asset editableAsset = editScope.Start(assetElem.Id);   // returns an editable copy of the appearance asset

         AssetProperty bumpMapProperty = editableAsset.FindByName("generic_bump_map");

         // Find the connected asset (with a shortcut to get the only one)

         Asset connectedAsset = bumpMapProperty.GetSingleConnectedAsset();

         if (connectedAsset == null)
         {
            // Add a new default connected asset
            bumpMapProperty.AddConnectedAsset("UnifiedBitmap");

            connectedAsset = bumpMapProperty.GetSingleConnectedAsset();
         }

         if (connectedAsset != null)
         {
            // Find the target asset property
            AssetPropertyString bumpmapBitmapProperty = connectedAsset.FindByName("unifiedbitmap_Bitmap") as AssetPropertyString;

            if (bumpmapBitmapProperty.IsValidValue(bumpmapImageFilepath))

               bumpmapBitmapProperty.Value = bumpmapImageFilepath;
         }


         editScope.Commit(true);
      }

      t.Commit();
   }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub SetBumpmapBitmap(material As Material, bumpmapImageFilepath As [String])
    Dim appearanceAssetId As ElementId = material.AppearanceAssetId

    Dim assetElem As AppearanceAssetElement = TryCast(material.Document.GetElement(appearanceAssetId), AppearanceAssetElement)

    Using t As New Transaction(material.Document, "Change material bumpmap bitmap")
        t.Start()

        Using editScope As New AppearanceAssetEditScope(assetElem.Document)
            Dim editableAsset As Asset = editScope.Start(assetElem.Id)
       ' returns an editable copy of the appearance asset
       Dim bumpMapProperty As AssetProperty = editableAsset.FindByName("generic_bump_map")

       ' Find the connected asset (with a shortcut to get the only one)


       Dim connectedAsset As Asset = bumpMapProperty.GetSingleConnectedAsset()

            If connectedAsset Is Nothing Then
                ' Add a new default connected asset
                bumpMapProperty.AddConnectedAsset("UnifiedBitmap")

                connectedAsset = bumpMapProperty.GetSingleConnectedAsset()
            End If

            If connectedAsset IsNot Nothing Then
          ' Find the target asset property
          Dim bumpmapBitmapProperty As AssetPropertyString = TryCast(connectedAsset.FindByName("unifiedbitmap_Bitmap"), AssetPropertyString)

          If bumpmapBitmapProperty.IsValidValue(bumpmapImageFilepath) Then

                    bumpmapBitmapProperty.Value = bumpmapImageFilepath
                End If
            End If


            editScope.Commit(True)
        End Using

        t.Commit()
    End Using
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Asset is connected to more than one asset. |

# See Also

[AssetProperty Class](7be89499-d011-ab43-4715-0ee6f9335970.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3a1b0e1e-e7f2-cb08-9983-c36137cac754.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetJoinedElements Method

---



|  |
| --- |
| [JoinGeometryUtils Class](c45b6484-3efd-1d81-0b47-ba678857fff1.htm)   [See Also](#seeAlsoToggle) |

Returns all elements joined to given element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> GetJoinedElements( 	Document document, 	Element element ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetJoinedElements ( _ 	document As Document, _ 	element As Element _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ GetJoinedElements( 	Document^ document,  	Element^ element ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the element.

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element.

#### Return Value

The set of elements that are joined to the given element.

# Remarks

This functionality is not available for family documents.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- The element element was not found in the given document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[JoinGeometryUtils Class](c45b6484-3efd-1d81-0b47-ba678857fff1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a1b6772-e7e6-78e0-91e2-63b578733413.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceRotation Property

---



|  |
| --- |
| [AdvancedTransparent Class](123a1d0d-0c2f-b510-fe5e-e4db5f247f27.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Rotation" from the "AdvancedTransparent" schema.

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

[AdvancedTransparent Class](123a1d0d-0c2f-b510-fe5e-e4db5f247f27.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3a1c089f-082f-e0f6-fc80-68a3c60db8ef.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundingBoxIntersectsFilter Constructor (Outline)

---



|  |
| --- |
| [BoundingBoxIntersectsFilter Class](1fbe1cff-ed94-4815-564b-05fd9e8f61fe.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to match elements with a bounding box that intersects the given Outline.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public BoundingBoxIntersectsFilter( 	Outline outline ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	outline As Outline _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: BoundingBoxIntersectsFilter( 	Outline^ outline ) ``` |

#### Parameters

outline
:   Type:  [Autodesk.Revit.DB Outline](1ffe9215-0dd5-358f-495d-e983f9e7d295.htm)    
     The Outline used to find elements with a bounding box that intersect it.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | outline is an empty Outline. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[BoundingBoxIntersectsFilter Class](1fbe1cff-ed94-4815-564b-05fd9e8f61fe.htm)

[BoundingBoxIntersectsFilter Overload](05ca6834-0efa-3970-3e1b-9c62c7cee423.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a1d96af-0993-c9c4-039b-4a39df72dba2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ContinuousFootingStructuralUsage Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Structural Usage"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ContinuousFootingStructuralUsage { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ContinuousFootingStructuralUsage As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ContinuousFootingStructuralUsage { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a1e5eb4-e997-6d95-4c9c-3614aba235d7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateHanger Method (Document, FabricationServiceButton, Int32, ElementId, Connector, Double, Boolean)

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Creates a hanger on the fabrication part.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static FabricationPart CreateHanger( 	Document document, 	FabricationServiceButton button, 	int condition, 	ElementId hostId, 	Connector hostConnector, 	double distance, 	bool attachToStructure ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateHanger ( _ 	document As Document, _ 	button As FabricationServiceButton, _ 	condition As Integer, _ 	hostId As ElementId, _ 	hostConnector As Connector, _ 	distance As Double, _ 	attachToStructure As Boolean _ ) As FabricationPart ``` |

 

| Visual C++ |
| --- |
| ``` public: static FabricationPart^ CreateHanger( 	Document^ document,  	FabricationServiceButton^ button,  	int condition,  	ElementId^ hostId,  	Connector^ hostConnector,  	double distance,  	bool attachToStructure ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

button
:   Type:  [Autodesk.Revit.DB FabricationServiceButton](6a21f232-3a37-239b-8bb1-a8b02f2984ec.htm)    
     The fabrication service button to use.

condition
:   Type:  System Int32    
     The condition index. If the button has multiple conditions.

hostId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The host part id. The host should be one horizontal straight part.

hostConnector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The connector of the host.

distance
:   Type:  System Double    
     The distance from the input connector of the host part. Units are in feet (ft).

attachToStructure
:   Type:  System Boolean    
     Attach to the nearest structural element. The structural element might be one of Floor/Roof/Stair/Structural Framing.

#### Return Value

The newly-created fabrication hanger.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Hangers may only be placed on straight horizontal fabrication segments and some kind of fittings. -or- Invalid fabrication service button. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the index condition is not larger or equal to 0 and less than ConditionCount |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | the distance is out of range. -or- cannot find suitable fabrication part for the host. -or- cannot place hanger on the host. |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[CreateHanger Overload](aafc60d9-fd3e-59e1-1278-eda915ce1848.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a223d55-0f7e-aa63-7314-e8ad1cd525c9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Style Property

---



|  |
| --- |
| [RebarHookType Class](3c7a78d5-f92b-e58b-e7c9-7927537498fd.htm)   [See Also](#seeAlsoToggle) |

The hook may only be applied to shapes of the specified style.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public RebarStyle Style { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Style As RebarStyle 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property RebarStyle Style { 	RebarStyle get (); 	void set (RebarStyle value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[RebarHookType Class](3c7a78d5-f92b-e58b-e7c9-7927537498fd.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3a27bf10-faac-de5e-7473-2a83be9e3d57.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DimensionCount Property

---



|  |
| --- |
| [RepeatingReferenceSource Class](c1a3887e-0272-7dcb-bed3-85c807ec39a0.htm)   [See Also](#seeAlsoToggle) |

The dimension count of the repeating reference array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public int DimensionCount { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property DimensionCount As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int DimensionCount { 	int get (); } ``` |

# See Also

[RepeatingReferenceSource Class](c1a3887e-0272-7dcb-bed3-85c807ec39a0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a297e1f-c338-a53c-24b2-d63ac4c4b844.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetActiveServerId Method

---



|  |
| --- |
| [SingleServerService Class](8491691e-2a26-684e-f43c-e8e0095fd129.htm)   [See Also](#seeAlsoToggle) |

Returns the Id of the currently active application-level server of the service.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public Guid GetActiveServerId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetActiveServerId As Guid ``` |

 

| Visual C++ |
| --- |
| ``` public: Guid GetActiveServerId() ``` |

#### Return Value

The GUID of the active server, or an invalid GUID if there is no active server assigned.

# See Also

[SingleServerService Class](8491691e-2a26-684e-f43c-e8e0095fd129.htm)

[GetActiveServerId Overload](34f4d53a-f644-52e4-e109-d7f8ea9b1035.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)

<!-- Start of Syntax__3a2c1bf4-a48a-371c-e6d5-0c4cdcfd14b3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBoundingElementFace Method

---



|  |
| --- |
| [SpatialElementBoundarySubface Class](0a8f3677-3320-a8a5-674e-b0d055ac6671.htm)   [See Also](#seeAlsoToggle) |

Returns the face of the bounding element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public Face GetBoundingElementFace() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBoundingElementFace As Face ``` |

 

| Visual C++ |
| --- |
| ``` public: Face^ GetBoundingElementFace() ``` |

#### Return Value

The face of the bounding element.

# Remarks

Applies only if the options chosen for the extraction of the element's geometry is Finish. Faces do not contain voids in room-bounding elements (such the voids in walls created by doors and windows).

# See Also

[SpatialElementBoundarySubface Class](0a8f3677-3320-a8a5-674e-b0d055ac6671.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a30affe-5cdd-1042-45ae-046c2c0d3454.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetItalicStatus Method

---



|  |
| --- |
| [FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)   [See Also](#seeAlsoToggle) |

Returns whether  [All](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  ,  [None](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  or a  [Mixed](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  of characters in the entire text are italic.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public FormatStatus GetItalicStatus() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetItalicStatus As FormatStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: FormatStatus GetItalicStatus() ``` |

#### Return Value

The format status of italic on characters  [FormatStatus](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  .

# Remarks

This function only returns  [All](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  or  [None](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  if the entire text contains one character.

# See Also

[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)

[GetItalicStatus Overload](85c2a15f-6982-66e5-d5ae-aab8909b74b9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a30f767-9284-8287-ba2f-dc1660c368b8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasElbow Property

---



|  |
| --- |
| [SpatialElementTag Class](0a20cdd6-6e44-bc77-a4c3-2d35470ba911.htm)   [See Also](#seeAlsoToggle) |

Identifies if the tag's leader has an elbow point or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public bool HasElbow { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HasElbow As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool HasElbow { 	bool get (); } ``` |

# Remarks

Straight leaders do not have elbow points. Use  [LeaderElbow](8c75fb6c-8b26-077b-125e-b4e2bce3d230.htm)  to get or set elbow point.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | There is no leader for this tag. |

# See Also

[SpatialElementTag Class](0a20cdd6-6e44-bc77-a4c3-2d35470ba911.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a344606-8ee1-c68f-ed1e-62c4f150e1fa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Append Method

---



|  |
| --- |
| [SymbolicCurveArray Class](a8ca9e0e-9838-96e4-5e6b-d5ffc11ea968.htm)   [See Also](#seeAlsoToggle) |

Add the model curve to the end of the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual void Append( 	SymbolicCurve item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Sub Append ( _ 	item As SymbolicCurve _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void Append( 	SymbolicCurve^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB SymbolicCurve](c6c3bde4-4aa9-1b08-cd71-2fad0613d276.htm)    
     The model curve to be added.

# See Also

[SymbolicCurveArray Class](a8ca9e0e-9838-96e4-5e6b-d5ffc11ea968.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a374069-5d74-7af9-4316-8cc6ef232279.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateEqualsRule Method (ElementId, Int32)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether integer values from the document equal a certain value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateEqualsRule( 	ElementId parameter, 	int value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateEqualsRule ( _ 	parameter As ElementId, _ 	value As Integer _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateEqualsRule( 	ElementId^ parameter,  	int value ) ``` |

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

[CreateEqualsRule Overload](0637b53b-96aa-7683-6535-8a1217c5809e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a39e3ab-fb5d-10f0-13d6-1c68d98396d3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaterialParamShininess Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Shininess"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MaterialParamShininess { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MaterialParamShininess As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MaterialParamShininess { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a4036c3-6e64-6b5f-1246-fe8ef68a7526.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UserAssignability Property

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

An option controlling the ability of DirectShapes to assign this DirectShapeType as its type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public DirectShapeTypeUserAssignability UserAssignability { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property UserAssignability As DirectShapeTypeUserAssignability 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property DirectShapeTypeUserAssignability UserAssignability { 	DirectShapeTypeUserAssignability get (); 	void set (DirectShapeTypeUserAssignability value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a45e2af-d541-9fc6-fe33-e314f8712558.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanBeDuplicated Method

---



|  |
| --- |
| [ViewSheet Class](af2ee879-173d-df3a-9793-8d5750a17b49.htm)   [See Also](#seeAlsoToggle) |

Identifies if this sheet can be duplicated.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public bool CanBeDuplicated( 	SheetDuplicateOption duplicateOption ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanBeDuplicated ( _ 	duplicateOption As SheetDuplicateOption _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanBeDuplicated( 	SheetDuplicateOption duplicateOption ) ``` |

#### Parameters

duplicateOption
:   Type:  [Autodesk.Revit.DB SheetDuplicateOption](0d924cfe-327d-d3ca-9576-9e3280a1b1a4.htm)    
     The option to use when duplicating the sheet.

#### Return Value

True if the sheet can be duplicated, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ViewSheet Class](af2ee879-173d-df3a-9793-8d5750a17b49.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a48f343-428e-56f9-36c9-ee82cc732ef8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Position Property

---



|  |
| --- |
| [ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)   [See Also](#seeAlsoToggle) |

Progress bar position - value is always between zero and upperRange and is incremented by one with each event of stage "PositionChanged"

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public int Position { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Position As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int Position { 	int get (); } ``` |

# See Also

[ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__3a4adeb7-4a89-02ad-4061-8fd3ca9fdde7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### KNPerMSup3 Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol kN/mÂ³, indicating unit Kilonewtons per cubic meter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId KNPerMSup3 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property KNPerMSup3 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ KNPerMSup3 { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a4e2d9e-41a8-380e-46b1-ab000c4b6a60.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FolderPath Property

---



|  |
| --- |
| [ExternalResourceBrowserData Class](94a46450-5467-45f2-0228-4c9f9821b4c9.htm)   [See Also](#seeAlsoToggle) |

The current folder path to which the new resources and subfolder belong.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public string FolderPath { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property FolderPath As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ FolderPath { 	String^ get (); } ``` |

# See Also

[ExternalResourceBrowserData Class](94a46450-5467-45f2-0228-4c9f9821b4c9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a51d58c-3e29-b641-e8bb-4d8a17c31527.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ModelText Class

---



|  |
| --- |
| [Members](d9725e63-08f7-b8f3-67a5-2dee38085d4f.htm)   [See Also](#seeAlsoToggle) |

A model text element in an Autodesk Revit family document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class ModelText : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ModelText _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ModelText : public Element ``` |

# Remarks

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB ModelText

# See Also

[ModelText Members](d9725e63-08f7-b8f3-67a5-2dee38085d4f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a54ad97-7e93-185f-63e6-c1348ce17395.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyzeAs Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Analyze As has various functions within the Analytical Model, and is Element-dependent. "Not for Analysis" usually means that there will not be an Analytical Model generated. The others indicate how the Analytical Model behavior will treat the Element in question. For instance "Hanger" columns have different support expectations than "Gravity" columns.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum AnalyzeAs ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration AnalyzeAs ``` |

 

| Visual C++ |
| --- |
| ``` public enum class AnalyzeAs ``` |

# Members

| Member name | Description |
| --- | --- |
| Hanger | A hanging Element. |
| Gravity | Interpreted as Gravity (support going down). |
| Lateral | Interpreted as Lateral (support going across). |
| SlabOneWay | Floor interpreted as Slab One-Way. |
| Mat | Floor interpreted as Mat Foundation, or general foundation. |
| SlabOnGrade | Floor interpreted as Slab on a Grade. |
| NotForAnalysis | Element is not for Analysis. |
| NotApplicable | Analyze As is not applicable. |
| SlabTwoWay | Floor interpreted as Slab Two-Way. |
| GravityLateral | Wall interpreted as Gravity and Lateral |

# See Also

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3a555f5f-3a8d-ab45-395e-8bdd8a5d40e8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotSplitOldMullions Property

---



|  |
| --- |
| [BuiltInFailures CurtainWallFailures Class](a3d691c9-5f8f-29ca-cfad-fa1d1d66f203.htm)   [See Also](#seeAlsoToggle) |

Split does not work on curtain walls containing mullions created in Revit prior to version 4.0. You may delete the mullions, place them again, and then proceed with splitting the wall.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotSplitOldMullions { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotSplitOldMullions As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotSplitOldMullions { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CurtainWallFailures Class](a3d691c9-5f8f-29ca-cfad-fa1d1d66f203.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a590b8a-b0d3-fba1-8844-61d2c4cabeca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OverallLegend Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Overall Legend"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId OverallLegend { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property OverallLegend As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ OverallLegend { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a5c4860-23a1-65bc-e825-8277c0720f45.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HookAngleMatchesRebarShapeDefinition Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Checks that the hook angle of the specified RebarHookType matches the hook angle used in the Rebar's RebarShape at the specified end of the bar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool HookAngleMatchesRebarShapeDefinition( 	int iEnd, 	ElementId proposedHookId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function HookAngleMatchesRebarShapeDefinition ( _ 	iEnd As Integer, _ 	proposedHookId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool HookAngleMatchesRebarShapeDefinition( 	int iEnd,  	ElementId^ proposedHookId ) ``` |

#### Parameters

iEnd
:   Type:  System Int32    
     0 for the start hook, 1 for the end hook.

proposedHookId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The Id of the RebarHookType

#### Return Value

Returns true if the hook angle of the RebarHookType matches the angle used in the RebarShape at the specified end of the bar.

# Remarks

Also checks that the specified id is a valid RebarHookType. If RebarShapeDefinesHooks property of ReinforcementSettings is false (European shapes), every valid hook angle matches RebarShape definition. If RebarShapeDefinesHooks property of ReinforcementSettings is true (non-European shapes), hook angle matches RebarShape definition if it is null or equal RebarShape default hook angle.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | iEnd must be 0 or 1. |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3a60e44d-7c2c-a82a-eec0-7109aed1935e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpacingNumDivisionsn2 Property

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
| ``` public static ForgeTypeId SpacingNumDivisionsn2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpacingNumDivisionsn2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpacingNumDivisionsn2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a65312a-dffd-07d3-0b1d-6040248a6e86.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LevelDataVolume Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Floor Volume"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LevelDataVolume { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LevelDataVolume As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LevelDataVolume { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a67af27-5ec8-d59a-4a05-367c724e5cd9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFailedViewElementIds Method

---



|  |
| --- |
| [DocumentPrintedEventArgs Class](12e3944c-0c43-8c08-d3d0-15828d9a6337.htm)   [See Also](#seeAlsoToggle) |

Returns ElementIds of the views that that failed to print (if any).

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> GetFailedViewElementIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFailedViewElementIds As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ GetFailedViewElementIds() ``` |

#### Return Value

ElementIds of the views that that failed to print (if any).

# See Also

[DocumentPrintedEventArgs Class](12e3944c-0c43-8c08-d3d0-15828d9a6337.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__3a6a237e-bd05-261a-a6ce-c25a02168f5b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ThermalProperties Property

---



|  |
| --- |
| [BuildingPadType Class](355ade63-59db-5d4d-dac2-1f490ff7c1c0.htm)   [See Also](#seeAlsoToggle) |

The calculated and settable thermal properties of the BuildingPadType

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ThermalProperties ThermalProperties { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ThermalProperties As ThermalProperties 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ThermalProperties^ ThermalProperties { 	ThermalProperties^ get (); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | the building pad does not have thermal properties. |

# See Also

[BuildingPadType Class](355ade63-59db-5d4d-dac2-1f490ff7c1c0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a6a5942-1fd7-cd1c-306b-c582da4f2abf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GroundPlane Property

---



|  |
| --- |
| [EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)   [See Also](#seeAlsoToggle) |

Id of level which represents ground level.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElementId GroundPlane { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property GroundPlane As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ GroundPlane { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Remarks

The ground plane defines what is above and below ground for Conceptual Energy Analysis. The ground plane can optionally used for the rendering cast shadows.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The input element is not a level or invalidElementId. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3a6aa337-4f25-30d9-e35f-7ed6c96e17d0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ResetToposurfacePhaseCreated Property

---



|  |
| --- |
| [BuiltInFailures SiteFailures Class](7ab66d74-f1ab-17f6-9ecf-e51b3d5326bf.htm)   [See Also](#seeAlsoToggle) |

The parameter Phase Created of the Toposurface is not set to the first Phase. No pre-existing toposurface were detected. The parameter will be reset to the first Phase unless Keep Phase Created option is picked.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ResetToposurfacePhaseCreated { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ResetToposurfacePhaseCreated As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ResetToposurfacePhaseCreated { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SiteFailures Class](7ab66d74-f1ab-17f6-9ecf-e51b3d5326bf.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a6e710d-e6dd-14f5-3520-193c8f5cca3c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionCProfile Constructor

---



|  |
| --- |
| [StructuralSectionCProfile Class](8e30622c-4454-8088-30b0-3a32de8a7d5b.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of Structural Section C Profile shape with the associated set of parameters, used to attach to structural element.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public StructuralSectionCProfile( 	double width, 	double height, 	double wallNominalThickness, 	double wallDesignThickness, 	double innerFillet, 	double centroidHorizontal, 	double centroidVertical, 	double principalAxesAngle, 	double sectionArea, 	double perimeter, 	double nominalWeight, 	double momentOfInertiaStrongAxis, 	double momentOfInertiaWeakAxis, 	double elasticModulusStrongAxis, 	double elasticModulusWeakAxis, 	double plasticModulusStrongAxis, 	double plasticModulusWeakAxis, 	double torsionalMomentOfInertia, 	double torsionalModulus, 	double warpingConstant, 	double shearAreaStrongAxis, 	double shearAreaWeakAxis ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	width As Double, _ 	height As Double, _ 	wallNominalThickness As Double, _ 	wallDesignThickness As Double, _ 	innerFillet As Double, _ 	centroidHorizontal As Double, _ 	centroidVertical As Double, _ 	principalAxesAngle As Double, _ 	sectionArea As Double, _ 	perimeter As Double, _ 	nominalWeight As Double, _ 	momentOfInertiaStrongAxis As Double, _ 	momentOfInertiaWeakAxis As Double, _ 	elasticModulusStrongAxis As Double, _ 	elasticModulusWeakAxis As Double, _ 	plasticModulusStrongAxis As Double, _ 	plasticModulusWeakAxis As Double, _ 	torsionalMomentOfInertia As Double, _ 	torsionalModulus As Double, _ 	warpingConstant As Double, _ 	shearAreaStrongAxis As Double, _ 	shearAreaWeakAxis As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: StructuralSectionCProfile( 	double width,  	double height,  	double wallNominalThickness,  	double wallDesignThickness,  	double innerFillet,  	double centroidHorizontal,  	double centroidVertical,  	double principalAxesAngle,  	double sectionArea,  	double perimeter,  	double nominalWeight,  	double momentOfInertiaStrongAxis,  	double momentOfInertiaWeakAxis,  	double elasticModulusStrongAxis,  	double elasticModulusWeakAxis,  	double plasticModulusStrongAxis,  	double plasticModulusWeakAxis,  	double torsionalMomentOfInertia,  	double torsionalModulus,  	double warpingConstant,  	double shearAreaStrongAxis,  	double shearAreaWeakAxis ) ``` |

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

centroidHorizontal
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Distance from centroid to the left extremites along horizontal axis.

centroidVertical
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Distance from centroid to the upper extremites along vertical axis.

principalAxesAngle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Rotation angle between the principal axes and cross section reference planes.

sectionArea
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Cross section area.

perimeter
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Painting surface of the unit length.

nominalWeight
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Unit weight (not mass) per unit length, for self-weight calculation or quantity survey.

momentOfInertiaStrongAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Moment of Inertia about main strong axis (I).

momentOfInertiaWeakAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Moment of Inertia about main weak axis (I).

elasticModulusStrongAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Elastic section modulus about main strong axis for calculation of bending stresses.

elasticModulusWeakAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Elastic section modulus about main weak axis for calculation of bending stresses.

plasticModulusStrongAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Plastic section modulus in bending about main strong axis (Z, Wpl)

plasticModulusWeakAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Plastic section modulus in bending about main weak axis.

torsionalMomentOfInertia
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Torsional Moment of inertia (J, IT, K), for calculation of torsional deformation

torsionalModulus
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Section modulus for calculations of torsion stresses (Ct)

warpingConstant
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Warping constant (Cw, Iomega, H)

shearAreaStrongAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Shear area (reduced extreme shear stress coefficient) in the direction of strong axis (Wq).

shearAreaWeakAxis
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Shear area (reduced extreme shear stress coefficient) in the direction of weak axis (Wq).

# See Also

[StructuralSectionCProfile Class](8e30622c-4454-8088-30b0-3a32de8a7d5b.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__3a6edf2d-5338-b2cf-d857-a8d9321bdf16.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewCombinableElementArray Method

---



|  |
| --- |
| [Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)   [See Also](#seeAlsoToggle) |

Returns an array that can hold combinable element objects.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public CombinableElementArray NewCombinableElementArray() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewCombinableElementArray As CombinableElementArray ``` |

 

| Visual C++ |
| --- |
| ``` public: CombinableElementArray^ NewCombinableElementArray() ``` |

#### Return Value

An empty array that can contain any CombinableElement derived objects.

# See Also

[Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__3a6f5412-1efd-c4c0-b35b-621c9a29a1a5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPlainText Method (TextRange)

---



|  |
| --- |
| [FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)   [See Also](#seeAlsoToggle) |

Returns a substring of the text in a plain text form. The start and end of the substring is identified by a given  [TextRange](8a00baaf-8cb8-d9f0-e0a0-eaa5aa16e55e.htm)  .

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public string GetPlainText( 	TextRange textRange ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPlainText ( _ 	textRange As TextRange _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetPlainText( 	TextRange^ textRange ) ``` |

#### Parameters

textRange
:   Type:  [Autodesk.Revit.DB TextRange](8a00baaf-8cb8-d9f0-e0a0-eaa5aa16e55e.htm)    
     The given  [TextRange](8a00baaf-8cb8-d9f0-e0a0-eaa5aa16e55e.htm)  .

#### Return Value

The substring of the text in a plain text form.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This start index of this text range is not within the text range identifying the entire text. -or- The end of this text range is not within the text range identifying the entire text. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)

[GetPlainText Overload](d02fe570-137e-5487-5ffe-2745356efa7a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a713b67-a0da-8110-8d38-b27bd12e1eba.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateGreaterRule Method (ElementId, String)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether strings from the document are greater than a certain value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateGreaterRule( 	ElementId parameter, 	string value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateGreaterRule ( _ 	parameter As ElementId, _ 	value As String _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateGreaterRule( 	ElementId^ parameter,  	String^ value ) ``` |

#### Parameters

parameter
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A string-typed parameter used to get values from the document for a given element.

value
:   Type:  System String    
     The user-supplied string value against which values from the document will be compared.

#### Return Value

Created filter rule object.

# Remarks

For strings, a value is "greater" than another if it would appear after the other in an alphabetically-sorted list.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)

[CreateGreaterRule Overload](3885f1a1-d26c-a3c3-54e1-81f75c04148a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a745c87-d4d2-f9ce-f724-eaaeb736e4ff.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsFamilyContentSecondaryDistribsys Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Secondary Distribution System"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsFamilyContentSecondaryDistribsys { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsFamilyContentSecondaryDistribsys As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsFamilyContentSecondaryDistribsys { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a76651c-dd91-ec9d-9979-50b0af3d462b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WireTypeSetIterator Class

---



|  |
| --- |
| [Members](e59cfec0-e796-1b8a-8939-28b8eeae34fc.htm)   [See Also](#seeAlsoToggle) |

An iterator to a wire type set.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public abstract class WireTypeSetIterator : APIObject,  	IEnumerator ``` |

 

| Visual Basic |
| --- |
| ``` Public MustInherit Class WireTypeSetIterator _ 	Inherits APIObject _ 	Implements IEnumerator ``` |

 

| Visual C++ |
| --- |
| ``` public ref class WireTypeSetIterator abstract : public APIObject,  	IEnumerator ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB.Electrical WireTypeSetIterator

# See Also

[WireTypeSetIterator Members](e59cfec0-e796-1b8a-8939-28b8eeae34fc.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3a785976-c892-9f25-bb13-a7ff69b9dc2e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [FabricationAncillaryUsage Class](558a5a38-b4d8-84ed-3260-3253db661a62.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [FabricationAncillaryUsage](558a5a38-b4d8-84ed-3260-3253db661a62.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
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

[FabricationAncillaryUsage Class](558a5a38-b4d8-84ed-3260-3253db661a62.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a791c57-0441-8cd3-5285-697d794e7019.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.SpanDirectionSymbolFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](4fccbed4-eb4c-4a58-0c4d-30dc530a8c95.htm)   [See Also](#seeAlsoToggle) |

Failures about SpanDirectionSymbol.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class SpanDirectionSymbolFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class SpanDirectionSymbolFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SpanDirectionSymbolFailures abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BuiltInFailures SpanDirectionSymbolFailures

# See Also

[BuiltInFailures SpanDirectionSymbolFailures Members](4fccbed4-eb4c-4a58-0c4d-30dc530a8c95.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a7a5b16-2684-553d-6a25-ee3257f4d5c7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FbxLightSurfaceLoss Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Surface Depreciation Loss"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FbxLightSurfaceLoss { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FbxLightSurfaceLoss As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FbxLightSurfaceLoss { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a7df23f-f396-b7f7-5a14-28ebde0d42b7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotKeepJoined Property

---



|  |
| --- |
| [BuiltInFailures JoinElementsFailures Class](2d7e4353-c24a-38d5-f3aa-3cbc2cb92698.htm)   [See Also](#seeAlsoToggle) |

Can't keep elements joined.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotKeepJoined { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotKeepJoined As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotKeepJoined { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures JoinElementsFailures Class](2d7e4353-c24a-38d5-f3aa-3cbc2cb92698.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a7e18fd-fcd4-1335-ce10-841d2bfd2322.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLayer Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Sets a single layer for this CompoundStructure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetLayer( 	int layerIdx, 	CompoundStructureLayer layer ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLayer ( _ 	layerIdx As Integer, _ 	layer As CompoundStructureLayer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLayer( 	int layerIdx,  	CompoundStructureLayer^ layer ) ``` |

#### Parameters

layerIdx
:   Type:  System Int32    
     The index of a layer. This should range from 0 to the number of layers - 1.

layer
:   Type:  [Autodesk.Revit.DB CompoundStructureLayer](faece83a-6d49-41b0-2713-fe6cfaa5a3b5.htm)    
     The layer to be set.

# Remarks

This function does not support addition of new layers, use SetLayers() to change the number of layers.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The layer is not valid for this operation. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The layer index is out of range. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This operation is valid only for non-vertically compound structures. |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a7ffc07-bd02-39c2-1846-865973db8d7f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportScope Property

---



|  |
| --- |
| [NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)   [See Also](#seeAlsoToggle) |

Options which specifies the export scope of Navisworks Exporter. Default value is Model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public NavisworksExportScope ExportScope { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExportScope As NavisworksExportScope 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property NavisworksExportScope ExportScope { 	NavisworksExportScope get (); 	void set (NavisworksExportScope value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[NavisworksExportOptions Class](a58dbe71-1be7-dad6-51b6-5386c162cf87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a8404ea-680d-8c1a-1618-fcaa0eeea515.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointLightShape Constructor (PointLightShape)

---



|  |
| --- |
| [PointLightShape Class](54dba66a-07b0-2588-0e96-997497984e0b.htm)   [See Also](#seeAlsoToggle) |

Creates a copy of the given point light shape

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public PointLightShape( 	PointLightShape other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	other As PointLightShape _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: PointLightShape( 	PointLightShape^ other ) ``` |

#### Parameters

other
:   Type:  [Autodesk.Revit.DB.Lighting PointLightShape](54dba66a-07b0-2588-0e96-997497984e0b.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PointLightShape Class](54dba66a-07b0-2588-0e96-997497984e0b.htm)

[PointLightShape Overload](5fe4c51f-062a-56aa-2146-11f601b01db5.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__3a868628-038c-df32-df1b-2a6a55404c27.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Cities Property

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

Returns a set of all the known city locations within Revit.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public CitySet Cities { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Cities As CitySet 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property CitySet^ Cities { 	CitySet^ get (); } ``` |

# Remarks

Each city has information about longitude, latitude etc.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__3a872707-d9e4-646d-51f3-bf769e6a8c5f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForwardIterator Method

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
| ``` public virtual GroundConductorSizeSetIterator ForwardIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ForwardIterator As GroundConductorSizeSetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual GroundConductorSizeSetIterator^ ForwardIterator() ``` |

#### Return Value

Returns a forward moving iterator to the set.

# See Also

[GroundConductorSizeSet Class](c0db891d-23ad-f1d1-0b7f-8e5073aa9bab.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3a89372e-05d7-0a5a-0c91-d88500936bb5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProjectAuthor Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Author"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ProjectAuthor { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ProjectAuthor As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ProjectAuthor { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a89e724-75b2-8dac-41e3-2bc1654a7888.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCAggregateIterator Class

---



|  |
| --- |
| [Members](5437095f-c7b3-f7c0-4364-ae404551ec3b.htm)   [See Also](#seeAlsoToggle) |

A class used to iterate individual objects in an IFCAggregate.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class IFCAggregateIterator : IEnumerator<IFCData> ``` |

 

| Visual Basic |
| --- |
| ``` Public Class IFCAggregateIterator _ 	Implements IEnumerator(Of IFCData) ``` |

 

| Visual C++ |
| --- |
| ``` public ref class IFCAggregateIterator : IEnumerator<IFCData^> ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.IFC IFCAggregateIterator

# See Also

[IFCAggregateIterator Members](5437095f-c7b3-f7c0-4364-ae404551ec3b.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__3a8ad72e-5aa7-8fef-10ba-72041fe47346.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PanelType Class

---



|  |
| --- |
| [Members](a3c52194-0fc3-839e-f483-4b8a8afcd769.htm)   [See Also](#seeAlsoToggle) |

An object that represents a curtain panel type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class PanelType : FamilySymbol ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PanelType _ 	Inherits FamilySymbol ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PanelType : public FamilySymbol ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  [Autodesk.Revit.DB InsertableObject](73d870e0-a408-719c-58bd-1fb2ab8f9e5b.htm)    
  [Autodesk.Revit.DB FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)    
  Autodesk.Revit.DB PanelType

# See Also

[PanelType Members](a3c52194-0fc3-839e-f483-4b8a8afcd769.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a907b7c-df51-71b3-a4cc-7da9bfdf0486.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExternallyTaggedNonBRep Constructor

---



|  |
| --- |
| [ExternallyTaggedNonBRep Class](c482cb3d-c4ae-3473-29e7-b9c2de3f2119.htm)   [See Also](#seeAlsoToggle) |

Constructs an ExternallyTaggedGeometryObject associating a given ExternalGeometryId with a particular GeometryObject.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public ExternallyTaggedNonBRep( 	ExternalGeometryId externalId, 	GeometryObject geometry ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	externalId As ExternalGeometryId, _ 	geometry As GeometryObject _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ExternallyTaggedNonBRep( 	ExternalGeometryId^ externalId,  	GeometryObject^ geometry ) ``` |

#### Parameters

externalId
:   Type:  [Autodesk.Revit.DB ExternalGeometryId](6074854d-72b6-fa2f-b4ec-df48a33b862b.htm)    
     The Id of the input geometry object.

geometry
:   Type:  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
     The externally tagged geometry object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | geometry cannot be used with an ExternallyTaggedGeometry. -or- geometry must not be a Solid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternallyTaggedNonBRep Class](c482cb3d-c4ae-3473-29e7-b9c2de3f2119.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a9485bb-f64a-dc82-e67e-cc83166e4a32.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [IFCLegacyStairOrRamp Class](8956431a-7234-2923-094d-0a82f3097e05.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [IFCLegacyStairOrRamp](8956431a-7234-2923-094d-0a82f3097e05.htm)

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

[IFCLegacyStairOrRamp Class](8956431a-7234-2923-094d-0a82f3097e05.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__3a99879a-efe1-8611-01c3-2de9af62341f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Import Method (String, STLImportOptions, View)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Imports an STL file into the document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022.1

# Syntax

| C# |
| --- |
| ``` public ElementId Import( 	string file, 	STLImportOptions options, 	View pDBView ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Import ( _ 	file As String, _ 	options As STLImportOptions, _ 	pDBView As View _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ Import( 	String^ file,  	STLImportOptions^ options,  	View^ pDBView ) ``` |

#### Parameters

file
:   Type:  System String    
     Full path of the file to import. File must exist and must be a valid STL file.

options
:   Type:  [Autodesk.Revit.DB STLImportOptions](0e42500a-7595-5a1b-27e5-23ef168d1ebf.htm)    
     Various import options applicable to the STL format. If    a null reference (  Nothing  in Visual Basic)  , all options will be set to their respective default values.

pDBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     View used to aid placement of the imported file. If the options specify ThisViewOnly, this argument is required and the imported file will only be visible in the specified view. If the options specify center-to-center placement, this argument is required and the imported file will be placed in the center of the specified view. Otherwise, this view is used to obtain a base level to associate with the imported file. If not specified, an existing view will be chosen instead and may open a view or associate the imported file to an arbitrary level.

#### Return Value

Returns the element Id of the imported instance.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Not a valid file for STL import (.stl files are valid). -or- ThisViewOnly cannot be true when importing a DWG|DGN drawing into a 3D view. -or- The provided view is not valid for the options provided. -or- One or more strings describing layer selection is invalid or empty. -or- The scale is not valid as a CustomScale for use during import. -or- NullOrEmpty -or- The view is not printable. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The given file does not exist. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Import is temporarily disabled. |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |
| [Autodesk.Revit.Exceptions OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The STL Import/Link module is not available in the installed Revit. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Import Overload](05c3dbe2-fe7e-c293-761d-b11f356a011b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a9c9e1c-2d03-0896-fdfd-ac75f97a745e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsDuctRoutingPreferenceParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Routing Preferences"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsDuctRoutingPreferenceParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsDuctRoutingPreferenceParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsDuctRoutingPreferenceParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3a9e1089-b8d8-568c-5ce0-89fa17a4f682.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointElementDriven Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Driven by Host"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PointElementDriven { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PointElementDriven As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PointElementDriven { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3aa3ea05-474f-f2d6-f8c9-dc821fcfc782.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Size Property

---



|  |
| --- |
| [DimensionSegmentArray Class](ea274891-53e6-efbe-6dec-fc2c32636ad2.htm)   [See Also](#seeAlsoToggle) |

Returns the number of objects that are in the array.

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

[DimensionSegmentArray Class](ea274891-53e6-efbe-6dec-fc2c32636ad2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3aa923fb-a314-c5fd-c28d-d6aefe97f889.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [DirectContext3DHandleSettings Class](cc9d7b07-a4d9-8570-9ed8-c953e241c0d6.htm)   [See Also](#seeAlsoToggle) |

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

[DirectContext3DHandleSettings Class](cc9d7b07-a4d9-8570-9ed8-c953e241c0d6.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__3aa9bc3b-5ce0-e0ba-4211-9a08526c1c1b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCExtrusionCalculatorOptions Class

---



|  |
| --- |
| [Members](ca6ab5f3-4440-bbea-0177-bd764e4570cc.htm)   [See Also](#seeAlsoToggle) |

This class contains the options used to calculate extrusions from Revit geometry.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class IFCExtrusionCalculatorOptions : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class IFCExtrusionCalculatorOptions _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class IFCExtrusionCalculatorOptions : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.IFC IFCExtrusionCalculatorOptions

# See Also

[IFCExtrusionCalculatorOptions Members](ca6ab5f3-4440-bbea-0177-bd764e4570cc.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__3aad9ec3-80f9-b6fc-2743-3101c929ccf9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanViewNorth Property

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
| ``` public static ForgeTypeId PlanViewNorth { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PlanViewNorth As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PlanViewNorth { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3aaeaadb-08ec-e89c-ea7c-166e1e98ff35.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SectionDimension Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Section Dimension, in discipline Structural.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SectionDimension { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SectionDimension As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SectionDimension { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3aafd0ed-d439-3c4e-ce26-a3b63a279361.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCoincidentEnergyAnalyticalModelFaceReference Method

---



|  |
| --- |
| [MassEnergyAnalyticalModel Class](1e8b2837-0572-d788-a6eb-db5060fc423c.htm)   [See Also](#seeAlsoToggle) |

Returns a Reference to a Face from the same or a different MassEnergyAnalyticalModel that is coincident with the input Face.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static Reference GetCoincidentEnergyAnalyticalModelFaceReference( 	Document document, 	Reference referenceToFace ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetCoincidentEnergyAnalyticalModelFaceReference ( _ 	document As Document, _ 	referenceToFace As Reference _ ) As Reference ``` |

 

| Visual C++ |
| --- |
| ``` public: static Reference^ GetCoincidentEnergyAnalyticalModelFaceReference( 	Document^ document,  	Reference^ referenceToFace ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document.

referenceToFace
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     A Reference to a Face of a MassEnergyAnalyticalModel.

# Remarks

The result is always a Reference to a Face. The Reference Type should report as REFERENCE\_TYPE\_SURFACE. Currently Revit improperly reports it as REFERENCE\_TYPE\_NONE.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The Reference is not a Face of a MassEnergyAnalyticalModel. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MassEnergyAnalyticalModel Class](1e8b2837-0572-d788-a6eb-db5060fc423c.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3aafe2e6-d765-acea-971a-70b5a21fcd47.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEqual Method

---



|  |
| --- |
| [AnalysisDisplayDiagramSettings Class](57e0c5ff-555c-7345-ac24-3592207a4d70.htm)   [See Also](#seeAlsoToggle) |

Compares two diagram settings objects.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsEqual( 	AnalysisDisplayDiagramSettings other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsEqual ( _ 	other As AnalysisDisplayDiagramSettings _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsEqual( 	AnalysisDisplayDiagramSettings^ other ) ``` |

#### Parameters

other
:   Type:  [Autodesk.Revit.DB.Analysis AnalysisDisplayDiagramSettings](57e0c5ff-555c-7345-ac24-3592207a4d70.htm)    
     Diagram settings object to compare with.

#### Return Value

True if objects are equal, false otherwise.

# See Also

[AnalysisDisplayDiagramSettings Class](57e0c5ff-555c-7345-ac24-3592207a4d70.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3ab35910-ed41-5748-00cb-4e2235b51595.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPlaneOrigins Method

---



|  |
| --- |
| [RoofComponents Class](edd1717d-fe80-067c-d5f1-4d84c6a3573b.htm)   [See Also](#seeAlsoToggle) |

The plane origins of roof slabs.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public IList<XYZ> GetPlaneOrigins() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPlaneOrigins As IList(Of XYZ) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<XYZ^>^ GetPlaneOrigins() ``` |

#### Return Value

The origins.

# See Also

[RoofComponents Class](edd1717d-fe80-067c-d5f1-4d84c6a3573b.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__3ab72175-e838-f6d3-691d-8e375a26b83a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StringerCurveTooShort Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

A piece of boundary is too short to create stringer on it.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId StringerCurveTooShort { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StringerCurveTooShort As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ StringerCurveTooShort { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ab731f0-b37a-49b9-0419-b5ca48df783d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CutFailureReason Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The reason why a solid-solid cut cannot be created.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public enum CutFailureReason ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration CutFailureReason ``` |

 

| Visual C++ |
| --- |
| ``` public enum class CutFailureReason ``` |

# Members

| Member name | Description |
| --- | --- |
| CutAllowed | Yes, the cutting element can add a cut to the target element. |
| CutAlreadyExists | The cutting element has already cut the target element. |
| OppositeCutExists | The target element has already cut the cutting element. |
| CutNotAppropriateForElements | The cut is not appropriate for the two elements. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ab7de26-5e32-b3c7-0d35-5e739aad614c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InCanvasControlData Constructor (String)

---



|  |
| --- |
| [InCanvasControlData Class](5fdf010d-7dbb-332d-4704-8e067f2338dc.htm)   [See Also](#seeAlsoToggle) |

Constructs an InCanvasControlData with specific values assigned.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public InCanvasControlData( 	string imagePath ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	imagePath As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: InCanvasControlData( 	String^ imagePath ) ``` |

#### Parameters

imagePath
:   Type:  System String    
     File path with the image to be used. This must be an absolute path to a location on disk.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The file format specified by imagePath is an unsupported format - only \*.bmp files are supported. -or- The file path specified by imagePath is not absolute. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The file specified by imagePath doesn't exist. |

# See Also

[InCanvasControlData Class](5fdf010d-7dbb-332d-4704-8e067f2338dc.htm)

[InCanvasControlData Overload](995d0129-b6ab-4640-f476-7fdfde9ee7d8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3abcb2a7-e687-0d30-f0c4-bff2f57276de.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRibbonPanels Method

---



|  |
| --- |
| [ApplicationEntryPoint Class](7ff0ad2b-7713-ec77-ccc9-8a01fffcf83e.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.UI.Macros](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public override List<RibbonPanel> GetRibbonPanels() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Function GetRibbonPanels As List(Of RibbonPanel) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual List<RibbonPanel^>^ GetRibbonPanels() override ``` |

# See Also

[ApplicationEntryPoint Class](7ff0ad2b-7713-ec77-ccc9-8a01fffcf83e.htm)

[GetRibbonPanels Overload](5792a404-20b3-d513-5db9-16046bc72fe9.htm)

[Autodesk.Revit.UI.Macros Namespace](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)

<!-- Start of Syntax__3ac09c30-2ccd-5d30-2490-b290a7f13d3b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CutMarkSymbolSize Property

---



|  |
| --- |
| [CutMarkType Class](6f2d8dc7-6a19-fba3-00ae-a88cfe0e3d34.htm)   [See Also](#seeAlsoToggle) |

The size of the cut mark symbol.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double CutMarkSymbolSize { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CutMarkSymbolSize As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double CutMarkSymbolSize { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for cutMarkSymbolSize must be greater than 0 and no more than 30000 feet. |

# See Also

[CutMarkType Class](6f2d8dc7-6a19-fba3-00ae-a88cfe0e3d34.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__3ac1a2c4-9afc-98cf-d5b8-c0c6a15fb4e8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PickObjects Method (ObjectType, ISelectionFilter)

---



|  |
| --- |
| [Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)   [See Also](#seeAlsoToggle) |

Prompts the user to select multiple objects which pass a customer filter.

**Namespace:**   [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IList<Reference> PickObjects( 	ObjectType objectType, 	ISelectionFilter selectionFilter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function PickObjects ( _ 	objectType As ObjectType, _ 	selectionFilter As ISelectionFilter _ ) As IList(Of Reference) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Reference^>^ PickObjects( 	ObjectType objectType,  	ISelectionFilter^ selectionFilter ) ``` |

#### Parameters

objectType
:   Type:  [Autodesk.Revit.UI.Selection ObjectType](2d0cbbba-d4ab-84b7-b081-36c14769d82c.htm)    
     Specifies the type of object to be selected.

selectionFilter
:   Type:  [Autodesk.Revit.UI.Selection ISelectionFilter](d552f44b-221c-0ecd-d001-41a5099b2f9f.htm)    
     The selection filter.

#### Return Value

A collection of references selected by the user.

Note: if the user cancels the operation (for example, through ESC), the method will throw an OperationCanceledException instance.

# Remarks

The user will be shown "Finish" and "Cancel" buttons on the dialog bar to complete the selection operation. Uncheck the "Multiple" check-box to select single object and it will return the selected object directly.

Revit users will be permitted to manipulate the Revit view (zooming, panning, and rotating the view), but will not be permitted to click other items in the Revit user interface. Users are not permitted to switch the active view, close the active document or Revit application in the pick session, otherwise an exception will be thrown.

The selection will not be automatically added to the active selection buffer.

Note: this method must not be called during dynamic update, otherwise ForbiddenForDynamicUpdateException will be thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the objectType is not a recognized value. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the selectionFilter is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | Thrown when the Revit user cancelled this operation. Thrown when the Revit user tried to switch the active view, close the active document or Revit application when responding to this mode. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | Thrown if this method is called during dynamic update. |

# See Also

[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)

[PickObjects Overload](e5a547a2-3cf5-7638-2daa-ea85b4d3de2d.htm)

[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.htm)

<!-- Start of Syntax__3ac3334b-158b-847f-eee6-f49ba26bc6db.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FloorAttrDefaultHeightParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Default Height above level"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FloorAttrDefaultHeightParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FloorAttrDefaultHeightParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FloorAttrDefaultHeightParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ac41b1a-a2a8-c15f-6bba-eb41e48006c6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetInitialIntensity Method

---



|  |
| --- |
| [LightType Class](42c83d85-60cd-52c3-7b97-b89e81d7d9fe.htm)   [See Also](#seeAlsoToggle) |

Return a copy of an object derived from InitialIntensity

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public InitialIntensity GetInitialIntensity() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetInitialIntensity As InitialIntensity ``` |

 

| Visual C++ |
| --- |
| ``` public: InitialIntensity^ GetInitialIntensity() ``` |

# See Also

[LightType Class](42c83d85-60cd-52c3-7b97-b89e81d7d9fe.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__3ac89d60-4b71-694f-002f-125d2e6565fc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddParameter Method (String, ForgeTypeId, ForgeTypeId, Boolean)

---



|  |
| --- |
| [FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)   [See Also](#seeAlsoToggle) |

Add a new family parameter with a given name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyParameter AddParameter( 	string parameterName, 	ForgeTypeId groupTypeId, 	ForgeTypeId specTypeId, 	bool isInstance ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddParameter ( _ 	parameterName As String, _ 	groupTypeId As ForgeTypeId, _ 	specTypeId As ForgeTypeId, _ 	isInstance As Boolean _ ) As FamilyParameter ``` |

 

| Visual C++ |
| --- |
| ``` public: FamilyParameter^ AddParameter( 	String^ parameterName,  	ForgeTypeId^ groupTypeId,  	ForgeTypeId^ specTypeId,  	bool isInstance ) ``` |

#### Parameters

parameterName
:   Type:  System String    
     The name of the new family parameter.

groupTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     The identifier of the new family parameter's parameter group.

specTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     The type of new family parameter.

isInstance
:   Type:  System Boolean    
     Indicates if the new family parameter is instance or type.

#### Return Value

If creation was successful the new parameter is returned, otherwise an exception with failure information will be thrown.

# Remarks

This method can work even without any family type, but it cannot be assigned the value via FamilyManager.Set methods when there is no current type. To add a parameter of family type use the AddParameter overload that accepts a category instead.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument-"parameterName"-is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the input argument-"parameterName"-is already in use, or when the input argument -"specTypeId" is an invalid type, or the input parameter group cannot be assigned to the new parameter. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the family parameter creation failed. Or trying to add an instance parameter of image type. |

# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)

[AddParameter Overload](fb4f8475-440f-6454-768f-777388a7fdd4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3acc195c-36fa-4ec9-78e0-370a12fddda5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementId Constructor (Int32)

---



|  |
| --- |
| [ElementId Class](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)   [See Also](#seeAlsoToggle) |

Create an ElementId handle with the given integer id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ElementId( 	int id ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	id As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId( 	int id ) ``` |

#### Parameters

id
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The id.

# See Also

[ElementId Class](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

[ElementId Overload](daf607ff-e2f0-77a2-73a5-59a7da52fa38.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3acc20f9-40cd-d2d0-cb84-6b47d2140a14.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAllMeasurableSpecs Method

---



|  |
| --- |
| [UnitUtils Class](128dd879-fea8-5d7b-1eb2-d64f87753990.htm)   [See Also](#seeAlsoToggle) |

Gets the identifiers of all available measurable specs.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static IList<ForgeTypeId> GetAllMeasurableSpecs() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetAllMeasurableSpecs As IList(Of ForgeTypeId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<ForgeTypeId^>^ GetAllMeasurableSpecs() ``` |

#### Return Value

The spec identifiers.

# See Also

[UnitUtils Class](128dd879-fea8-5d7b-1eb2-d64f87753990.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3acc25be-ddb8-99e8-ea8c-ef0b86b6eb8c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Print Method (ViewSet)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Prints a set of views with default view template and default print settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void Print( 	ViewSet views ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Print ( _ 	views As ViewSet _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Print( 	ViewSet^ views ) ``` |

#### Parameters

views
:   Type:  [Autodesk.Revit.DB ViewSet](47b47de2-4234-01e0-af21-64334e2a4a4b.htm)    
     The set of views which need to be printed.

# Remarks

If one view in the set can not be printed successfully then an exception will be thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when printing is not allowed in the current application mode. Or when at least one view from the view set is not a printable view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the view set to be printed is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the view set contains a    a null reference (  Nothing  in Visual Basic)  element. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when at least one view from the view set could not be printed. |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | Thrown when print is cancelled by event handler. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Print Overload](e491ce6c-4350-0335-5388-28875da09c7e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3acdcd08-f0f1-f23b-94a2-90d1f4ca0eaf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewDisplayDepthCueing Class

---



|  |
| --- |
| [Members](86be30af-5c94-1565-22d7-dd48b113ff7c.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Represents the settings for depth cueing.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public class ViewDisplayDepthCueing : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ViewDisplayDepthCueing _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ViewDisplayDepthCueing : IDisposable ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void AdjustDepthCueing(View view)
{
    if (view.CanUseDepthCueing())
    {
        using (Transaction t = new Transaction(view.Document, "Change depth cueing"))
        {
            t.Start();
            ViewDisplayDepthCueing depthCueing = view.GetDepthCueing();
            depthCueing.EnableDepthCueing = true;
            depthCueing.FadeTo = 50;    // set fade to percent
            depthCueing.SetStartEndPercentages(0, 75);
            view.SetDepthCueing(depthCueing);
            t.Commit();
        }
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub AdjustDepthCueing(view As View)
    If view.CanUseDepthCueing() Then
        Using t As New Transaction(view.Document, "Change depth cueing")
            t.Start()
            Dim depthCueing As ViewDisplayDepthCueing = view.GetDepthCueing()
            depthCueing.EnableDepthCueing = True
            depthCueing.FadeTo = 50
            ' set fade to percent
            depthCueing.SetStartEndPercentages(0, 75)
            view.SetDepthCueing(depthCueing)
            t.Commit()
        End Using
    End If
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ViewDisplayDepthCueing

# See Also

[ViewDisplayDepthCueing Members](86be30af-5c94-1565-22d7-dd48b113ff7c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ace8772-001c-443d-ab7d-46ada4dba628.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BasisY Property

---



|  |
| --- |
| [XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)   [See Also](#seeAlsoToggle) |

The basis of the Y axis.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static XYZ BasisY { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BasisY As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property XYZ^ BasisY { 	XYZ^ get (); } ``` |

# Remarks

The basis of the Y axis is the vector (0,1,0), the unit vector on the Y axis.

# See Also

[XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ad09fc7-03a8-8720-78f1-9dda95f99128.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [KeyBasedTreeEntryError Class](045029df-f8bd-d8df-e5bb-df840012d804.htm)   [See Also](#seeAlsoToggle) |

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

[KeyBasedTreeEntryError Class](045029df-f8bd-d8df-e5bb-df840012d804.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ad2a7db-b1c9-ba0e-661e-bb4117e3a538.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSuperscriptStatus Method (TextRange)

---



|  |
| --- |
| [FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)   [See Also](#seeAlsoToggle) |

Returns whether  [All](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  ,  [None](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  or a  [Mixed](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  set of characters in a given text range are superscripted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public FormatStatus GetSuperscriptStatus( 	TextRange textRange ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSuperscriptStatus ( _ 	textRange As TextRange _ ) As FormatStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: FormatStatus GetSuperscriptStatus( 	TextRange^ textRange ) ``` |

#### Parameters

textRange
:   Type:  [Autodesk.Revit.DB TextRange](8a00baaf-8cb8-d9f0-e0a0-eaa5aa16e55e.htm)    
     The given text range.

#### Return Value

The format status of superscript on characters  [FormatStatus](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  .

# Remarks

This function only returns  [All](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  or  [None](81333f80-2181-8faa-9c1e-cadcda7f3b5e.htm)  if the text contains one character. The given text range should not be empty.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This text range is empty. -or- This start index of this text range is not within the text range identifying the entire text. -or- The end of this text range is not within the text range identifying the entire text. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)

[GetSuperscriptStatus Overload](68e6c6df-ed20-52b7-025a-cb3c18b021b4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ad4f99d-77b2-51b9-8b94-376e4594fbb3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElemAnchorAssembly Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Assembly"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SteelElemAnchorAssembly { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElemAnchorAssembly As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SteelElemAnchorAssembly { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ade0249-e172-0bc2-32d6-9076f6b079cb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointOnEdgeFaceIntersection Class

---



|  |
| --- |
| [Members](7d5f1440-80ee-8b31-03ad-a0a09d649800.htm)   [See Also](#seeAlsoToggle) |

Define a ReferencePoint at the intersection of a referenceable edge or curve and a referenceable face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class PointOnEdgeFaceIntersection : PointElementReference ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PointOnEdgeFaceIntersection _ 	Inherits PointElementReference ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PointOnEdgeFaceIntersection : public PointElementReference ``` |

# Remarks

The ReferencePoint's orientation is partially constrained either to the edge (in the manner of PointOnEdge) or to the face (in the manner of PointOnFace).

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB PointElementReference](f1548185-45ba-c1c6-8bde-4f9bb0669026.htm)    
  Autodesk.Revit.DB PointOnEdgeFaceIntersection

# See Also

[PointOnEdgeFaceIntersection Members](7d5f1440-80ee-8b31-03ad-a0a09d649800.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ade1350-e510-1df5-4497-8ff18ec2d22e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsVelocity Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Velocity"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsVelocity { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsVelocity As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsVelocity { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ae24cde-82ec-1000-ea36-c3a84ee402ae.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OrthogonalProjectionWidth Property

---



|  |
| --- |
| [HomeCamera Class](433ba3ea-00f0-0a6b-9543-8f49dc9922e1.htm)   [See Also](#seeAlsoToggle) |

The width of orthogonal projection view volume.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public double OrthogonalProjectionWidth { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property OrthogonalProjectionWidth As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double OrthogonalProjectionWidth { 	double get (); } ``` |

# See Also

[HomeCamera Class](433ba3ea-00f0-0a6b-9543-8f49dc9922e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ae28cc1-ba19-6e32-c326-ab32d06151ca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [MacroModule Class](d604a3cb-4f41-78a8-6353-270c566ac661.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPIMacros  (in RevitAPIMacros.dll) Version: 2015.0.0.0 (2015.0.0.0)   
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

[MacroModule Class](d604a3cb-4f41-78a8-6353-270c566ac661.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)

<!-- Start of Syntax__3ae2b35d-7807-5218-497d-a39b982bc02c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DirectContext3DHandleSettings Constructor

---



|  |
| --- |
| [DirectContext3DHandleSettings Class](cc9d7b07-a4d9-8570-9ed8-c953e241c0d6.htm)   [See Also](#seeAlsoToggle) |

Constructs an instance of settings with default values.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public DirectContext3DHandleSettings() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: DirectContext3DHandleSettings() ``` |

# See Also

[DirectContext3DHandleSettings Class](cc9d7b07-a4d9-8570-9ed8-c953e241c0d6.htm)

[DirectContext3DHandleSettings Overload](872efff9-4d0f-69c5-c0f5-06a7544ff9e0.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__3ae47923-787f-4e00-efb1-34122688ad2f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceAnisotropy Property

---



|  |
| --- |
| [AdvancedMetal Class](762ef4cc-3219-0f8a-8cd5-137e20225eb0.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Anisotropy" from the "AdvancedMetal" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string SurfaceAnisotropy { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SurfaceAnisotropy As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ SurfaceAnisotropy { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble". This property allows a connected asset.

# See Also

[AdvancedMetal Class](762ef4cc-3219-0f8a-8cd5-137e20225eb0.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3ae60a87-0602-e5cb-4c96-ce6f79aff60a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### KilogramForceMeters Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Kilogram force meters.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId KilogramForceMeters { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property KilogramForceMeters As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ KilogramForceMeters { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3aea334b-d5ad-f2bc-d85d-31ceb5c2fa6b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetHookOrientation Method

---



|  |
| --- |
| [RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)   [See Also](#seeAlsoToggle) |

Defines the orientation of the hook plane at the start or at the end of the rebar with respect to the orientation of the first or the last curve and the plane normal.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void SetHookOrientation( 	int iEnd, 	RebarHookOrientation hookOrientation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetHookOrientation ( _ 	iEnd As Integer, _ 	hookOrientation As RebarHookOrientation _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetHookOrientation( 	int iEnd,  	RebarHookOrientation hookOrientation ) ``` |

#### Parameters

iEnd
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     0 for the start hook, 1 for the end hook.

hookOrientation
:   Type:  [Autodesk.Revit.DB.Structure RebarHookOrientation](e8365754-0811-8d4e-864a-55bf34af3a87.htm)    
     Only two values are permitted: Value = Right: The hook is on your right as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up." Value = Left: The hook is on your left as you stand at the end of the bar, with the bar behind you, taking the bar's normal as "up."

# Remarks

If RebarShapeDefinesHooks property of ReinforcementSettings is true (non-European shapes), setHookOrientation method does nothing.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | iEnd must be 0 or 1. -or- A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |

# See Also

[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3aed4f35-aeda-a06f-2b6e-d7c40e93d529.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UISaveAsOptions Class

---



|  |
| --- |
| [Members](e3eba2ab-eb6f-8bc1-8758-723ff1ab6e5f.htm)   [See Also](#seeAlsoToggle) |

This class contains UI options available for saving a document to disk with a new filename.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public class UISaveAsOptions : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class UISaveAsOptions _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class UISaveAsOptions : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.UI UISaveAsOptions

# See Also

[UISaveAsOptions Members](e3eba2ab-eb6f-8bc1-8758-723ff1ab6e5f.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3af1491a-2a6d-d5c7-1e54-c8ac642dd257.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Definitions Constructor

---



|  |
| --- |
| [Definitions Class](5ff217ff-215d-9d1a-6555-3f45b34a5517.htm)   [See Also](#seeAlsoToggle) |

Constructs an empty set of parameter definitions.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Definitions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: Definitions() ``` |

# See Also

[Definitions Class](5ff217ff-215d-9d1a-6555-3f45b34a5517.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3af27a3a-64c0-517f-f37d-601fae0e9fe1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPartMakerMethodToDivideVolumeFW Method

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Obtains the object allowing access to the divided volume properties of the PartMaker.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static PartMakerMethodToDivideVolumes GetPartMakerMethodToDivideVolumeFW( 	PartMaker partMaker ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetPartMakerMethodToDivideVolumeFW ( _ 	partMaker As PartMaker _ ) As PartMakerMethodToDivideVolumes ``` |

 

| Visual C++ |
| --- |
| ``` public: static PartMakerMethodToDivideVolumes^ GetPartMakerMethodToDivideVolumeFW( 	PartMaker^ partMaker ) ``` |

#### Parameters

partMaker
:   Type:  [Autodesk.Revit.DB PartMaker](ec5be0eb-bf10-0f05-83a4-77daa2cfb0fd.htm)    
     The PartMaker.

#### Return Value

The object handle. Returns    a null reference (  Nothing  in Visual Basic)  if the PartMaker does not represent divided volumes.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3af59293-3253-c0b5-b491-48fd4d5afae3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddRule Method (RoutingPreferenceRuleGroupType, RoutingPreferenceRule)

---



|  |
| --- |
| [RoutingPreferenceManager Class](a8300b97-72a6-beb5-733b-ec4cfea6c472.htm)   [See Also](#seeAlsoToggle) |

Adds a new routing preference rule to the rule group.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void AddRule( 	RoutingPreferenceRuleGroupType groupType, 	RoutingPreferenceRule rule ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddRule ( _ 	groupType As RoutingPreferenceRuleGroupType, _ 	rule As RoutingPreferenceRule _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddRule( 	RoutingPreferenceRuleGroupType groupType,  	RoutingPreferenceRule^ rule ) ``` |

#### Parameters

groupType
:   Type:  [Autodesk.Revit.DB RoutingPreferenceRuleGroupType](79896fd9-e90c-6561-3bc4-7cefd4692ae5.htm)    
     The routing preference group in which the rule should be added.

rule
:   Type:  [Autodesk.Revit.DB RoutingPreferenceRule](28dd1a35-5115-c0fb-26e3-7bce14893b89.htm)    
     The new rule to be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The rule cannot be added to the groupType. -or- Thrown if the index is out of bounds, or the rule is not valid for this group (e.g. an elbow may not be added to the junction group). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[RoutingPreferenceManager Class](a8300b97-72a6-beb5-733b-ec4cfea6c472.htm)

[AddRule Overload](06817419-419d-35bf-8538-3584e415a1c4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3af604c4-9144-43f3-51f0-db3730e9e5a3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlphanumericRevisionSettings Constructor

---



|  |
| --- |
| [AlphanumericRevisionSettings Class](ee27c0eb-9f9b-b59c-728d-24b2654a2bc2.htm)   [See Also](#seeAlsoToggle) |

Constructs an AlphanumericRevisionSettings with a simple, default sequence.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public AlphanumericRevisionSettings() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: AlphanumericRevisionSettings() ``` |

# Remarks

The default sequence contains each letter of the alphabet (may differ based on language settings).

# See Also

[AlphanumericRevisionSettings Class](ee27c0eb-9f9b-b59c-728d-24b2654a2bc2.htm)

[AlphanumericRevisionSettings Overload](48da20f1-0e3d-875e-4789-f9923c654238.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3af783ff-1aca-2c81-659d-edbaa72065d7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ClosestPointsPairBetweenTwoCurves Class

---



|  |
| --- |
| [Members](558bacf8-270b-20a3-1f8d-59ced33ba320.htm)   [See Also](#seeAlsoToggle) |

This class captures results of computation of closest points between two generic curves.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public class ClosestPointsPairBetweenTwoCurves : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ClosestPointsPairBetweenTwoCurves _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ClosestPointsPairBetweenTwoCurves : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ClosestPointsPairBetweenTwoCurves

# See Also

[ClosestPointsPairBetweenTwoCurves Members](558bacf8-270b-20a3-1f8d-59ced33ba320.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3af826dc-5d69-f9b3-0b92-3a101cbfe7b2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreaCreationData Class

---



|  |
| --- |
| [Members](8a6c758d-94ed-e07c-cce6-294043426bf2.htm)   [See Also](#seeAlsoToggle) |

A class which wraps the arguments of Area for batch creation

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class AreaCreationData ``` |

 

| Visual Basic |
| --- |
| ``` Public Class AreaCreationData ``` |

 

| Visual C++ |
| --- |
| ``` public ref class AreaCreationData ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.Creation AreaCreationData

# See Also

[AreaCreationData Members](8a6c758d-94ed-e07c-cce6-294043426bf2.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__3afc8d1b-7c97-851f-0d1b-95d6daf88ba0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CapWasAddedWarning Property

---



|  |
| --- |
| [BuiltInFailures GenericMEPFailures Class](8f72d552-0b22-732d-462e-dfb39606d451.htm)   [See Also](#seeAlsoToggle) |

1 cap was added.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CapWasAddedWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CapWasAddedWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CapWasAddedWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GenericMEPFailures Class](8f72d552-0b22-732d-462e-dfb39606d451.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3afcdf82-b25c-3092-d42c-b60490075d22.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewFamilyInstance Method (Face, XYZ, XYZ, FamilySymbol)

---



|  |
| --- |
| [ItemFactoryBase Class](cba2c84a-22c0-e6e7-a99c-67656901853a.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Inserts a new instance of a family onto a face of an existing element, using a location, reference direction, and a type/symbol.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyInstance NewFamilyInstance( 	Face face, 	XYZ location, 	XYZ referenceDirection, 	FamilySymbol symbol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewFamilyInstance ( _ 	face As Face, _ 	location As XYZ, _ 	referenceDirection As XYZ, _ 	symbol As FamilySymbol _ ) As FamilyInstance ``` |

 

| Visual C++ |
| --- |
| ``` public: FamilyInstance^ NewFamilyInstance( 	Face^ face,  	XYZ^ location,  	XYZ^ referenceDirection,  	FamilySymbol^ symbol ) ``` |

#### Parameters

face
:   Type:  [Autodesk.Revit.DB Face](e32b3b1f-66fc-57cb-6e1c-aa81d1bf3e63.htm)    
     A face of a geometry object.

location
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Point on the face where the instance is to be placed.

referenceDirection
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     A vector that defines the direction of the family instance. Note that this direction defines the rotation of the instance on the face, and thus cannot be parallel to the face normal.

symbol
:   Type:  [Autodesk.Revit.DB FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)    
     A FamilySymbol object that represents the type of the instance that is to be inserted. Note that this symbol must represent a family whose  [FamilyPlacementType](7fcd2fda-21c3-9b9b-8ef3-ae2e53e02a05.htm)  is WorkPlaneBased.

#### Return Value

An instance of the new object if creation was successful, otherwise    a null reference (  Nothing  in Visual Basic)  .

# Remarks

Use this method to insert one family instance on a face of another element, using a point on the face and a vector to define the position and direction of the new symbol.

The type/symbol that is used must be loaded into the document before this method is called. Families and their symbols can be loaded using the Document.LoadFamily or Document.LoadFamilySymbol methods.

The host object must support insertion of instances, otherwise this method will fail. If the instances fails to be created an exception may be thrown.

Some Families, such as Beams, have more than one endpoint and are inserted in the same manner as single point instances. Once inserted, these linear family instances can have their endpoints changed by using the instance's Element.Location property.

Note: if the created family instance includes nested instances, the API framework will automatically regenerate the document during this method call.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
void CreateLightFixtureOnWall(Autodesk.Revit.DB.Document document, Wall wall)
{
    FilteredElementCollector collector = new FilteredElementCollector(document);
    collector.OfClass(typeof(FamilySymbol)).OfCategory(BuiltInCategory.OST_LightingFixtures);
    FamilySymbol symbol = collector.FirstElement() as FamilySymbol;

    // The only way to get a Face to use with this NewFamilyInstance overload
    // is from Element.Geometry with ComputeReferences turned on
    Face face = null;
    Options geomOptions = new Options();
    geomOptions.ComputeReferences = true;
    GeometryElement wallGeom = wall.get_Geometry(geomOptions);
    foreach (GeometryObject geomObj in wallGeom)
    {
        Solid geomSolid = geomObj as Solid;
        if (null != geomSolid)
        {
            foreach (Face geomFace in geomSolid.Faces)
            {
                face = geomFace;
                break;
            }
            break;
        }
    }

    // Get the center of the wall 
    BoundingBoxUV bboxUV = face.GetBoundingBox();
    UV center = (bboxUV.Max + bboxUV.Min) / 2.0;
    XYZ location = face.Evaluate(center);
    XYZ normal = face.ComputeNormal(center);
    XYZ refDir = normal.CrossProduct(XYZ.BasisZ);

    FamilyInstance instance = document.Create.NewFamilyInstance(face, location, refDir, symbol);         
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub CreateLightFixtureOnWall(document As Autodesk.Revit.DB.Document, wall As Wall)
    Dim collector As New FilteredElementCollector(document)
    collector.OfClass(GetType(FamilySymbol)).OfCategory(BuiltInCategory.OST_LightingFixtures)
    Dim symbol As FamilySymbol = TryCast(collector.FirstElement(), FamilySymbol)

    ' The only way to get a Face to use with this NewFamilyInstance overload
    ' is from Element.Geometry with ComputeReferences turned on
    Dim face As Face = Nothing
    Dim geomOptions As New Options()
    geomOptions.ComputeReferences = True
    Dim wallGeom As GeometryElement = wall.Geometry(geomOptions)
    For Each geomObj As GeometryObject In wallGeom
        Dim geomSolid As Solid = TryCast(geomObj, Solid)
        If geomSolid IsNot Nothing Then
            For Each geomFace As Face In geomSolid.Faces
                face = geomFace
                Exit For
            Next
            Exit For
        End If
    Next

    ' Get the center of the wall 
    Dim bboxUV As BoundingBoxUV = face.GetBoundingBox()
    Dim center As UV = (bboxUV.Max + bboxUV.Min) / 2.0
    Dim location As XYZ = face.Evaluate(center)
    Dim normal As XYZ = face.ComputeNormal(center)
    Dim refDir As XYZ = normal.CrossProduct(XYZ.BasisZ)

    Dim instance As FamilyInstance = document.Create.NewFamilyInstance(face, location, refDir, symbol)
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when a non-optional argument was null. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the function cannot get the Reference from the face, or, when the Family cannot be placed as line-based on an input face reference, because its FamilyPlacementType is not WorkPlaneBased |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | Thrown when reference direction is parallel to face normal at insertion point. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when Revit is unable to place the family instance. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if The symbol is not active. |

# See Also

[ItemFactoryBase Class](cba2c84a-22c0-e6e7-a99c-67656901853a.htm)

[NewFamilyInstance Overload](451ee414-cea0-e9bd-227b-c73bc93507dd.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__3aff0677-7049-fe66-f37b-fcfbd78f3872.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExpandedContent Property

---



|  |
| --- |
| [TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)   [See Also](#seeAlsoToggle) |

ExpandedContent is hidden by default and will display at the bottom of the task dialog when the "Show details" button is pressed.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string ExpandedContent { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExpandedContent As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ ExpandedContent { 	String^ get (); 	void set (String^ value); } ``` |

# Remarks

If added to a dialog, a Show/Hide toggle button displays at the bottom of the task dialog. The Expanded Content is hidden by default. This area is used when even more information needs to be relayed to the user than space allows. It is rarely used, but can be used for showing technical information passed through in a variable, for example back-end error information, lists of files, etc. Variable information should always be introduced with a lead-in sentence.

# See Also

[TaskDialog Class](853afb57-7455-a636-9881-61a391118c16.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3b05e6fa-f8e4-1eda-3456-8a8287f1d3e0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [GeomCombinationSetIterator Class](2f5bbf46-374a-447c-73e2-91c0eb283e91.htm)   [See Also](#seeAlsoToggle) |

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

[GeomCombinationSetIterator Class](2f5bbf46-374a-447c-73e2-91c0eb283e91.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b088335-98d9-ddd1-a9c1-a861e7bff9ed.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FrameworkElement Property

---



|  |
| --- |
| [DockablePaneProviderData Class](25c4224d-bc54-f2ed-589d-881a6ccbda87.htm)   [See Also](#seeAlsoToggle) |

The Windows Presentation Framework object containing the pane's user interface.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public FrameworkElement FrameworkElement { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FrameworkElement As FrameworkElement 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property FrameworkElement^ FrameworkElement { 	FrameworkElement^ get (); 	void set (FrameworkElement^ value); } ``` |

# Remarks

Using a System.Windows.Controls.Page is recommended. This can be null, in which case it is assumed an IFrameworkElementCreator is provided to create the element on demand.

# See Also

[DockablePaneProviderData Class](25c4224d-bc54-f2ed-589d-881a6ccbda87.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3b0c7afc-7d63-fb59-29ec-6b52a5a8c496.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallTypeDefaultTaperedInteriorInwardAngle Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Default Interior Angle"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId WallTypeDefaultTaperedInteriorInwardAngle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WallTypeDefaultTaperedInteriorInwardAngle As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ WallTypeDefaultTaperedInteriorInwardAngle { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b0d256f-2611-57f5-05b7-065d60259e7a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VoltageLineToLine Property

---



|  |
| --- |
| [DistributionSysType Class](03754b33-fd20-b19b-a718-6dc2eeccd76c.htm)   [See Also](#seeAlsoToggle) |

Get or set line to line voltage type of distribution system type.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public VoltageType VoltageLineToLine { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property VoltageLineToLine As VoltageType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property VoltageType^ VoltageLineToLine { 	VoltageType^ get (); 	void set (VoltageType^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The voltage retrieved here is read only and actions to modify its properties it will throw an System.InvalidOperationException. |

# See Also

[DistributionSysType Class](03754b33-fd20-b19b-a718-6dc2eeccd76c.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3b104f7a-7b5d-3244-77b6-14ab86774479.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HomeCamera Constructor

---



|  |
| --- |
| [HomeCamera Class](433ba3ea-00f0-0a6b-9543-8f49dc9922e1.htm)   [See Also](#seeAlsoToggle) |

Constructs a new copy of the input HomeCamera object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public HomeCamera( 	HomeCamera other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	other As HomeCamera _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: HomeCamera( 	HomeCamera^ other ) ``` |

#### Parameters

other
:   Type:  [Autodesk.Revit.DB HomeCamera](433ba3ea-00f0-0a6b-9543-8f49dc9922e1.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[HomeCamera Class](433ba3ea-00f0-0a6b-9543-8f49dc9922e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b1056bf-44ce-9d34-0f48-aaa3a761772d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApparentLoad Property

---



|  |
| --- |
| [ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)   [See Also](#seeAlsoToggle) |

The ApparentLoad value of the Electrical System.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2011

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

# Remarks

This property is used to retrieve the ApparentLoad value of the Electrical System.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This property only available when System Type is Power! |

# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3b143519-2fe3-f1e8-f889-77a9d36a1540.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationHangerSizeNotMatch Property

---



|  |
| --- |
| [BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)   [See Also](#seeAlsoToggle) |

The hanger size does not match the size of the host, so it can not be connected.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FabricationHangerSizeNotMatch { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationHangerSizeNotMatch As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FabricationHangerSizeNotMatch { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b17583b-b874-1744-5686-a638d344ec8b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetEnumerator Method

---



|  |
| --- |
| [VertexIndexPairArray Class](ebf9396b-0cd1-2510-3957-80cd871a9db7.htm)   [See Also](#seeAlsoToggle) |

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

[VertexIndexPairArray Class](ebf9396b-0cd1-2510-3957-80cd871a9db7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b1ad4d2-8e3a-d0aa-e9cc-d5dd841c9542.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InvalidSlantedColumnOffsetsInNestedFamily Property

---



|  |
| --- |
| [BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)   [See Also](#seeAlsoToggle) |

Instance of family [Family Name] can't be updated because in nested family the column's base (Base Level + Base Offset) must be below its top (Top Level + Top Offset).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId InvalidSlantedColumnOffsetsInNestedFamily { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InvalidSlantedColumnOffsetsInNestedFamily As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ InvalidSlantedColumnOffsetsInNestedFamily { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b2163e0-fe34-a8a2-6c57-6d39e7769021.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomPhaseId Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Phase Id"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RoomPhaseId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoomPhaseId As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RoomPhaseId { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b22e25e-f934-3931-6f22-e451ffcc11b0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IndexLine Class

---



|  |
| --- |
| [Members](8018ef77-be41-4e85-dbab-c59e668039f2.htm)   [See Also](#seeAlsoToggle) |

A line segment primitive consisting of two indices.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public class IndexLine : IndexPrimitive ``` |

 

| Visual Basic |
| --- |
| ``` Public Class IndexLine _ 	Inherits IndexPrimitive ``` |

 

| Visual C++ |
| --- |
| ``` public ref class IndexLine : public IndexPrimitive ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB.DirectContext3D IndexPrimitive](b9718ac0-7194-1944-ce7f-a5c618f20ced.htm)    
  Autodesk.Revit.DB.DirectContext3D IndexLine

# See Also

[IndexLine Members](8018ef77-be41-4e85-dbab-c59e668039f2.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__3b257113-5220-c9df-dd3c-50e1e28b847b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RotationAngle Property

---



|  |
| --- |
| [IndependentTag Class](e52073e2-9d98-6fb5-eb43-288cf9ed2e28.htm)   [See Also](#seeAlsoToggle) |

The rotation angle of the tag relative to its view

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public double RotationAngle { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RotationAngle As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double RotationAngle { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: Angle can only be changed for AnyModelDirection orientation |

# See Also

[IndependentTag Class](e52073e2-9d98-6fb5-eb43-288cf9ed2e28.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b25dee2-4aa7-1aa9-dc0c-c4b7ce36945f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathReinEndSpanhookPrim Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"End Hook Angle Primary"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PathReinEndSpanhookPrim { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PathReinEndSpanhookPrim As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PathReinEndSpanhookPrim { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b279e84-422c-ddc4-44df-fa5498124b14.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewActivatingEventArgs Class

---



|  |
| --- |
| [Members](4807ca42-0b76-8f20-38a4-806bfb8a03cc.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by the ViewActivating event.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public class ViewActivatingEventArgs : RevitAPIPreDocEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ViewActivatingEventArgs _ 	Inherits RevitAPIPreDocEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ViewActivatingEventArgs : public RevitAPIPreDocEventArgs ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPreEventArgs](14097470-c9d9-0143-dc1b-b93a60a460e6.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPreDocEventArgs](ef0073c4-f86b-64b9-12f2-268f4e1b8bbe.htm)    
  Autodesk.Revit.UI.Events ViewActivatingEventArgs

# See Also

[ViewActivatingEventArgs Members](4807ca42-0b76-8f20-38a4-806bfb8a03cc.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__3b31273c-bcf8-818c-62ca-7761e2e8c27f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PinnedFabricationPartNotChangeExtension Property

---



|  |
| --- |
| [BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)   [See Also](#seeAlsoToggle) |

Failed to change extension of part.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId PinnedFabricationPartNotChangeExtension { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PinnedFabricationPartNotChangeExtension As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ PinnedFabricationPartNotChangeExtension { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b356471-a29d-a1f4-d61d-4c3bf7c0d358.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CantCopyFrom2dTo3dFam Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

Can't copy 2D element(s) into a 3D family.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CantCopyFrom2dTo3dFam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CantCopyFrom2dTo3dFam As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CantCopyFrom2dTo3dFam { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b3a2c2f-32ff-92ee-68d8-41f98e35e0de.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnableToMakeConnectionInDirection Property

---



|  |
| --- |
| [BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)   [See Also](#seeAlsoToggle) |

The application is unable to make a connection in that direction. If the connectors are pointing up, make sure that the elevations of the segments (ducts and pipes) are above them. If the connectors are pointing down, make sure that the elevations of the segments (ducts and pipes) are below them.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId UnableToMakeConnectionInDirection { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property UnableToMakeConnectionInDirection As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ UnableToMakeConnectionInDirection { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b3b58bd-187a-47b8-840f-fa5e858f731b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsStackedWallMember Property

---



|  |
| --- |
| [Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)   [See Also](#seeAlsoToggle) |

Identifies if the wall is a member of a stacked wall.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool IsStackedWallMember { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsStackedWallMember As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsStackedWallMember { 	bool get (); } ``` |

# See Also

[Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b3d671d-47ec-2ed8-1818-a7c19d01884b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OpenAndActivateDocument Method (String)

---



|  |
| --- |
| [UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)   [See Also](#seeAlsoToggle) |

Opens and activates a Revit document.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public UIDocument OpenAndActivateDocument( 	string fileName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function OpenAndActivateDocument ( _ 	fileName As String _ ) As UIDocument ``` |

 

| Visual C++ |
| --- |
| ``` public: UIDocument^ OpenAndActivateDocument( 	String^ fileName ) ``` |

#### Parameters

fileName
:   Type:  System String    
     A full path to a revit file to be opened. The file can be either a Revit project, template, or family document.

#### Return Value

The opened document.

# Remarks

This method, if successful, changes the active document. It is not allowed to have an open transaction in the active document when calling this method. Additionally, this method may not be called from inside an event handler.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given 'fileName' is not a Revit file (a project, template, or family document). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | If    a null reference (  Nothing  in Visual Basic)  is passed as 'fileName'. -or- A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The file specified by 'fileName' cannot be found. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | * If the active document is currently modifiable. * If an API event handler is currently being executed. |
| [Autodesk.Revit.Exceptions RevitServerCommunicationException](a0003d89-0113-6623-65da-0db5c568bfb6.htm) | If there is any server internal error. |

# See Also

[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)

[OpenAndActivateDocument Overload](5018fbdb-e7c3-6e32-7ca3-ee5c20dbc56f.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__3b3dba69-ee23-51f0-1299-83ff109fb4b4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LayeredFraction Property

---



|  |
| --- |
| [AdvancedLayered Class](308d3112-a63f-0c76-7737-8cf201454790.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Fraction" from the "AdvancedLayered" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string LayeredFraction { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LayeredFraction As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ LayeredFraction { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble". This property allows a connected asset.

# See Also

[AdvancedLayered Class](308d3112-a63f-0c76-7737-8cf201454790.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3b3fa530-b0c4-cc72-a10d-69b236e8781c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricAreaLapSplicesIncorrect Property

---



|  |
| --- |
| [BuiltInFailures FabricAreaFailures Class](5f812624-6bf0-37fc-971a-421ca56a151d.htm)   [See Also](#seeAlsoToggle) |

Fabric Area lap splice is incorrect.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FabricAreaLapSplicesIncorrect { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricAreaLapSplicesIncorrect As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FabricAreaLapSplicesIncorrect { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FabricAreaFailures Class](5f812624-6bf0-37fc-971a-421ca56a151d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b423e14-35bb-db8b-fd20-c22b239bdb38.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TileLineShift Property

---



|  |
| --- |
| [Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Line Shift" from the "Tile" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TileLineShift { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TileLineShift As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TileLineShift { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble" within the range of "0, 100".

# See Also

[Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3b4352ce-a453-421c-1a3f-e8834620a9da.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalModelBaseAlignmentMethod Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Base Alignment Method"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnalyticalModelBaseAlignmentMethod { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticalModelBaseAlignmentMethod As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnalyticalModelBaseAlignmentMethod { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b47a813-1bde-865b-98ce-330caaebc48a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [RoutingConditions Class](15fcc55d-b099-6ed4-1915-8beaee70b596.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [RoutingConditions](15fcc55d-b099-6ed4-1915-8beaee70b596.htm)

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

[RoutingConditions Class](15fcc55d-b099-6ed4-1915-8beaee70b596.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b49b235-96f1-7215-004f-f0b779ba1571.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForwardIterator Method

---



|  |
| --- |
| [MEPBuildingConstructionSet Class](fbe2c9fe-89ea-fc75-e418-cebc452ca1dd.htm)   [See Also](#seeAlsoToggle) |

Retrieve a forward moving iterator to the set.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual MEPBuildingConstructionSetIterator ForwardIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ForwardIterator As MEPBuildingConstructionSetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual MEPBuildingConstructionSetIterator^ ForwardIterator() ``` |

#### Return Value

Returns a forward moving iterator to the set.

# See Also

[MEPBuildingConstructionSet Class](fbe2c9fe-89ea-fc75-e418-cebc452ca1dd.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__3b4a64f9-b794-c7f8-4f20-b028d5cc0b9e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MetalFinish Property

---



|  |
| --- |
| [Metal Class](618a6255-d79c-e405-6804-994c56317dc4.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Finish" from the "Metal" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string MetalFinish { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MetalFinish As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ MetalFinish { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyInteger" with accepted values in the enumerated type "MetalFinishType".

# See Also

[Metal Class](618a6255-d79c-e405-6804-994c56317dc4.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__3b4d7726-f4de-f10f-4a14-8cf4a3912a4d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CustomDataExists Method

---



|  |
| --- |
| [FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)   [See Also](#seeAlsoToggle) |

Checks to see if the specified custom data exists.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool CustomDataExists( 	int customDataId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CustomDataExists ( _ 	customDataId As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CustomDataExists( 	int customDataId ) ``` |

#### Parameters

customDataId
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The custom data identifier.

#### Return Value

Returns true if the custom data exists.

# See Also

[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b512e73-a626-b0a0-42b7-a8bd0f6e2ca9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DuctShape Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Enumerated type listing possible shapes for ducts.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum DuctShape ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration DuctShape ``` |

 

| Visual C++ |
| --- |
| ``` public enum class DuctShape ``` |

# Members

| Member name | Description |
| --- | --- |
| Round | Round duct shape. |
| Rectangular | Rectangular duct shape. |
| Oval | Oval duct shape. |

# See Also

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__3b527b0f-dae3-6146-60df-765426f1876f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurveBottomLevel Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bottom Level"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CurveBottomLevel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CurveBottomLevel As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CurveBottomLevel { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b5b0548-1ae5-5c04-cb86-615dfa503de8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsRailingRailHeight Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Rail Height"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsRailingRailHeight { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsRailingRailHeight As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsRailingRailHeight { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b5dda8c-f9a9-683c-959c-789e454978ab.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Size Property

---



|  |
| --- |
| [WireSet Class](44035985-f6a1-72de-ae57-ac08507c8bbb.htm)   [See Also](#seeAlsoToggle) |

Returns the number of objects that are in the set.

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

[WireSet Class](44035985-f6a1-72de-ae57-ac08507c8bbb.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3b6086d3-65f7-8b3f-51c8-d261ad0be933.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DamperExists Method

---



|  |
| --- |
| [FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)   [See Also](#seeAlsoToggle) |

Checks to see if the specified damper exists.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool DamperExists( 	int damperId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function DamperExists ( _ 	damperId As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool DamperExists( 	int damperId ) ``` |

#### Parameters

damperId
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The damper identifier to check.

#### Return Value

Returns true if the damper exists.

# See Also

[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b640fff-8676-9a8e-d541-083e5b0ddd31.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [FilteredElementIdIterator Class](dfd0acee-d626-d5b2-fa2a-f9fc4edb49e8.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [FilteredElementIdIterator](dfd0acee-d626-d5b2-fa2a-f9fc4edb49e8.htm)

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

[FilteredElementIdIterator Class](dfd0acee-d626-d5b2-fa2a-f9fc4edb49e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b659498-23da-879d-011f-d61da8fafa51.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [FilteredWorksetIdIterator Class](3d4b2969-fe55-7b1a-bdc0-b60165e12856.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [FilteredWorksetIdIterator](3d4b2969-fe55-7b1a-bdc0-b60165e12856.htm)

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

[FilteredWorksetIdIterator Class](3d4b2969-fe55-7b1a-bdc0-b60165e12856.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b65b2e6-e868-09bf-9c35-a92c083aeaf2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEmpty Property

---



|  |
| --- |
| [TemperatureRatingTypeSet Class](572d809d-fc08-6038-5279-b43903e9a6b8.htm)   [See Also](#seeAlsoToggle) |

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

[TemperatureRatingTypeSet Class](572d809d-fc08-6038-5279-b43903e9a6b8.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3b67078d-f8fd-83f4-ee2e-b83e8ec23a23.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Build Method

---



|  |
| --- |
| [TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)   [See Also](#seeAlsoToggle) |

Builds the designated geometrical objects from the stored face sets. Stores the result in this TessellatedShapeBuilder object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void Build() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Build ``` |

 

| Visual C++ |
| --- |
| ``` public: void Build() ``` |

# Remarks

The behavior of this function is affected by Target, Fallback and GStyleId properties of this TessellatedShapeBuilder object. Currently only "Solid/Abort", "AnyGeometry/Mesh" and "Mesh/Salvage" target/fallback combinations are supported. Note that this function does not erase the face sets stored in the builder. If the same builder is used to construct geometrical objects for different collections of face sets, (  [Clear](8c2cd942-f8c3-3288-bac6-8d4d1f064714.htm)  ) should be called while switching from one collection to another.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Throws if data in the stored face sets are so inconsistent, that they cannot be used in their entirety, or if an attempt is made to create unacceptable geometry with too many facets. |

# See Also

[TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b690620-3881-ee14-72dc-33e7df239417.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetOffsetForIntersectingReference Method

---



|  |
| --- |
| [PartMakerMethodToDivideVolumes Class](611ca5f7-3ffb-6f83-3aaf-df4533038ed0.htm)   [See Also](#seeAlsoToggle) |

Gets offset for the intersecting reference.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double GetOffsetForIntersectingReference( 	ElementId intersectingReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetOffsetForIntersectingReference ( _ 	intersectingReference As ElementId _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetOffsetForIntersectingReference( 	ElementId^ intersectingReference ) ``` |

#### Parameters

intersectingReference
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The intersecting reference to obtain offset value from.

#### Return Value

The offset for the intersecting reference

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | PartMaker does not use the specified intersecting reference. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartMakerMethodToDivideVolumes Class](611ca5f7-3ffb-6f83-3aaf-df4533038ed0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b71f55f-76af-55e2-814b-1dd4553671bb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ExternalResourceSubFolder Class](b9b20e80-9af0-557b-7a3e-a35168c5eab0.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ExternalResourceSubFolder](b9b20e80-9af0-557b-7a3e-a35168c5eab0.htm)

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
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

[ExternalResourceSubFolder Class](b9b20e80-9af0-557b-7a3e-a35168c5eab0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b747951-4e30-6ad1-4ff7-02557d8ff691.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLinePatternElementByName Method

---



|  |
| --- |
| [LinePatternElement Class](8f4678ba-1824-fd00-73b6-dfb9c7802f83.htm)   [See Also](#seeAlsoToggle) |

Retrieves the LinePatternElement by its name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static LinePatternElement GetLinePatternElementByName( 	Document document, 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetLinePatternElementByName ( _ 	document As Document, _ 	name As String _ ) As LinePatternElement ``` |

 

| Visual C++ |
| --- |
| ``` public: static LinePatternElement^ GetLinePatternElementByName( 	Document^ document,  	String^ name ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to retrieve the LinePatternElement.

name
:   Type:  System String    
     The name of the LinePatternElement.

#### Return Value

The LinePatternElement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[LinePatternElement Class](8f4678ba-1824-fd00-73b6-dfb9c7802f83.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b754027-2f58-c902-e232-073a663ab85b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PercentageGlazing Property

---



|  |
| --- |
| [EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)   [See Also](#seeAlsoToggle) |

Used for the conceptual energy model. The approximate percentage of the building exterior wall surfaces which are covered by windows or other glazing.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public double PercentageGlazing { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PercentageGlazing As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double PercentageGlazing { 	double get (); 	void set (double value); } ``` |

# Remarks

This value is used to automatically model these glazed openings in massing instances for the Conceptual Energy Analytical Model.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The percentage glazing value is not between 0.00 and 0.95. |

# See Also

[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3b76b99d-65c3-d2b9-25ad-8069da549af1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddTab Method

---



|  |
| --- |
| [DisplayingOptionsDialogEventArgs Class](b803dfe4-f87c-ec59-a04c-89900c74bd10.htm)   [See Also](#seeAlsoToggle) |

Add tab to option dialog with tab name and handler information.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void AddTab( 	string newTabName, 	TabbedDialogExtension tabbedDialogExtension ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddTab ( _ 	newTabName As String, _ 	tabbedDialogExtension As TabbedDialogExtension _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddTab( 	String^ newTabName,  	TabbedDialogExtension^ tabbedDialogExtension ) ``` |

#### Parameters

newTabName
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The new tab page name.

tabbedDialogExtension
:   Type:  [Autodesk.Revit.UI TabbedDialogExtension](06ae60a6-3fbe-c334-ee00-ae9628e2169a.htm)    
     The handlers information for the new tab page.

# Remarks

There is a limit to the number of options page permitted in the dialog.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the limit of pages allowed in the Options dialog will be exceeded (99). |

# See Also

[DisplayingOptionsDialogEventArgs Class](b803dfe4-f87c-ec59-a04c-89900c74bd10.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__3b78e1fa-58d2-2e47-9955-78646763fdd0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlaceInstance Method

---



|  |
| --- |
| [AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.htm)   [See Also](#seeAlsoToggle) |

Places an assembly instance of a given assembly type at the specified location.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static AssemblyInstance PlaceInstance( 	Document document, 	ElementId assemblyTypeId, 	XYZ location ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function PlaceInstance ( _ 	document As Document, _ 	assemblyTypeId As ElementId, _ 	location As XYZ _ ) As AssemblyInstance ``` |

 

| Visual C++ |
| --- |
| ``` public: static AssemblyInstance^ PlaceInstance( 	Document^ document,  	ElementId^ assemblyTypeId,  	XYZ^ location ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document for the new assembly instance.

assemblyTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the assembly type to be used for the instance.

location
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The placement location for the instance in project coordinates.

#### Return Value

The newly created assembly instance.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AssemblyInstance Class](4e60704c-dfe3-72b6-7892-6440503fa078.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b7b6087-d17b-c916-4896-94254dab08c7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConvertFaceRegionsToFacesCrashed Property

---



|  |
| --- |
| [BuiltInFailures GeometryFailures Class](6c30543b-4a09-53d0-0867-a2c2c49a4e57.htm)   [See Also](#seeAlsoToggle) |

Failed to replace an instance face with its face regions.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ConvertFaceRegionsToFacesCrashed { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ConvertFaceRegionsToFacesCrashed As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ConvertFaceRegionsToFacesCrashed { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GeometryFailures Class](6c30543b-4a09-53d0-0867-a2c2c49a4e57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b7d9168-aaa1-9efa-cc74-d384736e62c7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForceVector2 Property

---



|  |
| --- |
| [LineLoad Class](ee5ec273-350a-1cdb-d136-0c454bb1446a.htm)   [See Also](#seeAlsoToggle) |

The force vector applied to the end point of the line load, oriented according to OrientTo setting.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public XYZ ForceVector2 { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ForceVector2 As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ ForceVector2 { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

The default force unit is kN/m for metric, and kip/ft for imperial. Use UnitUtils class methods to convert value from or to internal units.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[LineLoad Class](ee5ec273-350a-1cdb-d136-0c454bb1446a.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3b81a9f7-f72c-12f2-206d-bf7b4165b525.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ServerId Property

---



|  |
| --- |
| [LinkConversionData Class](2d05cfbb-8386-d1c6-b751-fe6f57dc2b63.htm)   [See Also](#seeAlsoToggle) |

The service responsible for converting the data into a Revit file.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public Guid ServerId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ServerId As Guid 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Guid ServerId { 	Guid get (); } ``` |

# See Also

[LinkConversionData Class](2d05cfbb-8386-d1c6-b751-fe6f57dc2b63.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b8b0e94-5765-aa0d-0dbe-6612ed9183f1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StopOnError Property

---



|  |
| --- |
| [DWFExportOptions Class](e83b223d-b846-027e-8859-7ea5b89ea685.htm)   [See Also](#seeAlsoToggle) |

Whether export process should stop when a view fails to export.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool StopOnError { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property StopOnError As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool StopOnError { 	bool get (); 	void set (bool value); } ``` |

# Remarks

If set to false, the export would continue until all views are processed. This option has an effect only when a set of more than one view is specified.

# See Also

[DWFExportOptions Class](e83b223d-b846-027e-8859-7ea5b89ea685.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b8d6b55-0cab-1810-1188-840800e5eaa2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementLogicalFilter Class

---



|  |
| --- |
| [Members](a12ccff6-75e6-fc39-b0a4-894d9a3554af.htm)   [See Also](#seeAlsoToggle) |

A filter used to logically combine two or more filters.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class ElementLogicalFilter : ElementFilter ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ElementLogicalFilter _ 	Inherits ElementFilter ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ElementLogicalFilter : public ElementFilter ``` |

# Remarks

The component filters may be reordered by Revit to cause the quickest acting filters to be evaluated first.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB ElementFilter](b8b46cbf-9ecc-0745-ec53-c3c3b6510113.htm)    
  Autodesk.Revit.DB ElementLogicalFilter    
  [Autodesk.Revit.DB LogicalAndFilter](3e334aaf-2b39-58bd-d2cc-94e9c89bac57.htm)    
  [Autodesk.Revit.DB LogicalOrFilter](a00da224-d330-452d-a45f-5abffa2e57e6.htm)

# See Also

[ElementLogicalFilter Members](a12ccff6-75e6-fc39-b0a4-894d9a3554af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b91b85e-1879-aa8b-8849-abecb0767927.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarInternalMultiplanarDuplicate Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"INTERNAL: Multiplanar Duplicate"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarInternalMultiplanarDuplicate { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarInternalMultiplanarDuplicate As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarInternalMultiplanarDuplicate { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b95d9e4-d12f-121d-3e33-4209fa3d8c52.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FlowDirection Property

---



|  |
| --- |
| [PipeFittingAndAccessoryConnectorData Class](f1233bf2-ec6a-67a6-50d0-b7ae1382c64e.htm)   [See Also](#seeAlsoToggle) |

The flow direction of this connector, In or Out.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public FlowDirectionType FlowDirection { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property FlowDirection As FlowDirectionType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property FlowDirectionType FlowDirection { 	FlowDirectionType get (); } ``` |

# See Also

[PipeFittingAndAccessoryConnectorData Class](f1233bf2-ec6a-67a6-50d0-b7ae1382c64e.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__3b989793-1ed9-3d70-e630-514123f57e7c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TrussShiftedReferences Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Truss top and bottom references (chains of one or more reference lines) must overlap at least partially in the vertical direction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId TrussShiftedReferences { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TrussShiftedReferences As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ TrussShiftedReferences { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3b9c5835-a3a7-8d7c-3eb3-34e4d03d7dff.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMassEnergyAnalyticalModelIdForMassInstance Method

---



|  |
| --- |
| [MassEnergyAnalyticalModel Class](1e8b2837-0572-d788-a6eb-db5060fc423c.htm)   [See Also](#seeAlsoToggle) |

Get the ElementId of the MassEnergyAnalyticalModel for a mass instance.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static ElementId GetMassEnergyAnalyticalModelIdForMassInstance( 	Document document, 	ElementId massInstanceId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetMassEnergyAnalyticalModelIdForMassInstance ( _ 	document As Document, _ 	massInstanceId As ElementId _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ GetMassEnergyAnalyticalModelIdForMassInstance( 	Document^ document,  	ElementId^ massInstanceId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document.

massInstanceId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     ElementId of a mass instance.

#### Return Value

ElementId of a MassEnergyAnalyticalModel.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The ElementId massInstanceId is not a mass instance. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MassEnergyAnalyticalModel Class](1e8b2837-0572-d788-a6eb-db5060fc423c.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3b9f2298-d268-34b0-405f-754557e1ca49.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [VertexBuffer](329e5617-ce46-a993-1131-85c64f0842f2.htm)

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

[VertexBuffer Class](329e5617-ce46-a993-1131-85c64f0842f2.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__3b9f3b78-d7b4-ba9c-92b1-0d32a7c3716c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsAttrStairsBottom Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Underside of Winder"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsAttrStairsBottom { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsAttrStairsBottom As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsAttrStairsBottom { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ba02d83-443a-2e7f-fa12-6ce9f30e531a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FieldId Property

---



|  |
| --- |
| [ScheduleSortGroupField Class](526680eb-ea68-35a7-b0c5-d63459fac04d.htm)   [See Also](#seeAlsoToggle) |

The ID of the field that the schedule will be sorted or grouped by.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ScheduleFieldId FieldId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FieldId As ScheduleFieldId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ScheduleFieldId^ FieldId { 	ScheduleFieldId^ get (); 	void set (ScheduleFieldId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ScheduleSortGroupField Class](526680eb-ea68-35a7-b0c5-d63459fac04d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ba25c52-38b9-2908-c073-3632537977a6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidSpecificFittingAngle Method

---



|  |
| --- |
| [ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)   [See Also](#seeAlsoToggle) |

Checks that the given value is a valid specific fitting angle. The specific fitting angles are angles of 90, 60, 45, 30, 22.5 or 11.25 degrees.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsValidSpecificFittingAngle( 	double angle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidSpecificFittingAngle ( _ 	angle As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidSpecificFittingAngle( 	double angle ) ``` |

#### Parameters

angle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The angle value (in degree).

#### Return Value

True if the given value is a valid specific fitting angle.

# See Also

[ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__3ba5cf6d-0e62-e6cf-49c7-e16af844c83b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Resolution Property

---



|  |
| --- |
| [ConnectionValidationWarning Class](610c2f13-1d95-3a43-b845-b39ab3f02d46.htm)   [See Also](#seeAlsoToggle) |

Enumeration for resolution that was applied.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public ConnectionResolution Resolution { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Resolution As ConnectionResolution 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ConnectionResolution Resolution { 	ConnectionResolution get (); } ``` |

# See Also

[ConnectionValidationWarning Class](610c2f13-1d95-3a43-b845-b39ab3f02d46.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3ba94bad-a426-0f12-ba41-05f7cd0637bc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetOffset Method

---



|  |
| --- |
| [PlanViewRange Class](7edc5f13-a5fa-5c7a-9a03-ac6cbed1f005.htm)   [See Also](#seeAlsoToggle) |

Set the offset value associated with a View Depth plane

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetOffset( 	PlanViewPlane planViewPlane, 	double offset ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetOffset ( _ 	planViewPlane As PlanViewPlane, _ 	offset As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetOffset( 	PlanViewPlane planViewPlane,  	double offset ) ``` |

#### Parameters

planViewPlane
:   Type:  [Autodesk.Revit.DB PlanViewPlane](80d20187-97ea-f6c0-a3a8-d5545e0b3863.htm)    
     View Depth plane

offset
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Offset value

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[PlanViewRange Class](7edc5f13-a5fa-5c7a-9a03-ac6cbed1f005.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3bad88bc-139c-a0a9-39b6-4c048ef2313a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [KeyBasedTreeEntriesIterator Class](d842419d-d2a9-a839-0944-82f163884362.htm)   [See Also](#seeAlsoToggle) |

Gets the item at the current position of the iterator.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public virtual KeyBasedTreeEntry Current { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable ReadOnly Property Current As KeyBasedTreeEntry 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property KeyBasedTreeEntry^ Current { 	KeyBasedTreeEntry^ get (); } ``` |

#### Implements

 [IEnumerator T Current](http://msdn2.microsoft.com/en-us/library/58e146b7)

# Remarks

There is no current item if the iterator has not started yet or has been done.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | There is no current item in the iterator. |

# See Also

[KeyBasedTreeEntriesIterator Class](d842419d-d2a9-a839-0944-82f163884362.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3bb1dbe4-c356-a4d0-ab2c-67d6ef1063e5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProductSpecificationDescription Property

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

The product specification description of the fabrication part.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public string ProductSpecificationDescription { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ProductSpecificationDescription As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ ProductSpecificationDescription { 	String^ get (); } ``` |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3bb3ec29-db01-161b-8158-09fbda364603.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRegisteredResults Method

---



|  |
| --- |
| [SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)   [See Also](#seeAlsoToggle) |

Returns an array of indices of all registered results

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<int> GetRegisteredResults() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRegisteredResults As IList(Of Integer) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<int>^ GetRegisteredResults() ``` |

# See Also

[SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__3bb6037d-39be-3517-c0ad-3921b39803ca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlanTopologySet Constructor

---



|  |
| --- |
| [PlanTopologySet Class](37cd93b8-bed4-0000-a389-48d5305d908e.htm)   [See Also](#seeAlsoToggle) |

Initializes a new instance of the  [PlanTopologySet](37cd93b8-bed4-0000-a389-48d5305d908e.htm)  class

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PlanTopologySet() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: PlanTopologySet() ``` |

# See Also

[PlanTopologySet Class](37cd93b8-bed4-0000-a389-48d5305d908e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3bb99a25-ae9d-6b16-3bc5-8f281f5e50bb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetCutForegroundPatternId Method

---



|  |
| --- |
| [OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)   [See Also](#seeAlsoToggle) |

Sets the ElementId of the cut face foreground pattern override. The fill pattern must be a drafting pattern. A value of InvalidElementId means no override is set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public OverrideGraphicSettings SetCutForegroundPatternId( 	ElementId fillPatternId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetCutForegroundPatternId ( _ 	fillPatternId As ElementId _ ) As OverrideGraphicSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: OverrideGraphicSettings^ SetCutForegroundPatternId( 	ElementId^ fillPatternId ) ``` |

#### Parameters

fillPatternId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Value of the cut face foreground fill pattern override.

#### Return Value

Reference to the changed object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3bc901fb-7137-9258-fa47-a2deea91a96b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsRuntypeStructuralDepth Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Structural Depth": Structural Depth

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsRuntypeStructuralDepth { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsRuntypeStructuralDepth As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsRuntypeStructuralDepth { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3bca4d88-f5df-a42a-7a75-87bf173c2ac7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SharedParameterApplicableRule Constructor

---



|  |
| --- |
| [SharedParameterApplicableRule Class](64d80468-27ac-8acb-25f1-48bc3597ab87.htm)   [See Also](#seeAlsoToggle) |

Constructs an instance of SharedParameterApplicableRule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public SharedParameterApplicableRule( 	string parameterName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	parameterName As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: SharedParameterApplicableRule( 	String^ parameterName ) ``` |

#### Parameters

parameterName
:   Type:  System String    
     The name of the parameter that an element must support to pass this rule.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SharedParameterApplicableRule Class](64d80468-27ac-8acb-25f1-48bc3597ab87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3bcbd93e-b382-4465-5a38-71167d93143e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MoreThanOneAxis Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

More than one axes of revolution.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId MoreThanOneAxis { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MoreThanOneAxis As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ MoreThanOneAxis { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3bcbe179-de35-86d8-6ae7-9bd60c1a22c3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpacingJustificationn2 Property

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
| ``` public static ForgeTypeId SpacingJustificationn2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpacingJustificationn2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpacingJustificationn2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3bcff20d-5715-10c6-a3b6-affee02e1263.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LapSplicePosition Property

---



|  |
| --- |
| [FabricArea Class](b8e6a637-e069-500d-b7d3-3500e1728681.htm)   [See Also](#seeAlsoToggle) |

The fabric lap splice position in the fabric distribution.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public FabricLapSplicePosition LapSplicePosition { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LapSplicePosition As FabricLapSplicePosition 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property FabricLapSplicePosition LapSplicePosition { 	FabricLapSplicePosition get (); 	void set (FabricLapSplicePosition value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[FabricArea Class](b8e6a637-e069-500d-b7d3-3500e1728681.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3bd18510-778a-2383-7334-f028e178732a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricParamCutByHost Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Cut by Host Cover": Single Fabric Sheet is cut or not cut by the Host Cover.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FabricParamCutByHost { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricParamCutByHost As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FabricParamCutByHost { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3bd2e404-2705-ad16-42c3-42c808890bb4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRefPoint Method

---



|  |
| --- |
| [AreaLoad Class](5dc205a9-cafd-911b-6a56-26f2e8bfcdc1.htm)   [See Also](#seeAlsoToggle) |

Returns the physical location of the reference point.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public XYZ GetRefPoint( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRefPoint ( _ 	index As Integer _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetRefPoint( 	int index ) ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the point to return.

# Remarks

The index should be between 0 and less than NumRefPoints.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when index is out of range. |

# See Also

[AreaLoad Class](5dc205a9-cafd-911b-6a56-26f2e8bfcdc1.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3bd3fa1d-dc68-86a7-86fb-c5fe91bb9491.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRibbonPanels Method (Tab)

---



|  |
| --- |
| [ApplicationEntryPoint Class](7ff0ad2b-7713-ec77-ccc9-8a01fffcf83e.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.UI.Macros](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public override List<RibbonPanel> GetRibbonPanels( 	Tab tab ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Function GetRibbonPanels ( _ 	tab As Tab _ ) As List(Of RibbonPanel) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual List<RibbonPanel^>^ GetRibbonPanels( 	Tab tab ) override ``` |

#### Parameters

tab
:   Type:  [Autodesk.Revit.UI Tab](bfde6ca7-941b-744c-a91a-2d85bbcff9bf.htm)

# See Also

[ApplicationEntryPoint Class](7ff0ad2b-7713-ec77-ccc9-8a01fffcf83e.htm)

[GetRibbonPanels Overload](5792a404-20b3-d513-5db9-16046bc72fe9.htm)

[Autodesk.Revit.UI.Macros Namespace](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)

<!-- Start of Syntax__3bd52d75-7aea-1d0f-0ff6-0eae6b9a4928.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HostElementId Property

---



|  |
| --- |
| [InsulationLiningBase Class](938d1b57-b9bb-44b0-81ec-c22dff57fc8e.htm)   [See Also](#seeAlsoToggle) |

The id of the host element for the insulation or lining element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementId HostElementId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HostElementId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ HostElementId { 	ElementId^ get (); } ``` |

# See Also

[InsulationLiningBase Class](938d1b57-b9bb-44b0-81ec-c22dff57fc8e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3bddfeb2-4db2-1bf1-b7e8-09238c8dfb32.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathReinforcementType Class

---



|  |
| --- |
| [Members](21dc42b0-67dd-b3a6-6445-fe071a41b5ed.htm)   [See Also](#seeAlsoToggle) |

An object that specifies the type of a Structural Path Reinforcement element in Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class PathReinforcementType : ElementType ``` |

 

| Visual Basic |
| --- |
| ``` Public Class PathReinforcementType _ 	Inherits ElementType ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PathReinforcementType : public ElementType ``` |

# Remarks

The clear cover settings can be accessed via this object.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  Autodesk.Revit.DB.Structure PathReinforcementType

# See Also

[PathReinforcementType Members](21dc42b0-67dd-b3a6-6445-fe071a41b5ed.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3be0c01e-d21a-62de-5e9f-0186fdcfc5fe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Flow Property

---



|  |
| --- |
| [PipePressureDropData Class](d9c2df4c-512f-3f0c-4c04-2f5cc5afa7d8.htm)   [See Also](#seeAlsoToggle) |

The flow of the pipe. Units: (ftÂ³/s).

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public double Flow { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Flow As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Flow { 	double get (); } ``` |

# See Also

[PipePressureDropData Class](d9c2df4c-512f-3f0c-4c04-2f5cc5afa7d8.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__3be46c98-e6ee-21a2-fcb5-18f5e24d78af.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Transform1D Constructor (Double, Double)

---



|  |
| --- |
| [Transform1D Class](7366ab0c-173e-ff4b-fb56-4f307cf16bc9.htm)   [See Also](#seeAlsoToggle) |

Constructs the transformation by specifying the scale and the translation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public Transform1D( 	double scale, 	double translation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	scale As Double, _ 	translation As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform1D( 	double scale,  	double translation ) ``` |

#### Parameters

scale
:   Type:  System Double    
     The scale of the transformation.

translation
:   Type:  System Double    
     The translational part of the transformation.

# Remarks

1D space is tranformed according to the following formula: t --> scale\*t + translation

# See Also

[Transform1D Class](7366ab0c-173e-ff4b-fb56-4f307cf16bc9.htm)

[Transform1D Overload](c8d61a46-2668-7dea-1df8-f625081d6258.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3be5900e-4b7b-7197-8a7e-664b7ecc15e5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateGreaterOrEqualRule Method (ElementId, Double, Double)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether double-precision values from the document are greater than or equal to a certain value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateGreaterOrEqualRule( 	ElementId parameter, 	double value, 	double epsilon ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateGreaterOrEqualRule ( _ 	parameter As ElementId, _ 	value As Double, _ 	epsilon As Double _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateGreaterOrEqualRule( 	ElementId^ parameter,  	double value,  	double epsilon ) ``` |

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

# Remarks

Values less than the user-supplied value but within  *epsilon*  are considered equal; therefore, such values satisfy the condition.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for value is not finite -or- The given value for value is not a number -or- The given value for epsilon is not finite -or- The given value for epsilon is not a number |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)

[CreateGreaterOrEqualRule Overload](14d42cfa-d1e6-d955-f2d6-6cabd71679c0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__3be68918-5d12-01f9-c267-b44717592bd4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [RebarReinforcementData Class](04f8cd5d-d4cc-b598-c408-5bd608224b01.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of RebarReinforcementData, or    a null reference (  Nothing  in Visual Basic)  if the operation fails.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static RebarReinforcementData Create( 	ElementId rebarId, 	int iEnd ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	rebarId As ElementId, _ 	iEnd As Integer _ ) As RebarReinforcementData ``` |

 

| Visual C++ |
| --- |
| ``` public: static RebarReinforcementData^ Create( 	ElementId^ rebarId,  	int iEnd ) ``` |

#### Parameters

rebarId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     the Id of the rebar

iEnd
:   Type:  System Int32    
     The end of rebar where the coupler stays. This should be 0 or 1

#### Return Value

Creates a new instance of RebarReinforcementData

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarReinforcementData Class](04f8cd5d-d4cc-b598-c408-5bd608224b01.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__3beb67d2-4fc5-97d2-8314-6e848e11d56a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RailStructure Property

---



|  |
| --- |
| [RailingType Class](7e7551fe-1772-f2d3-a8b5-58d4bb42a34e.htm)   [See Also](#seeAlsoToggle) |

The NonContinuousRailStructure.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public NonContinuousRailStructure RailStructure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property RailStructure As NonContinuousRailStructure 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property NonContinuousRailStructure^ RailStructure { 	NonContinuousRailStructure^ get (); } ``` |

# See Also

[RailingType Class](7e7551fe-1772-f2d3-a8b5-58d4bb42a34e.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__3befd44a-4aee-e83c-369c-4beeebebaef5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPredefinedOptions Method

---



|  |
| --- |
| [DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.htm)   [See Also](#seeAlsoToggle) |

Returns an instance DGNExportOptions containing settings from a predefined export setup.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static DGNExportOptions GetPredefinedOptions( 	Document document, 	string setup ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetPredefinedOptions ( _ 	document As Document, _ 	setup As String _ ) As DGNExportOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: static DGNExportOptions^ GetPredefinedOptions( 	Document^ document,  	String^ setup ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     A Revit project document to retrieve the setup from.

setup
:   Type:  System String    
     The name of a predefined export setup from the specified document.

#### Return Value

An instance of predefined DGNExportOptions, or    a null reference (  Nothing  in Visual Basic)  if the name was not found.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65a0359a-ef13-e7aa-7d5c-7470fe177848.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Commit Method

---



|  |
| --- |
| [SubTransaction Class](801e5f17-cab0-044d-835c-a39592374f89.htm)   [See Also](#seeAlsoToggle) |

Commits all changes made to the model made during the sub-transaction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public TransactionStatus Commit() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Commit As TransactionStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: TransactionStatus Commit() ``` |

#### Return Value

If finished successfully, this method returns TransactionStatus.Committed

# Remarks

The changes are not permanently committed to the document yet. They will be committed only when the active transaction is committed. If the transaction is rolled back instead, the changes committed during this sub-transaction will be discarded.

Commit can be called only when all inner sub-transactions, if any, are already finished, i.e. they were either committed or rolled back. If there is still a sub-transaction open, an attempt to commit this outer sub-transaction will cause an exception.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | A sub-transaction can only be active inside an open Transaction. -or- The sub-transaction's current status is not TransactionStatus.Started, therefore it may not be committed or rolled back. |

# See Also

[SubTransaction Class](801e5f17-cab0-044d-835c-a39592374f89.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65a691e9-773a-5ec9-2249-5f344bf08e83.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FileVersion Property

---



|  |
| --- |
| [ACADExportOptions Class](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)   [See Also](#seeAlsoToggle) |

ACADVersion::Default Default value is ACADVersion.Default.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ACADVersion FileVersion { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FileVersion As ACADVersion 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ACADVersion FileVersion { 	ACADVersion get (); 	void set (ACADVersion value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ACADExportOptions Class](acd35939-8664-f5aa-2287-3eedb8cfdafc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65a997f9-7472-acf2-3983-f92e5e833a2b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Evaluate Method (Int32, Int32)

---



|  |
| --- |
| [FilterNumericRuleEvaluator Class](1f1a96bb-5f00-1a24-8c03-6984c88672b9.htm)   [See Also](#seeAlsoToggle) |

Derived classes should override this method to implement the desired test.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool Evaluate( 	int lhs, 	int rhs ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Evaluate ( _ 	lhs As Integer, _ 	rhs As Integer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Evaluate( 	int lhs,  	int rhs ) ``` |

#### Parameters

lhs
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     A value from an element in the document.

rhs
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The user-supplied value against which values from the document are tested.

#### Return Value

True if  *lhs*  ,  *rhs*  satisfy the condition implemented by this evaluator.

# See Also

[FilterNumericRuleEvaluator Class](1f1a96bb-5f00-1a24-8c03-6984c88672b9.htm)

[Evaluate Overload](2b8a81e5-aacb-22d8-540d-c0239c6491d8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65ae8ae5-6310-a937-913e-de7ff539aaed.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AssetPropertyInt64 Class

---



|  |
| --- |
| [Members](facbb925-a9de-9a85-2bcd-5d7364fbedbc.htm)   [See Also](#seeAlsoToggle) |

Represents a property of Int64 value.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class AssetPropertyInt64 : AssetProperty ``` |

 

| Visual Basic |
| --- |
| ``` Public Class AssetPropertyInt64 _ 	Inherits AssetProperty ``` |

 

| Visual C++ |
| --- |
| ``` public ref class AssetPropertyInt64 : public AssetProperty ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB.Visual AssetProperty](7be89499-d011-ab43-4715-0ee6f9335970.htm)    
  Autodesk.Revit.DB.Visual AssetPropertyInt64

# See Also

[AssetPropertyInt64 Members](facbb925-a9de-9a85-2bcd-5d7364fbedbc.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__65b15c08-d4f2-6200-732b-eac5c01dfe1c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, IList(CurveLoop), IList(XYZ), IList(Int32), IList(Int32), AreaLoadType)

---



|  |
| --- |
| [AreaLoad Class](5dc205a9-cafd-911b-6a56-26f2e8bfcdc1.htm)   [See Also](#seeAlsoToggle) |

Creates a new non-hosted area load within the project.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static AreaLoad Create( 	Document aDoc, 	IList<CurveLoop> loops, 	IList<XYZ> forceVectors, 	IList<int> refPointCurveIndexes, 	IList<int> refPointCurveSelectors, 	AreaLoadType symbol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	aDoc As Document, _ 	loops As IList(Of CurveLoop), _ 	forceVectors As IList(Of XYZ), _ 	refPointCurveIndexes As IList(Of Integer), _ 	refPointCurveSelectors As IList(Of Integer), _ 	symbol As AreaLoadType _ ) As AreaLoad ``` |

 

| Visual C++ |
| --- |
| ``` public: static AreaLoad^ Create( 	Document^ aDoc,  	IList<CurveLoop^>^ loops,  	IList<XYZ^>^ forceVectors,  	IList<int>^ refPointCurveIndexes,  	IList<int>^ refPointCurveSelectors,  	AreaLoadType^ symbol ) ``` |

#### Parameters

aDoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     Document to which new area load will be added.

loops
:   Type:  System.Collections.Generic IList   [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)    
     The loops that define geometry of the area load. The curve loop collection should contains a closed loops consisting of lines.

forceVectors
:   Type:  System.Collections.Generic IList   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The array of force vectors applied to the maximum three reference point of the area load.

refPointCurveIndexes
:   Type:  System.Collections.Generic IList   Int32    
     The array of maximum three curve indexes on which reference points should be placed on.

refPointCurveSelectors
:   Type:  System.Collections.Generic IList   Int32    
     The array of maximum three curve selectors (start or end points) indicating where reference points should be placed on.

symbol
:   Type:  [Autodesk.Revit.DB.Structure AreaLoadType](eb4b548c-059a-d0d7-2431-8203c29dfebd.htm)    
     The symbol of the AreaLoad. Set    a null reference (  Nothing  in Visual Basic)  to use default type.

#### Return Value

If successful, returns an object of the newly created AreaLoad.    a null reference (  Nothing  in Visual Basic)  is returned if the operation fails.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when force vector is equal zero. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if type could not be set for newly created line load. |

# See Also

[AreaLoad Class](5dc205a9-cafd-911b-6a56-26f2e8bfcdc1.htm)

[Create Overload](ad04ec26-96a4-ddc4-305a-e6316cdb6a70.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__65b2d71a-65ed-b90d-b82b-6c04d5587770.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpaceReferenceLevelParam Property

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
| ``` public static ForgeTypeId SpaceReferenceLevelParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpaceReferenceLevelParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpaceReferenceLevelParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65b33ddc-f8b4-c753-0300-70f764ed36d8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadMomentMz1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Mz 1"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LoadMomentMz1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoadMomentMz1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LoadMomentMz1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65b56092-69cf-d374-8e0f-689c91c53586.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetHookOrientationAngle Method

---



|  |
| --- |
| [RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)   [See Also](#seeAlsoToggle) |

Get the hook orientation angle at end.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public double GetHookOrientationAngle( 	int end ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetHookOrientationAngle ( _ 	end As Integer _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetHookOrientationAngle( 	int end ) ``` |

#### Parameters

end
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The end of bar. Should be 0 for start or 1 for end.

#### Return Value

The hook orientation angle at end.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Invalid end. |

# See Also

[RebarFreeFormAccessor Class](bf146aa3-f780-646e-c3cd-42e7a61d18e6.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__65b59d7d-bd7b-c71b-7159-dfc506a912ee.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSection Class

---



|  |
| --- |
| [Members](cc793a0d-9161-e4f4-5914-edb8257153de.htm)   [See Also](#seeAlsoToggle) |

The base class for StructuralSection specific classes, designed to provide common parameters and ability to differentiate between different structural section shapes.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class StructuralSection : IEnumerable,  	IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class StructuralSection _ 	Implements IEnumerable, IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class StructuralSection : IEnumerable,  	IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Structure.StructuralSections StructuralSection    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionRectangular](fc038108-6279-839c-285b-effe342b4491.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionRound](d46f7519-8b60-d73a-42a0-13e0f4455e62.htm)

# See Also

[StructuralSection Members](cc793a0d-9161-e4f4-5914-edb8257153de.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__65b5cb2e-ac1b-fad5-b101-43d26eab6022.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalysisDisplayColoredSurfaceSettings Constructor

---



|  |
| --- |
| [AnalysisDisplayColoredSurfaceSettings Class](fce3c08c-0ec4-4a73-6bbd-975f8b754012.htm)   [See Also](#seeAlsoToggle) |

Constructs a default instance of colored surface settings.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public AnalysisDisplayColoredSurfaceSettings() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: AnalysisDisplayColoredSurfaceSettings() ``` |

# See Also

[AnalysisDisplayColoredSurfaceSettings Class](fce3c08c-0ec4-4a73-6bbd-975f8b754012.htm)

[AnalysisDisplayColoredSurfaceSettings Overload](e401850d-efb6-3fca-c7a5-f961b3c9b8cc.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__65b68477-8c6c-ad75-32ff-1193e2bef945.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BasepointLongitudeParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Lon"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BasepointLongitudeParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BasepointLongitudeParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BasepointLongitudeParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65b98d30-3974-16ca-9cde-7f767fd1406b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CopingColumnBeamFailure Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

The support order for a beam/column connection has been changed. When a beam is supported by a column that same beam cannot be coped by the column. The existing coping has been removed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CopingColumnBeamFailure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CopingColumnBeamFailure As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CopingColumnBeamFailure { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65bd5b22-0211-e66c-18e9-72798ce675d5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ArrayLength Property

---



|  |
| --- |
| [RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)   [See Also](#seeAlsoToggle) |

Identifies the distribution path length of rebar set.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public double ArrayLength { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ArrayLength As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ArrayLength { 	double get (); 	void set (double value); } ``` |

#### Field Value

The distribution path length of rebar set.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: the set length arrayLength isn't acceptable. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | This rebar element represents a single bar (the layout rule is Single). |

# See Also

[RebarContainerItem Class](764f647c-9c3e-b971-1c44-b63f756e1448.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__65beb16f-59ae-07fb-44c3-04b5b37752ec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumberOfNormals Property

---



|  |
| --- |
| [Mesh Class](bf9cd59c-03c3-9e7f-1e2b-6aaf5c425b69.htm)   [See Also](#seeAlsoToggle) |

The number of normals associated with the mesh.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public int NumberOfNormals { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property NumberOfNormals As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int NumberOfNormals { 	int get (); } ``` |

# Remarks

The number is always equal either to '1', or the number of facets, or the number of points. The DistributionOfNormals property indicates how normals are distributed along the polymesh. If there is only one normal available, it applies to the entire mesh. Curved surfaces have normal vectors associated with either every facet or every point/vertex of the tessellated polymesh.

# See Also

[Mesh Class](bf9cd59c-03c3-9e7f-1e2b-6aaf5c425b69.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65beb5e8-3602-4ea7-2cc0-01504211a412.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DPartReinfDeletedEditDivision Property

---



|  |
| --- |
| [BuiltInFailures RebarSystemFailures Class](ef87224e-09b6-8d07-3b24-3a3b322a9ae5.htm)   [See Also](#seeAlsoToggle) |

Edits to the model will cause some Reinforcement hosted on Parts to be deleted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DPartReinfDeletedEditDivision { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DPartReinfDeletedEditDivision As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DPartReinfDeletedEditDivision { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarSystemFailures Class](ef87224e-09b6-8d07-3b24-3a3b322a9ae5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65bf0659-7656-9c84-c183-234f367d0c63.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallNominalThickness Property

---



|  |
| --- |
| [StructuralSectionGeneralH Class](512d0768-c2d3-f601-fd3e-c1db53d68f27.htm)   [See Also](#seeAlsoToggle) |

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

Nominal is measured real value of profile, should be thicker than designed.

# See Also

[StructuralSectionGeneralH Class](512d0768-c2d3-f601-fd3e-c1db53d68f27.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__65c20167-8861-44b5-af98-dd0093adce1f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [FabricationConnectorInfo Class](5da97d87-a3f6-f239-3c5c-102d2d82f942.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [FabricationConnectorInfo](5da97d87-a3f6-f239-3c5c-102d2d82f942.htm)

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

[FabricationConnectorInfo Class](5da97d87-a3f6-f239-3c5c-102d2d82f942.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65c43ffe-3972-ae2b-4aa4-e2901cdbb3a8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NurbSpline Class

---



|  |
| --- |
| [Members](7602714c-85c5-d3ba-e824-8f57590a59c8.htm)   [See Also](#seeAlsoToggle) |

A nurb spline.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class NurbSpline : Curve ``` |

 

| Visual Basic |
| --- |
| ``` Public Class NurbSpline _ 	Inherits Curve ``` |

 

| Visual C++ |
| --- |
| ``` public ref class NurbSpline : public Curve ``` |

# Remarks

The nurb spline lies in the plane defined by control point, weight,knots,degree.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
  Autodesk.Revit.DB NurbSpline

# See Also

[NurbSpline Members](7602714c-85c5-d3ba-e824-8f57590a59c8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65c57f0d-9813-6b85-401d-01bf85f5b944.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TileVerticalCount Property

---



|  |
| --- |
| [Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)   [See Also](#seeAlsoToggle) |

The property labeled "tile\_VerticalCount" from the "Tile" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TileVerticalCount { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TileVerticalCount As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TileVerticalCount { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble" within the range of "0, 100".

# See Also

[Tile Class](2871b849-9a05-b097-d27d-b998e8254311.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__65cba470-671d-bffa-462e-0c4829e1cbe3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallCrossSectionDefinition Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Cross-Section Definition"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId WallCrossSectionDefinition { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WallCrossSectionDefinition As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ WallCrossSectionDefinition { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65cce5b7-21db-94f0-f21b-cc7c41978576.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSolidInView Method

---



|  |
| --- |
| [FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)   [See Also](#seeAlsoToggle) |

Checks if this fabric sheet is shown solidly in a 3D view.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` [ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit. The FabricSheet will always be shown solidly in 3D views with Fine level of detail. To change this, you can override the detail level of view for Structural Fabric Reinforcement category.")] public bool IsSolidInView( 	View3D view ) ``` |

 

| Visual Basic |
| --- |
| ``` <ObsoleteAttribute("This method is deprecated in Revit 2023 and may be removed in a later version of Revit. The FabricSheet will always be shown solidly in 3D views with Fine level of detail. To change this, you can override the detail level of view for Structural Fabric Reinforcement category.")> _ Public Function IsSolidInView ( _ 	view As View3D _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` [ObsoleteAttribute(L"This method is deprecated in Revit 2023 and may be removed in a later version of Revit. The FabricSheet will always be shown solidly in 3D views with Fine level of detail. To change this, you can override the detail level of view for Structural Fabric Reinforcement category.")] public: bool IsSolidInView( 	View3D^ view ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View3D](d795a238-fc24-1875-e64f-a2bef56ae949.htm)    
     The 3D view element

#### Return Value

True if fabric sheet is shown solidly, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | This fabric sheet doesn't have valid visibility data. |

# See Also

[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__65cd0d19-bec2-20c5-daef-89fad225a9e4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsElecPanelMcbRatingParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"MCB Rating"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsElecPanelMcbRatingParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsElecPanelMcbRatingParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsElecPanelMcbRatingParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65cea5ae-be6c-c080-fbcb-34e99cd96b1b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SquareMetersPerSecond Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Square meters per second.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SquareMetersPerSecond { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SquareMetersPerSecond As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SquareMetersPerSecond { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65d623c8-e4af-4b8b-092e-62602d11ecc2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LandingType Property

---



|  |
| --- |
| [StairsType Class](efa84f53-19fa-039b-c5bb-8fcb72e09878.htm)   [See Also](#seeAlsoToggle) |

The type for all landings in the stair element.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId LandingType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LandingType As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ LandingType { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The specified landingTypeId is not a valid landing type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[StairsType Class](efa84f53-19fa-039b-c5bb-8fcb72e09878.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__65d75bca-24ee-c12d-11c3-6b5eb03ef755.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotMakeRoomsGeometry Property

---



|  |
| --- |
| [BuiltInFailures RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.htm)   [See Also](#seeAlsoToggle) |

Could not create geometry for [Room].

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotMakeRoomsGeometry { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotMakeRoomsGeometry As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotMakeRoomsGeometry { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65d77057-176c-ad71-5922-47ed6025e894.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TonOfRefrigeration Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol ton of refrigeration, indicating unit Tons of refrigeration.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TonOfRefrigeration { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TonOfRefrigeration As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TonOfRefrigeration { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65d947f6-178e-eb15-c249-0c82ae3357bc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Prefix Property

---



|  |
| --- |
| [DimensionEqualityLabelFormatting Class](019b51cc-346a-5861-f093-669a7446c874.htm)   [See Also](#seeAlsoToggle) |

The prefix to include before the parameter value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017 Subscription Update

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

[DimensionEqualityLabelFormatting Class](019b51cc-346a-5861-f093-669a7446c874.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65d9d47b-2f42-42c8-d220-afa7930c082b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCopyDuplicates Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

Can't paste duplicate types. Only non duplicate types will be pasted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCopyDuplicates { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCopyDuplicates As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCopyDuplicates { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65db161a-8993-ad61-b84c-bfd584f4e997.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CwpReuseGridsSameName Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Reuse Grids with the same name"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CwpReuseGridsSameName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CwpReuseGridsSameName As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CwpReuseGridsSameName { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65db2761-d588-ee8f-220f-a5ec1e24a710.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [UIMacroManager Class](187bf41e-4d8a-ecaf-d5f6-2579f9290681.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [UIMacroManager](187bf41e-4d8a-ecaf-d5f6-2579f9290681.htm)

**Namespace:**   [Autodesk.Revit.UI.Macros](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)    
  **Assembly:**   RevitAPIUIMacros  (in RevitAPIUIMacros.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

[UIMacroManager Class](187bf41e-4d8a-ecaf-d5f6-2579f9290681.htm)

[Autodesk.Revit.UI.Macros Namespace](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)

<!-- Start of Syntax__65dda5c0-af37-321a-b2d7-607cffb79102.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewGraphSchedBottomLevel Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bottom Level"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ViewGraphSchedBottomLevel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewGraphSchedBottomLevel As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ViewGraphSchedBottomLevel { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65de4469-e7b0-f8b0-915f-16688e5a298f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhyMaterialParamSpecies Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Species"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PhyMaterialParamSpecies { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PhyMaterialParamSpecies As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PhyMaterialParamSpecies { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65e1dc52-453d-4eda-54a2-3c8a4c100dac.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Point Property

---



|  |
| --- |
| [PointLoad Class](3f703eb6-7eac-c80e-e693-ebcdd6b35bbe.htm)   [See Also](#seeAlsoToggle) |

Returns the position of point load, measured in decimal feet.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ Point { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Point As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Point { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Remarks

Loacation can be set only for non-hosted loads. To determine if load is hosted use  [IsHosted](76965c6d-473a-9ad9-8a72-baa7a47b055a.htm)  property.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[PointLoad Class](3f703eb6-7eac-c80e-e693-ebcdd6b35bbe.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__65e6bd3b-9a51-26b4-cda9-c7abeafe7e14.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StartTangent Property

---



|  |
| --- |
| [FlexDuct Class](39e3bd3a-8304-7785-dd10-4043aa0d7da4.htm)   [See Also](#seeAlsoToggle) |

Gets or sets the tangent vector at the start of the curve. The invalid or zero vector is ignored when setting the tangent.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public XYZ StartTangent { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property StartTangent As XYZ 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ StartTangent { 	XYZ^ get (); 	void set (XYZ^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[FlexDuct Class](39e3bd3a-8304-7785-dd10-4043aa0d7da4.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__65e91f36-ae32-7c82-db05-ec214351a08a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ContinuousrailBeginningTerminationAttachmentParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Extension Style"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ContinuousrailBeginningTerminationAttachmentParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ContinuousrailBeginningTerminationAttachmentParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ContinuousrailBeginningTerminationAttachmentParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65e9d8c8-0371-8397-3a50-ec155e189999.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnloadServices Method

---



|  |
| --- |
| [FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)   [See Also](#seeAlsoToggle) |

Unload the specified fabrication services from the project.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void UnloadServices( 	IList<int> serviceIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub UnloadServices ( _ 	serviceIds As IList(Of Integer) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void UnloadServices( 	IList<int>^ serviceIds ) ``` |

#### Parameters

serviceIds
:   Type:  System.Collections.Generic IList   Int32    
     The ids of the fabrication services to unload.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Fabrication services can not be unloaded if they are in use currently. -or- Some services are not loaded yet. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The current fabrication configuration is not connected and updated to source configuration. Reload and try again. |

# See Also

[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65ef60c8-d523-b2d0-4d3a-b9f2f4266f38.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DoubleClickTarget Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Elements that support double-click in Revit. Note that this is meant to cover cases where the element itself is a double-click target. Individual controls that are targets are handled separately.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public enum DoubleClickTarget ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration DoubleClickTarget ``` |

 

| Visual C++ |
| --- |
| ``` public enum class DoubleClickTarget ``` |

# Members

| Member name | Description |
| --- | --- |
| Family | Family instances |
| SketchedElement | Sketch-based elements |
| ViewOnSheet | Views on sheets |
| Assembly | Assemblies |
| Group | Groups |
| ComponentStairs | Component-based stairs |
| OutsideViewOnSheet | Outside active view on sheet |

# See Also

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__65efc1ea-ac85-f6ea-43cd-8a04c6737d5a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralWallProjectionSurface Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Horizontal Projection"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralWallProjectionSurface { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralWallProjectionSurface As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralWallProjectionSurface { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65f19b4f-d73c-25ef-0c88-ce2ebade5bcf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Origin Property

---



|  |
| --- |
| [Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.htm)   [See Also](#seeAlsoToggle) |

Plane origin.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

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

[Plane Class](6a6ee978-f114-558d-3c69-00d289aa855f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65f97585-8c92-b52e-93dd-8a6b4bfc5a1a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Combine Property

---



|  |
| --- |
| [PDFExportOptions Class](e4236fc8-f8e7-fc74-1b81-9e3a4d9e966b.htm)   [See Also](#seeAlsoToggle) |

Whether export all views and sheets into one PDF file or multiple files.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public bool Combine { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Combine As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool Combine { 	bool get (); 	void set (bool value); } ``` |

# Remarks

If     true  (  True  in Visual Basic)  , all exported views and sheets will be exported into one PDF file, whose file name would be specified by  [FileName](26f04248-487f-bb5a-d04a-95c7b63a4394.htm)  . If     false  (  False  in Visual Basic)  , each exported view and sheet will have its own PDF file created, whose file name would be generated with  [!:NamingRule]  .

# See Also

[PDFExportOptions Class](e4236fc8-f8e7-fc74-1b81-9e3a4d9e966b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__65f9f835-daaa-3efa-2976-3f932aa18366.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsModifiable Property

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Identifies if the element is modifiable.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public bool IsModifiable { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsModifiable As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsModifiable { 	bool get (); } ``` |

# Remarks

This is not a permanent state. The value depends on the document state. For example, active edit modes can make IsModifiable false for many elements.

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66a123ef-e8f2-2ff6-1885-b1503b66576a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConcreteFinish Property

---



|  |
| --- |
| [Concrete Class](a3b65010-dc9e-f2ee-46ed-97e453198a62.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Type" from the "Concrete" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string ConcreteFinish { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ConcreteFinish As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ ConcreteFinish { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyInteger" with accepted values in the enumerated type "ConcreteFinishType".

# See Also

[Concrete Class](a3b65010-dc9e-f2ee-46ed-97e453198a62.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__66a9b9d1-f915-b85b-39e0-5ba41c03ffc9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExtensionsOverlapWarning Property

---



|  |
| --- |
| [BuiltInFailures RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.htm)   [See Also](#seeAlsoToggle) |

Vertical Extensions on these Walls overlap. This can cause undesirable Joins. Try starting with no overlap and extend the Walls toward one another.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ExtensionsOverlapWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ExtensionsOverlapWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ExtensionsOverlapWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66b07d77-bda9-02a6-a09e-3d45fdd00898.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MicrometersPerMeterDegreeCelsius Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Micrometers per meter degree Celsius.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MicrometersPerMeterDegreeCelsius { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MicrometersPerMeterDegreeCelsius As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MicrometersPerMeterDegreeCelsius { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66b3618d-614c-ba19-7cf6-ca0ebb648ecf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReverseIterator Method

---



|  |
| --- |
| [MEPBuildingConstructionSet Class](fbe2c9fe-89ea-fc75-e418-cebc452ca1dd.htm)   [See Also](#seeAlsoToggle) |

Retrieve a backward moving iterator to the set.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual MEPBuildingConstructionSetIterator ReverseIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ReverseIterator As MEPBuildingConstructionSetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual MEPBuildingConstructionSetIterator^ ReverseIterator() ``` |

#### Return Value

Returns a backward moving iterator to the set.

# See Also

[MEPBuildingConstructionSet Class](fbe2c9fe-89ea-fc75-e418-cebc452ca1dd.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__66b5296e-7bfb-c028-3214-6fb99499fd40.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SATImportOptions Constructor (SATImportOptions)

---



|  |
| --- |
| [SATImportOptions Class](ae7fbb19-3fdd-0f5e-6b11-a5301e134922.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of SATImportOptions as a copy of the import options.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public SATImportOptions( 	SATImportOptions option ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	option As SATImportOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: SATImportOptions( 	SATImportOptions^ option ) ``` |

#### Parameters

option
:   Type:  [Autodesk.Revit.DB SATImportOptions](ae7fbb19-3fdd-0f5e-6b11-a5301e134922.htm)    
     The SAT options to be copied.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SATImportOptions Class](ae7fbb19-3fdd-0f5e-6b11-a5301e134922.htm)

[SATImportOptions Overload](ba7c6201-aa6e-3185-f2f6-1e74c6222ada.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66b6c474-ba3a-6924-b00c-41b31702caf0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StartPost Property

---



|  |
| --- |
| [PostPattern Class](3368dd15-79bc-3116-6ced-4fc123d6300d.htm)   [See Also](#seeAlsoToggle) |

Accesses the object containing properties related to the start post.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public BalusterInfo StartPost { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property StartPost As BalusterInfo 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property BalusterInfo^ StartPost { 	BalusterInfo^ get (); } ``` |

# See Also

[PostPattern Class](3368dd15-79bc-3116-6ced-4fc123d6300d.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__66c1678c-2e01-e0de-1386-5a0e1eb3ccff.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShapeBuilder Class

---



|  |
| --- |
| [Members](f84829bc-bc5b-d132-7892-7b7abcb9004e.htm)   [See Also](#seeAlsoToggle) |

The base class for geometry builder classes.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public class ShapeBuilder : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ShapeBuilder _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ShapeBuilder : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ShapeBuilder    
  [Autodesk.Revit.DB BRepBuilder](94c1fef4-2933-ce67-9c2d-361cbf8a42b4.htm)    
  [Autodesk.Revit.DB TessellatedShapeBuilder](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)    
  [Autodesk.Revit.DB ViewShapeBuilder](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)    
  [Autodesk.Revit.DB WireframeBuilder](ae9e719b-5d13-45c5-22d8-49111edfcfc4.htm)

# See Also

[ShapeBuilder Members](f84829bc-bc5b-d132-7892-7b7abcb9004e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66c65e99-b215-b2b8-ed77-246010a463b9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsElementValidIntersectingReference Method (ElementId)

---



|  |
| --- |
| [PartMakerMethodToDivideVolumes Class](611ca5f7-3ffb-6f83-3aaf-df4533038ed0.htm)   [See Also](#seeAlsoToggle) |

Identifies if the provided member is valid.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsElementValidIntersectingReference( 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsElementValidIntersectingReference ( _ 	elementId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsElementValidIntersectingReference( 	ElementId^ elementId ) ``` |

#### Parameters

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Element ids to be tested for validity for intersecting references.

#### Return Value

True if the reference is valid, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartMakerMethodToDivideVolumes Class](611ca5f7-3ffb-6f83-3aaf-df4533038ed0.htm)

[IsElementValidIntersectingReference Overload](d9f5703a-a68d-aae9-65c1-346f81c7f7f5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66c70b07-0932-8a9d-5139-0c7e00eacc3e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAXMImportLinkAvailable Method

---



|  |
| --- |
| [OptionalFunctionalityUtils Class](98d35b3b-34ec-4105-f7c5-16e9215b6b52.htm)   [See Also](#seeAlsoToggle) |

Checks whether the AXM Import/Link functionality is available in the installed Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022.1

# Syntax

| C# |
| --- |
| ``` public static bool IsAXMImportLinkAvailable() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsAXMImportLinkAvailable As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsAXMImportLinkAvailable() ``` |

#### Return Value

True if the AXM Import/Link functionality is available in the installed Revit.

# Remarks

AXM Import/Link is optional functionality that does not have to be part of the Revit installation.

# See Also

[OptionalFunctionalityUtils Class](98d35b3b-34ec-4105-f7c5-16e9215b6b52.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66c74371-40e7-2053-5736-2bf8bc45972c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BtuPerLbDegreeF Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol BTU/(lbÂ·Â°F), indicating unit British thermal units per pound degree Fahrenheit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BtuPerLbDegreeF { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BtuPerLbDegreeF As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BtuPerLbDegreeF { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66c865d8-12fe-cc4c-cbdc-674c62d5f528.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAllConnectorData Method

---



|  |
| --- |
| [PipeFittingAndAccessoryData Class](05db3129-7016-4054-1e93-1c718f1ae3bf.htm)   [See Also](#seeAlsoToggle) |

Gets the connector data of the pipe fitting or pipe accessory.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public IList<PipeFittingAndAccessoryConnectorData> GetAllConnectorData() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAllConnectorData As IList(Of PipeFittingAndAccessoryConnectorData) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<PipeFittingAndAccessoryConnectorData^>^ GetAllConnectorData() ``` |

#### Return Value

All connector data.

# Remarks

PipeFittingAndAccessoryConnectorData contains connector data which is needed to calculate coefficient. such as width, height, diameter and flow.

# See Also

[PipeFittingAndAccessoryData Class](05db3129-7016-4054-1e93-1c718f1ae3bf.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__66c95308-4a86-1e63-c133-d00dbc2b9af6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathName Property

---



|  |
| --- |
| [DocumentSavingAsEventArgs Class](1bb9bb9f-be64-3c6f-804b-66fe6a2b0562.htm)   [See Also](#seeAlsoToggle) |

Target path to which the document is to be saved.

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public string PathName { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property PathName As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ PathName { 	String^ get (); } ``` |

# See Also

[DocumentSavingAsEventArgs Class](1bb9bb9f-be64-3c6f-804b-66fe6a2b0562.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__66cb17a0-83b1-3aa7-ee9b-42f5d8dafd25.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Categories Property

---



|  |
| --- |
| [Settings Class](9aa29bb7-d720-8c97-0ccb-e3e6046c545c.htm)   [See Also](#seeAlsoToggle) |

Retrieves an object that provides access to all the categories contained in the Autodesk Revit application and project.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Categories Categories { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Categories As Categories 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Categories^ Categories { 	Categories^ get (); } ``` |

# See Also

[Settings Class](9aa29bb7-d720-8c97-0ccb-e3e6046c545c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66ce9a24-c69a-7dbb-7b5f-fd1a50f1b4c7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProjectRevisionRevisionIssuedTo Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Issued to"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ProjectRevisionRevisionIssuedTo { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ProjectRevisionRevisionIssuedTo As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ProjectRevisionRevisionIssuedTo { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66d3d7fd-aa11-7140-c013-893ded5b8fbf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IFCExtrusionCalculatorOptions Constructor

---



|  |
| --- |
| [IFCExtrusionCalculatorOptions Class](3aa9bc3b-5ce0-e0ba-4211-9a08526c1c1b.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a class used to calculate extrusions from Revit geometry.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IFCExtrusionCalculatorOptions( 	ExporterIFC exporterIFC, 	IFCExtrusionAxes extrusionAxes, 	XYZ customAxis, 	double scale ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	exporterIFC As ExporterIFC, _ 	extrusionAxes As IFCExtrusionAxes, _ 	customAxis As XYZ, _ 	scale As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: IFCExtrusionCalculatorOptions( 	ExporterIFC^ exporterIFC,  	IFCExtrusionAxes extrusionAxes,  	XYZ^ customAxis,  	double scale ) ``` |

#### Parameters

exporterIFC
:   Type:  [Autodesk.Revit.DB.IFC ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.htm)    
     The exporter.

extrusionAxes
:   Type:  [Autodesk.Revit.DB.IFC IFCExtrusionAxes](ec83b366-85d1-3e3f-edc6-6cffd36848e6.htm)    
     The extrusion axes to try when doing the calculation.

customAxis
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The custom axis to try (if extrusionAxes includes an option for a custom direction).

scale
:   Type:  System Double    
     The scaling factor for length measurements from the default Revit units to the export units.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[IFCExtrusionCalculatorOptions Class](3aa9bc3b-5ce0-e0ba-4211-9a08526c1c1b.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__66d581a3-9a20-d3ba-47a3-6d17e52fda56.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ServerSupportsCADLinks Method

---



|  |
| --- |
| [ExternalResourceServerUtils Class](a3147faa-ddc7-6cc1-8906-260582b6bc4a.htm)   [See Also](#seeAlsoToggle) |

Checks that the server referenced by the given ExternalResourceReference supports CAD links.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static bool ServerSupportsCADLinks( 	ExternalResourceReference extRef ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ServerSupportsCADLinks ( _ 	extRef As ExternalResourceReference _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ServerSupportsCADLinks( 	ExternalResourceReference^ extRef ) ``` |

#### Parameters

extRef
:   Type:  [Autodesk.Revit.DB ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.htm)    
     The ExternalResourceReference to check.

#### Return Value

True if the ExternalResourceReference refers to a server that supports CAD links. False otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternalResourceServerUtils Class](a3147faa-ddc7-6cc1-8906-260582b6bc4a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66d69149-ad97-d7b4-8355-c05322916219.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CalculatingColor Property

---



|  |
| --- |
| [ColorOptions Class](1ca57d8c-b970-83b4-c5ce-9e39464e5cc2.htm)   [See Also](#seeAlsoToggle) |

The color used to render elements when some aspect of their properties is currently being recalculated.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public Color CalculatingColor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CalculatingColor As Color 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Color^ CalculatingColor { 	Color^ get (); 	void set (Color^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[ColorOptions Class](1ca57d8c-b970-83b4-c5ce-9e39464e5cc2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66d7ac46-c022-c65a-0c18-4fdedb77c5f6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRebarInSystemIds Method

---



|  |
| --- |
| [PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)   [See Also](#seeAlsoToggle) |

Returns the ids of the RebarInSystem elements owned by the PathReinforcement element.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> GetRebarInSystemIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRebarInSystemIds As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ GetRebarInSystemIds() ``` |

# Remarks

The RebarInSystem elements are only created if ReinforcementSettings.HostStructuralRebar is set to true. If that setting is false, this function returns an empty array.

# See Also

[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__66e0ab2e-920b-fd24-3f3b-bd63ef6eeb12.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [DirectContext3DHandleOverrides Class](8bef65c6-70bc-1a10-a9a4-47c8ec2cd842.htm)   [See Also](#seeAlsoToggle) |

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

[DirectContext3DHandleOverrides Class](8bef65c6-70bc-1a10-a9a4-47c8ec2cd842.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__66e250b9-081a-5a9b-6045-d779f1876e3a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FaceEdgeNode Class

---



|  |
| --- |
| [Members](c755b541-6536-54f7-6f85-a6f9407c09ad.htm)   [See Also](#seeAlsoToggle) |

An output node that represents a Face edge.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public class FaceEdgeNode : FaceDetailNode ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FaceEdgeNode _ 	Inherits FaceDetailNode ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FaceEdgeNode : public FaceDetailNode ``` |

# Remarks

See also:  [OnFaceEdge2D(FaceEdgeNode)](c45260d6-c34c-3198-3ccf-d256348832bd.htm)  .

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB RenderNode](9900b69b-7cb7-8555-75ac-4b5f22b5fa7f.htm)    
  [Autodesk.Revit.DB FaceDetailNode](033c07e7-4883-4998-0b2b-3b24f5e2f821.htm)    
  Autodesk.Revit.DB FaceEdgeNode

# See Also

[FaceEdgeNode Members](c755b541-6536-54f7-6f85-a6f9407c09ad.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66e53964-271f-cdc9-4583-c6a9e8582834.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextStyleBold Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bold"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TextStyleBold { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextStyleBold As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TextStyleBold { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66e5e11c-ed78-4b64-d458-77b525ba796f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BackgroundStyle Property

---



|  |
| --- |
| [RenderingSettings Class](7ba669f3-bd38-464b-f3f7-8a0b4e513a0a.htm)   [See Also](#seeAlsoToggle) |

The enum value that controls the background style for rendering.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public BackgroundStyle BackgroundStyle { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BackgroundStyle As BackgroundStyle 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property BackgroundStyle BackgroundStyle { 	BackgroundStyle get (); 	void set (BackgroundStyle value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[RenderingSettings Class](7ba669f3-bd38-464b-f3f7-8a0b4e513a0a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66e6adc1-452c-a9c6-1489-9092f62455aa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Grid1Offset Property

---



|  |
| --- |
| [CurtainGrid Class](5e0d5b7c-aaa1-d299-6fb8-2faa65b1857a.htm)   [See Also](#seeAlsoToggle) |

The offset for the U grid line pattern of the curtain grid.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double Grid1Offset { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Grid1Offset As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Grid1Offset { 	double get (); 	void set (double value); } ``` |

# See Also

[CurtainGrid Class](5e0d5b7c-aaa1-d299-6fb8-2faa65b1857a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66e8c11a-60fc-3046-de82-55020a2ceb3f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveMacro Method

---



|  |
| --- |
| [MacroModule Class](d604a3cb-4f41-78a8-6353-270c566ac661.htm)   [See Also](#seeAlsoToggle) |

Removes a macro from the module.

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPIMacros  (in RevitAPIMacros.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void RemoveMacro( 	Macro macro ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveMacro ( _ 	macro As Macro _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveMacro( 	Macro^ macro ) ``` |

#### Parameters

macro
:   Type:  [Autodesk.Revit.DB.Macros Macro](8e156c00-8aa8-51f5-be8f-4561ad51f1d8.htm)    
     The macro will be removed from this module.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Cannot remove the Macro due to no permission. |

# See Also

[MacroModule Class](d604a3cb-4f41-78a8-6353-270c566ac661.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)

<!-- Start of Syntax__66e96d4a-6c06-0c50-bd03-f1db2ae83efb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LineScaling Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing possible LineType scaling modes.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum LineScaling ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration LineScaling ``` |

 

| Visual C++ |
| --- |
| ``` public enum class LineScaling ``` |

# Members

| Member name | Description |
| --- | --- |
| ViewScale | Exporting lines as they were scaled by view scale. This option preserves visual fidelity. |
| ModelSpace | Modelspace scaling. LTSCALE is set to view scale and PSLTSCALE to 0. |
| PaperSpace | Paperspace scaling. Specifies the value 1 for both LTSCALE and PSLTSCALE. |

# Remarks

Whichever option is chosen, line type definitions are created so a dashed line always begins and ends with a dash. Using these options does change the default behavior of exported DWGs. Some lines expected to be dashed may appear solid or in a different scale.

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66ea5747-0492-62d8-8869-5a2455977348.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddModule Method

---



|  |
| --- |
| [MacroManager Class](49eb4b8a-ae13-95e7-fef4-11347bbb67d3.htm)   [See Also](#seeAlsoToggle) |

Adds a MacroModule to the application or document.

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPIMacros  (in RevitAPIMacros.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public MacroModule AddModule( 	ModuleSettings moduleSettings ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddModule ( _ 	moduleSettings As ModuleSettings _ ) As MacroModule ``` |

 

| Visual C++ |
| --- |
| ``` public: MacroModule^ AddModule( 	ModuleSettings^ moduleSettings ) ``` |

#### Parameters

moduleSettings
:   Type:  [Autodesk.Revit.DB.Macros ModuleSettings](2a0c5aed-a80e-6c91-0525-ad8d42d613a6.htm)    
     The module settings.

#### Return Value

The new module.

# Remarks

Note: document-level modules will not be saved to the document until the document is saved. Thus this operation is not undoable and does not require an open transaction even for document-level modules.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the module name is duplicated with the existing one, or the name is too long, or the name contains invalid identifier(s), such as include "#", "%", ... and key words in C# or VB.NET. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MacroManager Class](49eb4b8a-ae13-95e7-fef4-11347bbb67d3.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)

<!-- Start of Syntax__66eb3f1e-0df8-744d-590f-bf54ebde5ccf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reset Method

---



|  |
| --- |
| [EdgeArrayIterator Class](50ca2601-9cb4-d717-ac79-5796f85e1e76.htm)   [See Also](#seeAlsoToggle) |

Bring the iterator back to the start of the array.

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

The Reset method will return the iterator back to the start of the array in line with the definition of IEnumerator. Note that you must call MoveNext before the first item can be accessed via the Current property.

# See Also

[EdgeArrayIterator Class](50ca2601-9cb4-d717-ac79-5796f85e1e76.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66eb8785-4225-509c-b6a3-0bf9fe1612b2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### flipFacing Method

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [See Also](#seeAlsoToggle) |

The orientation of family instance facing will be flipped. If it can not be flipped, return false, otherwise return true.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool flipFacing() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function flipFacing As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool flipFacing() ``` |

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66ec8d4e-25cd-1e14-3b25-d9d3a0f5cce9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetStackedWallMemberIds Method

---



|  |
| --- |
| [Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)   [See Also](#seeAlsoToggle) |

Get the sub walls which belongs to the wall.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> GetStackedWallMemberIds() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetStackedWallMemberIds As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ GetStackedWallMemberIds() ``` |

#### Return Value

If the wall is a stacked wall, the Ids of the sub will be returned in bottom-top order.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This wall isn't a consistent stacked wall. |

# See Also

[Wall Class](b5891733-c602-12df-beab-da414b58d608.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66edda4f-79f3-30d7-f485-3e8a1ec33da4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreCoordinatesInBounds Method

---



|  |
| --- |
| [RepeaterBounds Class](99c1ffdf-818b-1918-a6ba-42b7904ca4bc.htm)   [See Also](#seeAlsoToggle) |

Determines whether given coordinates are within the bounds.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool AreCoordinatesInBounds( 	RepeaterCoordinates coordinates, 	bool treatCyclicalBoundsAsInfinite ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AreCoordinatesInBounds ( _ 	coordinates As RepeaterCoordinates, _ 	treatCyclicalBoundsAsInfinite As Boolean _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool AreCoordinatesInBounds( 	RepeaterCoordinates^ coordinates,  	bool treatCyclicalBoundsAsInfinite ) ``` |

#### Parameters

coordinates
:   Type:  [Autodesk.Revit.DB RepeaterCoordinates](17102857-7a63-7039-f5f4-88d07dc33c7a.htm)    
     The coordinates.

treatCyclicalBoundsAsInfinite
:   Type:  System Boolean    
     True if cyclical directions should be treated as unbounded.

#### Return Value

True if the coordinates are within the bounds.

# Remarks

The coordinates must have the same number of dimensions as the bounds. This method does not apply to zero dimensional bounds.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The coordinates coordinates have incompatible number of dimensions. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The bounds must have at least one dimension. |

# See Also

[RepeaterBounds Class](99c1ffdf-818b-1918-a6ba-42b7904ca4bc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66f12d78-a4ab-9b99-ef49-92c3a3e1835e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, IList(ElementId), ElectricalSystemType)

---



|  |
| --- |
| [ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)   [See Also](#seeAlsoToggle) |

Creates a new MEP Electrical System element from a set of electrical components.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static ElectricalSystem Create( 	Document document, 	IList<ElementId> electComponents, 	ElectricalSystemType elecSysType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	electComponents As IList(Of ElementId), _ 	elecSysType As ElectricalSystemType _ ) As ElectricalSystem ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElectricalSystem^ Create( 	Document^ document,  	IList<ElementId^>^ electComponents,  	ElectricalSystemType elecSysType ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The Document.

electComponents
:   Type:  System.Collections.Generic IList   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The electrical components in this system.

elecSysType
:   Type:  [Autodesk.Revit.DB.Electrical ElectricalSystemType](90f62108-9cd1-a66a-a123-8372307f4e7f.htm)    
     The System Type of electrical system.

#### Return Value

If successful a new MEP Electrical System element within the project, otherwise    a null reference (  Nothing  in Visual Basic)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | There should be at least one component that can create the specified circuit type |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[ElectricalSystem Class](158b4be3-bbe5-11eb-cccc-788edd3a7590.htm)

[Create Overload](b3ea7251-7230-ac0a-d5cc-0806b0c0ec1e.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__66f19c6e-c1d6-be9e-808b-36e3d8d9e1b6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAnElement Method

---



|  |
| --- |
| [IFCProductWrapper Class](368d2c50-1258-32a9-00ed-cc41059a6694.htm)   [See Also](#seeAlsoToggle) |

Gets the first element handle added to this wrapper.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public IFCAnyHandle GetAnElement() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAnElement As IFCAnyHandle ``` |

 

| Visual C++ |
| --- |
| ``` public: IFCAnyHandle^ GetAnElement() ``` |

#### Return Value

The handle.

# See Also

[IFCProductWrapper Class](368d2c50-1258-32a9-00ed-cc41059a6694.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__66f1e4a9-71b0-93da-b8be-56a743012fcf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateDuctConnector Method (Document, DuctSystemType, ConnectorProfileType, Reference, Edge)

---



|  |
| --- |
| [ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)   [See Also](#seeAlsoToggle) |

Create a new duct ConnectorElement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static ConnectorElement CreateDuctConnector( 	Document document, 	DuctSystemType ductSystemType, 	ConnectorProfileType profileShape, 	Reference planarFace, 	Edge edge ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateDuctConnector ( _ 	document As Document, _ 	ductSystemType As DuctSystemType, _ 	profileShape As ConnectorProfileType, _ 	planarFace As Reference, _ 	edge As Edge _ ) As ConnectorElement ``` |

 

| Visual C++ |
| --- |
| ``` public: static ConnectorElement^ CreateDuctConnector( 	Document^ document,  	DuctSystemType ductSystemType,  	ConnectorProfileType profileShape,  	Reference^ planarFace,  	Edge^ edge ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to add the connector to.

ductSystemType
:   Type:  [Autodesk.Revit.DB.Mechanical DuctSystemType](108631a7-6d3a-a5f6-cc0c-0579ca8cf999.htm)    
     The DuctSystemType of the connector.

profileShape
:   Type:  [Autodesk.Revit.DB ConnectorProfileType](94482e32-e0e3-2340-c23c-6cef9348434e.htm)    
     The profile shape of the duct.

planarFace
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The planar face to place the connector on.

edge
:   Type:  [Autodesk.Revit.DB Edge](7155ef49-fcd9-c80a-6232-70189a617bcc.htm)    
     One of the edges in the edge loop that defines the connector location on the planar face.

#### Return Value

The duct ConnectorElement.

# Remarks

Regenerates the document.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The reference is not a planar face. -or- document is not a family document. -or- Thrown when the edge does not belong to the face. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Connector creation is not allowed in this family. |

# See Also

[ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)

[CreateDuctConnector Overload](397c6cd9-1047-03c2-f24f-228780ef9a48.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66f1ebbe-f9e9-a24b-59ec-1061e0d1c532.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BadTreadRiserProfile Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Tread/Riser profile is invalid.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId BadTreadRiserProfile { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BadTreadRiserProfile As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ BadTreadRiserProfile { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66f2c679-d136-7252-d417-5cb122c9840d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlaceOnHost Method

---



|  |
| --- |
| [FabricationHostedInfo Class](c74f8adf-a227-098c-b58c-a2998560c0d3.htm)   [See Also](#seeAlsoToggle) |

Places the part on the specified host.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void PlaceOnHost( 	ElementId hostId, 	Connector hostConnector, 	double distance ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub PlaceOnHost ( _ 	hostId As ElementId, _ 	hostConnector As Connector, _ 	distance As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void PlaceOnHost( 	ElementId^ hostId,  	Connector^ hostConnector,  	double distance ) ``` |

#### Parameters

hostId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of the host fabrication part.

hostConnector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The connector of the host.

distance
:   Type:  System Double    
     The distance from the connector to place the hosted part. Units are in feet (ft).

# Remarks

The document must be regenerated before the fabrication part can be used. Check  ValidationStatus  after regeneration to see if the part is valid for fabrication.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Invalid fabrication part host. The host should be a straight fabrication part. -or- Invalid connector of fabrication part host. -or- The distance is out of range. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationHostedInfo Class](c74f8adf-a227-098c-b58c-a2998560c0d3.htm)

[PlaceOnHost Overload](6365aaba-168c-938a-e72d-597fcf4425d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66f5a5ba-4e72-6401-b29c-6df84b772b4a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetTransactionFinalizer Method

---



|  |
| --- |
| [FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)   [See Also](#seeAlsoToggle) |

Sets the callback to be executed after the transaction is completed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FailureHandlingOptions SetTransactionFinalizer( 	ITransactionFinalizer finalizer ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetTransactionFinalizer ( _ 	finalizer As ITransactionFinalizer _ ) As FailureHandlingOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: FailureHandlingOptions^ SetTransactionFinalizer( 	ITransactionFinalizer^ finalizer ) ``` |

#### Parameters

finalizer
:   Type:  [Autodesk.Revit.DB ITransactionFinalizer](e11d1d5a-00dc-a13f-55b5-4e2fc679f591.htm)    
     The callback to be executed after the transaction is completed.

#### Return Value

This FailureHandlingOptions object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66f5c45e-9b46-6bde-a95e-21291121ddba.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HostForCutHasNoGeometry Property

---



|  |
| --- |
| [BuiltInFailures OpeningFailures Class](7857c588-1861-cfd1-1423-7b950a01aba1.htm)   [See Also](#seeAlsoToggle) |

Host can't be cut because it has no geometry.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId HostForCutHasNoGeometry { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property HostForCutHasNoGeometry As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ HostForCutHasNoGeometry { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures OpeningFailures Class](7857c588-1861-cfd1-1423-7b950a01aba1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66f703f1-7ba9-fde3-fcdb-2f4429a44d91.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApiDelayedUpdateFailed Property

---



|  |
| --- |
| [BuiltInFailures DocumentFailures Class](51cc3f4c-5e1f-90e9-896a-db461e14ed43.htm)   [See Also](#seeAlsoToggle) |

Delayed Updating Failed. Please contact the 3rd Party Application vendor.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ApiDelayedUpdateFailed { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ApiDelayedUpdateFailed As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ApiDelayedUpdateFailed { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DocumentFailures Class](51cc3f4c-5e1f-90e9-896a-db461e14ed43.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66f9648b-dd64-6ff5-ef89-4f1d6b5c4a23.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSchedulableFields Method

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Gets a list of all non-calculated/non-combined fields that are eligible to be included in this schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public IList<SchedulableField> GetSchedulableFields() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSchedulableFields As IList(Of SchedulableField) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<SchedulableField^>^ GetSchedulableFields() ``` |

#### Return Value

A list of SchedulableField objects representing the non-calculated/non-combined fields that may be included in the schedule.

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__66fb3510-3fc7-d80b-9515-3593e1459e81.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BraceParallelLineOffset Property

---



|  |
| --- |
| [StructuralSettings Class](1d1b89be-c2ae-ca39-01ce-f5b01178fb1e.htm)   [See Also](#seeAlsoToggle) |

The distance by which brace symbols in plan views will be offset.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public double BraceParallelLineOffset { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BraceParallelLineOffset As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double BraceParallelLineOffset { 	double get (); 	void set (double value); } ``` |

# Remarks

Applies only when BracePlanRepresentation is set to ParallelLine.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[StructuralSettings Class](1d1b89be-c2ae-ca39-01ce-f5b01178fb1e.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__66fbaa58-1394-df12-7b50-f0ef50b2be44.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewSweep Method (Boolean, CurveArray, SketchPlane, SweepProfile, Int32, ProfilePlaneLocation)

---



|  |
| --- |
| [FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Adds a new sweep form to the family document, using a path of curve elements.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Sweep NewSweep( 	bool isSolid, 	CurveArray path, 	SketchPlane pathPlane, 	SweepProfile profile, 	int profileLocationCurveIndex, 	ProfilePlaneLocation profilePlaneLocation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewSweep ( _ 	isSolid As Boolean, _ 	path As CurveArray, _ 	pathPlane As SketchPlane, _ 	profile As SweepProfile, _ 	profileLocationCurveIndex As Integer, _ 	profilePlaneLocation As ProfilePlaneLocation _ ) As Sweep ``` |

 

| Visual C++ |
| --- |
| ``` public: Sweep^ NewSweep( 	bool isSolid,  	CurveArray^ path,  	SketchPlane^ pathPlane,  	SweepProfile^ profile,  	int profileLocationCurveIndex,  	ProfilePlaneLocation profilePlaneLocation ) ``` |

#### Parameters

isSolid
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     Indicates if the Sweep is Solid or Void.

path
:   Type:  [Autodesk.Revit.DB CurveArray](55103aad-38fd-45d2-6bf7-67a5203e99f3.htm)    
     The path of the sweep. The path should be 2D, where all input curves lie in one plane, and the curves are not required to reference existing geometry.

pathPlane
:   Type:  [Autodesk.Revit.DB SketchPlane](ba104029-d175-7e75-caef-667a4281f4af.htm)    
     The sketch plane for the path. Use this when you want to create a 2D path that resides on an existing planar face. Optional, can be    a null reference (  Nothing  in Visual Basic)  for 3D paths or for 2D paths where the path should not reference an existing face.

profile
:   Type:  [Autodesk.Revit.DB SweepProfile](1b77356c-e92b-e151-f8c9-727b3e2b8934.htm)    
     The profile of the newly created Sweep. This may contain more than one curve loop or a profile family. The profile must lie in the XY plane, and it will be transformed to the profile plane automatically. Each loop must be a fully closed curve loop and the loops must not intersect. The loop can be a unbound circle or ellipse, but its geometry will be split in two in order to satisfy requirements for sketches used in extrusions.

profileLocationCurveIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the path curves. The curve upon which the profile plane will be determined.

profilePlaneLocation
:   Type:  [Autodesk.Revit.DB ProfilePlaneLocation](7ee6064e-ae88-1efe-a030-dabfae9bacaf.htm)    
     The location on the profileLocationCurve where the profile plane will be determined.

#### Return Value

If creation was successful the new Sweep is returned, otherwise an exception with failure information will be thrown.

# Remarks

This method creates a sweep in a family document. The sweep will trace the profile along the path.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private Sweep CreateSweep(Autodesk.Revit.DB.Document document, SketchPlane sketchPlane)
{
    Sweep sweep = null;

    // make sure we have a family document
    if (true == document.IsFamilyDocument)
    {
        // Define a profile for the sweep
        CurveArrArray arrarr = new CurveArrArray();
        CurveArray arr = new CurveArray();

        // Create an ovoid profile
        XYZ pnt1 = new XYZ(0, 0, 0);
        XYZ pnt2 = new XYZ(2, 0, 0);
        XYZ pnt3 = new XYZ(1, 1, 0);
        arr.Append(Arc.Create(pnt2, 1.0d, 0.0d, 180.0d, XYZ.BasisX, XYZ.BasisY));
        arr.Append(Arc.Create(pnt1, pnt3, pnt2));
        arrarr.Append(arr);
        SweepProfile profile = document.Application.Create.NewCurveLoopsProfile(arrarr);

        // Create a path for the sweep
        XYZ pnt4 = new XYZ(10, 0, 0);
        XYZ pnt5 = new XYZ(0, 10, 0);
        Curve curve = Line.CreateBound(pnt4, pnt5);

        CurveArray curves = new CurveArray();
        curves.Append(curve);

        // create a solid ovoid sweep
        sweep = document.FamilyCreate.NewSweep(true, curves, sketchPlane, profile, 0, ProfilePlaneLocation.Start);

        if (null != sweep)
        {
            // move to proper place
            XYZ transPoint1 = new XYZ(11, 0, 0);
            ElementTransformUtils.MoveElement(document, sweep.Id, transPoint1);
        }
        else
        {
            throw new Exception("Failed to create a new Sweep.");
        }
    }
    else
    {
        throw new Exception("Please open a Family document before invoking this command.");
    }

    return sweep;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Function CreateSweep(document As Autodesk.Revit.DB.Document, sketchPlane As SketchPlane) As Sweep
    Dim sweep As Sweep = Nothing

    ' make sure we have a family document
    If True = document.IsFamilyDocument Then
        ' Define a profile for the sweep
        Dim arrarr As New CurveArrArray()
        Dim arr As New CurveArray()

        ' Create an ovoid profile
        Dim pnt1 As New XYZ(0, 0, 0)
        Dim pnt2 As New XYZ(2, 0, 0)
        Dim pnt3 As New XYZ(1, 1, 0)
        arr.Append(Arc.Create(pnt2, 1.0, 0.0, 180.0, XYZ.BasisX, XYZ.BasisY))
        arr.Append(Arc.Create(pnt1, pnt3, pnt2))
        arrarr.Append(arr)
        Dim profile As SweepProfile = document.Application.Create.NewCurveLoopsProfile(arrarr)

        ' Create a path for the sweep
        Dim pnt4 As New XYZ(10, 0, 0)
        Dim pnt5 As New XYZ(0, 10, 0)
        Dim curve As Curve = Line.CreateBound(pnt4, pnt5)

        Dim curves As New CurveArray()
        curves.Append(curve)

        ' create a solid ovoid sweep
        sweep = document.FamilyCreate.NewSweep(True, curves, sketchPlane, profile, 0, ProfilePlaneLocation.Start)

        If sweep IsNot Nothing Then
            ' move to proper place
            Dim transPoint1 As New XYZ(11, 0, 0)
            ElementTransformUtils.MoveElement(document, sweep.Id, transPoint1)
        Else
            Throw New Exception("Failed to create a new Sweep.")
        End If
    Else
        Throw New Exception("Please open a Family document before invoking this command.")
    End If

    Return sweep
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the input argument-path-is    a null reference (  Nothing  in Visual Basic)  or empty. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument-profile-is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the input argument-profileLocationCurveIndex-is out of index bounds. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the input argument-profilePlaneLocation-does not exist in the ProfilePlaneLocation enumeration. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when creation is attempted in Conceptual Mass, 2D, or other family where sweeps cannot be created. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the creation failed. |

# See Also

[FamilyItemFactory Class](a7622967-1381-c17f-ed04-1ebe40da0440.htm)

[NewSweep Overload](e22c07dd-0615-5b5d-e40f-eed749b7206f.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__66fc864b-ed7a-c9f9-7eae-209a9aa5c1b6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VendorIdIsValid Method

---



|  |
| --- |
| [SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)   [See Also](#seeAlsoToggle) |

Checks whether the given vendor ID string is valid. A valid vendor ID string: 1. Has a length of at least 4 characters and no more than 253 characters, and 2. Contains only letters, digits, or any of the following special characters: ! " # & \ ( ) + , . - : ; < = > ? \_ ` | ~

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool VendorIdIsValid( 	string vendorId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function VendorIdIsValid ( _ 	vendorId As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool VendorIdIsValid( 	String^ vendorId ) ``` |

#### Parameters

vendorId
:   Type:  System String    
     The vendor ID to check.

#### Return Value

True if the vendor ID is valid.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)

<!-- Start of Syntax__66fc8d10-b714-4fa6-588b-95fed4f84b85.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotMoveElementWarn Property

---



|  |
| --- |
| [BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)   [See Also](#seeAlsoToggle) |

Can't move element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotMoveElementWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotMoveElementWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotMoveElementWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67a7ff7f-ebea-b3ad-6af2-2cad9ee03073.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AutoGlazingFailedError Property

---



|  |
| --- |
| [BuiltInFailures MassFailures Class](c9804646-1735-fe87-b758-a466adf5eae8.htm)   [See Also](#seeAlsoToggle) |

Failure in Auto-Glazing region computation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId AutoGlazingFailedError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AutoGlazingFailedError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ AutoGlazingFailedError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MassFailures Class](c9804646-1735-fe87-b758-a466adf5eae8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67a8f4c0-9b01-adc7-04bd-85600761908c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectionInputPointInfo Constructor

---



|  |
| --- |
| [ConnectionInputPointInfo Class](1a44f5bf-0f28-e1f6-0085-e35bec49d5c6.htm)   [See Also](#seeAlsoToggle) |

Construct a default input point.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public ConnectionInputPointInfo() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: ConnectionInputPointInfo() ``` |

# See Also

[ConnectionInputPointInfo Class](1a44f5bf-0f28-e1f6-0085-e35bec49d5c6.htm)

[ConnectionInputPointInfo Overload](b7012c6c-ca3d-606c-ca9a-0aa1fc339378.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__67ae7e0e-00ff-4575-c39f-6b782e017f86.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FormulaEditingEventArgs Class

---



|  |
| --- |
| [Members](8bd4fdf3-307b-9fc3-d96f-c4a9f7b61178.htm)   [See Also](#seeAlsoToggle) |

The event arguments used by the DocumentSaving event.

**Namespace:**   [Autodesk.Revit.UI.Events](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public class FormulaEditingEventArgs : RevitAPIPreEventArgs ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FormulaEditingEventArgs _ 	Inherits RevitAPIPreEventArgs ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FormulaEditingEventArgs : public RevitAPIPreEventArgs ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)    
  [Autodesk.Revit.DB.Events RevitAPIEventArgs](7c98499c-e345-cfda-ef89-48eccd3c9992.htm)    
  [Autodesk.Revit.DB.Events RevitAPIPreEventArgs](14097470-c9d9-0143-dc1b-b93a60a460e6.htm)    
  Autodesk.Revit.UI.Events FormulaEditingEventArgs

# See Also

[FormulaEditingEventArgs Members](8bd4fdf3-307b-9fc3-d96f-c4a9f7b61178.htm)

[Autodesk.Revit.UI.Events Namespace](21d3e79a-2484-60b0-b4c6-5cf65cd96039.htm)

<!-- Start of Syntax__67af51c2-1c2b-64e0-35fa-448033fb4810.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WidthInPixels Property

---



|  |
| --- |
| [TableData Class](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)   [See Also](#seeAlsoToggle) |

Gets the width of the panel schedule in logical pixels

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public int WidthInPixels { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property WidthInPixels As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int WidthInPixels { 	int get (); } ``` |

# See Also

[TableData Class](ab967e17-822e-fd5f-760a-4810e2e7eb61.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67b163c9-8a6a-08bd-3abf-ae2d54e3c7e0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSectionData Method

---



|  |
| --- |
| [PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)   [See Also](#seeAlsoToggle) |

Gets section data that will be written to

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public TableSectionData GetSectionData( 	SectionType sectionType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSectionData ( _ 	sectionType As SectionType _ ) As TableSectionData ``` |

 

| Visual C++ |
| --- |
| ``` public: TableSectionData^ GetSectionData( 	SectionType sectionType ) ``` |

#### Parameters

sectionType
:   Type:  [Autodesk.Revit.DB SectionType](ad9a6cf0-aa1a-d011-b399-658345721aab.htm)    
     The section type

#### Return Value

The  [TableSectionData](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__67b4e27c-7f91-f233-681c-97ce858c6a65.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Hub Class

---



|  |
| --- |
| [Members](f2fd3f65-1f03-3f85-e7a7-154d57426382.htm)   [See Also](#seeAlsoToggle) |

Represents a connection between two or more Autodesk Revit Elements.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class Hub : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Hub _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Hub : public Element ``` |

# Remarks

* Elements connected via a Hub do not refer directly to each other - they each refer to the Hub that keeps all the connectivity information.
* Hubs connect only structural Analytical Model Elements.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB.Structure Hub

# See Also

[Hub Members](f2fd3f65-1f03-3f85-e7a7-154d57426382.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__67b96458-a5e4-33fc-8629-50f0cbe2a25f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewTemplate Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"View Template"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ViewTemplate { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewTemplate As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ViewTemplate { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67bb59c4-77cf-7cb4-d289-489ba85e09b2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasAllChangesFromCentral Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Returns whether the model in the current session is up to date with central.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool HasAllChangesFromCentral() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function HasAllChangesFromCentral As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool HasAllChangesFromCentral() ``` |

#### Return Value

True means up to date; false means out of date.

If central is locked but Revit can determine that the model in the current session is out of date without opening central, this method will return false instead of throwing CentralModelContentionException.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
void ReloadDocument(Document doc)
{
    ReloadLatestOptions reloadOpts = new ReloadLatestOptions();
    try
    {
        doc.ReloadLatest(reloadOpts);
        // Check to make sure no new changes were synced with Central during reload
        if (doc.HasAllChangesFromCentral() == false)
        {
            // If there are changes from central, reload again
            doc.ReloadLatest(reloadOpts);
        }
    }
    catch (Exception e)
    {
        TaskDialog.Show("Reload Failed", e.Message);
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub ReloadDocument(doc As Document)
    Dim reloadOpts As New ReloadLatestOptions()
    Try
        doc.ReloadLatest(reloadOpts)
        ' Check to make sure no new changes were synced with Central during reload
        If doc.HasAllChangesFromCentral() = False Then
            ' If there are changes from central, reload again
            doc.ReloadLatest(reloadOpts)
        End If
    Catch e As Exception
        TaskDialog.Show("Reload Failed", e.Message)
    End Try
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions CentralFileCommunicationException](20094e4f-8326-8378-e5bc-452341d131c2.htm) | The file-based central model could not be reached, because e.g. the network is down or the file server is down. |
| [Autodesk.Revit.Exceptions CentralModelAccessDeniedException](3e38b7b1-1ee8-c7f0-6cdd-bacf67bf61f4.htm) | Access to the central model was denied due to lack of access privileges. -or- Access to the central model was denied. A possible reason is because the model was under maintenance. |
| [Autodesk.Revit.Exceptions CentralModelContentionException](ad511076-c435-23c1-5720-1205c4ed28b9.htm) | The central model is locked by another client. |
| [Autodesk.Revit.Exceptions CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.htm) | Username does not match the one used to create the local file. -or- The central model has been replaced by a local model. -or- Local incompatible because it was closed without saving after synchronizing with central. -or- The central model is missing. -or- The central model is incompatible. -or- The central model is corrupt or not an RVT file. -or- The central model was rolled back. -or- The central model's elements have been relinquished -or- The central model is overritten by other user. -or- An internal error happened on the central model, please contact the server administrator. |
| [Autodesk.Revit.Exceptions FileNotFoundException](73250198-dbc6-e760-4297-ec062f00f574.htm) | Cannot access the local file. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This Document is not a workshared document. -or- This Document is a local file that is not owned by the current user, who therefore is not allowed to modify it. |
| [Autodesk.Revit.Exceptions RevitServerCommunicationException](a0003d89-0113-6623-65da-0db5c568bfb6.htm) | The server-based central model could not be accessed because of a network communication error. |
| [Autodesk.Revit.Exceptions RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.htm) | An internal error happened on the server, please contact the server administrator. |
| [Autodesk.Revit.Exceptions RevitServerUnauthenticatedUserException](b9b68e56-c767-4680-a65b-73d268ee8860.htm) | User is not signed in with Autodesk id. |
| [Autodesk.Revit.Exceptions RevitServerUnauthorizedException](9e8c1efc-8719-fe01-f311-cfade7b177ed.htm) | User is not authorized to access the specified A360 project. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67bc7fd9-4d37-efa0-6582-c34d14334f15.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementsSketchTooLarge Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

The sketch defining the highlighted element is too large.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ElementsSketchTooLarge { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ElementsSketchTooLarge As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ElementsSketchTooLarge { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67be446c-e2e1-9dfe-315f-f5d6adc779b9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFreeFormAccessor Method

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Returns an interface providing access to free-form properties and methods for this Rebar element.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public RebarFreeFormAccessor GetFreeFormAccessor() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFreeFormAccessor As RebarFreeFormAccessor ``` |

 

| Visual C++ |
| --- |
| ``` public: RebarFreeFormAccessor^ GetFreeFormAccessor() ``` |

#### Return Value

The interface providing access to free-form properties and methods for this Rebar element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This method applies only to free form rebar. |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__67be5463-3504-076e-4280-a36eaa1d0b1e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SurfaceNdfType Property

---



|  |
| --- |
| [AdvancedOpaque Class](e8a19a97-fc76-71ad-c713-f2a62415475f.htm)   [See Also](#seeAlsoToggle) |

The property labeled "NDF" from the "AdvancedOpaque" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string SurfaceNdfType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SurfaceNdfType As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ SurfaceNdfType { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyInteger" with accepted values in the enumerated type "SurfaceNdfType".

# See Also

[AdvancedOpaque Class](e8a19a97-fc76-71ad-c713-f2a62415475f.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__67c230d2-e446-fed9-f648-69cf5dd395f8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilySymbolFilter Constructor

---



|  |
| --- |
| [FamilySymbolFilter Class](24cfdb4a-07e4-522d-4b9a-e0bba9387d5f.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to find all family symbols of the given family.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FamilySymbolFilter( 	ElementId familyId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	familyId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: FamilySymbolFilter( 	ElementId^ familyId ) ``` |

#### Parameters

familyId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The family id.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The familyId is invalid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FamilySymbolFilter Class](24cfdb4a-07e4-522d-4b9a-e0bba9387d5f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67c282a5-7e20-7f93-ae98-9a1aa3f6e706.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreatePerspective Method

---



|  |
| --- |
| [View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Returns a new perspective View3D.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static View3D CreatePerspective( 	Document document, 	ElementId viewFamilyTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreatePerspective ( _ 	document As Document, _ 	viewFamilyTypeId As ElementId _ ) As View3D ``` |

 

| Visual C++ |
| --- |
| ``` public: static View3D^ CreatePerspective( 	Document^ document,  	ElementId^ viewFamilyTypeId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to which the new View3D will be added.

viewFamilyTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the ViewFamilyType which will be used by the new View3D. The type needs to be a ThreeDimensional ViewType.

#### Return Value

The new perspective View3D.

# Remarks

The new View3D will receive a unique view name. The view will be oriented in the same position as the default 3D view.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Find a 3D view type
Dim collector1 As New FilteredElementCollector(document)
collector1 = collector1.OfClass(GetType(ViewFamilyType))
Dim viewFamilyTypes As IEnumerable(Of ViewFamilyType)

viewFamilyTypes = From elem In collector1 _
                  Let vftype = TryCast(elem, ViewFamilyType) _
                  Where vftype.ViewFamily = ViewFamily.ThreeDimensional _
                  Select vftype
' Create a new Perspective View3D
Dim view3D__1 As View3D = View3D.CreatePerspective(document, viewFamilyTypes.First().Id)
If view3D__1 IsNot Nothing Then
    ' By default, the 3D view uses a default orientation.
    ' Change the orientation by creating and setting a ViewOrientation3D 
    Dim eye As New XYZ(0, -100, 10)
    Dim up As New XYZ(0, 0, 1)
    Dim forward As New XYZ(0, 1, 0)
    view3D__1.SetOrientation(New ViewOrientation3D(eye, up, forward))

    ' turn off the far clip plane with standard parameter API
    Dim farClip As Parameter = view3D__1.LookupParameter("Far Clip Active")
    farClip.[Set](0)
End If
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This View Family Type is not a ThreeDimensional view type. -or- 3D view creation is not allowed in this family. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67c49547-b5b9-59ad-8106-65d90886a381.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ValueAtPointBase Class

---



|  |
| --- |
| [Members](0a377364-9fd2-2755-96c9-036808668550.htm)   [See Also](#seeAlsoToggle) |

A base class representing storage of values at a given point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class ValueAtPointBase : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ValueAtPointBase _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ValueAtPointBase : IDisposable ``` |

# Remarks

This class stores a set of measurements and corresponding mapped flags. The flags are defined in the enumerated type ValueAtPointFlags.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ValueAtPointBase    
  [Autodesk.Revit.DB.Analysis ValueAtPoint](00d82cae-806a-8145-5228-bb362c641790.htm)    
  [Autodesk.Revit.DB.Analysis VectorAtPoint](fcda8b78-e0a7-d99f-6e4e-e53e3e26fc8c.htm)

# See Also

[ValueAtPointBase Members](0a377364-9fd2-2755-96c9-036808668550.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67c49bb1-4901-744e-66e6-d04aad194be3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BrOrgFilter Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Filter"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BrOrgFilter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BrOrgFilter As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BrOrgFilter { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67c5e3f4-ea25-c20c-7caa-fffcb7283780.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhyMaterialParamShearMod3 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Shear modulus Z"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PhyMaterialParamShearMod3 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PhyMaterialParamShearMod3 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PhyMaterialParamShearMod3 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67c6168e-d4dc-537c-d4f4-cda6132b7977.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SeekItemId Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Seek Item ID"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SeekItemId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SeekItemId As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SeekItemId { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67c79458-4ea0-ae6a-4e8c-2cd18b32dfd4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEndFace Method

---



|  |
| --- |
| [Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)   [See Also](#seeAlsoToggle) |

Given a face, tell if it is an end cap face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsEndFace( 	Reference faceReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsEndFace ( _ 	faceReference As Reference _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsEndFace( 	Reference^ faceReference ) ``` |

#### Parameters

faceReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The reference of the face to be checked.

# See Also

[Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67ccc28b-dcf5-aa69-44c1-5a4da62e260a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FlexDuctType Property

---



|  |
| --- |
| [FlexDuct Class](39e3bd3a-8304-7785-dd10-4043aa0d7da4.htm)   [See Also](#seeAlsoToggle) |

The flex duct type of this flex duct.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FlexDuctType FlexDuctType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FlexDuctType As FlexDuctType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property FlexDuctType^ FlexDuctType { 	FlexDuctType^ get (); 	void set (FlexDuctType^ value); } ``` |

# See Also

[FlexDuct Class](39e3bd3a-8304-7785-dd10-4043aa0d7da4.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__67ce2128-8f9a-0817-b814-04fc3ab50bc0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SKPImportOptions Constructor (SKPImportOptions)

---



|  |
| --- |
| [SKPImportOptions Class](79e692ab-e01d-f723-158a-1951f40aa2b6.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of SKPImportOptions as a copy of the import options.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public SKPImportOptions( 	SKPImportOptions option ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	option As SKPImportOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: SKPImportOptions( 	SKPImportOptions^ option ) ``` |

#### Parameters

option
:   Type:  [Autodesk.Revit.DB SKPImportOptions](79e692ab-e01d-f723-158a-1951f40aa2b6.htm)    
     The SKP options to be copied.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SKPImportOptions Class](79e692ab-e01d-f723-158a-1951f40aa2b6.htm)

[SKPImportOptions Overload](def60ab4-b40e-2dc0-507e-f493229e4de7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67cfc0fe-aa04-4801-86dd-131b115671c7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [RebarShapeMultiplanarDefinition Class](47a3135c-ce53-c041-f551-0795767eaa41.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [RebarShapeMultiplanarDefinition](47a3135c-ce53-c041-f551-0795767eaa41.htm)

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

[RebarShapeMultiplanarDefinition Class](47a3135c-ce53-c041-f551-0795767eaa41.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__67d00d1d-40f0-f8a4-d3c1-83c2b6731a2d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reset Method

---



|  |
| --- |
| [KeyBasedTreeEntriesIterator Class](d842419d-d2a9-a839-0944-82f163884362.htm)   [See Also](#seeAlsoToggle) |

Resets the iterator to the initial state.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

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

[KeyBasedTreeEntriesIterator Class](d842419d-d2a9-a839-0944-82f163884362.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67d23606-8c83-1a2d-e175-856223055470.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MatchlineTopPlane Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top Constraint"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MatchlineTopPlane { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MatchlineTopPlane As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MatchlineTopPlane { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67d4a404-89bb-7d7e-3198-dd6fd596dcf1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MemberForcesServiceData Class

---



|  |
| --- |
| [Members](f64921c9-5a8c-b0d8-bb88-f27de7fe25a2.htm)   [See Also](#seeAlsoToggle) |

The data needed by member forces server to perform type definition.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public class MemberForcesServiceData : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class MemberForcesServiceData _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class MemberForcesServiceData : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Structure MemberForcesServiceData

# See Also

[MemberForcesServiceData Members](f64921c9-5a8c-b0d8-bb88-f27de7fe25a2.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__67d50d01-5563-569c-a844-027e1010513c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BackgroundDraftPatternIdParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Background Fill Pattern"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BackgroundDraftPatternIdParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BackgroundDraftPatternIdParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BackgroundDraftPatternIdParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67d7d339-07d6-bd6d-a67c-189274892531.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BackgroundColor Property

---



|  |
| --- |
| [TableCellStyle Class](e9a5280b-4009-004f-57a4-af1f292f9619.htm)   [See Also](#seeAlsoToggle) |

The background color of this cell in the grid view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public Color BackgroundColor { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BackgroundColor As Color 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property Color^ BackgroundColor { 	Color^ get (); 	void set (Color^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[TableCellStyle Class](e9a5280b-4009-004f-57a4-af1f292f9619.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67db5744-2f94-526c-da65-9ba90e5c7e5b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCreateSlantedWallWithSingularLayers Property

---



|  |
| --- |
| [BuiltInFailures CreationFailures Class](62f22d53-ffd1-5c31-12c2-9bf34a79f079.htm)   [See Also](#seeAlsoToggle) |

Cannot create wall - its layers would degenerate or intersect. Reduce the wall's height or slant.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCreateSlantedWallWithSingularLayers { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCreateSlantedWallWithSingularLayers As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCreateSlantedWallWithSingularLayers { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CreationFailures Class](62f22d53-ffd1-5c31-12c2-9bf34a79f079.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67dcb25e-8797-031c-cdac-c4f7dc44b440.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathReinLengthn2 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Alternating Bar - Length"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PathReinLengthn2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PathReinLengthn2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PathReinLengthn2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67dd86d6-cb0b-fca7-978b-8ef19fd5b3e6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Current Property

---



|  |
| --- |
| [LeaderArrayIterator Class](18c89236-4fdb-5d13-3f0e-052daeeb1586.htm)   [See Also](#seeAlsoToggle) |

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

[LeaderArrayIterator Class](18c89236-4fdb-5d13-3f0e-052daeeb1586.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67de181f-a10b-ffe2-a841-771f4306b074.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### KNDashM Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol kN-m, indicating unit Kilonewton meters.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId KNDashM { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property KNDashM As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ KNDashM { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67e54cf8-f9ba-fb2c-5519-6b54bdb1c51d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetExactLength Method

---



|  |
| --- |
| [CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)   [See Also](#seeAlsoToggle) |

Returns the sum of exact lengths of all curves in the loop.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double GetExactLength() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetExactLength As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetExactLength() ``` |

#### Return Value

The total length of the curves in the loop.

# See Also

[CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67e7bcbb-1384-3e2b-fcb4-186ee3b1adea.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Spacing Property

---



|  |
| --- |
| [LayoutRuleClearSpacing Class](09ba6ef0-6c4d-904a-715a-33755540fd26.htm)   [See Also](#seeAlsoToggle) |

Get or set the spacing of the beam system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double Spacing { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Spacing As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Spacing { 	double get (); 	void set (double value); } ``` |

# Remarks

The value of spacing must be in [0, 30000), but in fact the spacing should not be too small or too great.

# See Also

[LayoutRuleClearSpacing Class](09ba6ef0-6c4d-904a-715a-33755540fd26.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67e85c2c-5fe2-85a7-ea52-0fe83203021e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurveLoop Property

---



|  |
| --- |
| [Path3d Class](459b6d79-a4e7-06f5-ab30-4ec8cffab15b.htm)   [See Also](#seeAlsoToggle) |

Get the Curve Loop of Path3d via index.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public CurveArray this[ 	int index ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property CurveLoop ( _ 	index As Integer _ ) As CurveArray 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property CurveArray^ CurveLoop[int index] { 	CurveArray^ get (int index); } ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

# Remarks

Returns the index order Curve Loop of Path3d.

# See Also

[Path3d Class](459b6d79-a4e7-06f5-ab30-4ec8cffab15b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67f0b78e-db6f-5095-f3e6-4e489274926f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForwardIterator Method

---



|  |
| --- |
| [ReferenceArray Class](bc9192b5-6666-a8de-0128-87dae479fd6a.htm)   [See Also](#seeAlsoToggle) |

Retrieve a forward moving iterator to the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual ReferenceArrayIterator ForwardIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ForwardIterator As ReferenceArrayIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual ReferenceArrayIterator^ ForwardIterator() ``` |

#### Return Value

Returns a forward moving iterator to the array.

# See Also

[ReferenceArray Class](bc9192b5-6666-a8de-0128-87dae479fd6a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67f79d01-2e87-3b9c-b7a9-5269673587e3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanSuppressTrailingZeros Method (ForgeTypeId)

---



|  |
| --- |
| [FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)   [See Also](#seeAlsoToggle) |

Checks whether trailing zeros can be suppressed for a given unit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool CanSuppressTrailingZeros( 	ForgeTypeId unitTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CanSuppressTrailingZeros ( _ 	unitTypeId As ForgeTypeId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool CanSuppressTrailingZeros( 	ForgeTypeId^ unitTypeId ) ``` |

#### Parameters

unitTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     Identifier of the unit.

#### Return Value

True if trailing zeros can be suppressed, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | unitTypeId is not a unit identifier. See UnitUtils.IsUnit(ForgeTypeId) and UnitUtils.GetUnitTypeId(DisplayUnitType). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)

[CanSuppressTrailingZeros Overload](55d9eef7-9cf3-3e2c-bdc2-f1e7eed04f73.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67f80199-6dad-2d0c-118c-85e83afed78a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidServer Method

---



|  |
| --- |
| [IExternalService Interface](37fe86a0-0668-5908-9966-dfac0e0c1fe3.htm)   [See Also](#seeAlsoToggle) |

Implement this method to check if the given instance represents a valid server of this service.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` bool IsValidServer( 	IExternalServer server ) ``` |

 

| Visual Basic |
| --- |
| ``` Function IsValidServer ( _ 	server As IExternalServer _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` bool IsValidServer( 	IExternalServer^ server ) ``` |

#### Parameters

server
:   Type:  [Autodesk.Revit.DB.ExternalService IExternalServer](91e4af0b-59c0-d640-107a-eebc4d99fa76.htm)    
     An instance of a server that is to be validated.

#### Return Value

True if the server is valid, False otherwise

# Remarks

This method is invoked by the framework upon registration of a server for this service. The simplest implementation would be to test whether the type of the object is as expected, but a service may have other rules for validating its servers.

# See Also

[IExternalService Interface](37fe86a0-0668-5908-9966-dfac0e0c1fe3.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)

<!-- Start of Syntax__67fd3e82-d717-98b7-1f35-19b47550f29c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExposureValue Property

---



|  |
| --- |
| [RenderingImageExposureSettings Class](94e2205c-ae49-e3a4-35e5-93d91f1bafb3.htm)   [See Also](#seeAlsoToggle) |

The value of rendering image exposure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double ExposureValue { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExposureValue As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ExposureValue { 	double get (); 	void set (double value); } ``` |

# Remarks

Default exposure value based on Lighting Scheme.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The value of rendering image exposure is not valid. The valid range is 0 to 21. |

# See Also

[RenderingImageExposureSettings Class](94e2205c-ae49-e3a4-35e5-93d91f1bafb3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__67ffcea7-1ebd-78c2-d8f3-b6cc5c3595d2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### gbXMLBuildingOperatingSchedule Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Enumerations for gbXML (Green Building XML) format, used for energy analysis, schema version 0.34.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum gbXMLBuildingOperatingSchedule ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration gbXMLBuildingOperatingSchedule ``` |

 

| Visual C++ |
| --- |
| ``` public enum class gbXMLBuildingOperatingSchedule ``` |

# Members

| Member name | Description |
| --- | --- |
| DefaultOperatingSchedule |  |
| TwentyFourHourSevenDayFacility |  |
| TwentyFourHourHourSixDayFacility |  |
| TwentyFourHourHourFiveDayFacility |  |
| TwelveHourSevenDayFacility |  |
| TwelveHourSixDayFacility |  |
| TwelveHourFiveDayFacility |  |
| KindergartenThruTwelveGradeSchool |  |
| YearRoundSchool |  |
| TheaterPerformingArts |  |
| Worship |  |
| NoOfOperatingScheduleEnums |  |

# Remarks

This enumeration corresponds to the buildingType attribute in gbXML and is used to specify the building operating schedule.

# See Also

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__68a666d3-3e85-d597-f409-da056e7b2e2b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Shape Property

---



|  |
| --- |
| [IConnector Interface](d5c02879-947d-d177-9c9a-52f662371da7.htm)   [See Also](#seeAlsoToggle) |

The shape of the connector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` ConnectorProfileType Shape { get; } ``` |

 

| Visual Basic |
| --- |
| ``` ReadOnly Property Shape As ConnectorProfileType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` property ConnectorProfileType Shape { 	ConnectorProfileType get (); } ``` |

# Remarks

This property is used to retrieve the shape of the connector.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Throw when this connector has no shape. |

# See Also

[IConnector Interface](d5c02879-947d-d177-9c9a-52f662371da7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68a95ba8-b6ff-6275-eb2b-2b54fe6d9e62.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetUnderlayBaseLevel Method

---



|  |
| --- |
| [ViewPlan Class](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)   [See Also](#seeAlsoToggle) |

Sets the level whose elevation will determine the bottom of the underlay range. The elevation of the next highest level will be used to determine the top of the underlay range.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetUnderlayBaseLevel( 	ElementId levelId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetUnderlayBaseLevel ( _ 	levelId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetUnderlayBaseLevel( 	ElementId^ levelId ) ``` |

#### Parameters

levelId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element id of a level in the project or else InvalidElementId.

# Remarks

If the level specified is the highest level, the underlay range will be unbounded. The underlay range will consist of everything above the specified level.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The ElementId levelId does not correspond to a Level in the project. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ViewPlan Class](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68ac11a5-1134-4944-3d57-e002cd376bec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSubFoldersData Method

---



|  |
| --- |
| [ExternalResourceBrowserData Class](94a46450-5467-45f2-0228-4c9f9821b4c9.htm)   [See Also](#seeAlsoToggle) |

Gets the subfolders data under the folder path of the browser data.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2019.1

# Syntax

| C# |
| --- |
| ``` public IList<ExternalResourceSubFolder> GetSubFoldersData() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSubFoldersData As IList(Of ExternalResourceSubFolder) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ExternalResourceSubFolder^>^ GetSubFoldersData() ``` |

#### Return Value

The subfolders data under folder path of the browser data.

# See Also

[ExternalResourceBrowserData Class](94a46450-5467-45f2-0228-4c9f9821b4c9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68ac67c4-ed50-e442-0ea1-9e04a98d1266.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PolygonSegmentTooShort Property

---



|  |
| --- |
| [BuiltInFailures GeometryFailures Class](6c30543b-4a09-53d0-0867-a2c2c49a4e57.htm)   [See Also](#seeAlsoToggle) |

Polygon segment too short

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId PolygonSegmentTooShort { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PolygonSegmentTooShort As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ PolygonSegmentTooShort { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GeometryFailures Class](6c30543b-4a09-53d0-0867-a2c2c49a4e57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68aea073-b430-27da-74e9-29786610476b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PanelScheduleType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

This enum declares the panel schedule type.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public enum PanelScheduleType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration PanelScheduleType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class PanelScheduleType ``` |

# Members

| Member name | Description |
| --- | --- |
| Unknown | Unknown panel schedule |
| Branch | Branch panel schedule |
| Switchboard | Switchboard schedule |
| Data | Data panel schedule |

# See Also

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__68af99e0-baee-d77a-b4da-576d1bd0648c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Rounding Property

---



|  |
| --- |
| [AnalysisDisplayDeformedShapeSettings Class](2d0041c8-1cb8-354f-678f-5719797c76fc.htm)   [See Also](#seeAlsoToggle) |

Increment to which numeric values of analysis results are rounded in deformed shape.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

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

[AnalysisDisplayDeformedShapeSettings Class](2d0041c8-1cb8-354f-678f-5719797c76fc.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__68b151b1-b170-f351-914a-5aa09ecdb1af.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidName Method

---



|  |
| --- |
| [NamingUtils Class](3c4e0c18-8133-ec1b-41a2-ed92c918e44c.htm)   [See Also](#seeAlsoToggle) |

Identifies if the input string is valid for use as an object name in Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static bool IsValidName( 	string string ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidName ( _ 	string As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidName( 	String^ string ) ``` |

#### Parameters

string
:   Type:  System String    
     The name to validate.

#### Return Value

True if the name is valid for use as a name in Revit, false if it contains prohibited characters and is invalid.

# Remarks

This routine checks only for prohibited characters in the string. When setting the name for an object there are other specific considerations which are checked (for example, the same name cannot be used twice for different elements of the same type). This routine does not check those conditions.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[NamingUtils Class](3c4e0c18-8133-ec1b-41a2-ed92c918e44c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68b24833-f329-eeae-cc06-0eab9dc22170.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadsMayBeNotUpToDate Property

---



|  |
| --- |
| [BuiltInFailures AnalyticalModelFailures Class](3633d562-0e24-5cad-ec0f-02e6cc6ad731.htm)   [See Also](#seeAlsoToggle) |

Reactions defined as Internal Load (Is Reaction) may no longer be valid since the analytical model has changed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId LoadsMayBeNotUpToDate { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoadsMayBeNotUpToDate As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ LoadsMayBeNotUpToDate { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AnalyticalModelFailures Class](3633d562-0e24-5cad-ec0f-02e6cc6ad731.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68b266bc-631e-fc0e-2d8f-e0b03ad72ec7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [LabelUtils](39d096e3-6f2f-13ac-237b-7549d9841ef5.htm)

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

[LabelUtils Class](39d096e3-6f2f-13ac-237b-7549d9841ef5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68b4818a-d737-be1e-0347-ebe305fe3b70.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InstanceVoidCutUtils Class

---



|  |
| --- |
| [Members](acedc5a0-5ad4-eeaf-a76a-c1410a847179.htm)   [See Also](#seeAlsoToggle) |

Utilities for cutting elements by unattached voids in family instances.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static class InstanceVoidCutUtils ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class InstanceVoidCutUtils ``` |

 

| Visual C++ |
| --- |
| ``` public ref class InstanceVoidCutUtils abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB InstanceVoidCutUtils

# See Also

[InstanceVoidCutUtils Members](acedc5a0-5ad4-eeaf-a76a-c1410a847179.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68b8e0f2-b5cd-8deb-44b4-f90d79e866a7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ClineSubcategory Property

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
| ``` public static ForgeTypeId ClineSubcategory { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ClineSubcategory As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ClineSubcategory { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68bdfa76-6d00-6305-acdb-d6b5a8d2c019.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [RoutingCriterionBase Class](6164e8ca-7eb1-2207-c596-d129e1aa146d.htm)   [See Also](#seeAlsoToggle) |

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

[RoutingCriterionBase Class](6164e8ca-7eb1-2207-c596-d129e1aa146d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68c1d227-424d-36da-0e5a-3f3e51e7f939.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DuctSizeSettings Class

---



|  |
| --- |
| [Members](c32219f2-4a33-846b-b41a-ab47dd6b8140.htm)   [See Also](#seeAlsoToggle) |

Duct sizes settings

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class DuctSizeSettings : Element,  	IEnumerable<KeyValuePair<DuctShape, DuctSizes>> ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DuctSizeSettings _ 	Inherits Element _ 	Implements IEnumerable(Of KeyValuePair(Of DuctShape, DuctSizes)) ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DuctSizeSettings : public Element,  	IEnumerable<KeyValuePair<DuctShape, DuctSizes^>> ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB.Mechanical DuctSizeSettings

# See Also

[DuctSizeSettings Members](c32219f2-4a33-846b-b41a-ab47dd6b8140.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__68c26af5-18b0-0a5f-5250-9a63c190c1eb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CircuitRating Property

---



|  |
| --- |
| [ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)   [See Also](#seeAlsoToggle) |

The default circuit rating for newly created circuit.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public double CircuitRating { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CircuitRating As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double CircuitRating { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The circuit rating should be non-negative. |

# See Also

[ElectricalSetting Class](d0c5bb12-7cf7-35e0-fc72-51e491c56bc2.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__68c7e9b9-a815-24f7-27fd-fb4eafe13f73.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AirChangesPerHour Property

---



|  |
| --- |
| [Space Class](b2c8970e-e554-8d73-06db-b65712c8a2e5.htm)   [See Also](#seeAlsoToggle) |

Get the Specified AirChangesPerHour of the Space.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public double AirChangesPerHour { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property AirChangesPerHour As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double AirChangesPerHour { 	double get (); } ``` |

# Remarks

This property is used to get the Specified AirChangesPerHour of the Space.

# See Also

[Space Class](b2c8970e-e554-8d73-06db-b65712c8a2e5.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__68c8df2b-2726-d198-75e1-8c050d604f95.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarIncludeLastBar Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Include Last Bar"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarIncludeLastBar { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarIncludeLastBar As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarIncludeLastBar { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68c995d8-f716-72e4-c63a-0aa8ae80d035.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleTopLevelOffsetParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top Offset"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ScheduleTopLevelOffsetParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ScheduleTopLevelOffsetParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ScheduleTopLevelOffsetParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68cb7547-8297-c341-e26f-3e6307247c6c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumberForScale Property

---



|  |
| --- |
| [AnalysisDisplayLegendSettings Class](a0362ecb-2442-6371-7e89-7a9ba66a0466.htm)   [See Also](#seeAlsoToggle) |

A fixed value to display on the legend scale (0 by default; 0 means width of legend scale is calculated dynamically).

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double NumberForScale { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property NumberForScale As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double NumberForScale { 	double get (); 	void set (double value); } ``` |

# See Also

[AnalysisDisplayLegendSettings Class](a0362ecb-2442-6371-7e89-7a9ba66a0466.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__68cc1abd-72f6-0b78-d983-b6b1ba7beafa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HVACLoadLoadsReportType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Enumerated type listing possible types of reports generated for HVAC loads.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public enum HVACLoadLoadsReportType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration HVACLoadLoadsReportType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class HVACLoadLoadsReportType ``` |

# Members

| Member name | Description |
| --- | --- |
| NoReport | No report |
| SimpleReport | A simple report with summaries |
| StandardReport | A standard report including zones and spaces |
| DetailedReport | A detailed report including orientation breakdowns |

# See Also

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__68d232d3-f67f-4c19-79e6-e7ceed0407f2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetHostPointReference Method

---



|  |
| --- |
| [PointRelativeToPoint Class](dbaeeb46-d0b2-5bbd-7a1c-2ad82920eeb6.htm)   [See Also](#seeAlsoToggle) |

Change the host point reference.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetHostPointReference( 	Reference hostPointReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetHostPointReference ( _ 	hostPointReference As Reference _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetHostPointReference( 	Reference^ hostPointReference ) ``` |

#### Parameters

hostPointReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)

# Remarks

Allowed references are to another Autodesk.Revit.DB.ReferencePoint element or to an Autodesk.Revit.DB.Point.

# See Also

[PointRelativeToPoint Class](dbaeeb46-d0b2-5bbd-7a1c-2ad82920eeb6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68d30140-93f9-9956-2d31-84b3c7b45af8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAssociatedZoneEquipment Method (Document, ISet(ElementId))

---



|  |
| --- |
| [ZoneEquipment Class](62330781-b72c-02ae-0c30-c557decfc38a.htm)   [See Also](#seeAlsoToggle) |

Gets the associated zone equipment of all specified analytical spaces.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020.1

# Syntax

| C# |
| --- |
| ``` public static ISet<ElementId> GetAssociatedZoneEquipment( 	Document document, 	ISet<ElementId> spaces ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetAssociatedZoneEquipment ( _ 	document As Document, _ 	spaces As ISet(Of ElementId) _ ) As ISet(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ISet<ElementId^>^ GetAssociatedZoneEquipment( 	Document^ document,  	ISet<ElementId^>^ spaces ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document where the analytical spaces and zone equipment exist.

spaces
:   Type:  System.Collections.Generic ISet   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The specified analytical spaces.

#### Return Value

All associated zone equipment, either explicitly assigned or implicitly assigned via system-zone.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ZoneEquipment Class](62330781-b72c-02ae-0c30-c557decfc38a.htm)

[GetAssociatedZoneEquipment Overload](10a1c7a8-3d0b-84fd-3f84-ca0336e4364e.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__68d3c8af-ee8f-8774-68aa-7618dc6de03e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ComputeArea Method

---



|  |
| --- |
| [Polyloop Class](207c5546-9116-fb85-8a7e-ff79654a7877.htm)   [See Also](#seeAlsoToggle) |

Gets the area for this polygon.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double ComputeArea() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ComputeArea As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double ComputeArea() ``` |

#### Return Value

The area for this polygon.

# Remarks

The area of the planar non-self-intersecting polygon computed as: A = 1/2 \* (X1 Y2) - (X2 Y1) + ... + (Xn Y1) - (X1 Yn)

# See Also

[Polyloop Class](207c5546-9116-fb85-8a7e-ff79654a7877.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__68d4a6b9-79f1-8b7e-704d-a3bfe6329e70.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSavedOrientation Method

---



|  |
| --- |
| [View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)   [See Also](#seeAlsoToggle) |

Gets the saved orientation of the View3D.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ViewOrientation3D GetSavedOrientation() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSavedOrientation As ViewOrientation3D ``` |

 

| Visual C++ |
| --- |
| ``` public: ViewOrientation3D^ GetSavedOrientation() ``` |

#### Return Value

The saved orientation of the View3D.

# See Also

[View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68d73a3e-8c67-ea9b-eaeb-2a30ff472e48.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarShapeFailureCustomError Property

---



|  |
| --- |
| [BuiltInFailures RebarFailures Class](2d5565b1-8ddd-7e13-0eb1-8537eb342225.htm)   [See Also](#seeAlsoToggle) |

'[ErrorMessage]'

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RebarShapeFailureCustomError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarShapeFailureCustomError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RebarShapeFailureCustomError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarFailures Class](2d5565b1-8ddd-7e13-0eb1-8537eb342225.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68d906bb-c8fc-6768-d277-291d1509fed7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HostAreaComputed Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Area"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId HostAreaComputed { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property HostAreaComputed As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ HostAreaComputed { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68da8230-c15e-bd91-42b9-90e8978fd9c5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShowGraphicalWarningPipeDisconnects Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Whether or not to show the graphical warnings for Pipe disconnects.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool ShowGraphicalWarningPipeDisconnects { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ShowGraphicalWarningPipeDisconnects As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ShowGraphicalWarningPipeDisconnects { 	bool get (); 	void set (bool value); } ``` |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__68db8e46-90de-6b54-3dae-598957d94201.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleSheetInstance Class

---



|  |
| --- |
| [Members](9eecbe0e-d837-be52-bf7d-7991606422be.htm)   [See Also](#seeAlsoToggle) |

An element that represents a particular placement of a schedule on a sheet.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class ScheduleSheetInstance : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ScheduleSheetInstance _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ScheduleSheetInstance : public Element ``` |

# Remarks

Use ScheduleSheetInstance.OwnerViewId to find the sheet on which a schedule is placed.

When a schedule is set to filter by sheet and placed on a sheet, it will create a new schedule with elements visible in the Viewport(s) on that sheet. The instance created belongs to the newly created schedule.

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB ScheduleSheetInstance

# See Also

[ScheduleSheetInstance Members](9eecbe0e-d837-be52-bf7d-7991606422be.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68dde6ef-ad0a-e53c-b0ce-3a4061528c5f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FlowAndPressureCalculationMethodHasBeenImproved Property

---



|  |
| --- |
| [BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)   [See Also](#seeAlsoToggle) |

During upgrade pressure drop calculations for hydronic piping systems using Simplified Colebrook or Custom Calculation methods have been recalculated using the Colebrook equation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FlowAndPressureCalculationMethodHasBeenImproved { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FlowAndPressureCalculationMethodHasBeenImproved As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FlowAndPressureCalculationMethodHasBeenImproved { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPCalculationFailures Class](9b5bb89e-0122-d5fe-6b2b-4963041f58e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68e04211-03ea-f0c6-50d5-b38fee4e7536.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetNumberOfShellLayers Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

Retrieves the number of interior or exterior shell layers.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int GetNumberOfShellLayers( 	ShellLayerType shellLayerType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetNumberOfShellLayers ( _ 	shellLayerType As ShellLayerType _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int GetNumberOfShellLayers( 	ShellLayerType shellLayerType ) ``` |

#### Parameters

shellLayerType
:   Type:  [Autodesk.Revit.DB ShellLayerType](75c640b9-9904-7882-43fc-a4dfc25ff53c.htm)    
     If ShellLayerType.Exterior return the number of exterior shell layers (or top shell layers for a roof, floor, or ceiling type). If ShellLayerType.Interior return the number of interior shell layers (or bottom shell layers for a roof, floor, or ceiling type).

#### Return Value

The number of shell layers in the interior or exterior shell, as specified by shellLayerType.

# Remarks

There will always be at least one core layer, i.e. one layer which is not a shell layer. You can change the shell/core layer boundary using  [SetNumberOfShellLayers(ShellLayerType, Int32)](8b8ea4e3-e697-6176-92c0-dc2687723a71.htm)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68e047a8-1349-2e7d-2029-e5afa9b14eeb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSlab Property

---



|  |
| --- |
| [MassSurfaceData Class](69fcb13c-6443-d1c2-29d5-08adc1261afd.htm)   [See Also](#seeAlsoToggle) |

Indicates if a floor is a slab.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsSlab { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsSlab As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsSlab { 	bool get (); } ``` |

# See Also

[MassSurfaceData Class](69fcb13c-6443-d1c2-29d5-08adc1261afd.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__68e13b86-805a-86ef-c1ed-e650c853dc0e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OpaqueAlbedo Property

---



|  |
| --- |
| [AdvancedOpaque Class](e8a19a97-fc76-71ad-c713-f2a62415475f.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Color" from the "AdvancedOpaque" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string OpaqueAlbedo { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property OpaqueAlbedo As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ OpaqueAlbedo { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDoubleArray4d". This property allows a connected asset.

# See Also

[AdvancedOpaque Class](e8a19a97-fc76-71ad-c713-f2a62415475f.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__68e5ec4d-5653-b23f-27f4-8b398bdf6a95.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Axis Property

---



|  |
| --- |
| [CylindricalFace Class](e0450bb3-d974-9759-ea41-55c332cd9926.htm)   [See Also](#seeAlsoToggle) |

Axis of the surface.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ Axis { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Axis As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Axis { 	XYZ^ get (); } ``` |

# See Also

[CylindricalFace Class](e0450bb3-d974-9759-ea41-55c332cd9926.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68e71157-fbce-c4a5-5e06-dcb8f8041e40.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarInternalMultiplanarArcConnector Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"INTERNAL: Multiplanar Arc Connector"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarInternalMultiplanarArcConnector { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarInternalMultiplanarArcConnector As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarInternalMultiplanarArcConnector { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68e76ff5-91fd-7db5-31b6-b65144c751b7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WallpaintFinish Property

---



|  |
| --- |
| [WallPaint Class](0eec978d-2f3f-e02d-32c8-082434311042.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Finish" from the "WallPaint" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string WallpaintFinish { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WallpaintFinish As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ WallpaintFinish { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyInteger" with accepted values in the enumerated type "WallpaintFinishType".

# See Also

[WallPaint Class](0eec978d-2f3f-e02d-32c8-082434311042.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__68e973e2-ae44-6a82-1d88-e526c60aea75.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [MEPAnalyticalConnection Class](5564555f-89fd-9348-33f2-f8d1d68cafe5.htm)   [See Also](#seeAlsoToggle) |

Creates a new analytical connection between two open connectors.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static MEPAnalyticalConnection Create( 	Document doc, 	ElementId typeId, 	Connector startConnector, 	Connector endConnector ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	doc As Document, _ 	typeId As ElementId, _ 	startConnector As Connector, _ 	endConnector As Connector _ ) As MEPAnalyticalConnection ``` |

 

| Visual C++ |
| --- |
| ``` public: static MEPAnalyticalConnection^ Create( 	Document^ doc,  	ElementId^ typeId,  	Connector^ startConnector,  	Connector^ endConnector ) ``` |

#### Parameters

doc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document where the new element is created.

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The type of new analytical connection.

startConnector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The open connector on the equipment side, whose level is inherited by the analytical connection.

endConnector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The open connector on the network.

#### Return Value

The newly created analytical connection element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Invalid connection type. -or- The connector does not support analytical connection. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MEPAnalyticalConnection Class](5564555f-89fd-9348-33f2-f8d1d68cafe5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68f2abd4-0f9c-01c0-47da-e228518f7d37.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ColorDepthType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type listing all Color Depth types of Print Setting.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum ColorDepthType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ColorDepthType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ColorDepthType ``` |

# Members

| Member name | Description |
| --- | --- |
| BlackLine | The type of Color Depth is Black Line. |
| GrayScale | The type of Color Depth is Gray Scale. |
| Color | The type of Color Depth is Color. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68f2c7d1-2d52-7055-c3c5-a2194fbb32b9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Insert Method

---



|  |
| --- |
| [WireTypeSet Class](4cd0b254-674b-e605-89e3-a016d586f535.htm)   [See Also](#seeAlsoToggle) |

Insert the specified wire type into the set.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool Insert( 	WireType item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Insert ( _ 	item As WireType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Insert( 	WireType^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB.Electrical WireType](f4d1a1cc-6968-251b-9692-247dc3ff6cff.htm)    
     The wire type to be inserted into the set.

#### Return Value

Returns whether the wire type was inserted into the set.

# See Also

[WireTypeSet Class](4cd0b254-674b-e605-89e3-a016d586f535.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__68f31f91-8806-fb68-52d7-50032582077d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WoodDiffusePerlinScaleZ Property

---



|  |
| --- |
| [AdvancedWood Class](1e8c37ad-69ea-aabc-df91-eda9c7fe54ff.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Anisotropic pos-z scale for diffuse albedo perlin" from the "AdvancedWood" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string WoodDiffusePerlinScaleZ { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WoodDiffusePerlinScaleZ As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ WoodDiffusePerlinScaleZ { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble".

# See Also

[AdvancedWood Class](1e8c37ad-69ea-aabc-df91-eda9c7fe54ff.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__68f3d01a-c7d8-9fa2-6b75-673061bfd09d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ColumnsExceedSegment Property

---



|  |
| --- |
| [BuiltInFailures ScheduleViewFailures Class](13d33852-f996-21d4-3d9b-f37c90785120.htm)   [See Also](#seeAlsoToggle) |

Some columns in Graphical Column Schedule exceed the segment's upper/lower bounds. You can add levels or adjust the view parameters.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ColumnsExceedSegment { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ColumnsExceedSegment As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ColumnsExceedSegment { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ScheduleViewFailures Class](13d33852-f996-21d4-3d9b-f37c90785120.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__68f7fb12-b59e-e418-2002-8c52d7143b4f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateContainsRule Method (ElementId, String)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether strings from the document contain a certain string value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateContainsRule( 	ElementId parameter, 	string value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateContainsRule ( _ 	parameter As ElementId, _ 	value As String _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateContainsRule( 	ElementId^ parameter,  	String^ value ) ``` |

#### Parameters

parameter
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A string-typed parameter used to get values from the document for a given element.

value
:   Type:  System String    
     The user-supplied string value for which values from the document will be searched.

#### Return Value

Created filter rule object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)

[CreateContainsRule Overload](edec10ee-1c85-8574-890b-3239ef96f34b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69a1f19c-cccd-3309-b80a-aa33cdfe9863.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundaryRestraintRotY Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Y Spring Modulus"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BoundaryRestraintRotY { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BoundaryRestraintRotY As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BoundaryRestraintRotY { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69a337fb-627e-d669-de4e-91dcad69c541.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NodeType Property

---



|  |
| --- |
| [ElectricalAnalyticalNode Class](562d1f7d-c9df-bee5-4659-4f8607ee4333.htm)   [See Also](#seeAlsoToggle) |

The type of electrical analytical node.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public ElectricalAnalyticalNodeType NodeType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property NodeType As ElectricalAnalyticalNodeType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElectricalAnalyticalNodeType NodeType { 	ElectricalAnalyticalNodeType get (); } ``` |

# See Also

[ElectricalAnalyticalNode Class](562d1f7d-c9df-bee5-4659-4f8607ee4333.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__69a596e8-72a8-52d6-a807-c443b5891dba.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidExternalFileReference Method

---



|  |
| --- |
| [ExternalFileReference Class](22f83514-5da8-bbf1-33e5-94e6212b53fe.htm)   [See Also](#seeAlsoToggle) |

Checks an ExternalFileReference to see if it is properly created.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool IsValidExternalFileReference( 	ExternalFileReference data ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidExternalFileReference ( _ 	data As ExternalFileReference _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidExternalFileReference( 	ExternalFileReference^ data ) ``` |

#### Parameters

data
:   Type:  [Autodesk.Revit.DB ExternalFileReference](22f83514-5da8-bbf1-33e5-94e6212b53fe.htm)    
     The ExternalFileReference to be checked

# Remarks

The following restrictions exist:

* PathType.Server is only valid for ExternalFileReferences of type ExternalFileReferenceType.RevitLink
* PathType.Content is only valid for ExternalFileReferences of type ExternalFileReferenceType.KeynoteTable, ExternalFileReferenceType.AssemblyCodeTable or ExternalFileReferenceType.Decal
* Keynote tables, assembly code tables and Decals (ExternalFileReferenceType.KeynoteTable, ExternalFileReferenceType.AssemblyCodeTable and ExternalFileReferenceType.Decal) may only be LinkedFileStatus.Loaded or LinkedFileStatus.NotFound.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternalFileReference Class](22f83514-5da8-bbf1-33e5-94e6212b53fe.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69a9ed44-2493-176d-b9b3-cd0381b6a1f2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CoverOffsetTooLong Property

---



|  |
| --- |
| [BuiltInFailures FabricFailures Class](1e10bead-55d2-51cb-dd33-80ed534cb0a8.htm)   [See Also](#seeAlsoToggle) |

Cover offset is greater than host thickness.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CoverOffsetTooLong { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CoverOffsetTooLong As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CoverOffsetTooLong { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FabricFailures Class](1e10bead-55d2-51cb-dd33-80ed534cb0a8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69aae96e-9ed0-5e40-066f-1abddb150d46.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DisplacedElementDisplacementZ Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Z Displacement"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DisplacedElementDisplacementZ { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DisplacedElementDisplacementZ As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DisplacedElementDisplacementZ { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69ae1bec-6c31-8b19-f1b1-69e2e2420674.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotConvertInstWorkPlaneToHost Property

---



|  |
| --- |
| [BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)   [See Also](#seeAlsoToggle) |

Can't convert Instance's Work Plane to Host. Try resetting Work Plane to a Level.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotConvertInstWorkPlaneToHost { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotConvertInstWorkPlaneToHost As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotConvertInstWorkPlaneToHost { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69af6934-c9a5-11ce-9387-35cc5bdec150.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpatialFieldMgrLegendTextType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Overall Legend Text"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpatialFieldMgrLegendTextType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpatialFieldMgrLegendTextType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpatialFieldMgrLegendTextType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69b54441-6ff1-14fa-2ff6-04d9bd5b1dcd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProjectRevisionRevisionNum Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Revision Number"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ProjectRevisionRevisionNum { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ProjectRevisionRevisionNum As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ProjectRevisionRevisionNum { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69b85527-f1e3-fee9-3431-4b8e0000963e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBoundingBox Method

---



|  |
| --- |
| [IDirectContext3DServer Interface](7709521d-9954-ef80-1f13-3bc6ee660d5d.htm)   [See Also](#seeAlsoToggle) |

Reports a bounding box of the geometry that this server submits for drawing.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` Outline GetBoundingBox( 	View dBView ) ``` |

 

| Visual Basic |
| --- |
| ``` Function GetBoundingBox ( _ 	dBView As View _ ) As Outline ``` |

 

| Visual C++ |
| --- |
| ``` Outline^ GetBoundingBox( 	View^ dBView ) ``` |

#### Parameters

dBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view where rendering will occur. If this argument is    a null reference (  Nothing  in Visual Basic)  , a view-independent bounding box should be reported.

#### Return Value

The bounding box as an Outline.

# Remarks

Revit uses the bounding box when navigating views, e.g., when a Zoom to Fit command is issued. The reported bounding box does not have to be tight. However, there may be unintended side-effects if the box is inconsistent with the submitted geometry.

# See Also

[IDirectContext3DServer Interface](7709521d-9954-ef80-1f13-3bc6ee660d5d.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__69b9940f-9890-8aa7-c935-67c5c80b2f24.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasBadLevel Method

---



|  |
| --- |
| [ClassificationEntry Class](11e0e748-358f-47f7-565d-e2e848d97fe8.htm)   [See Also](#seeAlsoToggle) |

Checks if the level is an integer in range between 1 and 5 inclusive.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool HasBadLevel() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function HasBadLevel As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool HasBadLevel() ``` |

#### Return Value

True if the level is not an integer from 1 to 5 inclusive. False otherwise.

# See Also

[ClassificationEntry Class](11e0e748-358f-47f7-565d-e2e848d97fe8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69bdb67a-57f1-1f9b-30ba-37d6c71c34db.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralElementDefinitionData Constructor

---



|  |
| --- |
| [StructuralElementDefinitionData Class](f7a0e8ec-6fd5-43e5-1a54-5cb6ebe009c7.htm)   [See Also](#seeAlsoToggle) |

Creates empty StructuralElementDefinitionData object.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public StructuralElementDefinitionData() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

 

| Visual C++ |
| --- |
| ``` public: StructuralElementDefinitionData() ``` |

# See Also

[StructuralElementDefinitionData Class](f7a0e8ec-6fd5-43e5-1a54-5cb6ebe009c7.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__69bf97c1-aa53-5448-69a7-3fc13c4910ef.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CoverTypeLength Property

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
| ``` public static ForgeTypeId CoverTypeLength { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CoverTypeLength As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CoverTypeLength { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69c3e2dc-e11e-7818-62a3-efdaede98d98.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StandardHookBendDiameterTooLarge Property

---



|  |
| --- |
| [BuiltInFailures RebarFailures Class](2d5565b1-8ddd-7e13-0eb1-8537eb342225.htm)   [See Also](#seeAlsoToggle) |

Rebar Standard Hook Bend Diameter is too large.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId StandardHookBendDiameterTooLarge { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StandardHookBendDiameterTooLarge As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ StandardHookBendDiameterTooLarge { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarFailures Class](2d5565b1-8ddd-7e13-0eb1-8537eb342225.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69c88357-8e5c-e6ba-377e-6177e262e945.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ExportFontInfo Class](c3dc100c-0e4d-419d-5cbd-1d59f149490c.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ExportFontInfo](c3dc100c-0e4d-419d-5cbd-1d59f149490c.htm)

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

[ExportFontInfo Class](c3dc100c-0e4d-419d-5cbd-1d59f149490c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69c92503-2025-ddab-ba91-3085aa2e8117.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasPlane Method

---



|  |
| --- |
| [CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)   [See Also](#seeAlsoToggle) |

Identifies if the CurveLoop is planar.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool HasPlane() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function HasPlane As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool HasPlane() ``` |

#### Return Value

True if the curve loop is planar, false otherwise.

# See Also

[CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69cf0c7b-6bd4-27bf-e3c8-1dc3cccf65f8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FunctionParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Function"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FunctionParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FunctionParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FunctionParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69d0e3b1-0fa5-a3a4-5554-3a26ae0c1c51.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reset Method

---



|  |
| --- |
| [PointIterator Class](0fba9730-8bb6-5f89-be4b-6132121b3058.htm)   [See Also](#seeAlsoToggle) |

Resets the iterator to the beginning of the collection.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

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

[PointIterator Class](0fba9730-8bb6-5f89-be4b-6132121b3058.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__69d4d684-9774-b729-551d-aacede3f86b9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetVisibility Method

---



|  |
| --- |
| [TemporaryGraphicsManager Class](1dd29f70-d381-fa60-8ffa-1076eac55ed7.htm)   [See Also](#seeAlsoToggle) |

Changes the visibility of temporary graphics object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void SetVisibility( 	int index, 	bool visible ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetVisibility ( _ 	index As Integer, _ 	visible As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetVisibility( 	int index,  	bool visible ) ``` |

#### Parameters

index
:   Type:  System Int32    
     Unique index of the temporary graphics object to be updated.

visible
:   Type:  System Boolean    
     if true, it will make the temporary graphics object visible. if false, it will make the temporary graphics object invisible.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | index is out of range of TemporaryGraphicsManager managed objects, or the indexed object has been removed from the document. |

# See Also

[TemporaryGraphicsManager Class](1dd29f70-d381-fa60-8ffa-1076eac55ed7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69d6f0a1-0dc0-a607-4b87-503b4a3ed833.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetTessellationSettings Method

---



|  |
| --- |
| [OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)   [See Also](#seeAlsoToggle) |

Sets all the tessellation parameters to its predefined values for the given resolution type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public void SetTessellationSettings( 	ExportResolution resolutionType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetTessellationSettings ( _ 	resolutionType As ExportResolution _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetTessellationSettings( 	ExportResolution resolutionType ) ``` |

#### Parameters

resolutionType
:   Type:  [Autodesk.Revit.DB ExportResolution](671e963b-c211-17e7-2c26-5d772d34798a.htm)    
     Type of exporting resolution.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69de97ea-b34e-108d-0cbb-dd766852a4b4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PushButtonData Constructor

---



|  |
| --- |
| [PushButtonData Class](a192ae26-cdca-3d36-72cb-51074ccd9fec.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of PushButtonData.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PushButtonData( 	string name, 	string text, 	string assemblyName, 	string className ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	name As String, _ 	text As String, _ 	assemblyName As String, _ 	className As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: PushButtonData( 	String^ name,  	String^ text,  	String^ assemblyName,  	String^ className ) ``` |

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

[PushButtonData Class](a192ae26-cdca-3d36-72cb-51074ccd9fec.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__69df17ad-927e-db03-b55c-8efdb5397494.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.GroupFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](15760715-852f-0b2d-d840-729a1a0a3e7a.htm)   [See Also](#seeAlsoToggle) |

Failures related to groups and their behavior.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class GroupFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class GroupFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class GroupFailures abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BuiltInFailures GroupFailures

# See Also

[BuiltInFailures GroupFailures Members](15760715-852f-0b2d-d840-729a1a0a3e7a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69dfa3e3-6dee-4f75-c3b0-a1188c14c33e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FeetOfWater39\_2DegreesFahrenheit Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Feet of water (39.2 Â°F).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FeetOfWater39_2DegreesFahrenheit { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FeetOfWater39_2DegreesFahrenheit As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FeetOfWater39_2DegreesFahrenheit { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69e99bb2-78d2-d3e0-af2e-71084838b771.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InfillCannotHaveDiffThickness Property

---



|  |
| --- |
| [BuiltInFailures InfillFailures Class](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.htm)   [See Also](#seeAlsoToggle) |

This infilling element must have the same thickness as its host.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId InfillCannotHaveDiffThickness { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InfillCannotHaveDiffThickness As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ InfillCannotHaveDiffThickness { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures InfillFailures Class](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69eb7a49-7e5a-da45-6579-c91386888a7f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LayoutRule Property

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

Identifies the layout rule of rebar set.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2009

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

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__69ec4266-efb4-3c69-a890-4b00d89b070d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Glazing Class

---



|  |
| --- |
| [Members](fa359f18-655d-6a69-1973-b65757f04424.htm)   [See Also](#seeAlsoToggle) |

A static class that provides access to the property names that appear in the Glazing visual asset schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static class Glazing ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class Glazing ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Glazing abstract sealed ``` |

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB.Visual Glazing

# See Also

[Glazing Members](fa359f18-655d-6a69-1973-b65757f04424.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__69ece493-bfac-d3c5-8a80-b99081ed0733.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomTagType Class

---



|  |
| --- |
| [Members](760d152d-e170-a279-4704-9d8a15704452.htm)   [See Also](#seeAlsoToggle) |

An object that represents a Room Tag type.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class RoomTagType : FamilySymbol ``` |

 

| Visual Basic |
| --- |
| ``` Public Class RoomTagType _ 	Inherits FamilySymbol ``` |

 

| Visual C++ |
| --- |
| ``` public ref class RoomTagType : public FamilySymbol ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
  [Autodesk.Revit.DB InsertableObject](73d870e0-a408-719c-58bd-1fb2ab8f9e5b.htm)    
  [Autodesk.Revit.DB FamilySymbol](a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm)    
  Autodesk.Revit.DB.Architecture RoomTagType

# See Also

[RoomTagType Members](760d152d-e170-a279-4704-9d8a15704452.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__69ecefc6-2bc3-d1b1-0777-b6ada9c4f789.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SegmentIndex Property

---



|  |
| --- |
| [ScheduleSheetInstance Class](68db8e46-90de-6b54-3dae-598957d94201.htm)   [See Also](#seeAlsoToggle) |

The schedule segment index of this ScheduleSheetInstance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022.1

# Syntax

| C# |
| --- |
| ``` public int SegmentIndex { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SegmentIndex As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int SegmentIndex { 	int get (); 	void set (int value); } ``` |

# Remarks

This property represents which schedule segment is referred to by this ScheduleSheetInstance. It normally starts with 0 and is less than the total number of the schedule segments, but there're some speccial cases:

* The segment index value could be -1, which means referring to the whole schedule but not a specific segment.
* The segment index value 0 should be considered the same as -1 if the referenced schedule is not split in normal cases.
* The segment index value must be 0 if the schedule is a revision schedule and in a family.
* The segment index value can't be modified if the schedule is filter by sheet. (In fact, The segment is referenced to is belongs to an internal schedule that only valid in the current view in this case.)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: segmentIndex is not a valid segment index. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The schedule of this ScheduleSheetInstance is a titleblock revision schedule or a sheet specific schedule. |

# See Also

[ScheduleSheetInstance Class](68db8e46-90de-6b54-3dae-598957d94201.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69ed6e9c-1ece-49b9-5cd2-5b68b3f72aed.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReverseIterator Method

---



|  |
| --- |
| [DefinitionBindingMap Class](52e2ee94-bcca-9e23-e835-6e9621da6059.htm)   [See Also](#seeAlsoToggle) |

Retrieve a backward moving iterator to the map.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual DefinitionBindingMapIterator ReverseIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ReverseIterator As DefinitionBindingMapIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual DefinitionBindingMapIterator^ ReverseIterator() ``` |

#### Return Value

Returns a backward moving iterator to the map.

# See Also

[DefinitionBindingMap Class](52e2ee94-bcca-9e23-e835-6e9621da6059.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69ed7d20-2170-9815-b92e-1df6d5e81256.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Lbf Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol lbf, indicating unit Pounds force.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Lbf { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Lbf As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Lbf { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69f129e5-5510-53ea-95be-ac0f4dcb2a4f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TotalLength Property

---



|  |
| --- |
| [Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)   [See Also](#seeAlsoToggle) |

The length of an individual bar multiplied by Quantity.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public double TotalLength { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property TotalLength As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double TotalLength { 	double get (); } ``` |

# See Also

[Rebar Class](70fd7426-f4a4-591c-8c06-3c18dda45e7d.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__69f30141-bd3b-8bdd-7a63-6353d4d495f9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Host Property

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [See Also](#seeAlsoToggle) |

If the instance is contained within another element, this property returns the containing element. An instance that is face hosted will return the element containing the face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Element Host { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Host As Element 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Element^ Host { 	Element^ get (); } ``` |

# Remarks

An example of an instance that is contained is a window. In this case the host property would return the wall in which the window is contained. Another example is an instance that is hosted to a planar or curved face in a Mass element will return the Mass element.

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69f35c0d-2570-8f9d-9518-172b9a22f077.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Comment Property

---



|  |
| --- |
| [SynchronizeWithCentralOptions Class](96eaf3af-971d-da6d-a857-88d6e602ffd4.htm)   [See Also](#seeAlsoToggle) |

User description of changes made since the last Sync with Central. Empty by default.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public string Comment { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Comment As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Comment { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: comment has more than 30,000 characters. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[SynchronizeWithCentralOptions Class](96eaf3af-971d-da6d-a857-88d6e602ffd4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69f6c21b-0a58-6d37-0c8c-d191671e5c2a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DatumVolumeOfInterest Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Scope Box"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DatumVolumeOfInterest { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DatumVolumeOfInterest As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DatumVolumeOfInterest { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69fa8c3d-d7ab-fb51-2d81-b0438b990018.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PhyMaterialParamMinimumYieldStress Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Minimum yield stress"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PhyMaterialParamMinimumYieldStress { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PhyMaterialParamMinimumYieldStress As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PhyMaterialParamMinimumYieldStress { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__69fcb13c-6443-d1c2-29d5-08adc1261afd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MassSurfaceData Class

---



|  |
| --- |
| [Members](604a0d68-9b18-59c3-ee68-53710f79ac69.htm)   [See Also](#seeAlsoToggle) |

Holds properties and other data about a face in the MassEnergyAnalyticalModel element.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` [ObsoleteAttribute("This class is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyAnalyticalDetailModel' and 'EnergyAnalysisSurface' classes instead.")] public class MassSurfaceData : Element ``` |

 

| Visual Basic |
| --- |
| ``` <ObsoleteAttribute("This class is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyAnalyticalDetailModel' and 'EnergyAnalysisSurface' classes instead.")> _ Public Class MassSurfaceData _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` [ObsoleteAttribute(L"This class is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use the 'EnergyAnalyticalDetailModel' and 'EnergyAnalysisSurface' classes instead.")] public ref class MassSurfaceData : public Element ``` |

# Remarks

Properties stored in the MassSurfaceData can be used in regeneration by the MassEnergyAnalyticalModel. For example, faces of the MassEnergyAnalyticalModel take their material values from the settings in the MassSurfaceData.

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB.Analysis MassSurfaceData

# See Also

[MassSurfaceData Members](604a0d68-9b18-59c3-ee68-53710f79ac69.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__69fdff13-7540-7c75-e975-8e47273ffd1b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DaNDashMPerM Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol daN-m/m, indicating unit Dekanewton meters per meter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DaNDashMPerM { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DaNDashMPerM As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DaNDashMPerM { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70a53592-01d0-7d35-afbc-fb59825b4124.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FilterDoubleRule Constructor

---



|  |
| --- |
| [FilterDoubleRule Class](221576be-5e81-8802-5487-671f58c6cd8c.htm)   [See Also](#seeAlsoToggle) |

Constructs an instance of FilterDoubleRule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FilterDoubleRule( 	FilterableValueProvider valueProvider, 	FilterNumericRuleEvaluator evaluator, 	double ruleValue, 	double epsilon ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	valueProvider As FilterableValueProvider, _ 	evaluator As FilterNumericRuleEvaluator, _ 	ruleValue As Double, _ 	epsilon As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: FilterDoubleRule( 	FilterableValueProvider^ valueProvider,  	FilterNumericRuleEvaluator^ evaluator,  	double ruleValue,  	double epsilon ) ``` |

#### Parameters

valueProvider
:   Type:  [Autodesk.Revit.DB FilterableValueProvider](50829fa2-03f1-9d4b-a3cd-2935d3bf8a8c.htm)    
     A pointer to a "value provider" object that will extract values from a Revit document.

evaluator
:   Type:  [Autodesk.Revit.DB FilterNumericRuleEvaluator](1f1a96bb-5f00-1a24-8c03-6984c88672b9.htm)    
     A pointer to the filter rule evaluator object that implements the desired test. The built-in evaluators implement commonly used tests such as less-than, greater-than less-than-or-equal-to, equal, etc.

ruleValue
:   Type:  System Double    
     The user-supplied value against which values from a Revit document will be tested.

epsilon
:   Type:  System Double    
     The tolerance within which two floating-point values may be considered equal.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for ruleValue is not finite -or- The given value for ruleValue is not a number -or- The given value for epsilon is not finite -or- The given value for epsilon is not a number |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FilterDoubleRule Class](221576be-5e81-8802-5487-671f58c6cd8c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70a80f11-165c-14ce-fcea-d19dba6591ee.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCutLayerModifiers Method

---



|  |
| --- |
| [ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.htm)   [See Also](#seeAlsoToggle) |

Gets all the cut layer modifiers from the layer info.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public IList<LayerModifier> GetCutLayerModifiers() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCutLayerModifiers As IList(Of LayerModifier) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<LayerModifier^>^ GetCutLayerModifiers() ``` |

#### Return Value

The cut layer modifier array.

# See Also

[ExportLayerInfo Class](88a99694-968a-99f7-870a-f46737bd5927.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70ab5511-d2f9-d818-d82b-33fd1016c361.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetServiceTypeName Method

---



|  |
| --- |
| [FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)   [See Also](#seeAlsoToggle) |

Gets the service type name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public string GetServiceTypeName( 	int serviceTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetServiceTypeName ( _ 	serviceTypeId As Integer _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetServiceTypeName( 	int serviceTypeId ) ``` |

#### Parameters

serviceTypeId
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The service type identifier.

# See Also

[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70b4c252-c6f4-5d00-c1ac-e4c2e3096baf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpaceOutdoorAirflow Property

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
| ``` public static ForgeTypeId SpaceOutdoorAirflow { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpaceOutdoorAirflow As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpaceOutdoorAirflow { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70b5d168-237b-b2d1-28cb-b022116ada4a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementParameterFilter Constructor (FilterRule)

---



|  |
| --- |
| [ElementParameterFilter Class](b0b40351-690c-eb5d-30c2-d4447a42fda1.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of an ElementParameterFilter from a single rule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElementParameterFilter( 	FilterRule filterRule ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	filterRule As FilterRule _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementParameterFilter( 	FilterRule^ filterRule ) ``` |

#### Parameters

filterRule
:   Type:  [Autodesk.Revit.DB FilterRule](a8f202ca-3c88-ecc4-fa93-549b26a412d7.htm)    
     The rule applied to test if the element passes this filter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElementParameterFilter Class](b0b40351-690c-eb5d-30c2-d4447a42fda1.htm)

[ElementParameterFilter Overload](11f624c6-b997-74f2-b3b0-61caaa3bfffb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70bc6ef7-27a5-b1a6-aada-7ffedfbf0260.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetStairs Method

---



|  |
| --- |
| [StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm)   [See Also](#seeAlsoToggle) |

Returns the stairs to which the stairs run belongs.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public Stairs GetStairs() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetStairs As Stairs ``` |

 

| Visual C++ |
| --- |
| ``` public: Stairs^ GetStairs() ``` |

#### Return Value

The stairs to which the stairs run belongs.

# See Also

[StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__70bd6afe-8775-cf7d-6f8e-3198f988ae71.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetNumericRevisionSettings Method

---



|  |
| --- |
| [RevisionNumberingSequence Class](52b6f8d8-4d5e-dfee-7782-5cd7a77ee543.htm)   [See Also](#seeAlsoToggle) |

Replaces the current numeric revision numbering settings with the provided settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void SetNumericRevisionSettings( 	NumericRevisionSettings settings ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetNumericRevisionSettings ( _ 	settings As NumericRevisionSettings _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetNumericRevisionSettings( 	NumericRevisionSettings^ settings ) ``` |

#### Parameters

settings
:   Type:  [Autodesk.Revit.DB NumericRevisionSettings](3de46f00-fbf9-0c6b-b7fa-5d33052d0091.htm)    
     The NumericRevisionSettings to be applied to numeric revision numbering.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | settings is not a valid NumericRevisionSettings. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RevisionNumberingSequence Class](52b6f8d8-4d5e-dfee-7782-5cd7a77ee543.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70c30770-b4ea-53e0-3906-1d5a5061c478.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [EnergyAnalysisDetailModel Class](858aed23-8a94-a70a-c1fc-ca03523e2f02.htm)   [See Also](#seeAlsoToggle) |

Creates a new energy analysis detailed model.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static EnergyAnalysisDetailModel Create( 	Document document, 	EnergyAnalysisDetailModelOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	options As EnergyAnalysisDetailModelOptions _ ) As EnergyAnalysisDetailModel ``` |

 

| Visual C++ |
| --- |
| ``` public: static EnergyAnalysisDetailModel^ Create( 	Document^ document,  	EnergyAnalysisDetailModelOptions^ options ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document that contains the physical model of the building.

options
:   Type:  [Autodesk.Revit.DB.Analysis EnergyAnalysisDetailModelOptions](18297392-d94a-cdab-feb3-81482771c44d.htm)    
     The options to control the calculation rules.

#### Return Value

The created model instance.

# Remarks

The generated energy model is always returned in world coordinates. The method TransformModel() transforms all surfaces in the model according to ground plane, shared coordinates and true north. The EnergyModelType in argument EnergyAnalysisDetailModelOptions indicates whether the generated energy model is based on rooms/spaces or building elements. The default value is EnergyModelType.SpatialElement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | An EnergyAnalysisDetailModel cannot be created if EnergyModelType.BuildingElement is input and AnalysisMode.ConceptualMasses is set in EnergyDataSettings (these values are incompatible). -or- Throws if there are no valid spatial bounding elements, or no valid spatial elements in the document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Failed to create the energy analysis detail model. |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | Throws if user aborted the energy analysis detail model creation. |

# See Also

[EnergyAnalysisDetailModel Class](858aed23-8a94-a70a-c1fc-ca03523e2f02.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__70c645c3-3787-18af-d4f9-86c292ed1b78.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Hours Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Hours.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Hours { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Hours As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Hours { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70c7de96-bfc4-9d58-c2a0-bc51c54027a4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpotSlopeSlopeDirection Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Slope Direction"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SpotSlopeSlopeDirection { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpotSlopeSlopeDirection As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SpotSlopeSlopeDirection { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70cdade6-f49f-e945-2314-ca4b2ee00cca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InsulationThickness Property

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

The insulation thickness of the fabrication part. If the fabrication part is not insulated, returns zero.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public double InsulationThickness { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property InsulationThickness As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double InsulationThickness { 	double get (); } ``` |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70cf4ab5-6187-8672-68c8-3de2f5457889.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Item Property

---



|  |
| --- |
| [CurveByPointsArray Class](05d7b8f5-e891-e58f-c1aa-3e0e5d96d19c.htm)   [See Also](#seeAlsoToggle) |

Gets or sets a curve at a specified index within the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual CurveByPoints this[ 	int index ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Property Item ( _ 	index As Integer _ ) As CurveByPoints 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property CurveByPoints^ Item[int index] { 	CurveByPoints^ get (int index); 	void set (int index, CurveByPoints^ value); } ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the curve to be set or retrieved.

#### Return Value

Returns the curve at the specified index.

# See Also

[CurveByPointsArray Class](05d7b8f5-e891-e58f-c1aa-3e0e5d96d19c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70cfd908-53b3-0415-b145-ed8baf50e40f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BasepointEastwestParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"E/W"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BasepointEastwestParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BasepointEastwestParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BasepointEastwestParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70d39629-0341-d1bc-58ed-b0d37200f693.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetVisibility Method

---



|  |
| --- |
| [ImportInstance Class](85b534b8-dd6c-bc13-7c46-c803c83481e4.htm)   [See Also](#seeAlsoToggle) |

Sets the visibility for the import instance in a family document.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetVisibility( 	FamilyElementVisibility visibility ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetVisibility ( _ 	visibility As FamilyElementVisibility _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetVisibility( 	FamilyElementVisibility^ visibility ) ``` |

#### Parameters

visibility
:   Type:  [Autodesk.Revit.DB FamilyElementVisibility](fae58e2d-817c-77f6-1747-58b0a4e01c7a.htm)

# Remarks

The visibility of the import instance geometry can be changed for different types of views and detail levels in the family document.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when visibility is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when regeneration failed, or the import instance is in a project document. |

# See Also

[ImportInstance Class](85b534b8-dd6c-bc13-7c46-c803c83481e4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70d4d92e-7b63-821c-4a00-b903e2f1d4e9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WinderLegTooShortOrRunWidthTooGreatFailure Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

One leg of the winder run is too small or the runwidth is too great.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId WinderLegTooShortOrRunWidthTooGreatFailure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WinderLegTooShortOrRunWidthTooGreatFailure As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ WinderLegTooShortOrRunWidthTooGreatFailure { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70d4fd18-cfe6-28ff-8fc1-5aa6af5b8d6e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewGraphSchedTextAppearance Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Text Appearance"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ViewGraphSchedTextAppearance { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewGraphSchedTextAppearance As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ViewGraphSchedTextAppearance { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70daa82a-8893-bc5c-fa4a-85737f5c261a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetWorksetIterator Method

---



|  |
| --- |
| [FilteredWorksetCollector Class](30e91d82-33a2-2561-db2a-28098a96b3ec.htm)   [See Also](#seeAlsoToggle) |

Returns a FilteredWorksetIterator to the worksets passing the current filter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public FilteredWorksetIterator GetWorksetIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetWorksetIterator As FilteredWorksetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: FilteredWorksetIterator^ GetWorksetIterator() ``` |

# Remarks

Calling this when you have an active iterator to this same collector will result in the first iterator being stopped by this call.

# See Also

[FilteredWorksetCollector Class](30e91d82-33a2-2561-db2a-28098a96b3ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70db68f9-a4a8-1b5c-3a55-336cb0920651.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CustMullionWidth2 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Width on side 2"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CustMullionWidth2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CustMullionWidth2 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CustMullionWidth2 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70e0e674-0f0d-1ec9-d7f6-78d750f49c3c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PascalSeconds Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Pascal seconds.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PascalSeconds { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PascalSeconds As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PascalSeconds { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70e3afea-50e2-5ff4-867d-c39094edbf65.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPartStatusDescription Method

---



|  |
| --- |
| [FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)   [See Also](#seeAlsoToggle) |

Gets the status description from its identifier.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public string GetPartStatusDescription( 	int statusId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPartStatusDescription ( _ 	statusId As Integer _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetPartStatusDescription( 	int statusId ) ``` |

#### Parameters

statusId
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The status identifier.

#### Return Value

The status description.

# See Also

[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70e93b7f-3c58-d43d-a323-0c4396bc8689.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsCabletrayBendradius Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Bend Radius"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsCabletrayBendradius { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsCabletrayBendradius As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsCabletrayBendradius { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70ea1fae-a218-8367-25ca-a9fa13237b70.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLossFactor Method

---



|  |
| --- |
| [LightType Class](42c83d85-60cd-52c3-7b97-b89e81d7d9fe.htm)   [See Also](#seeAlsoToggle) |

Return a copy of an object derived from LossFactor

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public LossFactor GetLossFactor() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLossFactor As LossFactor ``` |

 

| Visual C++ |
| --- |
| ``` public: LossFactor^ GetLossFactor() ``` |

# See Also

[LightType Class](42c83d85-60cd-52c3-7b97-b89e81d7d9fe.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__70ea4451-78f1-6a56-2d5d-c062edbd4f1f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSurfaces Method

---



|  |
| --- |
| [IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)   [See Also](#seeAlsoToggle) |

Gets the IfcSurface handles created representing the processed geometry and stored in this object.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ICollection<IFCAnyHandle> GetSurfaces() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSurfaces As ICollection(Of IFCAnyHandle) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<IFCAnyHandle^>^ GetSurfaces() ``` |

#### Return Value

The collection of surface handles.

# See Also

[IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__70ebd545-8eb1-4f3b-0381-c28d6b70ca2a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsReporting Property

---



|  |
| --- |
| [FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)   [See Also](#seeAlsoToggle) |

Indicates if the parameter is a reporting parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool IsReporting { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsReporting As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsReporting { 	bool get (); } ``` |

# Remarks

If true, the parameter is a reporting parameter associated to a dimension value, and cannot be modified. If false, the parameter is a driving parameter and if associated to a dimension, can modify the dimension it labels.

# See Also

[FamilyParameter Class](6175e974-870e-7fbc-3df7-46105f937a6e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70f177dd-6a33-e750-b6c5-1f48b72ce80b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UnableToMaintainExclusionsWarn Property

---



|  |
| --- |
| [BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)   [See Also](#seeAlsoToggle) |

Unable to maintain exclusion of some group members. Some excluded members have been restored.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId UnableToMaintainExclusionsWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property UnableToMaintainExclusionsWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ UnableToMaintainExclusionsWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70f24220-ca7b-6202-5167-1f8ca618b20b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDefaultParameterNameForKeySchedule Method

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

Gets the default parameter name that will be used when creating a key schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static string GetDefaultParameterNameForKeySchedule( 	Document document, 	ElementId categoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetDefaultParameterNameForKeySchedule ( _ 	document As Document, _ 	categoryId As ElementId _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ GetDefaultParameterNameForKeySchedule( 	Document^ document,  	ElementId^ categoryId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to which the new schedule will be added.

categoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ID of the category of elements that the schedule's keys will be associated with.

#### Return Value

The default parameter name.

# Remarks

See ViewSchedule.KeyScheduleParameterName for details.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- categoryId is not a valid category for a key schedule. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70f2ca0e-24eb-c921-7c51-4392ac5c6042.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathReinEndHookOrient2Wall Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Alternating Bar - End Hook Orientation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PathReinEndHookOrient2Wall { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PathReinEndHookOrient2Wall As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PathReinEndHookOrient2Wall { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70f78207-1109-3906-8e67-cd27df1f0ae8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FormatOptions Class

---



|  |
| --- |
| [Members](4b317c87-727e-b8e9-3f0b-2b5479090fb7.htm)   [See Also](#seeAlsoToggle) |

Options for formatting numbers with units.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class FormatOptions : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FormatOptions _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FormatOptions : IDisposable ``` |

# Remarks

The FormatOptions class contains settings that control how to format numbers with units as strings. It contains those settings that are typically chosen by an end user in the Format dialog and stored in the document.

The FormatOptions class is used in two different ways. A FormatOptions object in the  [Units](89d89465-897f-4105-b935-27edf67aab3e.htm)  class represents the default settings for the document. A FormatOptions object used elsewhere represents settings that may optionally override the default settings.

The  [UseDefault](e817be98-c824-0c22-bf5f-d293e67c8985.htm)  property controls whether a FormatOptions object represents default or custom formatting. If UseDefault is true, formatting will be according to the default settings in the Units class, and none of the other settings in the object are meaningful. If UseDefault is false, the object contains custom settings that override the default settings in the Units class. UseDefault is always false for FormatOptions objects in the Units class.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB FormatOptions

# See Also

[FormatOptions Members](4b317c87-727e-b8e9-3f0b-2b5479090fb7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__70fd7426-f4a4-591c-8c06-3c18dda45e7d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Rebar Class

---



|  |
| --- |
| [Members](8d51f38e-c03c-3ca7-da4c-7f4cb0ed77f4.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Represents a rebar element in Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2009

# Syntax

| C# |
| --- |
| ``` public class Rebar : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Rebar _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Rebar : public Element ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void Getinfo_Rebar(Rebar rebar)
{
    string message = "Rebar: ";
    //get the bar type of the rebar
    message += "\nBar Type: " + (rebar.Document.GetElement(rebar.GetTypeId()) as RebarBarType).Name;

    //get the curve information
    IList<Curve> curves = rebar.GetCenterlineCurves(false, false, false, MultiplanarOption.IncludeOnlyPlanarCurves, 0);
    message += "\n\nThe Curves property has " + curves.Count + " curves:";
    foreach (Curve curve in curves)
    {
        // Get curve start point
        message += "\nCurve start point:(" + curve.GetEndPoint(0).X + ", "
            + curve.GetEndPoint(0).Y + ", " + curve.GetEndPoint(0).Z + ")";
        // Get curve end point
        message += "; Curve end point:(" + curve.GetEndPoint(1).X + ", "
            + curve.GetEndPoint(1).Y + ", " + curve.GetEndPoint(1).Z + ")";
    }

    //get the host element of the rebar
    if (null != rebar.Document.GetElement(rebar.GetHostId())) //maybe some rebars don't have host
    {
        message += "\n\nThe host element ID : " + rebar.GetHostId().ToString();
    }

    TaskDialog.Show("Revit", message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub Getinfo_Rebar(rebar As Rebar)
    Dim message As String = "Rebar: "
    'get the bar type of the rebar
    message += vbLf & "Bar Type: " + TryCast(rebar.Document.GetElement(rebar.GetTypeId()), RebarBarType).Name

 'get the curve information
 Dim curves As IList(Of Curve) = rebar.GetCenterlineCurves(False, False, False, MultiplanarOption.IncludeOnlyPlanarCurves, 0)
 message += vbLf & vbLf & "The Curves property has " & curves.Count & " curves:"
    For Each curve As Curve In curves
        ' Get curve start point
        message += ((vbLf & "Curve start point:(" + curve.GetEndPoint(0).X & ", ") + curve.GetEndPoint(0).Y & ", ") + curve.GetEndPoint(0).Z & ")"
        ' Get curve end point
        message += (("; Curve end point:(" + curve.GetEndPoint(1).X & ", ") + curve.GetEndPoint(1).Y & ", ") + curve.GetEndPoint(1).Z & ")"
    Next

    'get the host element of the rebar
    If rebar.Document.GetElement(rebar.GetHostId()) IsNot Nothing Then
        'maybe some rebars don't have host
        message += vbLf & vbLf & "The host element ID : " + rebar.GetHostId().ToString()
    End If

    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB.Structure Rebar

# See Also

[Rebar Members](8d51f38e-c03c-3ca7-da4c-7f4cb0ed77f4.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__71a0301d-cff3-c411-5fcf-3bc9b3dacac6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FlowState Property

---



|  |
| --- |
| [PipePressureDropData Class](d9c2df4c-512f-3f0c-4c04-2f5cc5afa7d8.htm)   [See Also](#seeAlsoToggle) |

The flowState of the pipe.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public PipeFlowState FlowState { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FlowState As PipeFlowState 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property PipeFlowState FlowState { 	PipeFlowState get (); 	void set (PipeFlowState value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[PipePressureDropData Class](d9c2df4c-512f-3f0c-4c04-2f5cc5afa7d8.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__71a18217-7ec4-018f-4cd1-ced41b8d9e1b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsGrossBuildingArea Property

---



|  |
| --- |
| [AreaScheme Class](9b5fd895-692c-5b6f-87f9-e53b1cc7c163.htm)   [See Also](#seeAlsoToggle) |

Indicates if the area scheme is a Gross Building Area scheme.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsGrossBuildingArea { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsGrossBuildingArea As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsGrossBuildingArea { 	bool get (); } ``` |

# See Also

[AreaScheme Class](9b5fd895-692c-5b6f-87f9-e53b1cc7c163.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71a20b47-41d4-43be-4edb-b8b14cf56962.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RemoveAddInCommandBinding Method

---



|  |
| --- |
| [UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)   [See Also](#seeAlsoToggle) |

Removes an AddInCommandBinding.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void RemoveAddInCommandBinding( 	RevitCommandId revitCommandId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RemoveAddInCommandBinding ( _ 	revitCommandId As RevitCommandId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RemoveAddInCommandBinding( 	RevitCommandId^ revitCommandId ) ``` |

#### Parameters

revitCommandId
:   Type:  [Autodesk.Revit.UI RevitCommandId](0fb2f851-f469-f739-d6ee-89b40b25c4a2.htm)    
     The Revit command id to identify the command handler you want to remove the binding.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when uiApplication or revitCommandId is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the given command is not bound with this add-in. |

# See Also

[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__71a315e3-54db-cfc0-78ae-9aa8d0ed947c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticalModelWallTopProjection Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top y Projection"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnalyticalModelWallTopProjection { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticalModelWallTopProjection As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnalyticalModelWallTopProjection { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71a506f1-4b51-9c1a-ed04-c285769c22a3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReverseIterator Method

---



|  |
| --- |
| [FaceArray Class](8606c5c3-46fc-f66c-06a8-84fb35c56743.htm)   [See Also](#seeAlsoToggle) |

Retrieve a backward moving iterator to the array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual FaceArrayIterator ReverseIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ReverseIterator As FaceArrayIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual FaceArrayIterator^ ReverseIterator() ``` |

#### Return Value

Returns a backward moving iterator to the array.

# See Also

[FaceArray Class](8606c5c3-46fc-f66c-06a8-84fb35c56743.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71a5aa6f-f57d-001d-bb8a-a5f8e7c27bfe.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSheetLocation Method

---



|  |
| --- |
| [FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)   [See Also](#seeAlsoToggle) |

Gets the position and the orientation of the Fabric Sheet instance.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public Transform GetSheetLocation() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSheetLocation As Transform ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform^ GetSheetLocation() ``` |

#### Return Value

The location of the Fabric Sheet instance.

# See Also

[FabricSheet Class](1f420619-ab30-942a-e5b6-028b7ff3889f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__71a6ebc9-35f0-f23d-f0d3-ede51cc303f6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarSystemSpacingTopDirn1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top Major Spacing"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarSystemSpacingTopDirn1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarSystemSpacingTopDirn1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarSystemSpacingTopDirn1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71add4a4-9808-2d37-aab1-6fda4d09d16e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InstOutsideFaceBoundary Property

---



|  |
| --- |
| [BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)   [See Also](#seeAlsoToggle) |

Instance origin does not lie on host face. Instance will lose association to host.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId InstOutsideFaceBoundary { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property InstOutsideFaceBoundary As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ InstOutsideFaceBoundary { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71b38936-4019-4968-b834-6ae8650bc851.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConfusingPadByElementsInAnotherDesignOption Property

---



|  |
| --- |
| [BuiltInFailures DesignOptionFailures Class](306b7ebc-5d5e-e53f-d5e4-9a5da4162068.htm)   [See Also](#seeAlsoToggle) |

A pad in a Design Option cannot be hosted by a topography in another Design Option [--if you continue it will not be added to the design option set].

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ConfusingPadByElementsInAnotherDesignOption { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ConfusingPadByElementsInAnotherDesignOption As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ConfusingPadByElementsInAnotherDesignOption { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DesignOptionFailures Class](306b7ebc-5d5e-e53f-d5e4-9a5da4162068.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71b8da35-e50f-d642-e71b-26be20f1d80a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomDesignLightingLoadParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Specified Lighting Load"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RoomDesignLightingLoadParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoomDesignLightingLoadParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RoomDesignLightingLoadParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71b907a8-c147-3c2e-b2e0-dc268c461e71.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDockablePane Method

---



|  |
| --- |
| [UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)   [See Also](#seeAlsoToggle) |

Gets a DockablePane object by its ID.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public DockablePane GetDockablePane( 	DockablePaneId id ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDockablePane ( _ 	id As DockablePaneId _ ) As DockablePane ``` |

 

| Visual C++ |
| --- |
| ``` public: DockablePane^ GetDockablePane( 	DockablePaneId^ id ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.UI DockablePaneId](96149d8e-6393-9285-a721-76470e6c15b8.htm)    
     Unique identifier for the new pane.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if no dockable pane has been registered with identifier %id%. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the dockable pane with identifier %id% has not been created yet. |

# See Also

[UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__71be2141-457a-b6ce-9c67-ce7b21097316.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFillGrid Method

---



|  |
| --- |
| [FillPattern Class](cc546ee9-ba80-c13d-4b74-8c0e2517bc28.htm)   [See Also](#seeAlsoToggle) |

Gets the specified fill grid.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FillGrid GetFillGrid( 	int gridIdx ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFillGrid ( _ 	gridIdx As Integer _ ) As FillGrid ``` |

 

| Visual C++ |
| --- |
| ``` public: FillGrid^ GetFillGrid( 	int gridIdx ) ``` |

#### Parameters

gridIdx
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the fill grid.

#### Return Value

The fill grid.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The index of the FillGrid is not valid. |

# See Also

[FillPattern Class](cc546ee9-ba80-c13d-4b74-8c0e2517bc28.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71be9b9e-56cf-c332-2fd0-7c1204640dd6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementIdParameterValue Constructor (ElementId)

---



|  |
| --- |
| [ElementIdParameterValue Class](7de25c99-4f85-ef1d-7f64-74092f963c98.htm)   [See Also](#seeAlsoToggle) |

Value constructor

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public ElementIdParameterValue( 	ElementId value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	value As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementIdParameterValue( 	ElementId^ value ) ``` |

#### Parameters

value
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElementIdParameterValue Class](7de25c99-4f85-ef1d-7f64-74092f963c98.htm)

[ElementIdParameterValue Overload](3cfdcc52-e11f-089c-07ab-e5da79daeba8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71c2801a-771b-97ce-3ef4-4c4e0904c5ec.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Noise Class

---



|  |
| --- |
| [Members](79da97b7-f626-5896-d1e0-b030a840c16d.htm)   [See Also](#seeAlsoToggle) |

A static class that provides access to the property names that appear in the Noise visual asset schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static class Noise ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class Noise ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Noise abstract sealed ``` |

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB.Visual Noise

# See Also

[Noise Members](79da97b7-f626-5896-d1e0-b030a840c16d.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__71c475b0-8d24-e751-9811-195d398bde60.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoltSpacing Property

---



|  |
| --- |
| [StructuralSectionCSlopedFlange Class](f098856a-bf46-2f95-1e7d-20d5f9500f90.htm)   [See Also](#seeAlsoToggle) |

Standard bolt spacing, in. (mm)

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public double BoltSpacing { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property BoltSpacing As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double BoltSpacing { 	double get (); 	void set (double value); } ``` |

# See Also

[StructuralSectionCSlopedFlange Class](f098856a-bf46-2f95-1e7d-20d5f9500f90.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__71c684fd-fc43-fadd-92f2-a7048c86d0fc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Executed Event

---



|  |
| --- |
| [AddInCommandBinding Class](a457ac93-b849-d962-8719-2b3910358b04.htm)   [See Also](#seeAlsoToggle) |

Occurs when the command associated with this AddInCommandBinding executes.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public event EventHandler<ExecutedEventArgs> Executed ``` |

 

| Visual Basic |
| --- |
| ``` Public Event Executed As EventHandler(Of ExecutedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<ExecutedEventArgs^>^ Executed { 	void add (EventHandler<ExecutedEventArgs^>^ value); 	void remove (EventHandler<ExecutedEventArgs^>^ value); } ``` |

# See Also

[AddInCommandBinding Class](a457ac93-b849-d962-8719-2b3910358b04.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__71cc965d-3af4-216e-bd6c-5d0b2ebdda0e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [NonContinuousRailStructure Class](a47d9f99-df86-e25b-d24f-635362d065b6.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
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

[NonContinuousRailStructure Class](a47d9f99-df86-e25b-d24f-635362d065b6.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__71d0c529-a129-29c7-096b-6cb663597f73.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAHanger Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Checks whether it is a hanger.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool IsAHanger() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsAHanger As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsAHanger() ``` |

#### Return Value

True if the part is a hanger. False otherwise.

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71d2c7e0-3a42-1a63-6e30-f7300ff78041.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GroupedModelElemHasViewSpecificSubordinates Property

---



|  |
| --- |
| [BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)   [See Also](#seeAlsoToggle) |

Unable to group the selected elements. Model element in group has view specific subordinates or view specific element in group has non-view specific subordinates.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId GroupedModelElemHasViewSpecificSubordinates { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GroupedModelElemHasViewSpecificSubordinates As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ GroupedModelElemHasViewSpecificSubordinates { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71d66cd5-6dae-22f0-f364-838e13cfbf8e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalysisDisplayColorEntry Class

---



|  |
| --- |
| [Members](36dd761e-7313-9ea5-7e61-279f027a1276.htm)   [See Also](#seeAlsoToggle) |

Contains one entry of intermediate colors in color settings for analysis display style.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class AnalysisDisplayColorEntry : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class AnalysisDisplayColorEntry _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class AnalysisDisplayColorEntry : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Analysis AnalysisDisplayColorEntry

# See Also

[AnalysisDisplayColorEntry Members](36dd761e-7313-9ea5-7e61-279f027a1276.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__71d8572e-a333-3111-b5bf-c5d18304d2c4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RuleValue Property

---



|  |
| --- |
| [FilterIntegerRule Class](a1c00400-62b9-8f42-fbd2-fa36725136aa.htm)   [See Also](#seeAlsoToggle) |

The user-supplied value against which values from a Revit document will be tested.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public int RuleValue { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RuleValue As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int RuleValue { 	int get (); 	void set (int value); } ``` |

# See Also

[FilterIntegerRule Class](a1c00400-62b9-8f42-fbd2-fa36725136aa.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71dafbc2-6ff2-5931-9d31-66f206a65476.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarConstraintTargetHostFaceType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

A type to help identify the individual face on a host element to which a Rebar handle is constrained.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public enum RebarConstraintTargetHostFaceType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration RebarConstraintTargetHostFaceType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class RebarConstraintTargetHostFaceType ``` |

# Members

| Member name | Description |
| --- | --- |
| FaceWithTagId | Face identified by integer tag. |
| Top | Face forms the top surface of the host geometry. |
| Bottom | Face forms the bottom surface of the host geometry. |
| End0 | Face forms the starting end surface of the host geometry. |
| End1 | Face forms the end surface of the host geometry. |
| Side0 | Face forms the exterior surface of the host geometry. |
| Side1 | Face forms the interior surface of the host geometry. |

# Remarks

For some types of host, it is possible to describe the face in terms of recognizable topology (i.e. Top, Bottom, etc.). However, for most elements, the face can only be identified by integer tag. In all cases, a Pick to the host face can be obtained by calling RebarConstraint.GetTargetHostFaceReference().

# See Also

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__71df8d73-bd2a-6462-fd00-ca1c637200af.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HostElementId Property

---



|  |
| --- |
| [LinkElementId Class](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)   [See Also](#seeAlsoToggle) |

The id of the element in the host, or invalidElementId if there is a link.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementId HostElementId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HostElementId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ HostElementId { 	ElementId^ get (); } ``` |

# See Also

[LinkElementId Class](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71dffec6-4011-e761-4abf-be9988206ac3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RightSideSupportType Property

---



|  |
| --- |
| [StairsType Class](efa84f53-19fa-039b-c5bb-8fcb72e09878.htm)   [See Also](#seeAlsoToggle) |

The type of right support used in the stair.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId RightSideSupportType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property RightSideSupportType As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ RightSideSupportType { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: rightSideStringerTypeId is not a valid support type. -or- When setting this property: The specified rightSideStringerTypeId doesn't match the desired style of the right side support. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The right support style is none, so this related data cannot be set. |

# See Also

[StairsType Class](efa84f53-19fa-039b-c5bb-8fcb72e09878.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__71e6d932-6b3a-3efb-70ac-5449898e4b06.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApplicableSegmentLengthRounding Property

---



|  |
| --- |
| [RebarRoundingManager Class](db93e1af-7588-f7f9-b505-490979327dac.htm)   [See Also](#seeAlsoToggle) |

The applicable rounding for shared parameters used by rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

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

[RebarRoundingManager Class](db93e1af-7588-f7f9-b505-490979327dac.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__71e834d1-94f3-ff71-f6e5-91d24d89dcf3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasValue Property

---



|  |
| --- |
| [IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.htm)   [See Also](#seeAlsoToggle) |

Identifies if the data is empty or contains a value.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool HasValue { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property HasValue As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool HasValue { 	bool get (); } ``` |

# See Also

[IFCData Class](34762033-771a-ebee-bd69-509c55ae78f0.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__71eaa252-5e4c-ee0b-0096-fc06fddeff11.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewDisplayBackgroundImageFlags Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

A collection of bit flags that control how the background image is positioned in relation to the crop region (or the view boundary).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public enum ViewDisplayBackgroundImageFlags ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ViewDisplayBackgroundImageFlags ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ViewDisplayBackgroundImageFlags ``` |

# Members

| Member name | Description |
| --- | --- |
| None | The image is displayed pixel-to-pixel |
| FitToScreen | The image is stretched in both directions |
| FixedAspectRatio | The image is stretched but the ratio of its height to width is preserved. |
| UseTiling | The pixels of the background are filled by tiling of the image. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71eb322c-4781-2d86-1067-b6fe9648524f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShowActiveWorkPlane Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Show the active work plane of the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void ShowActiveWorkPlane() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ShowActiveWorkPlane ``` |

 

| Visual C++ |
| --- |
| ``` public: void ShowActiveWorkPlane() ``` |

# Remarks

If this method is invoked while the current work plane is hidden, only the outline of the updated work plane will be shown immediately. The updated sketch plane will be shown fully after the current transaction is committed. Therefore it is recommended the Add-On commits the transaction before performing UI operations (for example, PickPoint).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when there is no active sketch plane, or when an error occurs during setting the sketch plane visibility. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71ec86d8-1032-1d91-0114-bc29d8e5d48b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WidthMeasuredAt Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The allowed values for the WALL\_TYPE\_WIDTH\_MEASURED\_AT parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public enum WidthMeasuredAt ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration WidthMeasuredAt ``` |

 

| Visual C++ |
| --- |
| ``` public enum class WidthMeasuredAt ``` |

# Members

| Member name | Description |
| --- | --- |
| Top | The top of the wall taking into account the top offset before any attachment. |
| Base | The base constraint of the wall. |
| Bottom | The bottom of the wall taking into the base offset before any attachment. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71ec9099-79fa-07b0-495d-74ad73d6d4d8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsUGridLine Property

---



|  |
| --- |
| [CurtainGridLine Class](42c94f55-1972-5f12-1dd4-db15ad1af3d3.htm)   [See Also](#seeAlsoToggle) |

Retrieve the direction of a grid line.If it is true,we say it is a UGridLine,otherwise it is VGridLine

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsUGridLine { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsUGridLine As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsUGridLine { 	bool get (); } ``` |

# See Also

[CurtainGridLine Class](42c94f55-1972-5f12-1dd4-db15ad1af3d3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71eddf47-d7f7-32b6-fe9f-6868a9fbeae0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BarDiameter Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Bar Diameter, in discipline Structural.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BarDiameter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BarDiameter As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BarDiameter { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71ee69fe-7a99-2af7-fb5e-d6e1533ea16e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ServerSupportsIFCLinks Method

---



|  |
| --- |
| [ExternalResourceServerUtils Class](a3147faa-ddc7-6cc1-8906-260582b6bc4a.htm)   [See Also](#seeAlsoToggle) |

Checks that the server referenced by the given ExternalResourceReference supports IFC links.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static bool ServerSupportsIFCLinks( 	ExternalResourceReference extRef ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ServerSupportsIFCLinks ( _ 	extRef As ExternalResourceReference _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ServerSupportsIFCLinks( 	ExternalResourceReference^ extRef ) ``` |

#### Parameters

extRef
:   Type:  [Autodesk.Revit.DB ExternalResourceReference](ffad9c15-8fc9-fbfd-f328-101533f4cf74.htm)    
     The ExternalResourceReference to check.

#### Return Value

True if the ExternalResourceReference refers to a server that supports IFC links. False otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternalResourceServerUtils Class](a3147faa-ddc7-6cc1-8906-260582b6bc4a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71f2c027-0b36-1deb-2df9-b3e51f04b06e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProjectGridsOnSectionBox Property

---



|  |
| --- |
| [View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)   [See Also](#seeAlsoToggle) |

This option projects all grids from the current 3d view on the bottom face of the section box. Only grids that are inside or intersects the section box

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public bool ProjectGridsOnSectionBox { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ProjectGridsOnSectionBox As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ProjectGridsOnSectionBox { 	bool get (); 	void set (bool value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Returns true if the view is not a view template. |

# See Also

[View3D Class](d795a238-fc24-1875-e64f-a2bef56ae949.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__71f52490-cfce-db3b-0aa0-e3cab84805d4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LightSourceInsideGeometry Property

---



|  |
| --- |
| [BuiltInFailures RenderFailures Class](bc5428d4-330d-3bcc-7cf4-5778210cfa7b.htm)   [See Also](#seeAlsoToggle) |

Light source is inside solid geometry. No light will be emitted during rendering.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId LightSourceInsideGeometry { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LightSourceInsideGeometry As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ LightSourceInsideGeometry { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RenderFailures Class](bc5428d4-330d-3bcc-7cf4-5778210cfa7b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)