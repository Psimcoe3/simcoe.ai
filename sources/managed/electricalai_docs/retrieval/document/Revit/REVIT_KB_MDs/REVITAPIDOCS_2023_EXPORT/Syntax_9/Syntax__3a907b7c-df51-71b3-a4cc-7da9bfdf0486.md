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