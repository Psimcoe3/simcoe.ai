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