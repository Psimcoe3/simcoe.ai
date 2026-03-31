[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FindShortestPaths Method

---



|  |
| --- |
| [PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)   [See Also](#seeAlsoToggle) |

For a floor plan view, calculates paths from each start point to its closest destinations. Returns the path, represented by an array of XYZ points.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2021

# Syntax

| C# |
| --- |
| ``` public static IList<IList<XYZ>> FindShortestPaths( 	View DBView, 	IList<XYZ> destinationPoints, 	IList<XYZ> startPoints ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function FindShortestPaths ( _ 	DBView As View, _ 	destinationPoints As IList(Of XYZ), _ 	startPoints As IList(Of XYZ) _ ) As IList(Of IList(Of XYZ)) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<IList<XYZ^>^>^ FindShortestPaths( 	View^ DBView,  	IList<XYZ^>^ destinationPoints,  	IList<XYZ^>^ startPoints ) ``` |

#### Parameters

DBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The floor plan view to use when computing the points.

destinationPoints
:   Type:  System.Collections.Generic IList   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Destination points. The input Z coordinates are ignored and set to the view's level elevation.

startPoints
:   Type:  System.Collections.Generic IList   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Start points for which shortest paths are calculated.

#### Return Value

Array of paths calculated from each start point to its corresponding closest destination. If a path cannot be caculated the corresponsing sub-array is set to an empty array.

# Remarks

The calculation is done in a floor plan with one or more destinationPoints and one or more startPoints. The shortest path is calculated from each start point to its closest destination point.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | View is not a floor plan view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The Path of Travel calculation service is not available -or- This functionality is not available in Revit LT. |

# See Also

[PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)