[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetMaterialIdForCurrentExportState Method

---



|  |
| --- |
| [ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)   [See Also](#seeAlsoToggle) |

This gets the material id that is associated with the element in the current export state.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ElementId GetMaterialIdForCurrentExportState() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetMaterialIdForCurrentExportState As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ GetMaterialIdForCurrentExportState() ``` |

#### Return Value

The material id.

# Remarks

Even though there could be several materials associated with the element (set during PushExportState()), unless the element has support for IfcMaterialLayerSet, IFC output will include only this one.

# See Also

[ExporterIFC Class](c8697b81-e080-9202-14d3-ec883f951521.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)