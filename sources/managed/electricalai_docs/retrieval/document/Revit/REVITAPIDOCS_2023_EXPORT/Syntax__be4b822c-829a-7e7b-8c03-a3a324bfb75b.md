[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewFamilyInstance Method (Reference, XYZ, XYZ, FamilySymbol)

---



|  |
| --- |
| [ItemFactoryBase Class](cba2c84a-22c0-e6e7-a99c-67656901853a.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Inserts a new instance of a family onto a face referenced by the input Reference instance, using a location, reference direction, and a type/symbol.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyInstance NewFamilyInstance( 	Reference reference, 	XYZ location, 	XYZ referenceDirection, 	FamilySymbol symbol ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewFamilyInstance ( _ 	reference As Reference, _ 	location As XYZ, _ 	referenceDirection As XYZ, _ 	symbol As FamilySymbol _ ) As FamilyInstance ``` |

 

| Visual C++ |
| --- |
| ``` public: FamilyInstance^ NewFamilyInstance( 	Reference^ reference,  	XYZ^ location,  	XYZ^ referenceDirection,  	FamilySymbol^ symbol ) ``` |

#### Parameters

reference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     A reference to a face.

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
void CreateNurseCallDomeOnWall(Autodesk.Revit.DB.Document document, Wall wall)
{
    FilteredElementCollector collector = new FilteredElementCollector(document);
    collector.OfClass(typeof(FamilySymbol)).OfCategory(BuiltInCategory.OST_NurseCallDevices);

    FamilySymbol symbol = collector.FirstElement() as FamilySymbol;

    // Get interior face of wall
    IList<Reference> sideFaces = HostObjectUtils.GetSideFaces(wall, ShellLayerType.Interior);
    Reference interiorFaceRef = sideFaces[0];

    XYZ location = new XYZ(4, 2, 8);
    XYZ refDir = new XYZ(0, 0, 1);

    FamilyInstance instance = document.Create.NewFamilyInstance(interiorFaceRef, location, refDir, symbol);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub CreateNurseCallDomeOnWall(document As Autodesk.Revit.DB.Document, wall As Wall)
    Dim collector As New FilteredElementCollector(document)
    collector.OfClass(GetType(FamilySymbol)).OfCategory(BuiltInCategory.OST_NurseCallDevices)

    Dim symbol As FamilySymbol = TryCast(collector.FirstElement(), FamilySymbol)

    ' Get interior face of wall
    Dim sideFaces As IList(Of Reference) = HostObjectUtils.GetSideFaces(wall, ShellLayerType.Interior)
    Dim interiorFaceRef As Reference = sideFaces(0)

    Dim location As New XYZ(4, 2, 8)
    Dim refDir As New XYZ(0, 0, 1)

    Dim instance As FamilyInstance = document.Create.NewFamilyInstance(interiorFaceRef, location, refDir, symbol)
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when a non-optional argument was null. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the function cannot get the face from the reference, or, when the Family cannot be placed as line-based on an input face reference, because its FamilyPlacementType is not WorkPlaneBased |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | Thrown when reference direction is parallel to face normal at insertion point. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when Revit is unable to place the family instance. |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if The symbol is not active. |

# See Also

[ItemFactoryBase Class](cba2c84a-22c0-e6e7-a99c-67656901853a.htm)

[NewFamilyInstance Overload](451ee414-cea0-e9bd-227b-c73bc93507dd.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)