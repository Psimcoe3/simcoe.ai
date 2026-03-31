[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetIFCClassNameByCategory Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Obtains the IFC class name associated to a given category id for the current export.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static string GetIFCClassNameByCategory( 	ElementId catId, 	ExporterIFC exporterIFC ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetIFCClassNameByCategory ( _ 	catId As ElementId, _ 	exporterIFC As ExporterIFC _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ GetIFCClassNameByCategory( 	ElementId^ catId,  	ExporterIFC^ exporterIFC ) ``` |

#### Parameters

catId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The category id.

exporterIFC
:   Type:  [Autodesk.Revit.DB.IFC ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.htm)    
     The exporter.

#### Return Value

The IFC class name. This is an empty string if the element should not be exported because it is not found in the mapping file.

# Remarks

IFC class names are affected by the user's entries in the mapping file set for a given export operation.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)