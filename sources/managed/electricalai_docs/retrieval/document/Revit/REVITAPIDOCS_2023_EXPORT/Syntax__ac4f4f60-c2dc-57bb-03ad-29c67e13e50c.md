[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateFaceGeometryInfo Method (ExporterIFC, Plane, XYZ, Double, Boolean)

---



|  |
| --- |
| [IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)   [See Also](#seeAlsoToggle) |

Creates a new container object which holds IfcFace handles processed from a Revit geometry object.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static IFCGeometryInfo CreateFaceGeometryInfo( 	ExporterIFC ExporterIFC, 	Plane Plane, 	XYZ ProjDir, 	double epsilon, 	bool createRepresentations ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateFaceGeometryInfo ( _ 	ExporterIFC As ExporterIFC, _ 	Plane As Plane, _ 	ProjDir As XYZ, _ 	epsilon As Double, _ 	createRepresentations As Boolean _ ) As IFCGeometryInfo ``` |

 

| Visual C++ |
| --- |
| ``` public: static IFCGeometryInfo^ CreateFaceGeometryInfo( 	ExporterIFC^ ExporterIFC,  	Plane^ Plane,  	XYZ^ ProjDir,  	double epsilon,  	bool createRepresentations ) ``` |

#### Parameters

ExporterIFC
:   Type:  [Autodesk.Revit.DB.IFC ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.htm)    
     The exporter.

Plane
:   Type:  [Autodesk.Revit.DB Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)    
     The plane in which the face handles must lie.

ProjDir
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The normal vector to the input plane.

epsilon
:   Type:  System Double    
     The epsilon value used to process surfaces.

createRepresentations
:   Type:  System Boolean    
     Indicates if this should also create geometry representation handles.

#### Return Value

The new geometry info container.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)

[CreateFaceGeometryInfo Overload](208595c0-eacf-dffe-7514-3a545dd94991.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)