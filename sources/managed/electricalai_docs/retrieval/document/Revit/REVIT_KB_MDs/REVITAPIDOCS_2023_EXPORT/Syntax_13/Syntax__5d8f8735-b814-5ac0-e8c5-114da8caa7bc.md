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