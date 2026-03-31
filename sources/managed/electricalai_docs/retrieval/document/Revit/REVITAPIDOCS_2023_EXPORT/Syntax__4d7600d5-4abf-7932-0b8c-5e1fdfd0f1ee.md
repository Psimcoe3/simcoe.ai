[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MeasureFrom Property

---



|  |
| --- |
| [PointLocationOnCurve Class](f2e008f9-e1d1-a8ff-6a28-f15e180bf85f.htm)   [See Also](#seeAlsoToggle) |

The location on the curve from which the measurement is taken.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public PointOnCurveMeasureFrom MeasureFrom { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property MeasureFrom As PointOnCurveMeasureFrom 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property PointOnCurveMeasureFrom MeasureFrom { 	PointOnCurveMeasureFrom get (); 	void set (PointOnCurveMeasureFrom value); } ``` |

# Remarks

The measure-from is not checked until this class is assigned for a particular reference point on a particular curve. At that time, the measure-from must be valid for the curve.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[PointLocationOnCurve Class](f2e008f9-e1d1-a8ff-6a28-f15e180bf85f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)