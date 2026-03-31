[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetGridCoordinates Method

---



|  |
| --- |
| [FieldDomainPointsByUV Class](aa1eb974-d283-f16e-8431-a7e02fe4e076.htm)   [See Also](#seeAlsoToggle) |

Set u and v coordinates that specify a grid on the surface. The display of the grid is controlled by AnalysisDisplayColoredSurfaceSettings::getShowGridLines(). If AnalysisDisplayColoredSurfaceSettings::getShowGridLines() returns true and both sets are empty then a grid will be displayed using a default spacing; if only one of the sets is non-empty, then only the corresponding set of grid lines will be displayed, i.e. the grid will consist solely of parallel lines at the specified coordinates.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void SetGridCoordinates( 	ICollection<double> uCoordinates, 	ICollection<double> vCoordinates ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetGridCoordinates ( _ 	uCoordinates As ICollection(Of Double), _ 	vCoordinates As ICollection(Of Double) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetGridCoordinates( 	ICollection<double>^ uCoordinates,  	ICollection<double>^ vCoordinates ) ``` |

#### Parameters

uCoordinates
:   Type:  System.Collections.Generic ICollection   Double    
     Set of u coordinates at which to draw grid lines

vCoordinates
:   Type:  System.Collections.Generic ICollection   Double    
     Set of v coordinates at which to draw grid lines

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FieldDomainPointsByUV Class](aa1eb974-d283-f16e-8431-a7e02fe4e076.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)