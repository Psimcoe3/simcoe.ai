[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CalculateExtrusionData Method (IFCExtrusionCalculatorOptions, GeometryObject)

---



|  |
| --- |
| [IFCExtrusionCalculatorUtils Class](926b73c9-932f-d429-e316-a905a9434fca.htm)   [See Also](#seeAlsoToggle) |

Calculates the extrusion data from a Revit geometry object.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static IList<IFCExtrusionData> CalculateExtrusionData( 	IFCExtrusionCalculatorOptions extrusionOptions, 	GeometryObject geometryObject ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CalculateExtrusionData ( _ 	extrusionOptions As IFCExtrusionCalculatorOptions, _ 	geometryObject As GeometryObject _ ) As IList(Of IFCExtrusionData) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<IFCExtrusionData^>^ CalculateExtrusionData( 	IFCExtrusionCalculatorOptions^ extrusionOptions,  	GeometryObject^ geometryObject ) ``` |

#### Parameters

extrusionOptions
:   Type:  [Autodesk.Revit.DB.IFC IFCExtrusionCalculatorOptions](3aa9bc3b-5ce0-e0ba-4211-9a08526c1c1b.htm)    
     The options for extrusion extraction.

geometryObject
:   Type:  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
     The geometry object.

#### Return Value

A collection of extrusion data calculated for the geometry. If the function fails to calculate one or more valid extrusions, this collection will be empty.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[IFCExtrusionCalculatorUtils Class](926b73c9-932f-d429-e316-a905a9434fca.htm)

[CalculateExtrusionData Overload](9982943c-d766-bc0e-428f-4dee262f35c4.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)