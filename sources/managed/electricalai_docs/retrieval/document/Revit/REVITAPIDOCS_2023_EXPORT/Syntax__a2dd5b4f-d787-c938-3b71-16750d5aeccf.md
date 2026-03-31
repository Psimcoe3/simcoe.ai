[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateFaceGeometryInfo Method (Double)

---



|  |
| --- |
| [IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)   [See Also](#seeAlsoToggle) |

Creates a new container object which holds IfcFace handles processed from a Revit geometry object.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static IFCGeometryInfo CreateFaceGeometryInfo( 	double epsilon ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateFaceGeometryInfo ( _ 	epsilon As Double _ ) As IFCGeometryInfo ``` |

 

| Visual C++ |
| --- |
| ``` public: static IFCGeometryInfo^ CreateFaceGeometryInfo( 	double epsilon ) ``` |

#### Parameters

epsilon
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The epsilon value used to process surfaces.

#### Return Value

The new geometry info container.

# See Also

[IFCGeometryInfo Class](741c57df-a409-ea0d-8cb8-edc93c19b74d.htm)

[CreateFaceGeometryInfo Overload](208595c0-eacf-dffe-7514-3a545dd94991.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)