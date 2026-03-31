[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateSpatialFieldManager Method

---



|  |
| --- |
| [SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)   [See Also](#seeAlsoToggle) |

Factory method - creates manager object for the given view

**Namespace:**   [Autodesk.Revit.DB.Analysis](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static SpatialFieldManager CreateSpatialFieldManager( 	View view, 	int numberOfMeasurements ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreateSpatialFieldManager ( _ 	view As View, _ 	numberOfMeasurements As Integer _ ) As SpatialFieldManager ``` |

 

| Visual C++ |
| --- |
| ``` public: static SpatialFieldManager^ CreateSpatialFieldManager( 	View^ view,  	int numberOfMeasurements ) ``` |

#### Parameters

view
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     View for which manager object is created or retrieved

numberOfMeasurements
:   Type:  System Int32    
     Total number of measurements in the calculated results. This number defines the length of value arrays in ValueAtPoint objects

#### Return Value

Manager object for the view passed in the argument

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | numberOfMeasurements is less than one |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | View is not allowed to display analysis results or a manager object for this view already exists |

# See Also

[SpatialFieldManager Class](0a6d155e-6ef1-7215-f8f1-c1d8203797ee.htm)

[Autodesk.Revit.DB.Analysis Namespace](958e2e12-587d-f188-5d7b-f13d7dbfdf48.htm)