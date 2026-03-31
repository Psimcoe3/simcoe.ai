[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Origin Property

---



|  |
| --- |
| [Dimension Class](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm)   [See Also](#seeAlsoToggle) |

The dimension origin.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015 Subscription Update

# Syntax

| C# |
| --- |
| ``` public XYZ Origin { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Origin As XYZ 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property XYZ^ Origin { 	XYZ^ get (); } ``` |

# Remarks

The origin is the middle point of the dimension line that makes up the dimension. This property is for use with single-segment dimensions only. For multi-segment dimensions use the corresponding property of the DimensionSegment class.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when:  * SpotDimension has more than one segments. |

# See Also

[Dimension Class](210f88be-e3c5-26a4-7dd8-3296f6725cce.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)