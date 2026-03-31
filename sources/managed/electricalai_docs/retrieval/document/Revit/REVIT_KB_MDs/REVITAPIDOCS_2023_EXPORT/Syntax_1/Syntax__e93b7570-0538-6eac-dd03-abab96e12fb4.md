[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetLegacyStairsProperties Method

---



|  |
| --- |
| [ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)   [See Also](#seeAlsoToggle) |

Returns one or more properties for legacy (created in R2012 or before) Stairs.

**Namespace:**   [Autodesk.Revit.DB.IFC](b823fafb-1ba1-896b-4097-142c2817ce74.htm)    
  **Assembly:**   RevitAPIIFC  (in RevitAPIIFC.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static void GetLegacyStairsProperties( 	ExporterIFC exporterIFC, 	Element pElement, 	out int pNumRisers, 	out int pNumTreads, 	out double pRiserHeight, 	out double pTreadLength, 	out double pMinTreadLength, 	out double pNosingLength, 	out double pWaistThickness ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub GetLegacyStairsProperties ( _ 	exporterIFC As ExporterIFC, _ 	pElement As Element, _ 	<OutAttribute> ByRef pNumRisers As Integer, _ 	<OutAttribute> ByRef pNumTreads As Integer, _ 	<OutAttribute> ByRef pRiserHeight As Double, _ 	<OutAttribute> ByRef pTreadLength As Double, _ 	<OutAttribute> ByRef pMinTreadLength As Double, _ 	<OutAttribute> ByRef pNosingLength As Double, _ 	<OutAttribute> ByRef pWaistThickness As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void GetLegacyStairsProperties( 	ExporterIFC^ exporterIFC,  	Element^ pElement,  	[OutAttribute] int% pNumRisers,  	[OutAttribute] int% pNumTreads,  	[OutAttribute] double% pRiserHeight,  	[OutAttribute] double% pTreadLength,  	[OutAttribute] double% pMinTreadLength,  	[OutAttribute] double% pNosingLength,  	[OutAttribute] double% pWaistThickness ) ``` |

#### Parameters

exporterIFC
:   Type:  [Autodesk.Revit.DB.IFC ExporterIFC](c8697b81-e080-9202-14d3-ec883f951521.htm)    
     The exporter.

pElement
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     the legacy stair.

pNumRisers
:   Type:  System Int32   %    
     Number of Risers in the Stair.

pNumTreads
:   Type:  System Int32   %    
     Number of Treads in the Stair.

pRiserHeight
:   Type:  System Double   %    
     Riser Height of the risers in the Stair.

pTreadLength
:   Type:  System Double   %    
     Tread length of the treads in the Stair.

pMinTreadLength
:   Type:  System Double   %    
     Minimum Tread length of the treads in the Stair.

pNosingLength
:   Type:  System Double   %    
     Nosing length of the treads in the Stair.

pWaistThickness
:   Type:  System Double   %    
     Waist thickness of the flight of stair.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExporterIFCUtils Class](e0e78d67-739c-0cd6-9e3d-359e42758c93.htm)

[Autodesk.Revit.DB.IFC Namespace](b823fafb-1ba1-896b-4097-142c2817ce74.htm)