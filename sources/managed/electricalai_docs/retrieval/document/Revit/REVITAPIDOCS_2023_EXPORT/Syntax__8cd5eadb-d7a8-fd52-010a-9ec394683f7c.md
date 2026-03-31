[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsWallCompletelyClipped Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Determines if the input wall is completely removed by interaction with other elements within the given range.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool IsWallCompletelyClipped( 	Wall pVWall, 	ExporterIFC exporterIFC, 	IFCRange range ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsWallCompletelyClipped ( _ 	pVWall As Wall, _ 	exporterIFC As ExporterIFC, _ 	range As IFCRange _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsWallCompletelyClipped( 	Wall^ pVWall,  	ExporterIFC^ exporterIFC,  	IFCRange^ range ) ``` |

#### Parameters

pVWall
:   Type:  [Autodesk.Revit.DB Wall](b5891733-c602-12df-beab-da414b58d608.htm)    
     The wall.

exporterIFC
:   Type:  [Autodesk.Revit.DB.IFC ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.htm)    
     The exporter.

range
:   Type:  [Autodesk.Revit.DB.IFC IFCRange](dd18e556-a0d8-7bbb-1522-518d8a82736f.htm)    
     The range. This consists of two double values representing the height in Z at the start and the end of the range. If the values are identical the entire wall is used.

#### Return Value

True if the wall should be ignored within the given range.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)