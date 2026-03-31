[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Distance Property

---



|  |
| --- |
| [SpacingRule Class](d8a51fa2-f3cd-5f12-d8cc-87c3888570f9.htm)   [See Also](#seeAlsoToggle) |

The exact distance between layout lines.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public double Distance { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Distance As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double Distance { 	double get (); 	void set (double value); } ``` |

# Remarks

This property is only available when  [Layout](81018421-ab61-9115-b171-c359e557f49e.htm)  is equal to FixedDistance, MaximumSpacing, or MinimumSpacing. Must be a positive value less than 30000'.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the  [Layout](81018421-ab61-9115-b171-c359e557f49e.htm)  property is None or FixedNumber. |

# See Also

[SpacingRule Class](d8a51fa2-f3cd-5f12-d8cc-87c3888570f9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)