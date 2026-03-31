[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SketchedStairsCurveData Constructor

---



|  |
| --- |
| [SketchedStairsCurveData Class](db3920d1-6efe-0ed4-f951-4d69c254cc6c.htm)   [See Also](#seeAlsoToggle) |

Construct a SketchedStairsCurveData defined by a curve associated with its height and slope type.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public SketchedStairsCurveData( 	Curve boundaryCurve, 	double height, 	SketchedCurveSlopeOption slopeType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	boundaryCurve As Curve, _ 	height As Double, _ 	slopeType As SketchedCurveSlopeOption _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: SketchedStairsCurveData( 	Curve^ boundaryCurve,  	double height,  	SketchedCurveSlopeOption slopeType ) ``` |

#### Parameters

boundaryCurve
:   Type:  [Autodesk.Revit.DB Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)

height
:   Type:  System Double

slopeType
:   Type:  [Autodesk.Revit.DB.Architecture SketchedCurveSlopeOption](aee63133-70ad-7902-c3b5-1f162151679b.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[SketchedStairsCurveData Class](db3920d1-6efe-0ed4-f951-4d69c254cc6c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)