[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateCurveGeometryInfo Method (ExporterIFC, Transform, XYZ, Boolean)

---



|  |
| --- |
| [IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)   [See Also](#seeAlsoToggle) |

Creates a new container object which holds IfcCurve handles processed from a Revit geometry object.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static IFCGeometryInfo CreateCurveGeometryInfo( 	ExporterIFC ExporterIFC, 	Transform lcs, 	XYZ projectionDir, 	bool planViewOnly ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateCurveGeometryInfo ( _ 	ExporterIFC As ExporterIFC, _ 	lcs As Transform, _ 	projectionDir As XYZ, _ 	planViewOnly As Boolean _ ) As IFCGeometryInfo ``` |

 

| Visual C++ |
| --- |
| ``` public: static IFCGeometryInfo^ CreateCurveGeometryInfo( 	ExporterIFC^ ExporterIFC,  	Transform^ lcs,  	XYZ^ projectionDir,  	bool planViewOnly ) ``` |

#### Parameters

ExporterIFC
:   Type:  [Autodesk.Revit.DB.IFC ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.htm)    
     The exporter.

lcs
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     The local coordinate system that defines the plane in which the curve handles must lie.

projectionDir
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The normal vector to the input plane.

planViewOnly
:   Type:  System Boolean    
     True to match curves with plan view visibility only, false to match curves regardless of their plan view visibility.

#### Return Value

The new geometry info container.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)