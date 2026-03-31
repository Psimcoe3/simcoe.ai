[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PushTransform Method

---



|  |
| --- |
| [ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)   [See Also](#seeAlsoToggle) |

Sets the internal transform of the exporter to process the geometry and properties of the input element.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void PushTransform( 	Transform trf ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub PushTransform ( _ 	trf As Transform _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void PushTransform( 	Transform^ trf ) ``` |

#### Parameters

trf
:   Type:  [Autodesk.Revit.DB Transform](58dd01c8-b3fc-7142-e4f3-c524079a282d.htm)    
     The transform.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)