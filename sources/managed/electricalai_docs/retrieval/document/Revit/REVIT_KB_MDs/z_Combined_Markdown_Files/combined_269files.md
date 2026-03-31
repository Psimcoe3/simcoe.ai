

<!-- Start of Syntax__fb021210-3324-def7-23bd-cb437d2c29f8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementMulticategoryFilter Constructor (ICollection(ElementId))

---



|  |
| --- |
| [ElementMulticategoryFilter Class](8d2774eb-3c47-5c3d-2866-8d4ab7408d2d.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to find elements whose category matches any of a given set of categories.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementMulticategoryFilter( 	ICollection<ElementId> categoryIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	categoryIds As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementMulticategoryFilter( 	ICollection<ElementId^>^ categoryIds ) ``` |

#### Parameters

categoryIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The category ids to match.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One or more categories was not valid for filtering. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElementMulticategoryFilter Class](8d2774eb-3c47-5c3d-2866-8d4ab7408d2d.htm)

[ElementMulticategoryFilter Overload](12249cf2-5f4d-0d13-5f7f-b282ecbd4bac.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb029049-10fb-0e2c-5216-813ff9b3e6b3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Origin Property

---



|  |
| --- |
| [CylindricalSurface Class](95d452c1-6f7f-9d8e-a4fb-e2f1fe2818bc.htm)   [See Also](#seeAlsoToggle) |

Center of the circle that defines the base of the cylinder. This is the origin of the local coordinate system associated with this cylinder.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

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

[CylindricalSurface Class](95d452c1-6f7f-9d8e-a4fb-e2f1fe2818bc.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb041590-6361-7fda-4f48-6e381dbb9f5d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DrawSplitLine Method

---



|  |
| --- |
| [SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)   [See Also](#seeAlsoToggle) |

Draws a split line on the corresponding slab, roof or floor.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public SlabShapeCreaseArray DrawSplitLine( 	SlabShapeVertex startVertex, 	SlabShapeVertex endVertex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function DrawSplitLine ( _ 	startVertex As SlabShapeVertex, _ 	endVertex As SlabShapeVertex _ ) As SlabShapeCreaseArray ``` |

 

| Visual C++ |
| --- |
| ``` public: SlabShapeCreaseArray^ DrawSplitLine( 	SlabShapeVertex^ startVertex,  	SlabShapeVertex^ endVertex ) ``` |

#### Parameters

startVertex
:   Type:  [Autodesk.Revit.DB SlabShapeVertex](8c022b91-723f-045d-3024-8cb037a41acc.htm)    
     The vertex to start the split line.

endVertex
:   Type:  [Autodesk.Revit.DB SlabShapeVertex](8c022b91-723f-045d-3024-8cb037a41acc.htm)    
     The vertex to end the split line.

#### Return Value

The newly created creases.

# Remarks

Drawing a split line may result in multiple creases, for example when the line crosses existing creases or boundary edges.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input vertex is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the input vertex is invalid. |

# See Also

[SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb11f6be-d1e2-728a-9c43-26ae89c8cc7c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### JournalingMode Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

All journaling modes supported by Revit external commands.

**Namespace:**   [Autodesk.Revit.Attributes](59587eb2-4714-707c-9ec9-766e70658df7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public enum JournalingMode ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration JournalingMode ``` |

 

| Visual C++ |
| --- |
| ``` public enum class JournalingMode ``` |

# Members

| Member name | Description |
| --- | --- |
| UsingCommandData | Uses the "StringStringMap" supplied in the command data. Hides all Revit journal entries in between the external command invocation and the StringStringMap entry. Commands which invoke the Revit UI for selection or for responses to task dialogs may not replay correctly. |
| NoCommandData | Does not write contents of the ExternalCommandData.Data map to the Revit journal. But does allow Revit API calls to write to the journal as needed. This option should allow commands which invoke the Revit UI for selection or for responses to task dialogs to replay correctly. |

# See Also

[Autodesk.Revit.Attributes Namespace](59587eb2-4714-707c-9ec9-766e70658df7.htm)

<!-- Start of Syntax__fb16978c-8211-7b64-33d9-faff78715a5f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureRealWorldScaleX Property

---



|  |
| --- |
| [BumpMap Class](7301801c-eef2-3077-7891-a3ee27db1a9b.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Size X" from the "BumpMap" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TextureRealWorldScaleX { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextureRealWorldScaleX As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TextureRealWorldScaleX { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDistance" with a minimum of "0.01".

# See Also

[BumpMap Class](7301801c-eef2-3077-7891-a3ee27db1a9b.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__fb175e54-120e-39c0-3a9f-ddf74f7f14fc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [DirectShapeLibrary Class](07489bae-ab9f-e2a8-0ac1-0a4d70cea458.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [DirectShapeLibrary](07489bae-ab9f-e2a8-0ac1-0a4d70cea458.htm)

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

[DirectShapeLibrary Class](07489bae-ab9f-e2a8-0ac1-0a4d70cea458.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb253656-e397-25cb-44a4-ac6c15ed783d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConnectPipePlaceholdersAtElbow Method (Document, ElementId, ElementId)

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
| ``` public static bool ConnectPipePlaceholdersAtElbow( 	Document document, 	ElementId placeholder1Id, 	ElementId placeholder2Id ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ConnectPipePlaceholdersAtElbow ( _ 	document As Document, _ 	placeholder1Id As ElementId, _ 	placeholder2Id As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ConnectPipePlaceholdersAtElbow( 	Document^ document,  	ElementId^ placeholder1Id,  	ElementId^ placeholder2Id ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

placeholder1Id
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element Id of pipe placeholder.

placeholder2Id
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element Id of pipe placeholder.

#### Return Value

True if connection succeeds, false otherwise.

# Remarks

There must be a physical end connection of placeholders. If connection fails, the placeholders cannot be physically connected.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element id placeholder1Id is not pipe placeholder. -or- The element id placeholder2Id is not pipe placeholder. -or- The elements belong to different types of system. -or- The curve placeholder1Id and placeholder2Id are not physically connected. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.htm)

[ConnectPipePlaceholdersAtElbow Overload](7c2063f9-d469-1e24-2eb9-602d96a8b635.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__fb30e6fc-5fbf-c96d-b66e-b22124fd6394.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetProfileCurve Method

---



|  |
| --- |
| [RevolvedSurface Class](ce0b47e0-2b24-61f5-1434-87fe3ff70390.htm)   [See Also](#seeAlsoToggle) |

Returns a copy of the profile curve expressed in the surface's coordinate system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public Curve GetProfileCurve() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetProfileCurve As Curve ``` |

 

| Visual C++ |
| --- |
| ``` public: Curve^ GetProfileCurve() ``` |

#### Return Value

A copy of the profile curve.

# See Also

[RevolvedSurface Class](ce0b47e0-2b24-61f5-1434-87fe3ff70390.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb311dd8-5106-6da8-f53d-a46d3e6912db.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GenericBumpMap Property

---



|  |
| --- |
| [Generic Class](dd16eb59-16ec-f121-289b-a69d26d7c789.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Bump" from the "Generic" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string GenericBumpMap { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GenericBumpMap As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ GenericBumpMap { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDoubleArray4d". This property allows a connected asset.

# See Also

[Generic Class](dd16eb59-16ec-f121-289b-a69d26d7c789.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__fb317cdc-63ec-3c9b-b7df-087d729fb52e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, Element, IList(Curve), Boolean, ElementId, ElementId, ElementId, ElementId)

---



|  |
| --- |
| [PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Creates a new PathReinforcement object from an array of curves. The newly created object will use a default Rebar Shape.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static PathReinforcement Create( 	Document document, 	Element hostElement, 	IList<Curve> curveArray, 	bool flip, 	ElementId pathReinforcementTypeId, 	ElementId rebarBarTypeId, 	ElementId startRebarHookTypeId, 	ElementId endRebarHookTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	hostElement As Element, _ 	curveArray As IList(Of Curve), _ 	flip As Boolean, _ 	pathReinforcementTypeId As ElementId, _ 	rebarBarTypeId As ElementId, _ 	startRebarHookTypeId As ElementId, _ 	endRebarHookTypeId As ElementId _ ) As PathReinforcement ``` |

 

| Visual C++ |
| --- |
| ``` public: static PathReinforcement^ Create( 	Document^ document,  	Element^ hostElement,  	IList<Curve^>^ curveArray,  	bool flip,  	ElementId^ pathReinforcementTypeId,  	ElementId^ rebarBarTypeId,  	ElementId^ startRebarHookTypeId,  	ElementId^ endRebarHookTypeId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

hostElement
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element that will host the PathReinforcement. The host can be a Structural Floor, Structural Wall, Structural Slab, or a Part created from a structural layer belonging to one of those element types.

curveArray
:   Type:  System.Collections.Generic IList   [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     An array of curves that will define the outline of the PathReinforcement.

flip
:   Type:  System Boolean    
     A flag controlling the bars relative to the curves.

pathReinforcementTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the PathReinforcementType.

rebarBarTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the RebarBarType.

startRebarHookTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the RebarHookType for the start of the bar. If this parameter is InvalidElementId, it means to create a rebar with no start hook.

endRebarHookTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the RebarHookType for the end of the bar. If this parameter is InvalidElementId, it means to create a rebar with no end hook.

#### Return Value

The newly created PathReinforcement.

# Remarks

The method sets Rebar Shape of primary bars only.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
PathReinforcement CreatePathReinforcement(Autodesk.Revit.DB.Document document, Wall wall)
{
    // Create a geometry line in the selected wall as the path
    List<Curve> curves = new List<Curve>();
    LocationCurve location = wall.Location as LocationCurve;
    XYZ start = location.Curve.GetEndPoint(0);
    XYZ end = location.Curve.GetEndPoint(1);
    curves.Add(Line.CreateBound(start, end));

    // Obtain the default types
    ElementId defaultRebarBarTypeId = document.GetDefaultElementTypeId(ElementTypeGroup.RebarBarType);
    ElementId defaultPathReinforcementTypeId = document.GetDefaultElementTypeId(ElementTypeGroup.PathReinforcementType);
    ElementId defaultHookTypeId = ElementId.InvalidElementId;

    // Begin to create the path reinforcement
    PathReinforcement rein = PathReinforcement.Create(document, wall, curves, true, defaultPathReinforcementTypeId, defaultRebarBarTypeId, defaultHookTypeId, defaultHookTypeId);
    if (null == rein)
    {
        throw new Exception("Create path reinforcement failed.");
    }

    // Give the user some information
    TaskDialog.Show("Revit","Create path reinforcement succeed.");

    return rein;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Function CreatePathReinforcement(document As Autodesk.Revit.DB.Document, wall As Wall) As PathReinforcement
    ' Create a geometry line in the selected wall as the path
    Dim curves As New List(Of Curve)()
    Dim location As LocationCurve = TryCast(wall.Location, LocationCurve)
    Dim start As XYZ = location.Curve.GetEndPoint(0)
    Dim [end] As XYZ = location.Curve.GetEndPoint(1)
    curves.Add(Line.CreateBound(start, [end]))

    ' Obtain the default types
    Dim defaultRebarBarTypeId As ElementId = document.GetDefaultElementTypeId(ElementTypeGroup.RebarBarType)
    Dim defaultPathReinforcementTypeId As ElementId = document.GetDefaultElementTypeId(ElementTypeGroup.PathReinforcementType)
    Dim defaultHookTypeId As ElementId = ElementId.InvalidElementId

    ' Begin to create the path reinforcement
    Dim rein As PathReinforcement = PathReinforcement.Create(document, wall, curves, True, defaultPathReinforcementTypeId, defaultRebarBarTypeId, _
        defaultHookTypeId, defaultHookTypeId)
    If rein Is Nothing Then
        Throw New Exception("Create path reinforcement failed.")
    End If

    ' Give the user some information
    TaskDialog.Show("Revit", "Create path reinforcement succeed.")

    Return rein
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input curveArray is empty. -or- The input curveArray contains at least one helical curve and is not supported for this operation. -or- The element hostElement was not found in the given document. -or- the host Element is not a valid host for Area Reinforcement, Path Reinforcement, Fabric Area or Fabric Sheet. -or- curves in curveArray are not continuous and open. -or- pathReinforcementTypeId should refer to an Path Reinforcement Type element. -or- rebarBarTypeId should refer to an RebarBarType element. -or- startRebarHookTypeId should be invalid or refer to an RebarHookType element. -or- endRebarHookTypeId should be invalid or refer to an RebarHookType element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | This method may not be called during dynamic update. |

# See Also

[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)

[Create Overload](073bd440-fbd7-5185-994c-224e7c52b172.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__fb334dfa-b6da-4c32-10c8-780be95772dc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SheetAssemblyDescription Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Assembly: Description"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SheetAssemblyDescription { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SheetAssemblyDescription As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SheetAssemblyDescription { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb345daf-b097-a458-8c69-2d8cbfa1eff3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SlabShapeCreases Property

---



|  |
| --- |
| [SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)   [See Also](#seeAlsoToggle) |

All of the creases that can be edited.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public SlabShapeCreaseArray SlabShapeCreases { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property SlabShapeCreases As SlabShapeCreaseArray 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property SlabShapeCreaseArray^ SlabShapeCreases { 	SlabShapeCreaseArray^ get (); } ``` |

# See Also

[SlabShapeEditor Class](06308ccc-46e7-6ff8-582c-6891af8b75e9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb368db2-914d-5867-0c4b-2380fbd3db49.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewSlabEdge Method (SlabEdgeType, ReferenceArray)

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [See Also](#seeAlsoToggle) |

Creates a slab edge along a reference array.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public SlabEdge NewSlabEdge( 	SlabEdgeType SlabEdgeType, 	ReferenceArray references ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewSlabEdge ( _ 	SlabEdgeType As SlabEdgeType, _ 	references As ReferenceArray _ ) As SlabEdge ``` |

 

| Visual C++ |
| --- |
| ``` public: SlabEdge^ NewSlabEdge( 	SlabEdgeType^ SlabEdgeType,  	ReferenceArray^ references ) ``` |

#### Parameters

SlabEdgeType
:   Type:  [Autodesk.Revit.DB SlabEdgeType](0f6f73b4-26b9-044e-590c-ef65a1210db8.htm)    
     The type of the slab edge to create

references
:   Type:  [Autodesk.Revit.DB ReferenceArray](bc9192b5-6666-a8de-0128-87dae479fd6a.htm)    
     An array of planar lines and arcs that represents the place where you want to place the slab edge.

#### Return Value

If successful a new slab edge object within the project, otherwise    a null reference (  Nothing  in Visual Basic)  .

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the slab edge type does not exist in the given document. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[NewSlabEdge Overload](d9f19a39-e6db-01ef-ae8c-b491ca8cbc51.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

<!-- Start of Syntax__fb42b3c0-86d2-ae03-a5c0-7d499f78e67d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLinePatternId Method

---



|  |
| --- |
| [Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)   [See Also](#seeAlsoToggle) |

Gets the line pattern id associated with this category for the given graphics style type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public ElementId GetLinePatternId( 	GraphicsStyleType graphicsStyleType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLinePatternId ( _ 	graphicsStyleType As GraphicsStyleType _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetLinePatternId( 	GraphicsStyleType graphicsStyleType ) ``` |

#### Parameters

graphicsStyleType
:   Type:  [Autodesk.Revit.DB GraphicsStyleType](60a5cce6-2cdc-dd63-e737-f584582ceeca.htm)    
     The type of graphics style.

#### Return Value

Returns the line pattern id associated with this category for the given graphics style type.

# Remarks

* The line pattern id will be one of the following:
* A negative value (representing a built-in line pattern)
* The id of a LinePatternElement
* InvalidElementId, indicating that this category does not have a stored line pattern id for this graphics style type.

# See Also

[Category Class](d390ecf6-e5db-d7c1-d7f2-766c0686e975.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb43e302-3ba7-a5cd-0ca2-428ec9e6a422.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCellText Method

---



|  |
| --- |
| [TableView Class](ba608411-21af-e924-2aa2-3595548ab39f.htm)   [See Also](#seeAlsoToggle) |

Gets the cell's text based on its type

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public string GetCellText( 	SectionType sectionType, 	int row, 	int column ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCellText ( _ 	sectionType As SectionType, _ 	row As Integer, _ 	column As Integer _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetCellText( 	SectionType sectionType,  	int row,  	int column ) ``` |

#### Parameters

sectionType
:   Type:  [Autodesk.Revit.DB SectionType](ad9a6cf0-aa1a-d011-b399-658345721aab.htm)    
     The requested section type

row
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Row Number in the Section

column
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Column Number in the Section

#### Return Value

The text for the given cell

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The sectionType is not a valid type for this view. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given row number row is invalid. -or- The given column number column is invalid. -or- A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[TableView Class](ba608411-21af-e924-2aa2-3595548ab39f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb484864-f9d0-7335-1f91-d7ac587f15fb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WiringType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

An enumerated type to list all wiring types.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public enum WiringType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration WiringType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class WiringType ``` |

# Members

| Member name | Description |
| --- | --- |
| Arc | Arc wiring is used to indicate wiring that is concealed within walls, ceilings, or floors. |
| Chamfer | Chamfered wiring can be used to indicate wiring that is exposed. |

# See Also

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fb54c007-6873-68f4-4772-e777609a441b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLeaderEnd Method

---



|  |
| --- |
| [IndependentTag Class](e52073e2-9d98-6fb5-eb43-288cf9ed2e28.htm)   [See Also](#seeAlsoToggle) |

Set the end position of the tag's leader that points to specified reference.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public void SetLeaderEnd( 	Reference referenceTagged, 	XYZ pointEnd ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLeaderEnd ( _ 	referenceTagged As Reference, _ 	pointEnd As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLeaderEnd( 	Reference^ referenceTagged,  	XYZ^ pointEnd ) ``` |

#### Parameters

referenceTagged
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The reference which is tagged.

pointEnd
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Point representing the end position of tag's leader

# Remarks

Tags with attached leaders or no leaders do not support leader ends.  [LeaderEndCondition](0b0575d6-446d-d3e8-3ef7-12faed553b20.htm)  for the tag's leader condition.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | There is no leader end because the tag does not use a free end leader or the leader is not visible. -or- The specified reference is not currently tagged. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IndependentTag Class](e52073e2-9d98-6fb5-eb43-288cf9ed2e28.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb59c48e-a7ab-1c99-60bb-3cda123691bb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDefaultNameForSchedule Method (Document, ElementId)

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

Gets the default view name that will be used when creating a regular schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static string GetDefaultNameForSchedule( 	Document document, 	ElementId categoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetDefaultNameForSchedule ( _ 	document As Document, _ 	categoryId As ElementId _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ GetDefaultNameForSchedule( 	Document^ document,  	ElementId^ categoryId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to which the new schedule will be added.

categoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ID of the category whose elements will be included in the schedule, or InvalidElementId for a multi-category schedule.

#### Return Value

The default view name.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- categoryId is not a valid category for a regular schedule. -or- The Areas category was specified but an area scheme ID was not provided. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[GetDefaultNameForSchedule Overload](f6494df4-739c-a9c4-4a77-856a453f3a3e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb60dfd3-e356-dadb-49b0-f8516b8e73a8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuildEntries Method

---



|  |
| --- |
| [KeyBasedTreeEntriesLoadContent Class](c612ce53-9774-8d74-28fc-5918c6491576.htm)   [See Also](#seeAlsoToggle) |

Builds a KeyBasedTreeEntries object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void BuildEntries() ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub BuildEntries ``` |

 

| Visual C++ |
| --- |
| ``` public: void BuildEntries() ``` |

# Remarks

This method will take all the entries that have been added, create a KeyBasedTreeEntries object out of these entries, and also record possible errors that occurred while constructing this KeyBasedTreeEntries object. After this function is called, no more entries can be added. And repeated calling of this function is not allowed either.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The KeyBasedTreeEntries object owned by this KeyBasedTreeEntriesLoadContent object is built already. Adding more KeyBasedTreeEntries as well as repeated building, is not supported. |

# See Also

[KeyBasedTreeEntriesLoadContent Class](c612ce53-9774-8d74-28fc-5918c6491576.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb631da2-2261-4683-a957-5b63ac985d62.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Print Method (ViewSet, View, Boolean)

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
| ``` public void Print( 	ViewSet views, 	View viewTemplate, 	bool useCurrentPrintSettings ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Print ( _ 	views As ViewSet, _ 	viewTemplate As View, _ 	useCurrentPrintSettings As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Print( 	ViewSet^ views,  	View^ viewTemplate,  	bool useCurrentPrintSettings ) ``` |

#### Parameters

views
:   Type:  [Autodesk.Revit.DB ViewSet](47b47de2-4234-01e0-af21-64334e2a4a4b.htm)    
     The set of views which need to be printed.

viewTemplate
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view template which apply to the set of views.

useCurrentPrintSettings
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     If true, print the view with the current print setting, otherwise with the print setting of the document of the view.

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

<!-- Start of Syntax__fb63b4c6-1702-538c-01b8-ee622e3e9993.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Profile Property

---



|  |
| --- |
| [BeamSystem Class](6c5c1bd2-8456-5ec9-c53e-0bd3f604ad06.htm)   [See Also](#seeAlsoToggle) |

Retrieve or set the profile of the BeamSystem.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public CurveArray Profile { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Profile As CurveArray 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property CurveArray^ Profile { 	CurveArray^ get (); 	void set (CurveArray^ value); } ``` |

# See Also

[BeamSystem Class](6c5c1bd2-8456-5ec9-c53e-0bd3f604ad06.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb63f7e3-b123-256a-41e9-8cb026d1faa6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCreateGutterError Property

---



|  |
| --- |
| [BuiltInFailures CreationFailures Class](62f22d53-ffd1-5c31-12c2-9bf34a79f079.htm)   [See Also](#seeAlsoToggle) |

Could not create Gutter. [Description]

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCreateGutterError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCreateGutterError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCreateGutterError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CreationFailures Class](62f22d53-ffd1-5c31-12c2-9bf34a79f079.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb781aa6-1ff9-b279-a64d-870d84ff1353.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlumbingFixturesSupplyPipe Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Supply Pipe"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PlumbingFixturesSupplyPipe { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PlumbingFixturesSupplyPipe As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PlumbingFixturesSupplyPipe { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb798428-a563-aba1-e53b-d002c911ebb3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralAttachmentTopReferencedend Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Top Attachment Referenced End"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralAttachmentTopReferencedend { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralAttachmentTopReferencedend As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralAttachmentTopReferencedend { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb84ce23-7f06-bac4-aec4-d63890b10597.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMatchingPreset Method

---



|  |
| --- |
| [SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.htm)   [See Also](#seeAlsoToggle) |

Finds the name of the 'per-document' SunAndShadowSettings that matches the properties of this per-view element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public string GetMatchingPreset() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMatchingPreset As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetMatchingPreset() ``` |

#### Return Value

Name of the per-document SunAndShadowSettings that matches the view specific element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The SunAndShadowSettings is not view-specific. |

# See Also

[SunAndShadowSettings Class](d616614b-a2ed-b0d0-4f11-f0a0b54a22e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb91d76a-10a0-bc20-1292-5d6919205b28.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FailedDowngradeCrossToElbow Property

---



|  |
| --- |
| [BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)   [See Also](#seeAlsoToggle) |

Failed to downgrade tee type to elbow type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FailedDowngradeCrossToElbow { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FailedDowngradeCrossToElbow As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FailedDowngradeCrossToElbow { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb9286fd-8d3b-04a9-8bcc-1867a917bcf5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GenericRepoHelperService Property

---



|  |
| --- |
| [ExternalServices BuiltInExternalServices Class](f189eb3f-7a3a-2891-657a-e18cbf014987.htm)   [See Also](#seeAlsoToggle) |

Unique service id.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ExternalServiceId GenericRepoHelperService { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GenericRepoHelperService As ExternalServiceId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ExternalServiceId^ GenericRepoHelperService { 	ExternalServiceId^ get (); } ``` |

# See Also

[ExternalServices BuiltInExternalServices Class](f189eb3f-7a3a-2891-657a-e18cbf014987.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)

<!-- Start of Syntax__fb92a4e7-f3a7-ef14-e631-342179b18de9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### View Class

---



|  |
| --- |
| [Members](d8d64cdb-46b7-6486-7cb5-07178b65a87b.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Base class for all types of views in Autodesk Revit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public class View : Element ``` |

 

| Visual Basic |
| --- |
| ``` Public Class View _ 	Inherits Element ``` |

 

| Visual C++ |
| --- |
| ``` public ref class View : public Element ``` |

# Remarks

A view can display an image produced from a Revit model. Views can be graphical (e.g. plans, elevations, or 3D views) or textual (e.g. schedules). Views keep track of Elements that can be seen in them.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void Getinfo_View(Autodesk.Revit.DB.View view)
{
    string message = "View: ";

    //get the name of the view
    message += "\nView name: " + view.Name;

    //The crop box sets display bounds of the view
    BoundingBoxXYZ cropBox = view.CropBox;
    XYZ max = cropBox.Max; //Maximum coordinates (upper-right-front corner of the box).
    XYZ min = cropBox.Min; //Minimum coordinates (lower-left-rear corner of the box).
    message += "\nCrop Box: ";
    message += "\nMaximum coordinates: (" + max.X + ", " + max.Y + ", " + max.Z + ")";
    message += "\nMinimum coordinates: (" + min.X + ", " + min.Y + ", " + min.Z + ")";


   //get the origin of the screen
    XYZ origin = view.Origin;
    message += "\nOrigin: (" + origin.X + ", " + origin.Y + ", " + origin.Z + ")";


    //The bounds of the view in paper space (in inches).
    BoundingBoxUV outline = view.Outline;
    UV maxUv = outline.Max; //Maximum coordinates (upper-right corner of the box).
    UV minUv = outline.Min; //Minimum coordinates (lower-left corner of the box).
    message += "\nOutline: ";
    message += "\nMaximum coordinates: (" + maxUv.U + ", " + maxUv.V + ")";
    message += "\nMinimum coordinates: (" + minUv.U + ", " + minUv.V + ")";

    //The direction towards the right side of the screen
    XYZ rightDirection = view.RightDirection;
    message += "\nRight direction: (" + rightDirection.X + ", " +
                   rightDirection.Y + ", " + rightDirection.Z + ")";

    //The direction towards the top of the screen
    XYZ upDirection = view.UpDirection;
    message += "\nUp direction: (" + upDirection.X + ", " +
                   upDirection.Y + ", " + upDirection.Z + ")";

    //The direction towards the viewer
    XYZ viewDirection = view.ViewDirection;
    message += "\nView direction: (" + viewDirection.X + ", " +
                   viewDirection.Y + ", " + viewDirection.Z + ")";

    //The scale of the view
    message += "\nScale: " + view.Scale;
    // Scale is meaningless for Schedules
    if (view.ViewType != ViewType.Schedule)
    {
        int testScale = 5;
        //set the scale of the view
        view.Scale = testScale;
        message += "\nScale after set: " + view.Scale;
    }

    TaskDialog.Show("Revit",message);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub Getinfo_View(view As Autodesk.Revit.DB.View)
    Dim message As String = "View: "

    'get the name of the view
    message += vbLf & "View name: " + view.Name

    'The crop box sets display bounds of the view
    Dim cropBox As BoundingBoxXYZ = view.CropBox
    Dim max As XYZ = cropBox.Max
    'Maximum coordinates (upper-right-front corner of the box).
    Dim min As XYZ = cropBox.Min
    'Minimum coordinates (lower-left-rear corner of the box).
    message += vbLf & "Crop Box: "
    message += vbLf & "Maximum coordinates: (" + max.X + ", " + max.Y + ", " + max.Z + ")"
    message += vbLf & "Minimum coordinates: (" + min.X + ", " + min.Y + ", " + min.Z + ")"


    'get the origin of the screen
    Dim origin As XYZ = view.Origin
    message += vbLf & "Origin: (" + origin.X + ", " + origin.Y + ", " + origin.Z + ")"


    'The bounds of the view in paper space (in inches).
    Dim outline As BoundingBoxUV = view.Outline
    Dim maxUv As UV = outline.Max
    'Maximum coordinates (upper-right corner of the box).
    Dim minUv As UV = outline.Min
    'Minimum coordinates (lower-left corner of the box).
    message += vbLf & "Outline: "
    message += vbLf & "Maximum coordinates: (" + maxUv.U + ", " + maxUv.V + ")"
    message += vbLf & "Minimum coordinates: (" + minUv.U + ", " + minUv.V + ")"

    'The direction towards the right side of the screen
    Dim rightDirection As XYZ = view.RightDirection
    message += vbLf & "Right direction: (" + rightDirection.X + ", " + rightDirection.Y + ", " + rightDirection.Z + ")"

    'The direction towards the top of the screen
    Dim upDirection As XYZ = view.UpDirection
    message += vbLf & "Up direction: (" + upDirection.X + ", " + upDirection.Y + ", " + upDirection.Z + ")"

    'The direction towards the viewer
    Dim viewDirection As XYZ = view.ViewDirection
    message += vbLf & "View direction: (" + viewDirection.X + ", " + viewDirection.Y + ", " + viewDirection.Z + ")"

    'The scale of the view
    message += vbLf & "Scale: " + view.Scale
    ' Scale is meaningless for Schedules
    If view.ViewType <> ViewType.Schedule Then
        Dim testScale As Integer = 5
        'set the scale of the view
        view.Scale = testScale
        message += vbLf & "Scale after set: " + view.Scale
    End If

    TaskDialog.Show("Revit", message)
End Sub
```

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  Autodesk.Revit.DB View    
  [Autodesk.Revit.DB.Analysis ViewSystemsAnalysisReport](a7b5b7de-dfdb-e57f-7fac-1ff1dbf35e4d.htm)    
  [Autodesk.Revit.DB TableView](ba608411-21af-e924-2aa2-3595548ab39f.htm)    
  [Autodesk.Revit.DB View3D](d795a238-fc24-1875-e64f-a2bef56ae949.htm)    
  [Autodesk.Revit.DB ViewDrafting](d0876cac-a93b-b89c-fa30-bcc14ab9d7f0.htm)    
  [Autodesk.Revit.DB ViewPlan](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)    
  [Autodesk.Revit.DB ViewSection](fcc75682-bd99-a97d-5a4d-0f8eb9e92ab5.htm)    
  [Autodesk.Revit.DB ViewSheet](af2ee879-173d-df3a-9793-8d5750a17b49.htm)

# See Also

[View Members](d8d64cdb-46b7-6486-7cb5-07178b65a87b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb981813-456a-c975-1610-aafc2a0fd1dd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShowArrowheadToCutMark Property

---



|  |
| --- |
| [StairsPathType Class](36994970-3d80-62a3-df6f-381d38f2eda0.htm)   [See Also](#seeAlsoToggle) |

True if the stairs path arrowhead should be shown to the cutmark, false if the arrow head is not shown.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool ShowArrowheadToCutMark { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ShowArrowheadToCutMark As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ShowArrowheadToCutMark { 	bool get (); 	void set (bool value); } ``` |

# See Also

[StairsPathType Class](36994970-3d80-62a3-df6f-381d38f2eda0.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__fb984692-75d6-cbc8-713f-045ea659e6cf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementsBelongToOtherSystem Property

---



|  |
| --- |
| [BuiltInFailures SystemsFailures Class](b67f74b9-4336-74df-edd9-04f5d08be033.htm)   [See Also](#seeAlsoToggle) |

You have selected elements that are already part of other Systems that have assigned Equipment. The elements you selected cannot be added to this System.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ElementsBelongToOtherSystem { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ElementsBelongToOtherSystem As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ElementsBelongToOtherSystem { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SystemsFailures Class](b67f74b9-4336-74df-edd9-04f5d08be033.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fb997601-df3a-2ea0-6dc9-c27f42dcfc29.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [ATFBaseExportOptions Class](7087cd85-a366-5f49-65a8-c58ed4bf74d8.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [ATFBaseExportOptions](7087cd85-a366-5f49-65a8-c58ed4bf74d8.htm)

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

[ATFBaseExportOptions Class](7087cd85-a366-5f49-65a8-c58ed4bf74d8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fba57dd8-45b1-f649-0c49-b553fb3b9e13.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementsAlreadyDisplacedInView Property

---



|  |
| --- |
| [BuiltInFailures DisplacementElementFailures Class](10e96831-1cc3-5fdc-48b2-44223537ef7c.htm)   [See Also](#seeAlsoToggle) |

You cannot copy a displacement set into a view if one or several of its elements already belong to another displacement set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ElementsAlreadyDisplacedInView { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ElementsAlreadyDisplacedInView As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ElementsAlreadyDisplacedInView { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DisplacementElementFailures Class](10e96831-1cc3-5fdc-48b2-44223537ef7c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fba62159-a0f3-2cb7-0e09-164a550d1c46.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BoundingBoxIsInsideFilter Constructor (Outline, Double, Boolean)

---



|  |
| --- |
| [BoundingBoxIsInsideFilter Class](eb8735d7-28fc-379d-9de9-1e02326851f5.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to match elements with a bounding box is contained by the given Outline, with the option to invert the filter and match all elements with a bounding box that are not contained by the given Outline.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public BoundingBoxIsInsideFilter( 	Outline outline, 	double tolerance, 	bool inverted ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	outline As Outline, _ 	tolerance As Double, _ 	inverted As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: BoundingBoxIsInsideFilter( 	Outline^ outline,  	double tolerance,  	bool inverted ) ``` |

#### Parameters

outline
:   Type:  [Autodesk.Revit.DB Outline](1ffe9215-0dd5-358f-495d-e983f9e7d295.htm)    
     The Outline used to find elements with a bounding box that are contained by it.

tolerance
:   Type:  System Double    
     The tolerance value to use instead of zero. See the tolerance property for details.

inverted
:   Type:  System Boolean    
     True if the filter should be inverted and match all elements with a bounding box that are not contained by the given Outline.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | outline is an empty Outline. -or- The given value for tolerance is not finite -or- The given value for tolerance is not a number |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[BoundingBoxIsInsideFilter Class](eb8735d7-28fc-379d-9de9-1e02326851f5.htm)

[BoundingBoxIsInsideFilter Overload](f7883323-6e5a-a1b8-486a-7664de5c0b92.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fba6d114-5249-e962-8f3b-2c93cfc35a6b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Btu Property

---



|  |
| --- |
| [SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)   [See Also](#seeAlsoToggle) |

Symbol Btu, indicating unit British thermal units.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Btu { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Btu As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Btu { 	ForgeTypeId^ get (); } ``` |

# See Also

[SymbolTypeId Class](6f430fd2-cbd1-237a-d4f5-4c9697e945e1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fba78904-560e-1536-d0fc-cbd8ac1e25f0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MaximumSize Property

---



|  |
| --- |
| [PrimarySizeCriterion Class](995cd666-6b07-2c7d-9052-6a36be3f7ed8.htm)   [See Also](#seeAlsoToggle) |

The maximum size of this criterion.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double MaximumSize { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MaximumSize As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double MaximumSize { 	double get (); 	void set (double value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[PrimarySizeCriterion Class](995cd666-6b07-2c7d-9052-6a36be3f7ed8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbabdfa5-a2fe-0cc4-1784-2739785e059b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetUV Method

---



|  |
| --- |
| [PolymeshTopology Class](fef5982c-3825-eed0-f792-1e0bff5509c2.htm)   [See Also](#seeAlsoToggle) |

Returns one UV coordinate at the given index.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public UV GetUV( 	int idx ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetUV ( _ 	idx As Integer _ ) As UV ``` |

 

| Visual C++ |
| --- |
| ``` public: UV^ GetUV( 	int idx ) ``` |

#### Parameters

idx
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     A zero-based index of a UV coordinate

#### Return Value

UV coordinates at the given index

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value is not a valid index of a UV coordinate of the polymesh. A valid valure is not negative and is smaller than the number of UV coordinates in the polymesh. |

# See Also

[PolymeshTopology Class](fef5982c-3825-eed0-f792-1e0bff5509c2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbaf12b9-14dd-573c-9cfb-88277f45a15e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### V1 Property

---



|  |
| --- |
| [PolymeshFacet Class](a7315aaf-631d-96af-368c-65f86b6c00ef.htm)   [See Also](#seeAlsoToggle) |

The first vertex of the facet

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int V1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property V1 As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int V1 { 	int get (); } ``` |

#### Field Value

An index of a vertex of a polymesh.

# See Also

[PolymeshFacet Class](a7315aaf-631d-96af-368c-65f86b6c00ef.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbb1043c-c83c-f6c5-5229-02e849d5d43a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BadRailingsError Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Can't create Railings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId BadRailingsError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BadRailingsError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ BadRailingsError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbb3ef78-b28c-9637-b995-b03e461bc9a4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsVertexPointValid Method

---



|  |
| --- |
| [Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)   [See Also](#seeAlsoToggle) |

Checks if the given vertex point can be added to this wire.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool IsVertexPointValid( 	XYZ vertexPoint ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsVertexPointValid ( _ 	vertexPoint As XYZ _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsVertexPointValid( 	XYZ^ vertexPoint ) ``` |

#### Parameters

vertexPoint
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vertex point.

#### Return Value

True if the vertex point can be added, false if the point cannot be added because there is already a vertex at this position on the view plane (within tolerance).

# Remarks

Vertices are projected to the view plane for comparison.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fbb5437c-cea9-1d12-a3af-460612c1f015.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLayoutMinimumSpacing Method

---



|  |
| --- |
| [SpacingRule Class](d8a51fa2-f3cd-5f12-d8cc-87c3888570f9.htm)   [See Also](#seeAlsoToggle) |

Set the Layout property to MinimumSpacing.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetLayoutMinimumSpacing( 	double distance, 	SpacingRuleJustification just, 	double gridlinesRotation, 	double offset ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLayoutMinimumSpacing ( _ 	distance As Double, _ 	just As SpacingRuleJustification, _ 	gridlinesRotation As Double, _ 	offset As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLayoutMinimumSpacing( 	double distance,  	SpacingRuleJustification just,  	double gridlinesRotation,  	double offset ) ``` |

#### Parameters

distance
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)

just
:   Type:  [Autodesk.Revit.DB SpacingRuleJustification](34e9dad9-8bfe-4ae3-9521-8021dc10dcd1.htm)

gridlinesRotation
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)

offset
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)

# Remarks

When changing the Layout to MinimumSpacing, you must also simultaneously set the Distance, Justification, GridlinesRotation, and Offset properties.

# See Also

[SpacingRule Class](d8a51fa2-f3cd-5f12-d8cc-87c3888570f9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbb9b3ea-b312-de08-006c-916e85663f62.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsSystemClassificationValid Method

---



|  |
| --- |
| [ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)   [See Also](#seeAlsoToggle) |

Checks that the MEPSystemType is valid for the domain of connector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsSystemClassificationValid( 	MEPSystemClassification systemClassification ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsSystemClassificationValid ( _ 	systemClassification As MEPSystemClassification _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsSystemClassificationValid( 	MEPSystemClassification systemClassification ) ``` |

#### Parameters

systemClassification
:   Type:  [Autodesk.Revit.DB MEPSystemClassification](43ec0d75-d6bb-2d08-a920-9715e83040e7.htm)    
     The MEPSystemType to be validated.

#### Return Value

True if the MEPSystemType is valid for the domain of the connector, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbbaaf4f-e89a-3190-f023-14c48eafa48f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FloorRecreateFailedWarning Property

---



|  |
| --- |
| [BuiltInFailures MassFailures Class](c9804646-1735-fe87-b758-a466adf5eae8.htm)   [See Also](#seeAlsoToggle) |

The floor cannot be created because no suitable level in the target document can be found.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FloorRecreateFailedWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FloorRecreateFailedWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FloorRecreateFailedWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MassFailures Class](c9804646-1735-fe87-b758-a466adf5eae8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbbd2c3a-435f-faa2-4284-4cf29b6fb1a2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementId Property

---



|  |
| --- |
| [LinkLoadResult Class](f846bfb0-b047-9332-567f-75ae880d8359.htm)   [See Also](#seeAlsoToggle) |

The id of the created or loaded linked model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId ElementId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ElementId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ ElementId { 	ElementId^ get (); } ``` |

# Remarks

This may be invalidElementId if there were errors (for example, LinkLoadResultType.SameModelAsHost causes no link to be created).

# See Also

[LinkLoadResult Class](f846bfb0-b047-9332-567f-75ae880d8359.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbc29ea7-aca2-9979-4acd-cb88c91b2cd9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Erase Method

---



|  |
| --- |
| [DefinitionBindingMap Class](52e2ee94-bcca-9e23-e835-6e9621da6059.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual int Erase( 	Definition key ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Erase ( _ 	key As Definition _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual int Erase( 	Definition^ key ) ``` |

#### Parameters

key
:   Type:  [Autodesk.Revit.DB Definition](8fe04f37-04e1-9e93-ffdb-e3900908e42a.htm)

# See Also

[DefinitionBindingMap Class](52e2ee94-bcca-9e23-e835-6e9621da6059.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbc36b17-8d42-96a3-4147-c8f361d82cf0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreationFailed Property

---



|  |
| --- |
| [BuiltInFailures MatchlineFailures Class](ab2c0054-0141-7327-f1eb-180d1ba68745.htm)   [See Also](#seeAlsoToggle) |

Matchline top extent should be higher than its bottom.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CreationFailed { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CreationFailed As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CreationFailed { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MatchlineFailures Class](ab2c0054-0141-7327-f1eb-180d1ba68745.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbc7f0fe-3e4c-f2f0-ce2c-478a202cd1e2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetToIdentity Method

---



|  |
| --- |
| [Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)   [See Also](#seeAlsoToggle) |

Set this TrfUV to the identity transform.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public Transform2D SetToIdentity() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetToIdentity As Transform2D ``` |

 

| Visual C++ |
| --- |
| ``` public: Transform2D^ SetToIdentity() ``` |

#### Return Value

Returns a pointer to "this"  [Transform2D](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)  .

# See Also

[Transform2D Class](49a13f08-08d7-95b1-d52e-65f90e6d4061.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbc9cf7c-8e63-00a8-bf9a-7277d2b5a38b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ActivateControlsAndDimensionsOnMultiSelect Property

---



|  |
| --- |
| [SelectionUIOptions Class](a87989f8-c37e-e5c6-7836-ff5014a66513.htm)   [See Also](#seeAlsoToggle) |

Indicates whether controls and temporary dimensions are activated on selection of multiple elements.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool ActivateControlsAndDimensionsOnMultiSelect { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ActivateControlsAndDimensionsOnMultiSelect As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool ActivateControlsAndDimensionsOnMultiSelect { 	bool get (); 	void set (bool value); } ``` |

# Remarks

Revit always shows certain controls and temporary dimensions for a single selected element When this option is set Revit also shows these controls and dimensions when multiple elements are selected. Note that this setting takes effect on the next selection change. To have this change take effect immediately use 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
Selection.SetElementIds(Selection.GetElementIds());
```

# See Also

[SelectionUIOptions Class](a87989f8-c37e-e5c6-7836-ff5014a66513.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)

<!-- Start of Syntax__fbd0d7af-ac40-e81e-8e06-8b2ce90be28b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FaceNode Class

---



|  |
| --- |
| [Members](9c9b3231-5470-7ee5-0d1a-89d78c4a1060.htm)   [See Also](#seeAlsoToggle) |

An output node that represents a Face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class FaceNode : RenderNode ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FaceNode _ 	Inherits RenderNode ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FaceNode : public RenderNode ``` |

# Remarks

See also:  [OnFaceBegin(FaceNode)](9a9f37ae-c8c2-7355-2c3b-f26762951f1d.htm)  .

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB RenderNode](9900b69b-7cb7-8555-75ac-4b5f22b5fa7f.htm)    
  Autodesk.Revit.DB FaceNode

# See Also

[FaceNode Members](9c9b3231-5470-7ee5-0d1a-89d78c4a1060.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbd33f0f-2c2c-c001-8041-996bc0872b2b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, Reference)

---



|  |
| --- |
| [SketchPlane Class](ba104029-d175-7e75-caef-667a4281f4af.htm)   [See Also](#seeAlsoToggle) |

Creates a new sketch plane from a reference to a planar face.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static SketchPlane Create( 	Document document, 	Reference planarFaceReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	planarFaceReference As Reference _ ) As SketchPlane ``` |

 

| Visual C++ |
| --- |
| ``` public: static SketchPlane^ Create( 	Document^ document,  	Reference^ planarFaceReference ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

planarFaceReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The reference of the planar face where the sketch plane will be created.

#### Return Value

The newly created sketch plane.

# Remarks

A reference relationship will be created between the face and the sketch plane.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Sketch plane creation is not allowed in this family. -or- The reference is not a planar face. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[SketchPlane Class](ba104029-d175-7e75-caef-667a4281f4af.htm)

[Create Overload](51d4403a-b78d-7527-f3bc-463d8044d0d4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbd36955-6804-f399-8662-c8b2519fd5ad.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarFreeFormHookStartPlaneAngle Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Hook Orientation At Start"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarFreeFormHookStartPlaneAngle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarFreeFormHookStartPlaneAngle As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarFreeFormHookStartPlaneAngle { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbd5a1a8-86ad-45a3-4099-01bc54ad99e1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FlowState Property

---



|  |
| --- |
| [Pipe Class](aa1b8294-c12d-ece0-00af-b17c1f1c9e03.htm)   [See Also](#seeAlsoToggle) |

The flow state of the pipe.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PipeFlowState FlowState { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property FlowState As PipeFlowState 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property PipeFlowState FlowState { 	PipeFlowState get (); } ``` |

# See Also

[Pipe Class](aa1b8294-c12d-ece0-00af-b17c1f1c9e03.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__fbd9f5a5-eb58-521e-66ba-fc003ccd6050.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### JoulesPerSquareMeterKelvin Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Joules per square meter Kelvin.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId JoulesPerSquareMeterKelvin { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property JoulesPerSquareMeterKelvin As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ JoulesPerSquareMeterKelvin { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbda471e-2e84-0263-89c3-ff21d6b96115.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReverseIterator Method

---



|  |
| --- |
| [PlanTopologySet Class](37cd93b8-bed4-0000-a389-48d5305d908e.htm)   [See Also](#seeAlsoToggle) |

Retrieve a backward moving iterator to the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual PlanTopologySetIterator ReverseIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ReverseIterator As PlanTopologySetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual PlanTopologySetIterator^ ReverseIterator() ``` |

#### Return Value

Returns a backward moving iterator to the set.

# See Also

[PlanTopologySet Class](37cd93b8-bed4-0000-a389-48d5305d908e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbdbb834-08e1-98d8-f9dc-28a1c4068ab7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FindReferenceTarget Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The type of reference to find from a ReferenceIntersector.

The type of reference to find

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum FindReferenceTarget ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration FindReferenceTarget ``` |

 

| Visual C++ |
| --- |
| ``` public enum class FindReferenceTarget ``` |

# Members

| Member name | Description |
| --- | --- |
| Element | An element. |
| Mesh | A mesh. |
| Edge | An edge. |
| Curve | A curve. |
| Face | A face. |
| All | All target types. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbdf6393-21be-362e-4033-56b62b2aff2c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetIntersectingElements Method

---



|  |
| --- |
| [DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)   [See Also](#seeAlsoToggle) |

Get the elements whose intersection with path produces points.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ICollection<ElementId> GetIntersectingElements() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetIntersectingElements As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ GetIntersectingElements() ``` |

# See Also

[DividedPath Class](8043b21a-7c78-e0cb-f7b3-495ace05de87.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbdfa9f5-a6fb-e335-689a-6935ca3a83d6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Distance Property

---



|  |
| --- |
| [WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)   [See Also](#seeAlsoToggle) |

Represents the distance from either the top or base of the wall for horizontal sweeps, or the parameter along the wall's path curve for vertical ones.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double Distance { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Distance As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Distance { 	double get (); 	void set (double value); } ``` |

#### Field Value

DistanceMeasuredFrom determines where the measurement starts from, depending on the orientation of the sweep. If the sweep or reveal is vertical, this distance is equal to the parameter along the wall's path curve.

# See Also

[WallSweepInfo Class](140876fa-4c17-ad27-8a12-a4bf755e06f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbe2c9fe-89ea-fc75-e418-cebc452ca1dd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MEPBuildingConstructionSet Class

---



|  |
| --- |
| [Members](a8caa03b-da29-6d9a-f156-9328436164bf.htm)   [See Also](#seeAlsoToggle) |

A set that contains MEPBuildingConstructions.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class MEPBuildingConstructionSet : APIObject,  	IEnumerable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class MEPBuildingConstructionSet _ 	Inherits APIObject _ 	Implements IEnumerable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class MEPBuildingConstructionSet : public APIObject,  	IEnumerable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB.Mechanical MEPBuildingConstructionSet

# See Also

[MEPBuildingConstructionSet Members](a8caa03b-da29-6d9a-f156-9328436164bf.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__fbe632a0-b829-a24d-1e12-32b1de7f3ed8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsMaxEdgeLengthSet Method

---



|  |
| --- |
| [OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)   [See Also](#seeAlsoToggle) |

Checks whether the MaxEdgeLength tessellation parameter is explicitly set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public bool IsMaxEdgeLengthSet() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsMaxEdgeLengthSet As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsMaxEdgeLengthSet() ``` |

#### Return Value

True if MaxEdgeLength tessellation parameter is explicitly set, false otherwise.

# See Also

[OBJExportOptions Class](fe6a5fe3-737a-1d30-fa65-37cc84e6e9d5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbea209c-4cbf-27c5-8b9e-31773c7cb014.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### KipFeetPerFoot Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

Kip feet per foot.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId KipFeetPerFoot { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property KipFeetPerFoot As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ KipFeetPerFoot { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbeaa68b-f16a-007f-4bd5-648bc597bb9e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Z Field

---



|  |
| --- |
| [CloudPoint Structure](c780514e-fc08-e055-bda4-c4fe455c13d3.htm)   [See Also](#seeAlsoToggle) |

The Z coordinate

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public float Z ``` |

 

| Visual Basic |
| --- |
| ``` Public Z As Single ``` |

 

| Visual C++ |
| --- |
| ``` public: float Z ``` |

# See Also

[CloudPoint Structure](c780514e-fc08-e055-bda4-c4fe455c13d3.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__fbedc21e-9c5e-7197-917e-70996023126d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HeatTransferCoefficient Property

---



|  |
| --- |
| [ThermalProperties Class](bfab51b3-ecd9-a082-9604-bf916248ca63.htm)   [See Also](#seeAlsoToggle) |

The heat transfer coefficient value (U-Value). The unit is watts per meter-squared kelvin (W/(m^2\*K)).

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

[ThermalProperties Class](bfab51b3-ecd9-a082-9604-bf916248ca63.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbef5afa-056f-a92c-f57b-36c5a1244d9a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotPasteViewSpecElemsFromDiffViews Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

Cannot paste view-specific elements from different views.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotPasteViewSpecElemsFromDiffViews { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotPasteViewSpecElemsFromDiffViews As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotPasteViewSpecElemsFromDiffViews { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbf09afd-0ccf-a489-5ebe-cadbe84f7137.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarSystemLayerSummaryDir2NoSpacing Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Minor, Both Faces (Brief)"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RebarSystemLayerSummaryDir2NoSpacing { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarSystemLayerSummaryDir2NoSpacing As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RebarSystemLayerSummaryDir2NoSpacing { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbf22d14-33c6-5d39-1703-a7c5576f4c53.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlignmentStationLabelSetEndStation Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Alignment Label Set End Station"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AlignmentStationLabelSetEndStation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AlignmentStationLabelSetEndStation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AlignmentStationLabelSetEndStation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbf3ae42-f2bb-c79c-01e3-bac772579ba6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurtaingridUseCurveDistn1 Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Use Curve Distance"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CurtaingridUseCurveDistn1 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CurtaingridUseCurveDistn1 As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CurtaingridUseCurveDistn1 { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbf71cbc-dc30-d600-0046-2e2303e336ea.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NoStructuralHostToAttachWarning Property

---



|  |
| --- |
| [BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)   [See Also](#seeAlsoToggle) |

There is no structural component to attach the hanger rod to.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NoStructuralHostToAttachWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NoStructuralHostToAttachWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NoStructuralHostToAttachWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures MEPFabricationFailures Class](e35f48ff-3e49-a71c-fb61-f7f9fa6c4382.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbf7861e-0b5e-3c66-56e1-87a18a28858b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [PanelScheduleSheetInstance Class](1fdb4d7e-ff99-78f7-8efa-87968f5defce.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of panel schedule on sheet and adds it to the document.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static PanelScheduleSheetInstance Create( 	Document ADoc, 	ElementId scheduleId, 	View DBView ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	ADoc As Document, _ 	scheduleId As ElementId, _ 	DBView As View _ ) As PanelScheduleSheetInstance ``` |

 

| Visual C++ |
| --- |
| ``` public: static PanelScheduleSheetInstance^ Create( 	Document^ ADoc,  	ElementId^ scheduleId,  	View^ DBView ) ``` |

#### Parameters

ADoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

scheduleId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)

DBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

#### Return Value

The newly created panel schedule sheet instance element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PanelScheduleSheetInstance Class](1fdb4d7e-ff99-78f7-8efa-87968f5defce.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fbf91f76-0c21-37dc-c69f-609c85753209.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BringForward Method (Document, View, ICollection(ElementId))

---



|  |
| --- |
| [DetailElementOrderUtils Class](7153db7b-62cc-f36b-b6a5-0ded8af7b5be.htm)   [See Also](#seeAlsoToggle) |

Moves the given detail instances one step closer to the front of all other detail instances in the view, while keeping the order of the given ones.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static void BringForward( 	Document pDocument, 	View pDBView, 	ICollection<ElementId> detailElementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub BringForward ( _ 	pDocument As Document, _ 	pDBView As View, _ 	detailElementIds As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void BringForward( 	Document^ pDocument,  	View^ pDBView,  	ICollection<ElementId^>^ detailElementIds ) ``` |

#### Parameters

pDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

pDBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view.

detailElementIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The set of detail elementIds to bring forward.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The set detailElementIds contains one or more non-detail element Ids. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DetailElementOrderUtils Class](7153db7b-62cc-f36b-b6a5-0ded8af7b5be.htm)

[BringForward Overload](974916e2-01a3-bfc1-6261-73f4ee83a719.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fbfe0796-bda1-2917-9532-c3bc399b90e4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [ForgeTypeId Class](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)   [See Also](#seeAlsoToggle) |

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

[ForgeTypeId Class](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc00110d-6c93-457f-9592-5336ecc59aac.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLineweightTableIterator Method

---



|  |
| --- |
| [ExportLineweightTable Class](5620708e-0c7c-ced6-9887-0237a9229800.htm)   [See Also](#seeAlsoToggle) |

Returns a ExportLineweightTableIterator that iterates through the collection.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ExportLineweightTableIterator GetLineweightTableIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLineweightTableIterator As ExportLineweightTableIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: ExportLineweightTableIterator^ GetLineweightTableIterator() ``` |

#### Return Value

A ExportLineweightTableIterator object that can be used to iterate through key-value pairs in the collection.

# See Also

[ExportLineweightTable Class](5620708e-0c7c-ced6-9887-0237a9229800.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc0333fa-a29d-aa50-559b-4d2cfac94eae.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadForceFy Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Fy"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LoadForceFy { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LoadForceFy As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LoadForceFy { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc038108-6279-839c-285b-effe342b4491.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionRectangular Class

---



|  |
| --- |
| [Members](df696d19-ab23-08a4-cc08-e6f128350d10.htm)   [See Also](#seeAlsoToggle) |

Defines common set of parameters for structural section rectangular contour.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public class StructuralSectionRectangular : StructuralSection ``` |

 

| Visual Basic |
| --- |
| ``` Public Class StructuralSectionRectangular _ 	Inherits StructuralSection ``` |

 

| Visual C++ |
| --- |
| ``` public ref class StructuralSectionRectangular : public StructuralSection ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSection](65b59d7d-bd7b-c71b-7159-dfc506a912ee.htm)    
  Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionRectangular    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionColdFormed](f77557fc-2bc9-e1f9-5984-57cbbe93508a.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionConcreteCross](e4ff1053-b04d-bd05-9cdd-f1dc33412bb2.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionConcreteRectangle](41507b3f-c1c1-bcc8-6606-fa270c324421.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionConcreteRectangleCut](bb633d61-429c-b20e-25b1-5ca59d1b2132.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionConcreteT](884cbd30-20f7-5ec2-958d-0713f731cdde.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionGeneralF](62ae95a2-2f1f-7541-75f9-7637f46baebd.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionGeneralH](512d0768-c2d3-f601-fd3e-c1db53d68f27.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionHotRolled](60cc6328-1e99-2a7b-03fb-983e52350e55.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionIWelded](d84c062e-4bfc-8da9-78f9-47174857db15.htm)    
  [Autodesk.Revit.DB.Structure.StructuralSections StructuralSectionUserDefined](bdd58bfd-3440-75c0-8d79-995713c75711.htm)

# See Also

[StructuralSectionRectangular Members](df696d19-ab23-08a4-cc08-e6f128350d10.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__fc07b9ff-9101-90d5-740d-0c19357c6919.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMEPConnectorInfo Method

---



|  |
| --- |
| [Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)   [See Also](#seeAlsoToggle) |

Gets MEP connector information.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public MEPConnectorInfo GetMEPConnectorInfo() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMEPConnectorInfo As MEPConnectorInfo ``` |

 

| Visual C++ |
| --- |
| ``` public: MEPConnectorInfo^ GetMEPConnectorInfo() ``` |

#### Return Value

Returns    a null reference (  Nothing  in Visual Basic)  if there is no MEP connector information associated.

# See Also

[Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc09d693-e4f2-8971-cb2d-b64cd6325227.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reset Method

---



|  |
| --- |
| [Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)   [See Also](#seeAlsoToggle) |

Resets the railing to the default one that the system generates.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

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

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Cannot reset the railing. |

# See Also

[Railing Class](4af1265f-859e-123b-ada5-a479324f3dee.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)

<!-- Start of Syntax__fc0cef9a-4418-83f4-faf7-d7628f2f3149.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ZoneEquipmentBehavior Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The behavior of zone equipment associated with spaces.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public enum ZoneEquipmentBehavior ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ZoneEquipmentBehavior ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ZoneEquipmentBehavior ``` |

# Members

| Member name | Description |
| --- | --- |
| OnePerSpace |  |
| GroupSpaces |  |

# See Also

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__fc13e8dc-133b-bb47-a784-d42608a7d8e4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IPointSetIterator Interface

---



|  |
| --- |
| [Members](7c4c6214-7b2e-6f99-0621-25321a9cd70f.htm)   [See Also](#seeAlsoToggle) |

An interface that Revit will call when iterating through sets of points on the engine.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public interface IPointSetIterator ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IPointSetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IPointSetIterator ``` |

# Remarks

An instance of this interface is obtained from the Point Cloud engine when the engine's CreatePointSetIterator method is called.

# See Also

[IPointSetIterator Members](7c4c6214-7b2e-6f99-0621-25321a9cd70f.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__fc160a77-9b51-6df5-a4e3-bf3f16ec3a8c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PipePressureDropService Property

---



|  |
| --- |
| [ExternalServices BuiltInExternalServices Class](f189eb3f-7a3a-2891-657a-e18cbf014987.htm)   [See Also](#seeAlsoToggle) |

The external service which permits registration of an alternate implementation for pipe pressure drop calculation. To use this service, programmers implement a server class that derives from  IPipePressureDropServer  .

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public static ExternalServiceId PipePressureDropService { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PipePressureDropService As ExternalServiceId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ExternalServiceId^ PipePressureDropService { 	ExternalServiceId^ get (); } ``` |

# See Also

[ExternalServices BuiltInExternalServices Class](f189eb3f-7a3a-2891-657a-e18cbf014987.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)

<!-- Start of Syntax__fc1af4a8-d97f-da4e-97bd-d97061977360.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElementArrayIterator Class

---



|  |
| --- |
| [Members](7e53aa77-9d68-bcb7-9aaa-3f6cfe15bb67.htm)   [See Also](#seeAlsoToggle) |

An iterator to an element array.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public abstract class ElementArrayIterator : APIObject,  	IEnumerator ``` |

 

| Visual Basic |
| --- |
| ``` Public MustInherit Class ElementArrayIterator _ 	Inherits APIObject _ 	Implements IEnumerator ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ElementArrayIterator abstract : public APIObject,  	IEnumerator ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  Autodesk.Revit.DB ElementArrayIterator

# See Also

[ElementArrayIterator Members](7e53aa77-9d68-bcb7-9aaa-3f6cfe15bb67.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc1bff98-15ce-be6e-5a23-89e20aad9e1d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [ConicalSurface Class](bcc299b6-ff1a-7f0c-c5da-8b040a326899.htm)   [See Also](#seeAlsoToggle) |

Creates a conical surface defined by a local reference frame and a half angle.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static ConicalSurface Create( 	Frame frameOfReference, 	double halfAngle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	frameOfReference As Frame, _ 	halfAngle As Double _ ) As ConicalSurface ``` |

 

| Visual C++ |
| --- |
| ``` public: static ConicalSurface^ Create( 	Frame^ frameOfReference,  	double halfAngle ) ``` |

#### Parameters

frameOfReference
:   Type:  [Autodesk.Revit.DB Frame](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.htm)    
     frameOfReference is an orthonormal frame that defines a local coordinate system for the cone.

    * Frame.Origin is a point on the cylinder's axis.
    * Frame.BasisZ points along the axis, while Frame.BasisX and Frame.BasisY are orthogonal to the axis.
    * The frame may be either left-handed or right-handed (see Frame.IsRightHanded). Note that the "handedness" of the frame does not, by itself, determine the surface's orientation.

halfAngle
:   Type:  System Double    
     Cone angle. Must be not 0, lesser than PI/2 and greater than -PI/2.

#### Return Value

The created ConicalSurface.

# Remarks

The parametric equation of the cone is S(u, v) = Frame.Origin + v\*[sin(halfAngle)(cos(u)\*Frame.BasisX + sin(u)\*Frame.BasisY) + cos(halfAngle)\*Frame.BasisZ] This implies the following facts:

* Frame.BasisX points from the axis point to the point on the cylinder with coordinates (0, 0).
* Frame.BasisY points in the direction of the partial derivative dS/du at (0, 0).
* Frame.BasisZ points in the direction of the partial derivative dS/dv at (0, 0).

Only the branch of the cone with v >= 0 should be used.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This Frame object may not be used as a local frame of reference. -or- The supplied value must be not 0, lesser than PI/2 and greater than -PI/2. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ConicalSurface Class](bcc299b6-ff1a-7f0c-c5da-8b040a326899.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc203b47-2781-23a6-6643-f74659869c5f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextStyleItalic Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Italic"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TextStyleItalic { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextStyleItalic As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TextStyleItalic { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc20a222-2bed-386e-062a-49748482079f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsDesiredNumberOfRisers Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Desired Number of Risers": The number of risers is calculated based on stairs height

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsDesiredNumberOfRisers { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsDesiredNumberOfRisers As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsDesiredNumberOfRisers { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc21537c-54b5-5834-f7a5-a40cc5897ea9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricSheetMajorDirectionWireType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Major Direction Wire Type": Major Direction Wire Type

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FabricSheetMajorDirectionWireType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricSheetMajorDirectionWireType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FabricSheetMajorDirectionWireType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc2416ab-309b-228e-81e8-8c897e29fdf7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotLockThisDimension Property

---



|  |
| --- |
| [BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)   [See Also](#seeAlsoToggle) |

Can't lock this Dimension because it breaks formulas

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotLockThisDimension { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotLockThisDimension As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotLockThisDimension { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc25c8d6-1123-27e1-528d-01820566fb60.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TextureAngle Property

---



|  |
| --- |
| [Wave Class](9c0cc26f-f6ae-708e-5612-d3d181058174.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Angle" from the "Wave" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string TextureAngle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TextureAngle As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ TextureAngle { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDoubleArray3d".

# See Also

[Wave Class](9c0cc26f-f6ae-708e-5612-d3d181058174.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__fc26f772-d49b-d023-0295-13cb3264b4d8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Utility Property

---



|  |
| --- |
| [Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)   [See Also](#seeAlsoToggle) |

Indicates if the connector is a utility connector.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool Utility { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Utility As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool Utility { 	bool get (); } ``` |

# See Also

[Connector Class](11e07082-b3f2-26a1-de79-16535f44716c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc2c72f5-1812-cb28-6665-03794e359f54.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCurveLoops Method

---



|  |
| --- |
| [RoofComponents Class](edd1717d-fe80-067c-d5f1-4d84c6a3573b.htm)   [See Also](#seeAlsoToggle) |

The CurveLoops of roof slabs.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public IList<CurveLoop> GetCurveLoops() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetCurveLoops As IList(Of CurveLoop) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<CurveLoop^>^ GetCurveLoops() ``` |

#### Return Value

The CurveLoops.

# See Also

[RoofComponents Class](edd1717d-fe80-067c-d5f1-4d84c6a3573b.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__fc2de49b-75ef-b407-cecf-3dd0199b775a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DegreeU Property

---



|  |
| --- |
| [NurbsSurfaceData Class](7d65dbde-8aac-7d7d-e811-a6c91a541de4.htm)   [See Also](#seeAlsoToggle) |

The degree of the spline in the u-direction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public int DegreeU { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property DegreeU As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int DegreeU { 	int get (); } ``` |

# See Also

[NurbsSurfaceData Class](7d65dbde-8aac-7d7d-e811-a6c91a541de4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc2efcc1-ad5f-1b7e-387e-2bec362b99dc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [ScheduleHeightsOnSheet Class](1af9b0b7-3949-6478-aea8-7e3d04bec24b.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
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

[ScheduleHeightsOnSheet Class](1af9b0b7-3949-6478-aea8-7e3d04bec24b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc32cc69-4691-e62c-61e3-57cf20dd9edf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Export Method (String, String, STLExportOptions)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Exports a view specified in the export options to the STL format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public bool Export( 	string folder, 	string name, 	STLExportOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Export ( _ 	folder As String, _ 	name As String, _ 	options As STLExportOptions _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Export( 	String^ folder,  	String^ name,  	STLExportOptions^ options ) ``` |

#### Parameters

folder
:   Type:  System String    
     Output folder into which the file will be exported. The folder must exist.

name
:   Type:  System String    
     Indicates the name of the STL file to export. If it doesn't end with ".stl", this extension will be added automatically. The name cannot contain any of the following characters: \/:\*?"<>|. Empty name is not acceptable.

options
:   Type:  [Autodesk.Revit.DB STLExportOptions](c8870dfe-9259-4981-4545-a6c0d0440552.htm)    
     Various options applicable to the STL format.

#### Return Value

True if successful, otherwise False.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | NullOrEmpty -or- Contains invalid characters. -or- The provided options are not valid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | This method may not be called during dynamic update. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Export is temporarily disabled. -or- Exporting is not allowed in the current application mode. |
| [Autodesk.Revit.Exceptions InvalidPathArgumentException](3f3c93a6-008b-f9de-40d4-5cd99bb32b34.htm) | The folder does not exist. |
| [Autodesk.Revit.Exceptions OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The ShapeExporter functionality is not available in the installed Revit. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Export Overload](2f535342-ee41-86f9-0022-92ba1f65112d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc35497c-304f-1a36-ded0-3eab1956441d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MepZoneAirLoop Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Air System"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MepZoneAirLoop { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MepZoneAirLoop As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MepZoneAirLoop { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc36ea5c-e146-394a-3bb4-e1f001623117.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Roughness Property

---



|  |
| --- |
| [MEPCurveType Class](97c98bd6-0966-5b0c-6f75-4c34f16adce1.htm)   [See Also](#seeAlsoToggle) |

The roughness of the MEP curve type. For PipeTypes, please use Segment::Roughness

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double Roughness { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Roughness As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Roughness { 	double get (); 	void set (double value); } ``` |

# See Also

[MEPCurveType Class](97c98bd6-0966-5b0c-6f75-4c34f16adce1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc38060a-ddfd-690d-6896-036df335cf40.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Insert Method

---



|  |
| --- |
| [ParameterSet Class](6e6e8667-ebe2-0c60-c180-9d8000cff598.htm)   [See Also](#seeAlsoToggle) |

Insert the specified parameter into the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual bool Insert( 	Parameter item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Insert ( _ 	item As Parameter _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Insert( 	Parameter^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB Parameter](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)    
     The parameter to be inserted into the set.

#### Return Value

Returns whether the parameter was inserted into the set.

# See Also

[ParameterSet Class](6e6e8667-ebe2-0c60-c180-9d8000cff598.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc3bc889-b274-3262-a126-849df2af9019.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### References Property

---



|  |
| --- |
| [Dimension Class](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm)   [See Also](#seeAlsoToggle) |

Returns an array of geometric references to which the dimension is attached.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ReferenceArray References { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property References As ReferenceArray 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ReferenceArray^ References { 	ReferenceArray^ get (); } ``` |

# See Also

[Dimension Class](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc3ffbfe-232e-767e-8b1d-8c2f01d93c64.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Behavior Property

---



|  |
| --- |
| [ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)   [See Also](#seeAlsoToggle) |

Flag indicating whether elements of this material behave isotropically or orthotropically.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public StructuralBehavior Behavior { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Behavior As StructuralBehavior 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property StructuralBehavior Behavior { 	StructuralBehavior get (); 	void set (StructuralBehavior value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ThermalAsset Class](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc405942-f9f1-36b7-b29f-eda46e433e1d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPipeSlopes Method

---



|  |
| --- |
| [PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.htm)   [See Also](#seeAlsoToggle) |

Get pipe slopes.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public IList<double> GetPipeSlopes() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPipeSlopes As IList(Of Double) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<double>^ GetPipeSlopes() ``` |

#### Return Value

Pipe slope values. Revit stores the slope value as a percentage (0-100).

# See Also

[PipeSettings Class](2de0109b-0d0d-a0fe-2adf-6edec8bc1a06.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__fc41074b-6416-0992-bd76-9c7418887e8c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AttachedGroupNoMirror Property

---



|  |
| --- |
| [BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)   [See Also](#seeAlsoToggle) |

Attached detail groups cannot be mirrored without also mirroring their parent group.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId AttachedGroupNoMirror { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AttachedGroupNoMirror As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ AttachedGroupNoMirror { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures GroupFailures Class](69df17ad-927e-db03-b55c-8efdb5397494.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc45f13e-33ba-47ca-3faf-558517899a90.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BRepBuilderState Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

This class defines an enumerative type used to specify the state of a BRepBuilder object.

This enumerative type corresponds to the possible states of a BRepBuilder object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public enum BRepBuilderState ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration BRepBuilderState ``` |

 

| Visual C++ |
| --- |
| ``` public enum class BRepBuilderState ``` |

# Members

| Member name | Description |
| --- | --- |
| InvalidState | BRepBuilder is in an invalid state. No further productive use is possible. |
| AcceptingData | BRepBuilder is accumulating data. New b-rep components such as edges or faces may be added. |
| Completed | Finish() successfully created a valid Geometry object. No new data may be added.The built object may be retrieved via GetResult(). |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc4e5245-d2e5-e31d-a6e3-177106e75e10.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetParameter Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Retrieves a parameter from the element given identifier.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public Parameter GetParameter( 	ForgeTypeId parameterTypeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetParameter ( _ 	parameterTypeId As ForgeTypeId _ ) As Parameter ``` |

 

| Visual C++ |
| --- |
| ``` public: Parameter^ GetParameter( 	ForgeTypeId^ parameterTypeId ) ``` |

#### Parameters

parameterTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     Identifier of the built-in parameter.

# Remarks

Parameters are a generic form of data storage within elements. The parameters are visible through the Autodesk Revit user interface in the Element Properties dialog. This method uses a built in parameter identifier to access the parameter. Autodesk Revit has a large number of built in parameters that are available via static properties.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | parameterTypeId does not identify a built-in parameter. See Parameter.IsBuiltInParameter(ForgeTypeId) and Parameter.GetParameterTypeId(BuiltInParameter). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was NULL |

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc50f245-7af9-68ae-2321-323e9366d65b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionCommonShearAreaStrongAxis Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Shear Area strong axis"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralSectionCommonShearAreaStrongAxis { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralSectionCommonShearAreaStrongAxis As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralSectionCommonShearAreaStrongAxis { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc5151f2-4f89-12f3-35d9-195925a3b86b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.PathOfTravelFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](75fbcded-440e-17b9-5ba5-e5f6b637123d.htm)   [See Also](#seeAlsoToggle) |

Failures about PathOfTravel.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public static class PathOfTravelFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class PathOfTravelFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PathOfTravelFailures abstract sealed ``` |

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.DB BuiltInFailures PathOfTravelFailures

# See Also

[BuiltInFailures PathOfTravelFailures Members](75fbcded-440e-17b9-5ba5-e5f6b637123d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc51effa-341f-6743-68bc-3c5eff0b2567.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AppendShape Method (IList(GeometryObject), DirectShapeTargetViewType)

---



|  |
| --- |
| [DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)   [See Also](#seeAlsoToggle) |

Appends the collection of GeometryObjects into the model or view specific shape representation stored in this DirectShapeType. Passing DirectShapeTargetViewType.Default as view type will cause the model shape to be updated.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public void AppendShape( 	IList<GeometryObject> pGeomArr, 	DirectShapeTargetViewType viewType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AppendShape ( _ 	pGeomArr As IList(Of GeometryObject), _ 	viewType As DirectShapeTargetViewType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AppendShape( 	IList<GeometryObject^>^ pGeomArr,  	DirectShapeTargetViewType viewType ) ``` |

#### Parameters

pGeomArr
:   Type:  System.Collections.Generic IList   [GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
     Shape expressed as a collection of GeometryObjects. For viewType = DirectShapeTargetViewType::Default, the supported types of GeometryObjects are: Solid, Mesh, GeometryInstance, Point, Curve and PolyLine. For viewType = DirectShapeTargetViewType::Plan, the supported types of GeometryObjects are: Point and Curve.

viewType
:   Type:  [Autodesk.Revit.DB DirectShapeTargetViewType](1c5cd94e-3804-54da-73af-505655b0948f.htm)    
     Passing DirectShapeTargetViewType.Default as view type will cause the default shape to be appended.

# Remarks

The existing shape will not be cleared by this function, and intersecting or overlapped geometry will not be joined with the appended geometry. It is up to the caller to ensure that the combination of geometry will have the correct appearance in Revit.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | At least one member of pGeomArr does not satisfy DirectShapeType validation criteria. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[DirectShapeType Class](9c7fdd8b-a899-7ba1-2a0f-ecc5e8fe85db.htm)

[AppendShape Overload](d2655b07-cda2-51c9-071c-c0db4843a37f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc539f83-b2dc-57c2-48f1-174588cc1535.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateDefaultEndTreatmentType Method

---



|  |
| --- |
| [EndTreatmentType Class](107f2dd4-7a92-e67e-0b79-a1c8c87dbf35.htm)   [See Also](#seeAlsoToggle) |

Creates a new EndTreatmentType object with a default name.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static ElementId CreateDefaultEndTreatmentType( 	Document ADoc ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateDefaultEndTreatmentType ( _ 	ADoc As Document _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: static ElementId^ CreateDefaultEndTreatmentType( 	Document^ ADoc ) ``` |

#### Parameters

ADoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

#### Return Value

The newly created type id.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[EndTreatmentType Class](107f2dd4-7a92-e67e-0b79-a1c8c87dbf35.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__fc565805-bda1-2cd3-6bf0-e0defa4edfc9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreTargetAndFallbackCompatible Method

---



|  |
| --- |
| [TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)   [See Also](#seeAlsoToggle) |

Checks whether this combination of fallback and target parameters can be used as a valid combination of inputs.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public bool AreTargetAndFallbackCompatible( 	TessellatedShapeBuilderTarget target, 	TessellatedShapeBuilderFallback fallback ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AreTargetAndFallbackCompatible ( _ 	target As TessellatedShapeBuilderTarget, _ 	fallback As TessellatedShapeBuilderFallback _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool AreTargetAndFallbackCompatible( 	TessellatedShapeBuilderTarget target,  	TessellatedShapeBuilderFallback fallback ) ``` |

#### Parameters

target
:   Type:  [Autodesk.Revit.DB TessellatedShapeBuilderTarget](c445e799-cb1d-a4cb-5333-719f5c19df18.htm)    
     What kind of geometrical objects should be built.

fallback
:   Type:  [Autodesk.Revit.DB TessellatedShapeBuilderFallback](ce755fa3-8727-2cd3-dbc3-c952bdc83a17.htm)    
     What should be done if a geometrical object described by 'target' parameter cannot be built using all data from all stored face sets.

#### Return Value

True if the combination of fallback and target are a valid combination, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[TessellatedShapeBuilder Class](a144b0e3-c997-eac1-5c00-51c56d9e66f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc592456-e99b-f662-cad1-adad16ac7d19.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BadReferenceBetweenOptions Property

---



|  |
| --- |
| [BuiltInFailures DesignOptionFailures Class](306b7ebc-5d5e-e53f-d5e4-9a5da4162068.htm)   [See Also](#seeAlsoToggle) |

An element may not reference an element in another Option of the same Option Set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId BadReferenceBetweenOptions { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BadReferenceBetweenOptions As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ BadReferenceBetweenOptions { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DesignOptionFailures Class](306b7ebc-5d5e-e53f-d5e4-9a5da4162068.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc5b51bd-2d83-a6ad-08e5-336f5dffa2c6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DivisionGeometry Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Division Geometry"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DivisionGeometry { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DivisionGeometry As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DivisionGeometry { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc5f1a12-b260-8ee2-1f5c-f06bf068d19c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Assign Method

---



|  |
| --- |
| [PointCloudOverrides Class](c39d51e3-cc31-ecae-fa41-d00c435cb700.htm)   [See Also](#seeAlsoToggle) |

Assigns values of the source overrides to this object.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Assign( 	PointCloudOverrides other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Assign ( _ 	other As PointCloudOverrides _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Assign( 	PointCloudOverrides^ other ) ``` |

#### Parameters

other
:   Type:  [Autodesk.Revit.DB.PointClouds PointCloudOverrides](c39d51e3-cc31-ecae-fa41-d00c435cb700.htm)    
     The source overrides.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PointCloudOverrides Class](c39d51e3-cc31-ecae-fa41-d00c435cb700.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__fc622f9f-c5df-7755-e519-71d663b2ae40.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [IFCImportOptions Class](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [IFCImportOptions](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
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

[IFCImportOptions Class](f98f40e2-dbab-4b4c-7fcb-36df9b35cad5.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__fc656f1a-7155-b96a-9482-0cbee29495b3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Erase Method

---



|  |
| --- |
| [PlanCircuitSet Class](8398c79d-1108-6846-cc0c-b7b2b5c1d026.htm)   [See Also](#seeAlsoToggle) |

Removes a specified object from the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual int Erase( 	PlanCircuit item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function Erase ( _ 	item As PlanCircuit _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual int Erase( 	PlanCircuit^ item ) ``` |

#### Parameters

item
:   Type:  [Autodesk.Revit.DB PlanCircuit](9fdb77cb-c579-1cbd-71de-01f06a18ea3a.htm)    
     The item to be erased.

#### Return Value

The number of items that were erased from the set.

# See Also

[PlanCircuitSet Class](8398c79d-1108-6846-cc0c-b7b2b5c1d026.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc6673a0-7994-6d89-c267-cad26cf6dcd0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReadPoints Method

---



|  |
| --- |
| [IPointSetIterator Interface](fc13e8dc-133b-bb47-a784-d42608a7d8e4.htm)   [See Also](#seeAlsoToggle) |

Implement this method to fill the provided buffer with points up to the number of maximum points for which the buffer was allocated.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` int ReadPoints( 	IntPtr buffer, 	int bufferSize ) ``` |

 

| Visual Basic |
| --- |
| ``` Function ReadPoints ( _ 	buffer As IntPtr, _ 	bufferSize As Integer _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` int ReadPoints( 	IntPtr buffer,  	int bufferSize ) ``` |

#### Parameters

buffer
:   Type:  [System IntPtr](http://msdn2.microsoft.com/en-us/library/5he14kz8)    
     Memory buffer into which the points should be written. The buffer was allocated by Revit and it is guaranteed to be valid for the duration of the call.

bufferSize
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The maximum number of CloudPoint objects that may be copied into the buffer.

#### Return Value

The actual number of CloudPoint objects placed in the buffer (can be less than the length of the buffer). If there are no more points available, return 0.

# See Also

[IPointSetIterator Interface](fc13e8dc-133b-bb47-a784-d42608a7d8e4.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__fc707d33-cbae-b032-1648-6d6f12eefdd8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Color2 Property

---



|  |
| --- |
| [PointCloudColorSettings Class](5f7af794-d52e-76a2-c38b-33eed5242484.htm)   [See Also](#seeAlsoToggle) |

Color 2

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public Color Color2 { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Color2 As Color 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Color^ Color2 { 	Color^ get (); } ``` |

# See Also

[PointCloudColorSettings Class](5f7af794-d52e-76a2-c38b-33eed5242484.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__fc70ad06-4e49-1689-f1a5-d14c03245fc1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsFontUnderline Property

---



|  |
| --- |
| [TableCellStyle Class](e9a5280b-4009-004f-57a4-af1f292f9619.htm)   [See Also](#seeAlsoToggle) |

Gets or sets whether the text font is set to Underline of this cell.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsFontUnderline { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsFontUnderline As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsFontUnderline { 	bool get (); 	void set (bool value); } ``` |

#### Field Value

true if the font is Underline; otherwise false.

# See Also

[TableCellStyle Class](e9a5280b-4009-004f-57a4-af1f292f9619.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc7879dd-dd2c-71f5-429b-b640d4ac20be.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMaterialAbbreviation Method

---



|  |
| --- |
| [FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)   [See Also](#seeAlsoToggle) |

Gets the abreviation of the material or the insulation or the double wall material.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public string GetMaterialAbbreviation( 	int materialId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMaterialAbbreviation ( _ 	materialId As Integer _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetMaterialAbbreviation( 	int materialId ) ``` |

#### Parameters

materialId
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The material identifier.

# See Also

[FabricationConfiguration Class](f7094105-2acf-03f1-7a7f-82dd24087a17.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc78f5a0-0570-d2bc-0ec4-984fde7870ad.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StartJoinCutback Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Start Join Cutback"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StartJoinCutback { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StartJoinCutback As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StartJoinCutback { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc7a9c1a-6a5d-3103-fbe0-87f7f4888c6e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Voltage Property

---



|  |
| --- |
| [AnalyticalPowerSourceData Class](844cf629-c023-47a8-55f1-b1d702780658.htm)   [See Also](#seeAlsoToggle) |

The voltage value of the analytical power source.

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

[AnalyticalPowerSourceData Class](844cf629-c023-47a8-55f1-b1d702780658.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fc8406bd-fa36-78cb-68e0-c9870198a6be.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotKeepReferenceOfJoinedElement Property

---



|  |
| --- |
| [BuiltInFailures JoinElementsFailures Class](2d7e4353-c24a-38d5-f3aa-3cbc2cb92698.htm)   [See Also](#seeAlsoToggle) |

Can't keep reference of joined element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotKeepReferenceOfJoinedElement { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotKeepReferenceOfJoinedElement As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotKeepReferenceOfJoinedElement { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures JoinElementsFailures Class](2d7e4353-c24a-38d5-f3aa-3cbc2cb92698.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc841a45-730b-c9df-27c6-8d1bacd9527b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Rebar Property

---



|  |
| --- |
| [NumberingSchemaTypes StructuralNumberingSchemas Class](f7e84519-92bf-bad3-df1f-bd05967eaeb0.htm)   [See Also](#seeAlsoToggle) |

Built-in schema used for numbering rebar elements

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static NumberingSchemaType Rebar { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Rebar As NumberingSchemaType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property NumberingSchemaType^ Rebar { 	NumberingSchemaType^ get (); } ``` |

# See Also

[NumberingSchemaTypes StructuralNumberingSchemas Class](f7e84519-92bf-bad3-df1f-bd05967eaeb0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc89169d-afb1-55e4-c8c0-98fab0f097ef.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlternateUnitsSuffix Property

---



|  |
| --- |
| [DimensionType Class](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.htm)   [See Also](#seeAlsoToggle) |

The suffix text for the alternate units value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public string AlternateUnitsSuffix { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property AlternateUnitsSuffix As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ AlternateUnitsSuffix { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[DimensionType Class](a6f6655d-3383-a0ea-670d-0bbe6d2bb964.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc89aa1f-96f7-b941-8723-087d2f038d3b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PathReinforcementClosedLoop Property

---



|  |
| --- |
| [BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)   [See Also](#seeAlsoToggle) |

Sketch contains a closed loop. Can't create Path Reinforcement.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId PathReinforcementClosedLoop { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PathReinforcementClosedLoop As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ PathReinforcementClosedLoop { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures SketchFailures Class](bd932d45-e417-9d4a-eb34-7974cc4f40ea.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc8efada-122c-e709-9b60-cd748a4f5fef.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ForwardIterator Method

---



|  |
| --- |
| [FamilyTypeSet Class](c38b1482-db14-7c2b-8efc-68a20bf35a24.htm)   [See Also](#seeAlsoToggle) |

Retrieve a forward moving iterator to the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual FamilyTypeSetIterator ForwardIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ForwardIterator As FamilyTypeSetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual FamilyTypeSetIterator^ ForwardIterator() ``` |

#### Return Value

Returns a forward moving iterator to the set.

# See Also

[FamilyTypeSet Class](c38b1482-db14-7c2b-8efc-68a20bf35a24.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc93ac37-fbb3-ac92-b1c5-bca5fd5d26bb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricationPartWidthIn Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Main Primary Width"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FabricationPartWidthIn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FabricationPartWidthIn As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FabricationPartWidthIn { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc94f2f8-ac92-9974-09f0-aaff0bfc499c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Angle Property

---



|  |
| --- |
| [DuctFittingAndAccessoryConnectorData Class](ffb25c4f-cd7a-bd51-8f78-3107a0955fc9.htm)   [See Also](#seeAlsoToggle) |

the angle of the fitting, Units:(rad).

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public double Angle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Angle As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Angle { 	double get (); } ``` |

# See Also

[DuctFittingAndAccessoryConnectorData Class](ffb25c4f-cd7a-bd51-8f78-3107a0955fc9.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__fc9601c1-64a5-dde1-e06e-c5481b360cc9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RebarHooksDontMatchShape Property

---



|  |
| --- |
| [BuiltInFailures RebarFailures Class](2d5565b1-8ddd-7e13-0eb1-8537eb342225.htm)   [See Also](#seeAlsoToggle) |

The Rebar's hooks do not match its Rebar Shape.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RebarHooksDontMatchShape { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RebarHooksDontMatchShape As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RebarHooksDontMatchShape { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarFailures Class](2d5565b1-8ddd-7e13-0eb1-8537eb342225.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc966bf7-766a-f6ec-2afe-4d1c19876e65.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalysisDisplayStyleDiagramFenceType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Defines fence visualization types for diagram settings of analysis display style.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public enum AnalysisDisplayStyleDiagramFenceType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration AnalysisDisplayStyleDiagramFenceType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class AnalysisDisplayStyleDiagramFenceType ``` |

# Members

| Member name | Description |
| --- | --- |
| ShowAll | Show fence for each point |
| ShowNone | Don't show fence |
| ShowPredefined | Show fence only for points that have flag ValueAtPointFlags::DisplayFence |

# See Also

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__fc97d569-248e-ffc8-67b3-08dd1498756d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Size Property

---



|  |
| --- |
| [WireConduitTypeSet Class](08d0cc98-554e-7f81-cb7c-f827d925de7d.htm)   [See Also](#seeAlsoToggle) |

Returns the number of conduit types that are in the set.

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

[WireConduitTypeSet Class](08d0cc98-554e-7f81-cb7c-f827d925de7d.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fc98381d-7925-9133-7567-3427ba5bbbf3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEmpty Property

---



|  |
| --- |
| [SymbolicCurveArray Class](a8ca9e0e-9838-96e4-5e6b-d5ffc11ea968.htm)   [See Also](#seeAlsoToggle) |

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

[SymbolicCurveArray Class](a8ca9e0e-9838-96e4-5e6b-d5ffc11ea968.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fc995172-e9d1-10a0-9c95-29f5a7ead0a2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FabricLocation Property

---



|  |
| --- |
| [FabricArea Class](b8e6a637-e069-500d-b7d3-3500e1728681.htm)   [See Also](#seeAlsoToggle) |

The Fabric location in the host.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public FabricLocation FabricLocation { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FabricLocation As FabricLocation 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property FabricLocation FabricLocation { 	FabricLocation get (); 	void set (FabricLocation value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | When setting this property: None of the following disciplines is enabled: Structural. |

# See Also

[FabricArea Class](b8e6a637-e069-500d-b7d3-3500e1728681.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__fc9b191e-cbd9-844c-0289-b58ccc19ac8b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VertexStreamPositionNormal Class

---



|  |
| --- |
| [Members](cc8066a8-cbcb-1a40-265d-a0207a130375.htm)   [See Also](#seeAlsoToggle) |

A stream that can be used to write vertices of type  [VertexPositionNormal](a40efda7-6e2f-a455-f65e-02b10b0bc1b4.htm)  into a buffer (see  [VertexBuffer](329e5617-ce46-a993-1131-85c64f0842f2.htm)  ).

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public class VertexStreamPositionNormal : VertexStream ``` |

 

| Visual Basic |
| --- |
| ``` Public Class VertexStreamPositionNormal _ 	Inherits VertexStream ``` |

 

| Visual C++ |
| --- |
| ``` public ref class VertexStreamPositionNormal : public VertexStream ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB.DirectContext3D VertexStream](a7a2d911-e3e4-84a7-a0c2-6aa5a28ae2ed.htm)    
  Autodesk.Revit.DB.DirectContext3D VertexStreamPositionNormal

# See Also

[VertexStreamPositionNormal Members](cc8066a8-cbcb-1a40-265d-a0207a130375.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__fca55ec0-cdcc-739f-edfe-08457134d214.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MacroLevel Property

---



|  |
| --- |
| [MacroManager Class](49eb4b8a-ae13-95e7-fef4-11347bbb67d3.htm)   [See Also](#seeAlsoToggle) |

The Macro level.

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPIMacros  (in RevitAPIMacros.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public MacroLevel MacroLevel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property MacroLevel As MacroLevel 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property MacroLevel MacroLevel { 	MacroLevel get (); } ``` |

# See Also

[MacroManager Class](49eb4b8a-ae13-95e7-fef4-11347bbb67d3.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)

<!-- Start of Syntax__fcaa12b3-c6d7-b7fa-99ab-fb8b90f311df.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateNotEndsWithRule Method (ElementId, String)

---



|  |
| --- |
| [ParameterFilterRuleFactory Class](317755a4-24ba-9f36-7639-f6fb2aa5a1a7.htm)   [See Also](#seeAlsoToggle) |

Creates a filter rule that determines whether strings from the document do not end with a certain string value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public static FilterRule CreateNotEndsWithRule( 	ElementId parameter, 	string value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateNotEndsWithRule ( _ 	parameter As ElementId, _ 	value As String _ ) As FilterRule ``` |

 

| Visual C++ |
| --- |
| ``` public: static FilterRule^ CreateNotEndsWithRule( 	ElementId^ parameter,  	String^ value ) ``` |

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

[CreateNotEndsWithRule Overload](bf313835-139c-f9b2-457b-640a0e115813.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcadb398-7b67-9259-a1a2-c6afd831dc14.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetLayoutAsMaximumSpacing Method

---



|  |
| --- |
| [RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)   [See Also](#seeAlsoToggle) |

Sets the Layout Rule property of rebar set to MaximumSpacing

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public void SetLayoutAsMaximumSpacing( 	double spacing, 	double arrayLength, 	bool barsOnNormalSide, 	bool includeFirstBar, 	bool includeLastBar ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetLayoutAsMaximumSpacing ( _ 	spacing As Double, _ 	arrayLength As Double, _ 	barsOnNormalSide As Boolean, _ 	includeFirstBar As Boolean, _ 	includeLastBar As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetLayoutAsMaximumSpacing( 	double spacing,  	double arrayLength,  	bool barsOnNormalSide,  	bool includeFirstBar,  	bool includeLastBar ) ``` |

#### Parameters

spacing
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The maximum spacing between rebar in rebar set

arrayLength
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The distribution length of rebar set

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

When changing the layout rule to MaximumSpacing, you must also simultaneously set Spacing, SetLength, BarsOnNormalSide, IncludeFirstBar, and IncludeLastBar properties.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The spacing isn't bigger than 0.0. -or- the set length arrayLength isn't acceptable. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions InapplicableDataException](dc1a6d15-8923-a1fe-722a-4e976634a519.htm) | This RebarShapeDrivenAccessor is an instance of a spiral or multiplanar shape. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RebarShapeDrivenAccessor doesn't contain a valid rebar reference. |

# See Also

[RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__fcadf274-66b3-21df-aaba-00ea79c70dcb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateParts Method (Document, ICollection(LinkElementId))

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Creates a new set of parts out of the original elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static void CreateParts( 	Document document, 	ICollection<LinkElementId> hostOrLinkElementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub CreateParts ( _ 	document As Document, _ 	hostOrLinkElementIds As ICollection(Of LinkElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void CreateParts( 	Document^ document,  	ICollection<LinkElementId^>^ hostOrLinkElementIds ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the elements.

hostOrLinkElementIds
:   Type:  System.Collections.Generic ICollection   [LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)    
     The elements that parts will be created from.

# Remarks

Parts will be added to the model after regeneration. To get the ids of the parts created by this method use PartUtils.GetAssociatedParts() with the contents of hostOrLinkElementIds.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | One or more element ids was not permitted for creating parts. HostOrLinkElements should be of a valid category and the ids should be valid and should not already be divided into parts. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[CreateParts Overload](7d85355b-ef4a-6c00-a2fe-01e6f5a7c4cb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcb075d8-7c62-197e-2054-ef609df490d0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Absorptance Property

---



|  |
| --- |
| [ThermalProperties Class](bfab51b3-ecd9-a082-9604-bf916248ca63.htm)   [See Also](#seeAlsoToggle) |

Value of absorptance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public double Absorptance { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Absorptance As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Absorptance { 	double get (); 	void set (double value); } ``` |

# See Also

[ThermalProperties Class](bfab51b3-ecd9-a082-9604-bf916248ca63.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcb2e002-473e-2b05-78cc-c469918461c2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumberOfLines Property

---



|  |
| --- |
| [LayoutRuleFixedNumber Class](5a2f6d39-0919-d5be-d146-bb985a4ab851.htm)   [See Also](#seeAlsoToggle) |

Get or set the number of the beams in a beam system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int NumberOfLines { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property NumberOfLines As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int NumberOfLines { 	int get (); 	void set (int value); } ``` |

# Remarks

The number must be positive.

# See Also

[LayoutRuleFixedNumber Class](5a2f6d39-0919-d5be-d146-bb985a4ab851.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcb341bd-8b22-e940-d94e-56430e19fdfc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### XDirection Property

---



|  |
| --- |
| [Ellipse Class](b966b82f-0627-c94a-9f37-994d00bdff18.htm)   [See Also](#seeAlsoToggle) |

The X direction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public XYZ XDirection { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property XDirection As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ XDirection { 	XYZ^ get (); } ``` |

# See Also

[Ellipse Class](b966b82f-0627-c94a-9f37-994d00bdff18.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcb6a64c-b116-5a14-409c-5d9db1c220a8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApparentPowerDensity Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Apparent Power Density, in discipline Electrical.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ApparentPowerDensity { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ApparentPowerDensity As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ApparentPowerDensity { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcb723de-befe-864d-9d4a-3084aea596b1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateMultiPlaneFilter Method (IList(Plane))

---



|  |
| --- |
| [PointCloudFilterFactory Class](fcbc90c3-0a9d-7522-e483-cad73468d698.htm)   [See Also](#seeAlsoToggle) |

Creates a new point cloud filter based upon planar boundaries.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static PointCloudFilter CreateMultiPlaneFilter( 	IList<Plane> planes ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateMultiPlaneFilter ( _ 	planes As IList(Of Plane) _ ) As PointCloudFilter ``` |

 

| Visual C++ |
| --- |
| ``` public: static PointCloudFilter^ CreateMultiPlaneFilter( 	IList<Plane^>^ planes ) ``` |

#### Parameters

planes
:   Type:  System.Collections.Generic IList   [Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)    
     All planes used for filtering; positive direction of the normal should point inside the volume of interest. Only points on the "positive" side of all planes will pass the filter.

#### Return Value

Filter object; can be used to get representative set of cloud points passing through the filter.

# Remarks

The filter will check whether a point is located on the "positive" side of each plane, as indicated by the positive direction of the plane normal. Therefore, such filter implicitly defines a volume, which is the intersection of the positive half-spaces corresponding to all the planes. This volume does not have to be closed, but it will always be convex.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PointCloudFilterFactory Class](fcbc90c3-0a9d-7522-e483-cad73468d698.htm)

[CreateMultiPlaneFilter Overload](69cc8914-6168-abf1-1e37-d2bc48a5ba18.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__fcb91231-2665-54b9-11d6-7ebcb7f235e2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### XYZ Constructor (Double, Double, Double)

---



|  |
| --- |
| [XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)   [See Also](#seeAlsoToggle) |

Creates an XYZ with the supplied coordinates.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ( 	double x, 	double y, 	double z ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	x As Double, _ 	y As Double, _ 	z As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ( 	double x,  	double y,  	double z ) ``` |

#### Parameters

x
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The first coordinate.

y
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The second coordinate.

z
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The third coordinate.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when setting an infinite number to the X, Y or Z property. |

# See Also

[XYZ Class](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)

[XYZ Overload](a1182d61-3e70-3099-76b9-23be9c64613b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcba2c30-7e6d-9ab7-8378-f4c6d5de06bf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DWGImportOptions Class

---



|  |
| --- |
| [Members](73b7f0c5-a18a-0051-0be9-5f067415b718.htm)   [See Also](#seeAlsoToggle) |

The import options used by importing DWG or DXF format file.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class DWGImportOptions : BaseImportOptions ``` |

 

| Visual Basic |
| --- |
| ``` Public Class DWGImportOptions _ 	Inherits BaseImportOptions ``` |

 

| Visual C++ |
| --- |
| ``` public ref class DWGImportOptions : public BaseImportOptions ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB BaseImportOptions](75898e94-cff4-fb64-c613-9596599444c4.htm)    
  Autodesk.Revit.DB DWGImportOptions

# See Also

[DWGImportOptions Members](73b7f0c5-a18a-0051-0be9-5f067415b718.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcbad45f-69b5-d391-7265-68304704fc4a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionISlopedFlange Constructor (Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double, Double)

---



|  |
| --- |
| [StructuralSectionISlopedFlange Class](37262abc-7f1d-3cab-da96-6cf631c0217f.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of Structural Section I Sloped Flange shape with the associated set of parameters, used to attach to structural element.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public StructuralSectionISlopedFlange( 	double width, 	double height, 	double flangeThickness, 	double flangeThicknessLocation, 	double webThickness, 	double webFillet, 	double flangeFillet, 	double centroidHorizontal, 	double centroidVertical, 	double principalAxesAngle, 	double sectionArea, 	double perimeter, 	double nominalWeight, 	double momentOfInertiaStrongAxis, 	double momentOfInertiaWeakAxis, 	double elasticModulusStrongAxis, 	double elasticModulusWeakAxis, 	double plasticModulusStrongAxis, 	double plasticModulusWeakAxis, 	double torsionalMomentOfInertia, 	double torsionalModulus, 	double warpingConstant, 	double shearAreaStrongAxis, 	double shearAreaWeakAxis, 	double clearWebHeight, 	double webToeOfFillet, 	double boltSpacing, 	double boltDiameter, 	double slopedFlangeAngle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	width As Double, _ 	height As Double, _ 	flangeThickness As Double, _ 	flangeThicknessLocation As Double, _ 	webThickness As Double, _ 	webFillet As Double, _ 	flangeFillet As Double, _ 	centroidHorizontal As Double, _ 	centroidVertical As Double, _ 	principalAxesAngle As Double, _ 	sectionArea As Double, _ 	perimeter As Double, _ 	nominalWeight As Double, _ 	momentOfInertiaStrongAxis As Double, _ 	momentOfInertiaWeakAxis As Double, _ 	elasticModulusStrongAxis As Double, _ 	elasticModulusWeakAxis As Double, _ 	plasticModulusStrongAxis As Double, _ 	plasticModulusWeakAxis As Double, _ 	torsionalMomentOfInertia As Double, _ 	torsionalModulus As Double, _ 	warpingConstant As Double, _ 	shearAreaStrongAxis As Double, _ 	shearAreaWeakAxis As Double, _ 	clearWebHeight As Double, _ 	webToeOfFillet As Double, _ 	boltSpacing As Double, _ 	boltDiameter As Double, _ 	slopedFlangeAngle As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: StructuralSectionISlopedFlange( 	double width,  	double height,  	double flangeThickness,  	double flangeThicknessLocation,  	double webThickness,  	double webFillet,  	double flangeFillet,  	double centroidHorizontal,  	double centroidVertical,  	double principalAxesAngle,  	double sectionArea,  	double perimeter,  	double nominalWeight,  	double momentOfInertiaStrongAxis,  	double momentOfInertiaWeakAxis,  	double elasticModulusStrongAxis,  	double elasticModulusWeakAxis,  	double plasticModulusStrongAxis,  	double plasticModulusWeakAxis,  	double torsionalMomentOfInertia,  	double torsionalModulus,  	double warpingConstant,  	double shearAreaStrongAxis,  	double shearAreaWeakAxis,  	double clearWebHeight,  	double webToeOfFillet,  	double boltSpacing,  	double boltDiameter,  	double slopedFlangeAngle ) ``` |

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

webThickness
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Web Thickness.

webFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Web Fillet - fillet radius between web and flange.

flangeFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Flange Fillet - fillet radius at the flange end.

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

clearWebHeight
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Detailing depth between the web toes of the fillets, in.(mm)

webToeOfFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Detailing distance from outer face of flange to web toe of fillet, in. (mm)

boltSpacing
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Standard bolt spacing, in. (mm)

boltDiameter
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Maximum bolt hole diameter, in. (mm)

slopedFlangeAngle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Sloped flange angle. (rad)

# See Also

[StructuralSectionISlopedFlange Class](37262abc-7f1d-3cab-da96-6cf631c0217f.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__fcbc90c3-0a9d-7522-e483-cad73468d698.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointCloudFilterFactory Class

---



|  |
| --- |
| [Members](d8048af0-2244-0ef0-104d-23d07255583a.htm)   [See Also](#seeAlsoToggle) |

A factory class for creating point cloud filters.

**Namespace:**   [Autodesk.Revit.DB.PointClouds](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static class PointCloudFilterFactory ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class PointCloudFilterFactory ``` |

 

| Visual C++ |
| --- |
| ``` public ref class PointCloudFilterFactory abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.PointClouds PointCloudFilterFactory

# See Also

[PointCloudFilterFactory Members](d8048af0-2244-0ef0-104d-23d07255583a.htm)

[Autodesk.Revit.DB.PointClouds Namespace](5974062a-47d4-c7bb-16f2-d5dd193bd170.htm)

<!-- Start of Syntax__fcbe6f51-9a2e-10bc-36bb-7705f554bd14.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Evaluate Method

---



|  |
| --- |
| [FilterStringRuleEvaluator Class](ba8dad25-3f85-1fbb-a164-323c3750018c.htm)   [See Also](#seeAlsoToggle) |

Derived classes override this method to implement the test that determines whether the two given string values satisfy the desired condition or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool Evaluate( 	string lhs, 	string rhs, 	bool caseSensitive ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Evaluate ( _ 	lhs As String, _ 	rhs As String, _ 	caseSensitive As Boolean _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Evaluate( 	String^ lhs,  	String^ rhs,  	bool caseSensitive ) ``` |

#### Parameters

lhs
:   Type:  System String    
     A value from an element in the document.

rhs
:   Type:  System String    
     The user-supplied value against which values from the document are tested.

caseSensitive
:   Type:  System Boolean    
     If true, string comparisons are done case-sensitively.

#### Return Value

True if the given arguments satisfy the condition, otherwise false.

# Remarks

The arguments may be thought of as the left and right operands of a binary expression; for example, "a < b", "x >= 100", etc. The left operand comes from an element in the Revit document (e.g., the value of a parameter.) The right operand is supplied by the user when creating the filter that contains the rule that uses this evaluator.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FilterStringRuleEvaluator Class](ba8dad25-3f85-1fbb-a164-323c3750018c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcc40b7f-3740-f797-0fcb-a22bd2b98bcd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DuplicatePoints Property

---



|  |
| --- |
| [BuiltInFailures OverlapFailures Class](b5f85718-fcb7-9396-e706-6d04f0c25c34.htm)   [See Also](#seeAlsoToggle) |

There are identical points in the same place. Lines created from points may not work as expected.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DuplicatePoints { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DuplicatePoints As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DuplicatePoints { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures OverlapFailures Class](b5f85718-fcb7-9396-e706-6d04f0c25c34.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcc75682-bd99-a97d-5a4d-0f8eb9e92ab5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewSection Class

---



|  |
| --- |
| [Members](0d37c868-8b5e-3ebd-d037-15b3c993f0d6.htm)   [See Also](#seeAlsoToggle) |

ViewSection covers sections, details, elevations, and callouts, all in their reference and non-reference variations.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public class ViewSection : View ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ViewSection _ 	Inherits View ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ViewSection : public View ``` |

# Remarks

The creation functions for elevations can be found in the ElevationMarker class.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
  Autodesk.Revit.DB ViewSection

# See Also

[ViewSection Members](0d37c868-8b5e-3ebd-d037-15b3c993f0d6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcca4b4b-d2bb-b286-64ef-9345f1a39585.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BackgroundStyle Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Indicates the background style in rendering settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum BackgroundStyle ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration BackgroundStyle ``` |

 

| Visual C++ |
| --- |
| ``` public enum class BackgroundStyle ``` |

# Members

| Member name | Description |
| --- | --- |
| SkyNoClouds | Sky background without clouds. |
| SkyVeryFewClouds | Sky background with very few clouds. |
| SkyFewClouds | Sky background with few clouds. |
| SkyCloudy | Cloudy sky background. |
| SkyVeryCloudy | Very cloudy sky background. |
| Color | Color background. |
| Image | Image background. |
| Transparent | Transparent background |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fccbe64c-8621-f8cc-6b63-b61581a2775a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomTagBadViewType Property

---



|  |
| --- |
| [BuiltInFailures RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.htm)   [See Also](#seeAlsoToggle) |

[Room] Tags can only be placed in Floor Plan, Reflected Ceiling Plan and Section Views.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RoomTagBadViewType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoomTagBadViewType As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RoomTagBadViewType { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fccc2688-a00f-9e3a-26bf-f6d04a58c56c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReferenceWithContext Class

---



|  |
| --- |
| [Members](f0db2af3-143a-3835-3aa1-c94e3ae93f61.htm)   [See Also](#seeAlsoToggle) |

An object including a reference to a geometric object and related context, as instance transform etc.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class ReferenceWithContext : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ReferenceWithContext _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ReferenceWithContext : IDisposable ``` |

# Remarks

The ReferenceWithContext is used as the returned value from the method  [!:Autodesk::Revit::DB::Document::FindReferencesWithContextByDirection]  , ReferenceIntersector.Find(XYZ, XYZ), or ReferenceIntersector.FindNearest(XYZ, XYZ). It includes a reference intersecting a line extended in a certain direction from an origin point and the context of the geometric object, as the transform and proximity.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ReferenceWithContext

# See Also

[ReferenceWithContext Members](f0db2af3-143a-3835-3aa1-c94e3ae93f61.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fccd5d74-e57f-94b9-0be9-1eb7fe83ba72.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SteelElemCopeZAngle Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Plan rotation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId SteelElemCopeZAngle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SteelElemCopeZAngle As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ SteelElemCopeZAngle { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcd19cf7-ce8e-3f33-7eb1-8ff64ac5e292.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEmpty Property

---



|  |
| --- |
| [VoltageTypeSet Class](3d6a14b7-0399-2ef9-8685-cbfaaf7739cf.htm)   [See Also](#seeAlsoToggle) |

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

[VoltageTypeSet Class](3d6a14b7-0399-2ef9-8685-cbfaaf7739cf.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fcd2ffc8-05bc-5d3c-f4e2-b62d5a3376ce.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetWidth Method

---



|  |
| --- |
| [CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)   [See Also](#seeAlsoToggle) |

The width implied by this compound structure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double GetWidth() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetWidth As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetWidth() ``` |

#### Return Value

The width of a host object with this compound structure.

# Remarks

If the structure is not vertically compound, then this is simply the sum of all layers' widths. If the structure is vertically compound, this is the width of the rectangular grid stored in the vertically compound structure. The presence of a layer with variable width has no effect on the value returned by this method. The value returned assumes that all layers have their specified width.

# See Also

[CompoundStructure Class](dc1a081e-8dab-565f-145d-a429098d353c.htm)

[GetWidth Overload](b131b5cc-f977-51bb-c0ab-be4a5a025b44.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcd30d2c-c23b-b964-562b-84dab4aa9e9a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LineSpringCoefficient Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Line Spring Coefficient, in discipline Structural.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId LineSpringCoefficient { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property LineSpringCoefficient As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ LineSpringCoefficient { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcd6e824-2bf6-17a8-839c-6d7d11283b9b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumWires Property

---



|  |
| --- |
| [DistributionSysType Class](03754b33-fd20-b19b-a718-6dc2eeccd76c.htm)   [See Also](#seeAlsoToggle) |

Get or set number of wires of distribution system.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int NumWires { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property NumWires As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int NumWires { 	int get (); 	void set (int value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | While assign a negative value to NumWires. |

# See Also

[DistributionSysType Class](03754b33-fd20-b19b-a718-6dc2eeccd76c.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fcd7e9f5-aac2-ddae-def2-f1e625306448.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportIFCCategoryTable Property

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Full path to the file that defines Revit category to IFC entity mappings for IFC export.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public string ExportIFCCategoryTable { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ExportIFCCategoryTable As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ ExportIFCCategoryTable { 	String^ get (); } ``` |

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__fcda8b78-e0a7-d99f-6e4e-e53e3e26fc8c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VectorAtPoint Class

---



|  |
| --- |
| [Members](d2038b2b-73d0-45d9-249a-541f256fa249.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Stores vectors at one domain point. Each vector corresponds to a "measurement" for which this vector was calculated.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public class VectorAtPoint : ValueAtPointBase ``` |

 

| Visual Basic |
| --- |
| ``` Public Class VectorAtPoint _ 	Inherits ValueAtPointBase ``` |

 

| Visual C++ |
| --- |
| ``` public ref class VectorAtPoint : public ValueAtPointBase ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Place analysis results in the form of vectors at each of a beam or column's analytical model curve
Transform transform = analyticalElem.GetTransform();
int index = spatialFieldManager.AddSpatialFieldPrimitive(curve, Transform.Identity);

IList<double> doubleList = new List<double>();
doubleList.Add(curve.GetEndParameter(0)); // vectors will be at each end of the analytical model curve
doubleList.Add(curve.GetEndParameter(1));
FieldDomainPointsByParameter pointsByParameter = new FieldDomainPointsByParameter(doubleList);

List<XYZ> xyzList = new List<XYZ>();
xyzList.Add(curve.ComputeDerivatives(0, true).BasisX.Normalize()); // vectors will be tangent to the curve at its ends
IList<VectorAtPoint> vectorList = new List<VectorAtPoint>();
vectorList.Add(new VectorAtPoint(xyzList));
xyzList.Clear();
xyzList.Add(curve.ComputeDerivatives(1, true).BasisX.Normalize().Negate());
vectorList.Add(new VectorAtPoint(xyzList));
FieldValues fieldValues = new FieldValues(vectorList);
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Place analysis results in the form of vectors at each of a beam or column's analytical model curve
Dim analyticalModel As Autodesk.Revit.DB.Structure.AnalyticalElement = Nothing
Dim relManager As Autodesk.Revit.DB.Structure.AnalyticalToPhysicalAssociationManager = Autodesk.Revit.DB.Structure.AnalyticalToPhysicalAssociationManager.GetAnalyticalToPhysicalAssociationManager(doc)

If (relManager Is Nothing) Then
   Exit Sub
End If

   Dim counterpartId As ElementId = relManager.GetAssociatedElementId(familyInstance.Id)
   If (counterpartId Is Nothing) Then
   Exit Sub
End If

analyticalModel = doc.GetElement(counterpartId)

Dim curve As Curve = analyticalModel.GetCurve()
Dim transform__1 As Transform = familyInstance.GetTransform()
   Dim index As Integer = spatialFieldManager.AddSpatialFieldPrimitive(curve, Transform.Identity)

   Dim doubleList As IList(Of Double) = New List(Of Double)()
   doubleList.Add(curve.GetEndParameter(0))
   ' vectors will be at each end of the analytical model curve
   doubleList.Add(curve.GetEndParameter(1))
   Dim pointsByParameter As New FieldDomainPointsByParameter(doubleList)

   Dim xyzList As New List(Of XYZ)()
   xyzList.Add(curve.ComputeDerivatives(0, True).BasisX.Normalize())
   ' vectors will be tangent to the curve at its ends
   Dim vectorList As IList(Of VectorAtPoint) = New List(Of VectorAtPoint)()
   vectorList.Add(New VectorAtPoint(xyzList))
   xyzList.Clear()
   xyzList.Add(curve.ComputeDerivatives(1, True).BasisX.Normalize().Negate())
   vectorList.Add(New VectorAtPoint(xyzList))
   Dim fieldValues As New FieldValues(vectorList)
```

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB ValueAtPointBase](67c49547-b5b9-59ad-8106-65d90886a381.htm)    
  Autodesk.Revit.DB.Analysis VectorAtPoint

# See Also

[VectorAtPoint Members](d2038b2b-73d0-45d9-249a-541f256fa249.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__fcdb6568-9715-4292-e903-c73c0b54dd67.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FilterNumericLess Class

---



|  |
| --- |
| [Members](0172ed7a-5348-a9b4-5f19-b1dc5e0667fd.htm)   [See Also](#seeAlsoToggle) |

Tests whether numeric values from the document are less than a certain value

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class FilterNumericLess : FilterNumericRuleEvaluator ``` |

 

| Visual Basic |
| --- |
| ``` Public Class FilterNumericLess _ 	Inherits FilterNumericRuleEvaluator ``` |

 

| Visual C++ |
| --- |
| ``` public ref class FilterNumericLess : public FilterNumericRuleEvaluator ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB FilterNumericRuleEvaluator](1f1a96bb-5f00-1a24-8c03-6984c88672b9.htm)    
  Autodesk.Revit.DB FilterNumericLess

# See Also

[FilterNumericLess Members](0172ed7a-5348-a9b4-5f19-b1dc5e0667fd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcde64b8-e345-25cd-29ad-0164438b16ef.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OvalDuctSizeSeparator Property

---



|  |
| --- |
| [DuctSettings Class](cd632c8e-a520-2efb-a417-9dfa5677d134.htm)   [See Also](#seeAlsoToggle) |

The oval duct size separator string.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public string OvalDuctSizeSeparator { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property OvalDuctSizeSeparator As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ OvalDuctSizeSeparator { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[DuctSettings Class](cd632c8e-a520-2efb-a417-9dfa5677d134.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__fce36964-2004-fb85-dfc3-84d49cd42ffa.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetExportLineweightTable Method

---



|  |
| --- |
| [DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.htm)   [See Also](#seeAlsoToggle) |

Sets the line weight table to use during export.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetExportLineweightTable( 	ExportLineweightTable lineweightTable ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetExportLineweightTable ( _ 	lineweightTable As ExportLineweightTable _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetExportLineweightTable( 	ExportLineweightTable^ lineweightTable ) ``` |

#### Parameters

lineweightTable
:   Type:  [Autodesk.Revit.DB ExportLineweightTable](5620708e-0c7c-ced6-9887-0237a9229800.htm)    
     The line weight table to be set.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DGNExportOptions Class](deca8dc2-439f-9567-9c60-70961b3f7c14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fce3a4b1-e029-5fd5-9f61-d389be460e03.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRodEndPosition Method

---



|  |
| --- |
| [FabricationRodInfo Class](b52fe314-2639-a697-cf97-b3e4824818f8.htm)   [See Also](#seeAlsoToggle) |

Gets the position of the rod end.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public XYZ GetRodEndPosition( 	int rodIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRodEndPosition ( _ 	rodIndex As Integer _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetRodEndPosition( 	int rodIndex ) ``` |

#### Parameters

rodIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the rod.

#### Return Value

The position of the rod end.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | the index rodIndex is should be in range of rod count. |

# See Also

[FabricationRodInfo Class](b52fe314-2639-a697-cf97-b3e4824818f8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fce3c08c-0ec4-4a73-6bbd-975f8b754012.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalysisDisplayColoredSurfaceSettings Class

---



|  |
| --- |
| [Members](3945b3ac-4ec9-8b7d-92e8-37b89995c5fe.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Contains colored surface settings for analysis display style element.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public class AnalysisDisplayColoredSurfaceSettings : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class AnalysisDisplayColoredSurfaceSettings _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class AnalysisDisplayColoredSurfaceSettings : IDisposable ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
AnalysisDisplayColoredSurfaceSettings coloredSurfaceSettings = new AnalysisDisplayColoredSurfaceSettings();
coloredSurfaceSettings.ShowGridLines = true;
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Dim coloredSurfaceSettings As New AnalysisDisplayColoredSurfaceSettings()
coloredSurfaceSettings.ShowGridLines = True
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Analysis AnalysisDisplayColoredSurfaceSettings

# See Also

[AnalysisDisplayColoredSurfaceSettings Members](3945b3ac-4ec9-8b7d-92e8-37b89995c5fe.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__fce4d0ee-9d95-f6ce-813a-e67cb28fe203.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPoint Method

---



|  |
| --- |
| [PolymeshTopology Class](fef5982c-3825-eed0-f792-1e0bff5509c2.htm)   [See Also](#seeAlsoToggle) |

Returns one point at the given index.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public XYZ GetPoint( 	int idx ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPoint ( _ 	idx As Integer _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetPoint( 	int idx ) ``` |

#### Parameters

idx
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     A zero-based index of a polymesh point

#### Return Value

XYZ coordinates of the point

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value is not a valid index of a point of the polymesh. A valid valure is not negative and is smaller than the number of points in the polymesh. |

# See Also

[PolymeshTopology Class](fef5982c-3825-eed0-f792-1e0bff5509c2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fce58e1d-47c7-9afb-d701-ec73d97d0f2b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SolidCurveIntersectionOptions Class

---



|  |
| --- |
| [Members](ce054463-24ae-c557-85ad-447d5e5f5354.htm)   [See Also](#seeAlsoToggle) |

This class contains the options used to calculate the intersection between a solid and a curve.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class SolidCurveIntersectionOptions : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class SolidCurveIntersectionOptions _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class SolidCurveIntersectionOptions : IDisposable ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB SolidCurveIntersectionOptions

# See Also

[SolidCurveIntersectionOptions Members](ce054463-24ae-c557-85ad-447d5e5f5354.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fce9ad33-53db-47a2-b505-993eff7fd532.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LegendTextTypeId Property

---



|  |
| --- |
| [SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)   [See Also](#seeAlsoToggle) |

Stores element id of text associated with common (result-independent) part of legend in view.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public ElementId LegendTextTypeId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LegendTextTypeId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ LegendTextTypeId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__fceb8867-2917-4259-4d83-b0408626934b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BritishThermalUnitsPerPound Property

---



|  |
| --- |
| [UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)   [See Also](#seeAlsoToggle) |

British thermal units per pound.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId BritishThermalUnitsPerPound { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property BritishThermalUnitsPerPound As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ BritishThermalUnitsPerPound { 	ForgeTypeId^ get (); } ``` |

# See Also

[UnitTypeId Class](bc1b6454-f10a-66dc-9268-1dccbc403f78.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcef8b4f-7eb1-f7c8-d0ff-25cd28f1f812.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Abbreviation Property

---



|  |
| --- |
| [FabricationService Class](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)   [See Also](#seeAlsoToggle) |

The short name of service.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public string Abbreviation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Abbreviation As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Abbreviation { 	String^ get (); } ``` |

# See Also

[FabricationService Class](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcf33ea0-0f2b-1e8a-746e-fdbb315e0f7f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsHvacloadRoofCoolingLoadParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Roof Cooling Load"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsHvacloadRoofCoolingLoadParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsHvacloadRoofCoolingLoadParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsHvacloadRoofCoolingLoadParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcf8e41d-f87d-13da-01e4-5e54442891bf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ElectricalCircuiting Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Electrical - Circuiting"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ElectricalCircuiting { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ElectricalCircuiting As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ElectricalCircuiting { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcfa13ce-0cbc-5dfc-752c-0464e76cd9f3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NotEnoughRoomForParallelPipes Property

---



|  |
| --- |
| [BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)   [See Also](#seeAlsoToggle) |

Due to changes in elevation, there is not enough room to generate all of the parallel pipes. As a result, some pipe segments have not been generated.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NotEnoughRoomForParallelPipes { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NotEnoughRoomForParallelPipes As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NotEnoughRoomForParallelPipes { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures ElectricalFailures Class](3797ca4f-563c-ec8c-ff8b-258789a73766.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcfc970f-2c31-8683-16b2-3b819416c29d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralCamber Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Camber Size"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StructuralCamber { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StructuralCamber As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StructuralCamber { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fcfeac53-570a-3238-9e50-41e7e1278f36.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CouplerCoupledEndtreatment Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"End Treatment 2"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CouplerCoupledEndtreatment { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CouplerCoupledEndtreatment As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CouplerCoupledEndtreatment { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd02b552-e0f0-84a1-229f-0c9b6b1cc4f8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LowerRange Property

---



|  |
| --- |
| [ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)   [See Also](#seeAlsoToggle) |

Lower part of progress bar range - always zero

**Namespace:**   [Autodesk.Revit.DB.Events](b86712d6-83b3-e044-8016-f9881ecd3800.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public int LowerRange { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property LowerRange As Integer 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property int LowerRange { 	int get (); } ``` |

# See Also

[ProgressChangedEventArgs Class](11e76066-82f3-21c7-6c1f-dfbbf0a1abd9.htm)

[Autodesk.Revit.DB.Events Namespace](b86712d6-83b3-e044-8016-f9881ecd3800.htm)

<!-- Start of Syntax__fd034d6f-e57d-7e95-4801-a43bc57e40d9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CurveParamSteelCantilever Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Steel Cantilever"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CurveParamSteelCantilever { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CurveParamSteelCantilever As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CurveParamSteelCantilever { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd03fb06-da32-0e66-2b01-8f3926788162.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ArePartsValidForMerge Method

---



|  |
| --- |
| [PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)   [See Also](#seeAlsoToggle) |

Identifies whether Part elements may be merged.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool ArePartsValidForMerge( 	Document document, 	ICollection<ElementId> partIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ArePartsValidForMerge ( _ 	document As Document, _ 	partIds As ICollection(Of ElementId) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ArePartsValidForMerge( 	Document^ document,  	ICollection<ElementId^>^ partIds ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

partIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Element ids of Parts.

#### Return Value

True if all element ids correspond to Part elements, none of the parts already has associated parts, the parts have contiguous geometry, all report the same materials, and all have the same creation and demolition phases.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PartUtils Class](a7384ccf-cd2b-9080-38d3-58b1253cd8e4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd047013-d138-f467-7bd5-6bdfb18099f0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ContinuousRailFilletCreationParallel Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Cannot create specified fillet at rail path corner because of the curves are already smoothed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId ContinuousRailFilletCreationParallel { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ContinuousRailFilletCreationParallel As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ ContinuousRailFilletCreationParallel { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd08a05b-e697-a519-60f8-e40a888e5bcb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LoadClassification Property

---



|  |
| --- |
| [AreaBasedLoadType Class](2800f280-409f-083d-5b57-127a19344de9.htm)   [See Also](#seeAlsoToggle) |

The load classification of area based load type.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public ElementId LoadClassification { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LoadClassification As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ LoadClassification { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The id is not a load classification id . |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[AreaBasedLoadType Class](2800f280-409f-083d-5b57-127a19344de9.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fd08c9bf-5574-ea44-fdd2-03247e8c4a19.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MultiReferenceAnnotationTagType Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Tag Family"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId MultiReferenceAnnotationTagType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MultiReferenceAnnotationTagType As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ MultiReferenceAnnotationTagType { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd0b9e4f-daa1-c1a4-2104-a2384c4e3fe0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TemporaryChangesOutOfDate Property

---



|  |
| --- |
| [BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)   [See Also](#seeAlsoToggle) |

You must Reload Latest before editing the element. Changes will be temporary, and will not be saved.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId TemporaryChangesOutOfDate { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TemporaryChangesOutOfDate As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ TemporaryChangesOutOfDate { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd0d677f-aad6-cb00-1b8f-9bd05a6f3dc6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MajorSegmentIndex Property

---



|  |
| --- |
| [RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)   [See Also](#seeAlsoToggle) |

Index of a segment that can be considered the most important. Revit attempts to preserve the orientation of this segment when a Rebar instance changes its RebarShape to one with a different number of segments.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public int MajorSegmentIndex { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MajorSegmentIndex As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int MajorSegmentIndex { 	int get (); 	void set (int value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: majorSegmentIndex is not between 0 and NumberOfSegments. |

# See Also

[RebarShapeDefinitionBySegments Class](7229fdba-1e8f-6cb7-e72e-0933e495ad62.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__fd0eab6d-0808-63ff-3cb0-a014f2adbbd7.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetBoldStatus Method (TextRange, Boolean)

---



|  |
| --- |
| [FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)   [See Also](#seeAlsoToggle) |

Sets the characters in a given text range to be bold or not bold.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetBoldStatus( 	TextRange textRange, 	bool isBold ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetBoldStatus ( _ 	textRange As TextRange, _ 	isBold As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetBoldStatus( 	TextRange^ textRange,  	bool isBold ) ``` |

#### Parameters

textRange
:   Type:  [Autodesk.Revit.DB TextRange](8a00baaf-8cb8-d9f0-e0a0-eaa5aa16e55e.htm)    
     The given text range.

isBold
:   Type:  System Boolean    
     The desired bold status of characters in the given text range. True to set bold, false to set not bold.

# Remarks

To make the numbers or letters in a list bold, apply the bold status to the carriage return character that ends the list paragraph.

The given text range should not be empty.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This text range is empty. -or- This start index of this text range is not within the text range identifying the entire text. -or- The end of this text range is not within the text range identifying the entire text. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)

[SetBoldStatus Overload](03b043e7-7056-6476-b223-d81c15b5ccc3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd1b0cff-3a22-870d-c22b-6275df02afdb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotCopyDetails Property

---



|  |
| --- |
| [BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)   [See Also](#seeAlsoToggle) |

Can't copy some or all of the detailing with the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotCopyDetails { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotCopyDetails As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotCopyDetails { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CopyPasteFailures Class](f9229467-317e-bcbf-4ff3-baf053cf1341.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd1bb4d1-9f6f-c330-b156-be71a86ec518.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [FabricationItemFile Class](ccf31061-ac40-f869-0b9e-834a9c146427.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
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

[FabricationItemFile Class](ccf31061-ac40-f869-0b9e-834a9c146427.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd1d56b8-6d89-b118-a7d5-d1e7f26a6bd9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RailingSystemFamilyTopRail Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Top Rail"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RailingSystemFamilyTopRail { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RailingSystemFamilyTopRail As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RailingSystemFamilyTopRail { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd2057f6-3bb7-6105-7553-43579020e53f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WoodGrowthPerlinEnable Property

---



|  |
| --- |
| [AdvancedWood Class](1e8c37ad-69ea-aabc-df91-eda9c7fe54ff.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Use perlin noise for ring growth" from the "AdvancedWood" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string WoodGrowthPerlinEnable { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property WoodGrowthPerlinEnable As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ WoodGrowthPerlinEnable { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyBoolean".

# See Also

[AdvancedWood Class](1e8c37ad-69ea-aabc-df91-eda9c7fe54ff.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__fd22e6c5-1482-2568-6a66-0187aafd756c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFailureDefinitionId Method

---



|  |
| --- |
| [FailureMessageAccessor Class](753477d8-b720-97a0-26f5-439d49de418c.htm)   [See Also](#seeAlsoToggle) |

Retrieves the Id of the FailureDefinition of the failure.

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

The Id of the FailureDefinition of the failure.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailureMessageAccessor has not been properly initialized. |

# See Also

[FailureMessageAccessor Class](753477d8-b720-97a0-26f5-439d49de418c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd255a5c-f079-e2bb-060b-4ca778f499fc.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FileExporting Event

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the FileExporting event to be notified when Revit is just about to export files of formats supported by the API.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<FileExportingEventArgs> FileExporting ``` |

 

| Visual Basic |
| --- |
| ``` Public Event FileExporting As EventHandler(Of FileExportingEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<FileExportingEventArgs^>^ FileExporting { 	void add (EventHandler<FileExportingEventArgs^>^ value); 	void remove (EventHandler<FileExportingEventArgs^>^ value); } ``` |

# Remarks

This event is raised when Revit is just about to export files of formats supported by the API.

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Event is cancellable. To cancel it, call the 'Cancel()' method in event's argument to True. Your application is responsible for providing feedback to the user about the reason for the cancellation.

The following API functions are not available for the current document during this event:

* All overloads of Autodesk.Revit.DB.Document.Export()
* Autodesk.Revit.Document.Print()
* [Print](1ea1e825-8044-7a27-d9b9-ca463443c3b9.htm)  and similar overloads.
* [SubmitPrint](0c9524b7-33b5-8c76-2843-c7024f03e4d7.htm)  and similar overloads.
* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  .
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

Another  [FileExported](54ac62e1-a215-ba22-c19e-6ad3c37ccc7c.htm)  event will be raised immediately after file exporting is finished.

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)

<!-- Start of Syntax__fd26704f-431c-0021-f57b-c67d4041a939.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GraphicDisplayOptionsBackground Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Background"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId GraphicDisplayOptionsBackground { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GraphicDisplayOptionsBackground As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ GraphicDisplayOptionsBackground { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd31e292-d129-3afc-6a7d-4e1a81ae2511.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewSolarstudyCurrentStudyTypeIndex Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Study type"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId ViewSolarstudyCurrentStudyTypeIndex { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property ViewSolarstudyCurrentStudyTypeIndex As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ ViewSolarstudyCurrentStudyTypeIndex { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd36a0ee-28b7-9521-c90d-3b27f8e0bec0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetExportFontInfo Method

---



|  |
| --- |
| [ExportFontTable Class](b3b4f237-f7f3-ced4-be3d-721f7ac05832.htm)   [See Also](#seeAlsoToggle) |

Gets a copy of the font info associated to the input font key.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ExportFontInfo GetExportFontInfo( 	ExportFontKey exportFontKey ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetExportFontInfo ( _ 	exportFontKey As ExportFontKey _ ) As ExportFontInfo ``` |

 

| Visual C++ |
| --- |
| ``` public: ExportFontInfo^ GetExportFontInfo( 	ExportFontKey^ exportFontKey ) ``` |

#### Parameters

exportFontKey
:   Type:  [Autodesk.Revit.DB ExportFontKey](bd33456d-7898-f32c-312e-b94af14c0007.htm)    
     The export font Key.

#### Return Value

Returns the fontInfo for this key.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | An entry with the given key is not present in the table. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportFontTable Class](b3b4f237-f7f3-ced4-be3d-721f7ac05832.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd3b4f99-3178-a3f9-c88d-2fd1a0a34fc5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AppendVertex Method

---



|  |
| --- |
| [Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)   [See Also](#seeAlsoToggle) |

Appends one vertex to the end of the wire.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void AppendVertex( 	XYZ vertexPoint ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AppendVertex ( _ 	vertexPoint As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AppendVertex( 	XYZ^ vertexPoint ) ``` |

#### Parameters

vertexPoint
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vertex to be appended.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The vertex point cannot be added to the wire because there is already a vertex at this position on the view plane (within tolerance). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The end point is already connected to an element, so a new endpoint vertex cannot be appended. |

# See Also

[Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fd41e15d-e934-e769-bc40-e468247d13d4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NoAutoRouteSolutionFoundWarning Property

---



|  |
| --- |
| [BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)   [See Also](#seeAlsoToggle) |

No auto-route solution was found.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NoAutoRouteSolutionFoundWarning { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NoAutoRouteSolutionFoundWarning As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NoAutoRouteSolutionFoundWarning { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures AutoRouteFailures Class](7cf86d0a-85aa-b09e-5378-36e02948233b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd422c8b-041f-7cd6-0362-877c13e73a58.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Add Method

---



|  |
| --- |
| [ExportLayerTable Class](e68ce1c7-a922-d1b7-53bb-f832a4bad273.htm)   [See Also](#seeAlsoToggle) |

Inserts a (key,info) pair into Export layer table.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void Add( 	ExportLayerKey exportLayerKey, 	ExportLayerInfo exportLayerInfo ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Add ( _ 	exportLayerKey As ExportLayerKey, _ 	exportLayerInfo As ExportLayerInfo _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Add( 	ExportLayerKey^ exportLayerKey,  	ExportLayerInfo^ exportLayerInfo ) ``` |

#### Parameters

exportLayerKey
:   Type:  [Autodesk.Revit.DB ExportLayerKey](64d77004-5c0c-9af2-cae4-39448bbaffe9.htm)    
     The export layer key to be added.

exportLayerInfo
:   Type:  [Autodesk.Revit.DB ExportLayerInfo](88a99694-968a-99f7-870a-f46737bd5927.htm)    
     The export layer info to be added.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The key already exists in the table. -or- The layer info does not contain the Category as a modifier type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExportLayerTable Class](e68ce1c7-a922-d1b7-53bb-f832a4bad273.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd4af0c2-583e-1c14-5525-2cf1cf7dd886.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSpecTypeId Method

---



|  |
| --- |
| [FamilySizeTableColumn Class](2442ffe1-07cf-3c1d-c4c1-033eb3bd681e.htm)   [See Also](#seeAlsoToggle) |

Gets the identifier of the spec describing values in the column.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public ForgeTypeId GetSpecTypeId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSpecTypeId As ForgeTypeId ``` |

 

| Visual C++ |
| --- |
| ``` public: ForgeTypeId^ GetSpecTypeId() ``` |

#### Return Value

Identifier of the spec.

# See Also

[FamilySizeTableColumn Class](2442ffe1-07cf-3c1d-c4c1-033eb3bd681e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd4dcd7b-fae9-aab3-4df4-766256b76aa2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpotElevationMissesReference Property

---



|  |
| --- |
| [BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)   [See Also](#seeAlsoToggle) |

Spot Dimension does not lie on its reference.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SpotElevationMissesReference { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpotElevationMissesReference As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SpotElevationMissesReference { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DimensionFailures Class](9a53db23-f09e-8bb7-5574-abeb470b9db7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd52beff-fc1d-ff30-3e60-454a1d863a44.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsMasking Property

---



|  |
| --- |
| [FilledRegionType Class](850ae173-379b-bfd6-7295-3950ccc229ca.htm)   [See Also](#seeAlsoToggle) |

If true then the FilledRegion will cover the lines and edges of objects behind it. If false then lines and edges will remain visible.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public bool IsMasking { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsMasking As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsMasking { 	bool get (); 	void set (bool value); } ``` |

# See Also

[FilledRegionType Class](850ae173-379b-bfd6-7295-3950ccc229ca.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd52ef85-8fb6-f740-d26b-649fe5d3513f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Clear Method

---



|  |
| --- |
| [ReferencePointArray Class](4780adea-9e68-b0b4-09c7-68f7752dd650.htm)   [See Also](#seeAlsoToggle) |

Removes every reference from the array, rendering it empty.

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

[ReferencePointArray Class](4780adea-9e68-b0b4-09c7-68f7752dd650.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd565083-b1f2-57f0-d476-495a7c4b19d3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DepthDimensionNotExisted Property

---



|  |
| --- |
| [BuiltInFailures RebarShapeFailures Class](7e0a8c39-c873-730e-6ffd-2fc6d6f71f3e.htm)   [See Also](#seeAlsoToggle) |

Multi-planar shape's depth dimension has been deleted. Please assign a new one to multi-planar depth.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DepthDimensionNotExisted { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DepthDimensionNotExisted As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DepthDimensionNotExisted { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RebarShapeFailures Class](7e0a8c39-c873-730e-6ffd-2fc6d6f71f3e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd56b6e1-77f4-de9f-5745-2eb5a4cfb0d3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyIsCorruptError Property

---



|  |
| --- |
| [BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)   [See Also](#seeAlsoToggle) |

Some families have become unusable. Reload the families, or delete them from the model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FamilyIsCorruptError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FamilyIsCorruptError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FamilyIsCorruptError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures FamilyFailures Class](4b2a4d9d-f77b-e466-e78a-df1ca741ec72.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd5c6d0f-3c77-6afd-a752-5ee7c7b8e1a1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PipingNetwork Property

---



|  |
| --- |
| [PipingSystem Class](6abbdfa2-69a5-eef1-2663-89a5faf91831.htm)   [See Also](#seeAlsoToggle) |

Pipes and fittings which are contained in this system.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public ElementSet PipingNetwork { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property PipingNetwork As ElementSet 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementSet^ PipingNetwork { 	ElementSet^ get (); } ``` |

# Remarks

The return value doesn't include mechanical equipment elements. The pipes and fittings are not returned in any particular order.

# See Also

[PipingSystem Class](6abbdfa2-69a5-eef1-2663-89a5faf91831.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__fd5fb218-eecf-c670-2907-59f5446a866c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreVertexPointsValid Method

---



|  |
| --- |
| [Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)   [See Also](#seeAlsoToggle) |

Checks if the given vertex points are valid for the wire.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static bool AreVertexPointsValid( 	IList<XYZ> vertexPoints, 	Connector startConnector, 	Connector endConnector ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function AreVertexPointsValid ( _ 	vertexPoints As IList(Of XYZ), _ 	startConnector As Connector, _ 	endConnector As Connector _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool AreVertexPointsValid( 	IList<XYZ^>^ vertexPoints,  	Connector^ startConnector,  	Connector^ endConnector ) ``` |

#### Parameters

vertexPoints
:   Type:  System.Collections.Generic IList   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The vertex points.

startConnector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The start connector of the wire.

endConnector
:   Type:  [Autodesk.Revit.DB Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)    
     The end connector of the wire.

#### Return Value

True if the given vertex points are valid, false otherwise.

# Remarks

X and Y values are compared of the vertices.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Wire Class](c2acf13b-0d8b-8415-9682-ae64eb5e5895.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fd61ed95-0d48-9e46-2dd7-4c8486a4ccce.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SlabEdgeType Property

---



|  |
| --- |
| [SlabEdge Class](8c1ba09e-d1d0-b1e4-bc2f-26ec4b6c5afa.htm)   [See Also](#seeAlsoToggle) |

Retrieves/set an object that represents the type of the SlabEdge.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public SlabEdgeType SlabEdgeType { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SlabEdgeType As SlabEdgeType 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property SlabEdgeType^ SlabEdgeType { 	SlabEdgeType^ get (); 	void set (SlabEdgeType^ value); } ``` |

# See Also

[SlabEdge Class](8c1ba09e-d1d0-b1e4-bc2f-26ec4b6c5afa.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd62adc1-005d-59b9-cfde-ab413cc7d0f9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DivisionRuleId Property

---



|  |
| --- |
| [PartMakerMethodToDivideVolumes Class](611ca5f7-3ffb-6f83-3aaf-df4533038ed0.htm)   [See Also](#seeAlsoToggle) |

Id of the 'DivisionRule' which is used to augment the cutting sketch.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId DivisionRuleId { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DivisionRuleId As ElementId 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ DivisionRuleId { 	ElementId^ get (); 	void set (ElementId^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: The provided element id cannot be assigned as a division rule to this PartMakerMethodToDivideVolumes. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[PartMakerMethodToDivideVolumes Class](611ca5f7-3ffb-6f83-3aaf-df4533038ed0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd65887a-3d13-3ff1-ec95-7c0379317c85.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Export Method (String, String, ICollection(ElementId), DXFExportOptions)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Exports a selection of views in DXF format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool Export( 	string folder, 	string name, 	ICollection<ElementId> views, 	DXFExportOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Export ( _ 	folder As String, _ 	name As String, _ 	views As ICollection(Of ElementId), _ 	options As DXFExportOptions _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Export( 	String^ folder,  	String^ name,  	ICollection<ElementId^>^ views,  	DXFExportOptions^ options ) ``` |

#### Parameters

folder
:   Type:  System String    
     Output folder, into which file(s) will be exported. The folder must exist.

name
:   Type:  System String    
     Either the name of a single file or a prefix for a set of files. If empty, automatic naming will be used.

views
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Selection of views to be exported. The set must contain at least one valid view.

options
:   Type:  [Autodesk.Revit.DB DXFExportOptions](00783eca-208f-cc58-d56f-b47814a6957a.htm)    
     Various options applicable to the DXF format. If    a null reference (  Nothing  in Visual Basic)  , all options will be set to their respective default values.

#### Return Value

True if successful, otherwise False.

# Remarks

All the views must be printable for the Export to succeed. It can be assured by checking the CanBePrinted property of each view.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | NullOrEmpty -or- Contains invalid characters. -or- non empty list of views must be provided. -or- some of the views are not printable (exportable). -or- Thrown when the options in DWGExportOptions is invalid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DirectoryNotFoundException](e6614e11-0fd4-df20-0d2d-02722b779128.htm) | Thrown when the directory does not exist. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Export is temporarily disabled. -or- Exporting is not allowed in the current application mode. |
| [Autodesk.Revit.Exceptions InvalidPathArgumentException](3f3c93a6-008b-f9de-40d4-5cd99bb32b34.htm) | The folder does not exist. |
| [Autodesk.Revit.Exceptions OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The DXF module is not available in the installed Revit. -or- The Graphics module is not available in the installed Revit. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Export Overload](2f535342-ee41-86f9-0022-92ba1f65112d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd65afe4-a7c9-f81b-4d02-fb09b5dabc3a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.NumberingFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](2ca2c698-f2d2-d4b1-56b0-05e519fdf350.htm)   [See Also](#seeAlsoToggle) |

Failures related to object numbering operations.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class NumberingFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class NumberingFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class NumberingFailures abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BuiltInFailures NumberingFailures

# See Also

[BuiltInFailures NumberingFailures Members](2ca2c698-f2d2-d4b1-56b0-05e519fdf350.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd68a412-172e-ed28-f4f1-554b51ff7188.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Suffix Property

---



|  |
| --- |
| [TableCellCombinedParameterData Class](f2303148-6e5e-d143-3725-3ac12c04ea86.htm)   [See Also](#seeAlsoToggle) |

The suffix for this parameter

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public string Suffix { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Suffix As String 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property String^ Suffix { 	String^ get (); 	void set (String^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non-optional argument was null |

# See Also

[TableCellCombinedParameterData Class](f2303148-6e5e-d143-3725-3ac12c04ea86.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd68b125-5b55-4abc-79e2-55691d45a7ad.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Shininess Property

---



|  |
| --- |
| [Material Class](2ec33007-7a2a-f86a-009b-d4c5d235a307.htm)   [See Also](#seeAlsoToggle) |

The shininess of the material.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int Shininess { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Shininess As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int Shininess { 	int get (); 	void set (int value); } ``` |

#### Field Value

The value ranges from 0 to 128.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: values for shininess must be between 0 and 128 |

# See Also

[Material Class](2ec33007-7a2a-f86a-009b-d4c5d235a307.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd6d2789-8499-512b-bae5-342b4a432570.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetAttribute Method (String, IList(Boolean))

---



|  |
| --- |
| [IFCAnyHandle Class](8b893943-70fa-94bf-90be-1523d516ecb3.htm)   [See Also](#seeAlsoToggle) |

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetAttribute( 	string name, 	IList<bool> values ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetAttribute ( _ 	name As String, _ 	values As IList(Of Boolean) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetAttribute( 	String^ name,  	IList<bool>^ values ) ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

values
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)

# See Also

[IFCAnyHandle Class](8b893943-70fa-94bf-90be-1523d516ecb3.htm)

[SetAttribute Overload](25c11a79-8e0f-5474-cbf5-6a3e7a2821d2.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)

<!-- Start of Syntax__fd6dd959-097d-38ce-2ce4-7295cb9f03bb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [DuctFittingAndAccessoryData Class](7db20bd9-6fba-bbd3-96ce-d08c0eec66c0.htm)   [See Also](#seeAlsoToggle) |

Specifies whether the .NET object represents a valid Revit entity.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
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

[DuctFittingAndAccessoryData Class](7db20bd9-6fba-bbd3-96ce-d08c0eec66c0.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__fd72877e-c266-4081-b03b-f68be0e0ef87.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLoadClassificationDemandCurrent Method

---



|  |
| --- |
| [PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)   [See Also](#seeAlsoToggle) |

Gets the Demand Current for given Load Classification

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public string GetLoadClassificationDemandCurrent( 	int nRow, 	int nCol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetLoadClassificationDemandCurrent ( _ 	nRow As Integer, _ 	nCol As Integer _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetLoadClassificationDemandCurrent( 	int nRow,  	int nCol ) ``` |

#### Parameters

nRow
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Row number of Load Summary Section

nCol
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Column number of Load Summary Section

#### Return Value

The Demand Current for the given Load Classification

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given row number nRow is invalid in Summary. -or- The given column number nCol is invalid in Summary. |

# See Also

[PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fd733756-fd68-4b47-0198-84ebdfe09c99.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlacementFailed Property

---



|  |
| --- |
| [BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)   [See Also](#seeAlsoToggle) |

Failed to place component.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId PlacementFailed { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PlacementFailed As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ PlacementFailed { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures EditingFailures Class](072adfe0-63f0-3613-f5a5-6c3cb4110f00.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd75e1f3-a3bd-24ce-ee16-7074354b88f4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReverseIterator Method

---



|  |
| --- |
| [GeomCombinationSet Class](854ed2aa-bd22-3352-383f-7a5230f154e5.htm)   [See Also](#seeAlsoToggle) |

Retrieve a backward moving iterator to the set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual GeomCombinationSetIterator ReverseIterator() ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Function ReverseIterator As GeomCombinationSetIterator ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual GeomCombinationSetIterator^ ReverseIterator() ``` |

#### Return Value

Returns a backward moving iterator to the set.

# See Also

[GeomCombinationSet Class](854ed2aa-bd22-3352-383f-7a5230f154e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd765b3c-368b-cf14-6bb0-b772f503370f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AssignElementsToSequence Method

---



|  |
| --- |
| [NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)   [See Also](#seeAlsoToggle) |

Assigns the input elements to a sequence identified by the given partition name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void AssignElementsToSequence( 	ISet<ElementId> elementIds, 	string partitionName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AssignElementsToSequence ( _ 	elementIds As ISet(Of ElementId), _ 	partitionName As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AssignElementsToSequence( 	ISet<ElementId^>^ elementIds,  	String^ partitionName ) ``` |

#### Parameters

elementIds
:   Type:  System.Collections.Generic ISet   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Ids of elements which are to be added to a sequence. All elements must be valid and belonging to this schema.

partitionName
:   Type:  System String    
     Name of the target sequence's partition

# Remarks

Elements will be added to the sequence by changing the value of their Partition parameter. The difference between this method and changing the parameter value explicitly is that the method here causes sequences to get assigned and renumbered automatically and immediately without needing to commit a transaction first.

A numbering sequence for the given partition does not need to exist yet; it will get created automatically by this method as needed.

The elements' numbers are likely to be affected by this operation, which is to be expected. The values of assigned numbers will depend on whether the given sequence already exists or not. In both cases the elements will get renumbered in order of their original creation, but the first value will be 1 if the sequence does not exist yet, respectively the next highest number if the sequence does exist already. The general matching policy is always applied causing matched elements to have the same number.

A special case is considered when the given elements are all the elements of one sequence and are being assigned to a sequence that does not exist yet. Such an operation is identical in effect to the  [MoveSequence](9ae38f60-e76f-5bd7-1d71-bd57cf06f641.htm)  method and all the elements will keep their numbers unchanged.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | the given partitionName cannot be used as a valid name of a numbering partition because it contains characters that are considered invalid, such as non-printable characters or those that cannot be used in a file's name. -or- Thrown when elementIds contains Ids that are either invalid or of elements not from this schema. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Either the schema or its document cannot be modified at present. -or- Thrown if there is an element that cannot have new value of the NUMBER\_PARTITION\_PARAM parameter assigned. It may be an indication that the element is not free to be edited at present. |

# See Also

[NumberingSchema Class](8f2b22da-5963-301f-44d8-10c68828c436.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd77a249-5245-9f3a-bfa9-b46a5f5f1418.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DividedSurfacePointNumber Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Point number"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId DividedSurfacePointNumber { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DividedSurfacePointNumber As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ DividedSurfacePointNumber { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd7c444c-e555-dd3f-9e0b-b9b9a9eeddc0.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Flexible Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Adaptive Component"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId Flexible { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property Flexible As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ Flexible { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd7c6249-7aff-3c0c-d8df-6473b2b13fc5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetBuildingConstruction Method

---



|  |
| --- |
| [MEPBuildingConstruction Class](3468e6dd-c676-cf39-b851-052b3e3a2f95.htm)   [See Also](#seeAlsoToggle) |

Sets the Building Construction of the Project Information.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetBuildingConstruction( 	ConstructionType constructionType, 	Construction buildingConstruction ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetBuildingConstruction ( _ 	constructionType As ConstructionType, _ 	buildingConstruction As Construction _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetBuildingConstruction( 	ConstructionType constructionType,  	Construction^ buildingConstruction ) ``` |

#### Parameters

constructionType
:   Type:  [Autodesk.Revit.DB.Analysis ConstructionType](5f6be035-3a2d-77ad-8402-4d6b87dec818.htm)    
     The Construction Type of Building Construction.

buildingConstruction
:   Type:  [Autodesk.Revit.DB Construction](b43d097e-b798-2aea-1008-ac79f71d3fc4.htm)    
     The Building Construction to be set.

# Remarks

This function is used to set the Building Construction of the Project Information.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | buildingConstruction is NULL. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Sets construction type to an invalid value. - or - Can not set construction type. |

# See Also

[MEPBuildingConstruction Class](3468e6dd-c676-cf39-b851-052b3e3a2f95.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)

<!-- Start of Syntax__fd876292-9f3a-7a90-dd41-019631baadca.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LightGroup Class

---



|  |
| --- |
| [Members](fa1c21d8-fde7-8d73-de4b-82a323e62bfc.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

This class represents a set of lights grouped together for easier management of various lighting scenarios

**Namespace:**   [Autodesk.Revit.DB.Lighting](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class LightGroup : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class LightGroup _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class LightGroup : IDisposable ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void AddRemoveLightInGroup(LightGroup groupOne, LightGroup groupTwo, FamilyInstance lightOne, FamilyInstance lightTwo)
{
    // Add two lights into groupOne.
    groupOne.AddLight(lightOne.Id);
    groupOne.AddLight(lightTwo.Id);

    // Move a light from groupOne to groupTwo
    groupTwo.AddLight(lightOne.Id);

    // Retrieve the added lights in the group
    ICollection<ElementId> existingLightIds = groupOne.GetLights();

    // remove the light
    groupOne.RemoveLight(lightTwo.Id);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub AddRemoveLightInGroup(groupOne As LightGroup, groupTwo As LightGroup, lightOne As FamilyInstance, lightTwo As FamilyInstance)
    ' Add two lights into groupOne.
    groupOne.AddLight(lightOne.Id)
    groupOne.AddLight(lightTwo.Id)

    ' Move a light from groupOne to groupTwo
    groupTwo.AddLight(lightOne.Id)

    ' Retrieve the added lights in the group
    Dim existingLightIds As ICollection(Of ElementId) = groupOne.GetLights()

    ' remove the light
    groupOne.RemoveLight(lightTwo.Id)
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB.Lighting LightGroup

# See Also

[LightGroup Members](fa1c21d8-fde7-8d73-de4b-82a323e62bfc.htm)

[Autodesk.Revit.DB.Lighting Namespace](a6a04f07-7fd2-0a4e-12e7-01842ee6daaf.htm)

<!-- Start of Syntax__fd8804c5-4c3b-e347-755d-5f6e8599b60c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MullionProfileContainsMoreThanOneOrOpenLoop Property

---



|  |
| --- |
| [BuiltInFailures CurtainGridFamilyFailures Class](35e77e14-b020-50ef-133f-1c029c28429e.htm)   [See Also](#seeAlsoToggle) |

The selected mullion profile either contains more than one profile loop or an open profile loop and cannot be used. Valid profiles can only have a single continuous closed profile loop.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId MullionProfileContainsMoreThanOneOrOpenLoop { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property MullionProfileContainsMoreThanOneOrOpenLoop As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ MullionProfileContainsMoreThanOneOrOpenLoop { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures CurtainGridFamilyFailures Class](35e77e14-b020-50ef-133f-1c029c28429e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd880d42-4601-cc6a-9f09-eae058318ebb.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VisibilityType Property

---



|  |
| --- |
| [FamilyElementVisibility Class](fae58e2d-817c-77f6-1747-58b0a4e01c7a.htm)   [See Also](#seeAlsoToggle) |

Indicates if the instance is Model or View specific.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyElementVisibilityType VisibilityType { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property VisibilityType As FamilyElementVisibilityType 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property FamilyElementVisibilityType VisibilityType { 	FamilyElementVisibilityType get (); } ``` |

# See Also

[FamilyElementVisibility Class](fae58e2d-817c-77f6-1747-58b0a4e01c7a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd892c31-0118-ddef-7396-2e9fc4b0cf27.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFirstProfileCurve Method

---



|  |
| --- |
| [RuledSurface Class](9a33fec9-bbcd-f035-3194-cf36122b6cc6.htm)   [See Also](#seeAlsoToggle) |

Returns a copy of the first profile curve if it is set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public Curve GetFirstProfileCurve() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFirstProfileCurve As Curve ``` |

 

| Visual C++ |
| --- |
| ``` public: Curve^ GetFirstProfileCurve() ``` |

#### Return Value

A copy of the first profile curve, if it exists. If a point was used to define the first profile, this function will return    a null reference (  Nothing  in Visual Basic)  .

# See Also

[RuledSurface Class](9a33fec9-bbcd-f035-3194-cf36122b6cc6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd8992de-402a-b620-503c-6aafaf0e6099.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CoolingLoadDividedByArea Property

---



|  |
| --- |
| [SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)   [See Also](#seeAlsoToggle) |

Cooling Load divided by Area, in discipline HVAC.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId CoolingLoadDividedByArea { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CoolingLoadDividedByArea As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ CoolingLoadDividedByArea { 	ForgeTypeId^ get (); } ``` |

# See Also

[SpecTypeId Class](35c5a3db-b4b3-daa0-ebdd-ae87d03cd5bb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd89c4f1-89f9-dadc-2d63-b14235a997c6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Dispose Method

---



|  |
| --- |
| [BuildingEnvelopeAnalyzerOptions Class](2a20b547-06bb-360c-c977-24466b56386a.htm)   [See Also](#seeAlsoToggle) |

Releases all resources used by the  [BuildingEnvelopeAnalyzerOptions](2a20b547-06bb-360c-c977-24466b56386a.htm)

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
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

[BuildingEnvelopeAnalyzerOptions Class](2a20b547-06bb-360c-c977-24466b56386a.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__fd8ae859-d418-c8a0-3e6b-86dd765206ad.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StoneBumpMap Property

---



|  |
| --- |
| [Stone Class](b7458faa-8242-d2b7-44a5-7df042a67ac3.htm)   [See Also](#seeAlsoToggle) |

The property labeled "Image" from the "Stone" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string StoneBumpMap { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StoneBumpMap As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ StoneBumpMap { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyReference" and will only contain a reference to a connected image.

# See Also

[Stone Class](b7458faa-8242-d2b7-44a5-7df042a67ac3.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__fd8afc78-4eb2-0a44-4714-d2247b58ce86.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NoRoofsSpacesBoundingWarn Property

---



|  |
| --- |
| [BuiltInFailures EnergyAnalysisFailures Class](8b9bfa39-1c9b-5cb0-14f1-0f49e2f8828a.htm)   [See Also](#seeAlsoToggle) |

The energy analysis model does not contain any roof surfaces! If there are roofs in your model, please verify that they are space bounding, and make sure that the space offsets are high enough to include the roofs.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId NoRoofsSpacesBoundingWarn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NoRoofsSpacesBoundingWarn As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ NoRoofsSpacesBoundingWarn { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures EnergyAnalysisFailures Class](8b9bfa39-1c9b-5cb0-14f1-0f49e2f8828a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd8b478b-38bd-5952-cc68-3eff5d0aff29.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DivisionContainsNoReferences Property

---



|  |
| --- |
| [BuiltInFailures DPartFailures Class](60230c02-eb7e-98f0-38c8-8da51b5109a8.htm)   [See Also](#seeAlsoToggle) |

The division contains no dividing references.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId DivisionContainsNoReferences { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property DivisionContainsNoReferences As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ DivisionContainsNoReferences { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures DPartFailures Class](60230c02-eb7e-98f0-38c8-8da51b5109a8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd8df892-efc9-0148-190d-6783bcac25ff.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumberSystemDisplayRule Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Display Rule"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId NumberSystemDisplayRule { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NumberSystemDisplayRule As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ NumberSystemDisplayRule { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd9030bb-cdeb-4862-404d-1efe46f56a61.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumberSystemOrientation Property

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
| ``` public static ForgeTypeId NumberSystemOrientation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property NumberSystemOrientation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ NumberSystemOrientation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd935c77-7633-9fda-3052-41540fbf5346.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetValueAsDoubles Method

---



|  |
| --- |
| [AssetPropertyDoubleArray4d Class](1fe933ae-e881-273a-fb8b-c4a7d9e66bc0.htm)   [See Also](#seeAlsoToggle) |

Gets the value property as doubles.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public IList<double> GetValueAsDoubles() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetValueAsDoubles As IList(Of Double) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<double>^ GetValueAsDoubles() ``` |

#### Return Value

The value as doubles.

# See Also

[AssetPropertyDoubleArray4d Class](1fe933ae-e881-273a-fb8b-c4a7d9e66bc0.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__fd95a0c2-367e-00cb-69c3-812819d35e1c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyInstanceIsNotCuttingHost Property

---



|  |
| --- |
| [BuiltInFailures InfillFailures Class](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.htm)   [See Also](#seeAlsoToggle) |

Instance is not cutting host.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId FamilyInstanceIsNotCuttingHost { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FamilyInstanceIsNotCuttingHost As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ FamilyInstanceIsNotCuttingHost { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures InfillFailures Class](13a26a89-322c-ef1a-f5f1-8cd481ee4ba0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd977456-eb4a-caf2-1d09-dedc8e1a4317.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetProfileCurveInWorldCoordinates Method

---



|  |
| --- |
| [RevolvedSurface Class](ce0b47e0-2b24-61f5-1434-87fe3ff70390.htm)   [See Also](#seeAlsoToggle) |

Returns a copy of the profile curve expressed in the world coordinate system.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017\_subscription\_update

# Syntax

| C# |
| --- |
| ``` public Curve GetProfileCurveInWorldCoordinates() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetProfileCurveInWorldCoordinates As Curve ``` |

 

| Visual C++ |
| --- |
| ``` public: Curve^ GetProfileCurveInWorldCoordinates() ``` |

#### Return Value

A copy of the profile curve in the world coordinate system.

# See Also

[RevolvedSurface Class](ce0b47e0-2b24-61f5-1434-87fe3ff70390.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd97ac9d-f94f-5fb0-2c33-415aaabf0de8.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotKeepTrussJoined Property

---



|  |
| --- |
| [BuiltInFailures JoinElementsFailures Class](2d7e4353-c24a-38d5-f3aa-3cbc2cb92698.htm)   [See Also](#seeAlsoToggle) |

Can't keep the highlighted [Element]s joined.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotKeepTrussJoined { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotKeepTrussJoined As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotKeepTrussJoined { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures JoinElementsFailures Class](2d7e4353-c24a-38d5-f3aa-3cbc2cb92698.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd9a9560-5984-91ee-f888-6550524215b9.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OrderedViewList Property

---



|  |
| --- |
| [IViewSheetSet Interface](4c3ef0b6-6d63-1e58-cff4-aabd4d8f75a2.htm)   [See Also](#seeAlsoToggle) |

Ordered views.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` IReadOnlyList<View> OrderedViewList { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Property OrderedViewList As IReadOnlyList(Of View) 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` property IReadOnlyList<View^>^ OrderedViewList { 	IReadOnlyList<View^>^ get (); 	void set (IReadOnlyList<View^>^ value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input ordered view list is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the set operation failed due to invalid view which cannot be printed. |

# See Also

[IViewSheetSet Interface](4c3ef0b6-6d63-1e58-cff4-aabd4d8f75a2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fd9e2a51-69ed-b225-10b7-21c85f6ad4dd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EndParameter Property

---



|  |
| --- |
| [PolylineSegments Class](d268283e-28de-c419-5e1f-7a870603506c.htm)   [See Also](#seeAlsoToggle) |

Parameter associated with the end point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public double EndParameter { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property EndParameter As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double EndParameter { 	double get (); } ``` |

# See Also

[PolylineSegments Class](d268283e-28de-c419-5e1f-7a870603506c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fda03f51-ce31-0cde-a41d-ec0e9885282d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [ColorFillLegend Class](81cbdc7c-9f7f-b454-5669-77ca0514eda7.htm)   [See Also](#seeAlsoToggle) |

Creates new instance of ColorFillLegend.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public static ColorFillLegend Create( 	Document document, 	ElementId viewId, 	ElementId catetoryId, 	XYZ origin ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	viewId As ElementId, _ 	catetoryId As ElementId, _ 	origin As XYZ _ ) As ColorFillLegend ``` |

 

| Visual C++ |
| --- |
| ``` public: static ColorFillLegend^ Create( 	Document^ document,  	ElementId^ viewId,  	ElementId^ catetoryId,  	XYZ^ origin ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

viewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the view to place legend in.

catetoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of category that color fill scheme belongs to.

origin
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The origin point of the legend, must be on the view plane.

# Remarks

Use  [SupportedColorFillCategoryIds](84197491-81de-0713-06bf-fa7073419485.htm)  to get list of supported categories.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- There's no valid color fill scheme applied for catetoryId in viewId. -or- The origin is not on the view plane. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[ColorFillLegend Class](81cbdc7c-9f7f-b454-5669-77ca0514eda7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fda07eca-edab-6dfb-9621-70410454de07.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RoomHeightNegative Property

---



|  |
| --- |
| [BuiltInFailures RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.htm)   [See Also](#seeAlsoToggle) |

[Room] must have a height greater than 0.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId RoomHeightNegative { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RoomHeightNegative As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ RoomHeightNegative { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures RoomFailures Class](7bece7b1-6ad8-1153-a15a-5b16feabe08b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fda0bd98-2636-3483-fb7e-de406b1bd252.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### BuiltInFailures.LevelFailures Class

---



|  |
| --- |
| [BuiltInFailures Class](eda15d4a-6b14-ee6b-0c44-6011077e6cfc.htm)   [Members](b7be803c-8375-0c1c-5bf7-39f67daf7df7.htm)   [See Also](#seeAlsoToggle) |

Failures about Level.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static class LevelFailures ``` |

 

| Visual Basic |
| --- |
| ``` Public NotInheritable Class LevelFailures ``` |

 

| Visual C++ |
| --- |
| ``` public ref class LevelFailures abstract sealed ``` |

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB BuiltInFailures LevelFailures

# See Also

[BuiltInFailures LevelFailures Members](b7be803c-8375-0c1c-5bf7-39f67daf7df7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdaa7f4a-e680-8d7e-3a9b-677b082432f5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CylindricalHelix Class

---



|  |
| --- |
| [Members](bc8abaf1-6ec7-47df-acbf-ffe80d2a15f2.htm)   [See Also](#seeAlsoToggle) |

A cylindrical helix.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class CylindricalHelix : Curve ``` |

 

| Visual Basic |
| --- |
| ``` Public Class CylindricalHelix _ 	Inherits Curve ``` |

 

| Visual C++ |
| --- |
| ``` public ref class CylindricalHelix : public Curve ``` |

# Remarks

The helix winds around a cylinder making constant angle with the axis of the cylinder. In this release, CylindricalHelix curves are used only in specific applications in stairs and railings, and should not be used or encountered when accessing curves of other Revit elements and geometry.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [Autodesk.Revit.DB APIObject](beb86ef5-39ad-3f0d-0cd9-0c929387a2bb.htm)    
  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
  Autodesk.Revit.DB CylindricalHelix

# See Also

[CylindricalHelix Members](bc8abaf1-6ec7-47df-acbf-ffe80d2a15f2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdac3194-8087-233a-0383-878f4716aea1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LightingSource Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Indicates the lighting scheme type in rendering settings.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum LightingSource ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration LightingSource ``` |

 

| Visual C++ |
| --- |
| ``` public enum class LightingSource ``` |

# Members

| Member name | Description |
| --- | --- |
| ExteriorSun | Exterior source of light, sun only. |
| ExteriorSunAndArtificial | Exterior source of light, sun and artificial light. |
| ExteriorArtificial | Exterior source of light, artificial light only. |
| InteriorSun | Interior source of light, sun only. |
| InteriorSunAndArtificial | Interior source of light, sun and artificial light. |
| InteriorArtificial | Interior source of light, artificial light only. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdad07eb-0668-cf65-2e47-1b8a30fbd3a1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpiralRunRadiusTooSmallFailure Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

The radius value for the run is too small.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId SpiralRunRadiusTooSmallFailure { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property SpiralRunRadiusTooSmallFailure As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ SpiralRunRadiusTooSmallFailure { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdae6998-e3b9-8cad-d7b0-7e786c94b71a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CantChangeParamMirror Property

---



|  |
| --- |
| [BuiltInFailures PointFailures Class](b1b1f464-16e5-fd74-9350-a0e4b0397b9b.htm)   [See Also](#seeAlsoToggle) |

Can't mirror Element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CantChangeParamMirror { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CantChangeParamMirror As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CantChangeParamMirror { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures PointFailures Class](b1b1f464-16e5-fd74-9350-a0e4b0397b9b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdb350a4-936d-d3fd-16ef-d11a8eb8ffc5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StructuralSectionIWideFlange Constructor

---



|  |
| --- |
| [StructuralSectionIWideFlange Class](8a3783c4-23a2-e433-1186-506fa70508ab.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of Structural Section I Wide Flange shape with the associated set of parameters, used to attach to structural element.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public StructuralSectionIWideFlange( 	double width, 	double height, 	double flangeThickness, 	double webThickness, 	double webFillet, 	double centroidHorizontal, 	double centroidVertical, 	double principalAxesAngle, 	double sectionArea, 	double perimeter, 	double nominalWeight, 	double momentOfInertiaStrongAxis, 	double momentOfInertiaWeakAxis, 	double elasticModulusStrongAxis, 	double elasticModulusWeakAxis, 	double plasticModulusStrongAxis, 	double plasticModulusWeakAxis, 	double torsionalMomentOfInertia, 	double torsionalModulus, 	double warpingConstant, 	double shearAreaStrongAxis, 	double shearAreaWeakAxis, 	double clearWebHeight, 	double flangeToeOfFillet, 	double webToeOfFillet, 	double boltSpacing, 	double boltSpacingTwoRows, 	double boltSpacingBetweenRows, 	double boltDiameter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	width As Double, _ 	height As Double, _ 	flangeThickness As Double, _ 	webThickness As Double, _ 	webFillet As Double, _ 	centroidHorizontal As Double, _ 	centroidVertical As Double, _ 	principalAxesAngle As Double, _ 	sectionArea As Double, _ 	perimeter As Double, _ 	nominalWeight As Double, _ 	momentOfInertiaStrongAxis As Double, _ 	momentOfInertiaWeakAxis As Double, _ 	elasticModulusStrongAxis As Double, _ 	elasticModulusWeakAxis As Double, _ 	plasticModulusStrongAxis As Double, _ 	plasticModulusWeakAxis As Double, _ 	torsionalMomentOfInertia As Double, _ 	torsionalModulus As Double, _ 	warpingConstant As Double, _ 	shearAreaStrongAxis As Double, _ 	shearAreaWeakAxis As Double, _ 	clearWebHeight As Double, _ 	flangeToeOfFillet As Double, _ 	webToeOfFillet As Double, _ 	boltSpacing As Double, _ 	boltSpacingTwoRows As Double, _ 	boltSpacingBetweenRows As Double, _ 	boltDiameter As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: StructuralSectionIWideFlange( 	double width,  	double height,  	double flangeThickness,  	double webThickness,  	double webFillet,  	double centroidHorizontal,  	double centroidVertical,  	double principalAxesAngle,  	double sectionArea,  	double perimeter,  	double nominalWeight,  	double momentOfInertiaStrongAxis,  	double momentOfInertiaWeakAxis,  	double elasticModulusStrongAxis,  	double elasticModulusWeakAxis,  	double plasticModulusStrongAxis,  	double plasticModulusWeakAxis,  	double torsionalMomentOfInertia,  	double torsionalModulus,  	double warpingConstant,  	double shearAreaStrongAxis,  	double shearAreaWeakAxis,  	double clearWebHeight,  	double flangeToeOfFillet,  	double webToeOfFillet,  	double boltSpacing,  	double boltSpacingTwoRows,  	double boltSpacingBetweenRows,  	double boltDiameter ) ``` |

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

webThickness
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Web Thickness.

webFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Web Fillet - fillet radius between web and flange.

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

clearWebHeight
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Detailing depth between the web toes of the fillets, in.(mm)

flangeToeOfFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Detailing distance from center of web to flange toe of fillet, in. (mm)

webToeOfFillet
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Detailing distance from outer face of flange to web toe of fillet, in. (mm)

boltSpacing
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Standard bolt spacing, in. (mm)

boltSpacingTwoRows
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Standard bolt spacing for two rows , in. (mm)

boltSpacingBetweenRows
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Standard bolt spacing between rows, in. (mm)

boltDiameter
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Maximum bolt hole diameter, in. (mm)

# See Also

[StructuralSectionIWideFlange Class](8a3783c4-23a2-e433-1186-506fa70508ab.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__fdb46c20-37e8-8483-730c-f169d0aca35c.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ShadowIntensity Property

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

The intesity of cast shadows - 0 = no shadows, 100 = black.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public int ShadowIntensity { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ShadowIntensity As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int ShadowIntensity { 	int get (); 	void set (int value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The value is invalid. The valid range is 0 through 100 |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: This view does not contain display-related properties. |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdb5ac56-200e-61aa-c2b9-4ffdd6ba9a12.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCircuitNamingSchemeSettings Method

---



|  |
| --- |
| [CircuitNamingSchemeSettings Class](60f49706-88f3-d2fb-0732-b1536c6e2e82.htm)   [See Also](#seeAlsoToggle) |

Gets the circuit naming scheme settings of the project.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static CircuitNamingSchemeSettings GetCircuitNamingSchemeSettings( 	Document cda ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetCircuitNamingSchemeSettings ( _ 	cda As Document _ ) As CircuitNamingSchemeSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: static CircuitNamingSchemeSettings^ GetCircuitNamingSchemeSettings( 	Document^ cda ) ``` |

#### Parameters

cda
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

#### Return Value

The circuit naming scheme settings of the project.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[CircuitNamingSchemeSettings Class](60f49706-88f3-d2fb-0732-b1536c6e2e82.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fdb603c0-d339-3693-1374-cefaa274aba2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotJoinElements Property

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
| ``` public static FailureDefinitionId CannotJoinElements { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotJoinElements As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotJoinElements { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures JoinElementsFailures Class](2d7e4353-c24a-38d5-f3aa-3cbc2cb92698.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdb61c29-089f-07a8-183a-84b0ecae4e55.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRelinquishedElements Method

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
| ``` public ICollection<ElementId> GetRelinquishedElements() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRelinquishedElements As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: ICollection<ElementId^>^ GetRelinquishedElements() ``` |

# See Also

[RelinquishedItems Class](50c43bae-6776-ed11-6489-ab4bea85d04f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdb6c343-77ee-166e-3017-4cfff5b5dd65.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CannotDrawStairsError Property

---



|  |
| --- |
| [BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)   [See Also](#seeAlsoToggle) |

Can't make stairs

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static FailureDefinitionId CannotDrawStairsError { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property CannotDrawStairsError As FailureDefinitionId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property FailureDefinitionId^ CannotDrawStairsError { 	FailureDefinitionId^ get (); } ``` |

# See Also

[BuiltInFailures StairRampFailures Class](4cd90111-4129-c210-f551-9ebdc20384ba.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdb8fda9-f9f5-ca7e-e59a-21252edbdf76.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsInUse Property

---



|  |
| --- |
| [VoltageType Class](6b462685-b825-f8f9-f218-035107f7aaf0.htm)   [See Also](#seeAlsoToggle) |

Indicates whether this voltage type is in service now, such as by other distribution system.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsInUse { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsInUse As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsInUse { 	bool get (); } ``` |

# See Also

[VoltageType Class](6b462685-b825-f8f9-f218-035107f7aaf0.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)

<!-- Start of Syntax__fdbf33c3-b84b-7fb1-9949-a7f25d8b3b09.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Reference Constructor

---



|  |
| --- |
| [Reference Class](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)   [See Also](#seeAlsoToggle) |

Creates a Reference with the supplied element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public Reference( 	Element element ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	element As Element _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: Reference( 	Element^ element ) ``` |

#### Parameters

element
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element to create a reference.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the parameter is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[Reference Class](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdbf4cd8-3066-2768-d94d-d8ebfb92009f.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBarGeometry Method

---



|  |
| --- |
| [RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.htm)   [See Also](#seeAlsoToggle) |

Returns the geometry for a bar at the specified index currently in the Rebar.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public IList<Curve> GetBarGeometry( 	int barIndex ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBarGeometry ( _ 	barIndex As Integer _ ) As IList(Of Curve) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Curve^>^ GetBarGeometry( 	int barIndex ) ``` |

#### Parameters

barIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the bar. Should be a number between 0 and GetNumberOfBars() - 1.

#### Return Value

Returns an array of curves that defines the bar at the specified index.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | barIndex is not in the range [ 0, GetNumberOfBars()-1 ]. |

# See Also

[RebarUpdateCurvesData Class](ff847aea-8397-8b79-b039-16a72e479c9f.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)

<!-- Start of Syntax__fdbfc683-adc4-b722-c466-a605216a0ee4.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanBeAssociatedWithGlobalParameters Method

---



|  |
| --- |
| [Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)   [See Also](#seeAlsoToggle) |

Tests whether this parameter can be associated with any global parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public bool CanBeAssociatedWithGlobalParameters() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanBeAssociatedWithGlobalParameters As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanBeAssociatedWithGlobalParameters() ``` |

#### Return Value

True if the given parameter can be associated (is parametrizable); False otherwise.

# Remarks

Only properties defined as parametrizable can be associated with global parameters. That excludes any read-only and formula-driven parameters, as well as those that have other explicit or implicit restrictions imposed by Revit.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | This parameter does not exist in the document anymore. |

# See Also

[Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdc49906-8a98-bcd2-d53d-061ffae7b97e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### StairsAttrEqResult Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Calculation Rules"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId StairsAttrEqResult { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property StairsAttrEqResult As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ StairsAttrEqResult { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdc4b575-9a16-417f-5ba3-1679865dca8a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyWorkPlaneBased Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Work Plane-Based"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId FamilyWorkPlaneBased { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property FamilyWorkPlaneBased As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ FamilyWorkPlaneBased { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdc63712-7bbe-086e-55f1-2ad3d8a85e32.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidObject Property

---



|  |
| --- |
| [TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)   [See Also](#seeAlsoToggle) |

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

[TableSectionData Class](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdc85ec8-320f-f377-6781-a352db5e031d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TranslationIn Property

---



|  |
| --- |
| [GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)   [See Also](#seeAlsoToggle) |

"Translation in"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId TranslationIn { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property TranslationIn As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ TranslationIn { 	ForgeTypeId^ get (); } ``` |

# See Also

[GroupTypeId Class](3339c438-5b0e-83e7-568a-6fe536e68d57.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdcb479b-a4f7-9ba8-b6f7-d8f7caba78fd.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### UseHeatingCredits Property

---



|  |
| --- |
| [EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)   [See Also](#seeAlsoToggle) |

If true, Revit will use heating credits in the final load sum calculations. If false, Revit will ignore heating credits in the final load sum calculations.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool UseHeatingCredits { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property UseHeatingCredits As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool UseHeatingCredits { 	bool get (); 	void set (bool value); } ``` |

# See Also

[EnergyDataSettings Class](63628109-daa0-e5b2-3dfd-153179e54816.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)

<!-- Start of Syntax__fdcdf691-e9f3-3cf0-1b84-23cafdc4eae3.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### HasOpenConnector Method

---



|  |
| --- |
| [PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.htm)   [See Also](#seeAlsoToggle) |

Checks if there is open piping connector for the given element - object of pipe curve, pipe fitting or pipe accessory.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool HasOpenConnector( 	Document document, 	ElementId elemId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function HasOpenConnector ( _ 	document As Document, _ 	elemId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool HasOpenConnector( 	Document^ document,  	ElementId^ elemId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

elemId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Element id to check.

#### Return Value

True if given element has open piping connector, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PlumbingUtils Class](958a3fa2-eb4b-2814-f674-42cac98f4910.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)

<!-- Start of Syntax__fdcf8a82-e71b-ec72-4cd0-12e5de45517b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetUnitTypeId Method

---



|  |
| --- |
| [Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)   [See Also](#seeAlsoToggle) |

Gets the identifier of the unit quantifying the parameter value.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)

# Syntax

| C# |
| --- |
| ``` public ForgeTypeId GetUnitTypeId() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetUnitTypeId As ForgeTypeId ``` |

 

| Visual C++ |
| --- |
| ``` public: ForgeTypeId^ GetUnitTypeId() ``` |

#### Return Value

Identifier of the unit of the parameter.

# Remarks

The property only applies to parameters of value types.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if this parameter is not of value type. |

# See Also

[Parameter Class](333ff41b-e6a7-d959-60bf-c3bfae495581.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdd22fcc-f58c-9a48-0287-868d1ea2537b.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CantileverHeight Property

---



|  |
| --- |
| [StructuralSectionConcreteT Class](884cbd30-20f7-5ec2-958d-0713f731cdde.htm)   [See Also](#seeAlsoToggle) |

Flange cantilever thickness.

**Namespace:**   [Autodesk.Revit.DB.Structure.StructuralSections](09862f38-63f6-a5f8-e560-ae775901bc92.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public double CantileverHeight { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property CantileverHeight As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double CantileverHeight { 	double get (); 	void set (double value); } ``` |

# See Also

[StructuralSectionConcreteT Class](884cbd30-20f7-5ec2-958d-0713f731cdde.htm)

[Autodesk.Revit.DB.Structure.StructuralSections Namespace](09862f38-63f6-a5f8-e560-ae775901bc92.htm)

<!-- Start of Syntax__fdd76258-57ff-1e74-8899-ee17bff133f6.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CutBackgroundPatternId Property

---



|  |
| --- |
| [OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)   [See Also](#seeAlsoToggle) |

The ElementId of the cut face background fill pattern override. A value of InvalidElementId means no override is set.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public ElementId CutBackgroundPatternId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property CutBackgroundPatternId As ElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property ElementId^ CutBackgroundPatternId { 	ElementId^ get (); } ``` |

# See Also

[OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdd9a2dd-4e5e-0776-cf4d-fb6af3a605cf.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsStartOffsetParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Start Middle Elevation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsStartOffsetParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsStartOffsetParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsStartOffsetParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fddb179b-83be-7bff-ed2f-2edf7803a724.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsCurveHorOffsetParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Horizontal Justification"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsCurveHorOffsetParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsCurveHorOffsetParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsCurveHorOffsetParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fddd1d58-98b7-099c-36a2-f16c4c6a3510.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSizeInShortInts Method

---



|  |
| --- |
| [IndexLine Class](3b22e25e-f934-3931-6f22-e451ffcc11b0.htm)   [See Also](#seeAlsoToggle) |

Gets the amount of storage that the primitive takes up in a buffer, measured in short integers.

**Namespace:**   [Autodesk.Revit.DB.DirectContext3D](f4ba10f0-55ea-5344-173b-688405391794.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static int GetSizeInShortInts() ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetSizeInShortInts As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: static int GetSizeInShortInts() ``` |

#### Return Value

The number of short integers occupied by the primitive.

# See Also

[IndexLine Class](3b22e25e-f934-3931-6f22-e451ffcc11b0.htm)

[Autodesk.Revit.DB.DirectContext3D Namespace](f4ba10f0-55ea-5344-173b-688405391794.htm)

<!-- Start of Syntax__fde24376-4e81-a336-7944-22c7ac31341a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsKeySchedule Property

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Indicates if the schedule is a key schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsKeySchedule { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsKeySchedule As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsKeySchedule { 	bool get (); } ``` |

# Remarks

A key schedule displays abstract "key" elements that can be used to populate parameters of ordinary model elements.

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fde81756-5518-4924-c14e-f9ef2bb3fa6e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsMonitoringLinkElement Method

---



|  |
| --- |
| [Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)   [See Also](#seeAlsoToggle) |

Indicate whether an element is monitoring any elements in any linked models.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool IsMonitoringLinkElement() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsMonitoringLinkElement As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsMonitoringLinkElement() ``` |

#### Return Value

True if this element is monitoring elements in a linked models. Otherwise, false will be returned.

# See Also

[Element Class](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fde8535e-501f-eee3-db5a-da383fa7067a.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AnalyticConstructionGbxmlTypeid Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Construction Type Id"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId AnalyticConstructionGbxmlTypeid { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property AnalyticConstructionGbxmlTypeid As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ AnalyticConstructionGbxmlTypeid { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdef8270-0f35-9bd3-1c7c-22bfeafca94e.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GradientNoiseHigh Property

---



|  |
| --- |
| [Gradient Class](2b517b49-c915-74a9-bb6f-2a233d6706be.htm)   [See Also](#seeAlsoToggle) |

The property labeled "High" from the "Gradient" schema.

**Namespace:**   [Autodesk.Revit.DB.Visual](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018.1

# Syntax

| C# |
| --- |
| ``` public static string GradientNoiseHigh { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property GradientNoiseHigh As String 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property String^ GradientNoiseHigh { 	String^ get (); } ``` |

# Remarks

This property is of type "AssetPropertyDouble" within the range of "0, 1".

# See Also

[Gradient Class](2b517b49-c915-74a9-bb6f-2a233d6706be.htm)

[Autodesk.Revit.DB.Visual Namespace](f5a10581-6ac2-be19-0e32-f87d05bc8b83.htm)

<!-- Start of Syntax__fdf4d267-dbf6-da09-88ea-b5b81fb47ed2.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RbsSegmentDescriptionParam Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Segment Description"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId RbsSegmentDescriptionParam { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property RbsSegmentDescriptionParam As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ RbsSegmentDescriptionParam { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdf7c733-319d-d355-3dc5-4c776b8ba9e5.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRenderingAsset Method

---



|  |
| --- |
| [AppearanceAssetElement Class](3493da3a-fea5-69cb-a18e-d0a954615bab.htm)   [See Also](#seeAlsoToggle) |

Gets the rendering asset for the appearance asset element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public Asset GetRenderingAsset() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRenderingAsset As Asset ``` |

 

| Visual C++ |
| --- |
| ``` public: Asset^ GetRenderingAsset() ``` |

#### Return Value

The rendering asset held by this appearance asset element.

# Remarks

The retrieved Asset may be empty if it is loaded from material library without any modification. In this case, you can use Application.GetAssets(AssetType.Appearance) to load all preset appearance assets, and retrieve the asset by its name.

# See Also

[AppearanceAssetElement Class](3493da3a-fea5-69cb-a18e-d0a954615bab.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdf8a2e6-62b0-a634-dc3f-d966c86f5483.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### STLExportOptions Constructor (STLExportResolution)

---



|  |
| --- |
| [STLExportOptions Class](c8870dfe-9259-4981-4545-a6c0d0440552.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of STLExportOptions with all predefined tessellation settings, depending on STL export resolution type. Note: in case of Custom resolution type, tessellation settings won't be predefined and will have default values.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` [ObsoleteAttribute("This constructor is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use another constructor with ExportResolution type of the input parameter instead.")] public STLExportOptions( 	STLExportResolution resolutionType ) ``` |

 

| Visual Basic |
| --- |
| ``` <ObsoleteAttribute("This constructor is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use another constructor with ExportResolution type of the input parameter instead.")> _ Public Sub New ( _ 	resolutionType As STLExportResolution _ ) ``` |

 

| Visual C++ |
| --- |
| ``` [ObsoleteAttribute(L"This constructor is deprecated in Revit 2023 and may be removed in a later version of Revit. We suggest you use another constructor with ExportResolution type of the input parameter instead.")] public: STLExportOptions( 	STLExportResolution resolutionType ) ``` |

#### Parameters

resolutionType
:   Type:  [Autodesk.Revit.DB STLExportResolution](75acb45f-3855-9a37-84ac-3f9b3e37fd23.htm)    
     The type of STL export resolution.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[STLExportOptions Class](c8870dfe-9259-4981-4545-a6c0d0440552.htm)

[STLExportOptions Overload](202b3151-da4b-fbad-08e1-d63e2fb80930.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fdf98941-eee4-d8af-e3f7-5b6c7ccc3c74.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetStatus Method

---



|  |
| --- |
| [Transaction Class](308ebf8d-d96d-4643-cd1d-34fffcea53fd.htm)   [See Also](#seeAlsoToggle) |

Returns the current status of the transaction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

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

The current status of the transaction.

# Remarks

If the status was set to TransactionStatus.Pending as the result of calling Commit or RollBack, the status will be changed later to either 'Committed' or 'RolledBack' after failure handling is finished. That status change will be made asynchronously.

# See Also

[Transaction Class](308ebf8d-d96d-4643-cd1d-34fffcea53fd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe0c22de-11c5-3436-e981-6703e45610c1.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PlacementLevelId Property

---



|  |
| --- |
| [NumberSystem Class](5c027e93-1dff-9a6e-8602-5b3a3da60ada.htm)   [See Also](#seeAlsoToggle) |

The id of the base level of stairs on which the NumberSystem is placed.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public LinkElementId PlacementLevelId { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property PlacementLevelId As LinkElementId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property LinkElementId^ PlacementLevelId { 	LinkElementId^ get (); } ``` |

# Remarks

In multistory stairs, a stairs element could be a stair group or individual stair, this level could be the base level of group member or stairs element.

# See Also

[NumberSystem Class](5c027e93-1dff-9a6e-8602-5b3a3da60ada.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe1ba644-b1dc-e037-08d5-339eac43bdda.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PointElevation Property

---



|  |
| --- |
| [ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)   [See Also](#seeAlsoToggle) |

"Elevation"

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ForgeTypeId PointElevation { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared ReadOnly Property PointElevation As ForgeTypeId 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: static property ForgeTypeId^ PointElevation { 	ForgeTypeId^ get (); } ``` |

# See Also

[ParameterTypeId Class](58412160-0861-d40d-f1ce-e1f320881d64.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)

<!-- Start of Syntax__fe1c02cc-e67f-2049-8bef-1df2f26fe37d.md -->

[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAttached Property

---



|  |
| --- |
| [Group Class](ca54af3c-52d8-0aed-cd22-440ec2584b89.htm)   [See Also](#seeAlsoToggle) |

Indicates wether or not this group is attached to a parent group.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2019.1

# Syntax

| C# |
| --- |
| ``` public bool IsAttached { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property IsAttached As Boolean 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsAttached { 	bool get (); } ``` |

# See Also

[Group Class](ca54af3c-52d8-0aed-cd22-440ec2584b89.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)