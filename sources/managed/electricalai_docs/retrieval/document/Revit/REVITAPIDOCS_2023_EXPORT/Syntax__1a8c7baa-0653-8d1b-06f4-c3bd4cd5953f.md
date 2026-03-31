[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDistance Method

---



|  |
| --- |
| [Alignment Class](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)   [See Also](#seeAlsoToggle) |

Calculates the relative distance along the alignment between two stations based on their alignment distances according to Revit Internal Origin Coordinate Base. The distance may be positive or negative depending on the relative positions of the input stations on the alignment.

**Namespace:**   [Autodesk.Revit.DB.Infrastructure](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)    
  **Assembly:**   Autodesk.CivilAlignments.DBApplication  (in Autodesk.CivilAlignments.DBApplication.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021.1

# Syntax

| C# |
| --- |
| ``` public double GetDistance( 	double fromStation, 	double toStation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetDistance ( _ 	fromStation As Double, _ 	toStation As Double _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetDistance( 	double fromStation,  	double toStation ) ``` |

#### Parameters

fromStation
:   Type:  System Double    
     The displayed alignment station from which 2D length is to be calculated, in Revit internal model units (standard Imperial feet).

toStation
:   Type:  System Double    
     The displayed alignment station to which 2D length is to be calculated, in Revit internal model units (standard Imperial feet).

#### Return Value

Distance (positive or negative) along the alignment between two stations. The sign of the distance depends on the relative positions of the input stations on the alignment.

# See Also

[Alignment Class](6594712d-3b22-9b08-ab4c-782df88f36d1.htm)

[Autodesk.Revit.DB.Infrastructure Namespace](cedea963-42a0-acf8-0f0e-5477c4212ae9.htm)