[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SpanDirectionAngle Property

---



|  |
| --- |
| [Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.htm)   [See Also](#seeAlsoToggle) |

Retrieve the span direction angle of the floor.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public double SpanDirectionAngle { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SpanDirectionAngle As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double SpanDirectionAngle { 	double get (); 	void set (double value); } ``` |

# Remarks

The angle returned is in radians. An exception will be thrown if the floor is non structural.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: |

# See Also

[Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)