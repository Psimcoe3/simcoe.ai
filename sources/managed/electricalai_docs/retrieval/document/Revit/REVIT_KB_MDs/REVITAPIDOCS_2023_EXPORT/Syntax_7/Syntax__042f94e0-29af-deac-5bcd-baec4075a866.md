[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### LocationLineJustification Property

---



|  |
| --- |
| [StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm)   [See Also](#seeAlsoToggle) |

The position of the run relative to the Up-direction path used to create the run.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public StairsRunJustification LocationLineJustification { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property LocationLineJustification As StairsRunJustification 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property StairsRunJustification LocationLineJustification { 	StairsRunJustification get (); 	void set (StairsRunJustification value); } ``` |

# Remarks

Only common runs(straight, spiral, winder) have location line justification.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The stairs run is sketched so the data being set is not applicable. |

# See Also

[StairsRun Class](ea0e49a0-a007-79d0-c902-a24b1359ae28.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)