[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FindStartsOfLongestPathsFromRooms Method

---



|  |
| --- |
| [PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)   [See Also](#seeAlsoToggle) |

For a floor plan view, calculates paths from points inside rooms to the closests of the destinations. Returns the start points of the longest path(s). If multiple paths have the same longest length, returns multiple start points.

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2020.2

# Syntax

| C# |
| --- |
| ``` public static IList<XYZ> FindStartsOfLongestPathsFromRooms( 	View DBView, 	IList<XYZ> destinationPoints ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function FindStartsOfLongestPathsFromRooms ( _ 	DBView As View, _ 	destinationPoints As IList(Of XYZ) _ ) As IList(Of XYZ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static IList<XYZ^>^ FindStartsOfLongestPathsFromRooms( 	View^ DBView,  	IList<XYZ^>^ destinationPoints ) ``` |

#### Parameters

DBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The floor plan view to use when computing the points.

destinationPoints
:   Type:  System.Collections.Generic IList   [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Destination points. The input Z coordinates are ignored and set to the view's level elevation.

#### Return Value

Start points of the paths with longest lengths. The array is empty if there are no valid paths from any points in rooms to any of the destination points.

# Remarks

The entire plan is divided in small tiles, and the distance to the closest destination point is calculated for each tile center point. Only tile center points that are located in rooms in the view are taken into account.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | View is not a floor plan view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The Path of Travel calculation service is not available -or- This functionality is not available in Revit LT. |

# See Also

[PathOfTravel Class](99c2bb04-151f-c325-84b2-40dee81447d6.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)