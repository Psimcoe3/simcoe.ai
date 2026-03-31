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