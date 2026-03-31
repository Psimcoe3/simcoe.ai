[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### MakeBound Method

---



|  |
| --- |
| [Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)   [See Also](#seeAlsoToggle) |

Changes the bounds of this curve to the specified values.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void MakeBound( 	double startParameter, 	double endParameter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub MakeBound ( _ 	startParameter As Double, _ 	endParameter As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void MakeBound( 	double startParameter,  	double endParameter ) ``` |

#### Parameters

startParameter
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The new parameter of the start point.

endParameter
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The new parameter of the end point.

# Remarks

If the curve is marked as read-only (because it was extracted directly from a Revit element or collection/aggregation object), calling this method causes the object to be changed to carry a disconnected copy of the original curve. The modification will not affect the original curve or the object that supplied it.

# Remarks

This method changes this curve to bound.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the specified values are infinite. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when endParameter is smaller than startParameter. |

# See Also

[Curve Class](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)