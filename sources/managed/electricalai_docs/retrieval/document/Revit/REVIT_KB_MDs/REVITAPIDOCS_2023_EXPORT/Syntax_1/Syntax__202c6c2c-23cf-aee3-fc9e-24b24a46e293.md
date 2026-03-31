[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ApproximateLength Property

---



|  |
| --- |
| [Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)   [See Also](#seeAlsoToggle) |

The approximate length of the curve.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double ApproximateLength { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ApproximateLength As Double 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ApproximateLength { 	double get (); } ``` |

# Remarks

Quickly estimates the length of the curve, may deviate by a factor of 2 in some cases. The computation is exact for lines and arcs.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the curve is unbound and not periodic. |

# See Also

[Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)