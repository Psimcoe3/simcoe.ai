[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRectangularHeight Method

---



|  |
| --- |
| [CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)   [See Also](#seeAlsoToggle) |

Returns the width of a curve loop if it is rectangular with respect to the projection plane.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public double GetRectangularHeight( 	Plane plane ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRectangularHeight ( _ 	plane As Plane _ ) As Double ``` |

 

| Visual C++ |
| --- |
| ``` public: double GetRectangularHeight( 	Plane^ plane ) ``` |

#### Parameters

plane
:   Type:  [Autodesk.Revit.DB Plane](6a6ee978-f114-558d-3c69-00d289aa855f.htm)    
     The plane to which the curves will be projected.

#### Return Value

The height.

# Remarks

The height is determined by the V extents of the UV curve created by from the curve loop plane.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The curve loop is not rectangular when projected to the input plane. |

# See Also

[CurveLoop Class](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)