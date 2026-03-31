[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExcessLengthFillSpacing Property

---



|  |
| --- |
| [BalusterPattern Class](bb7868e3-0665-07e5-59e4-a95efb3079ab.htm)   [See Also](#seeAlsoToggle) |

The value defines the spacing between each baluster instance inserted in the excess length.

**Namespace:**   [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public double ExcessLengthFillSpacing { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property ExcessLengthFillSpacing As Double 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property double ExcessLengthFillSpacing { 	double get (); 	void set (double value); } ``` |

# Remarks

The spacing is used only if a baluster family is set to excess length fill.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: The given value for excessLengthFillSpacing must be between 0 and 30000 feet. |

# See Also

[BalusterPattern Class](bb7868e3-0665-07e5-59e4-a95efb3079ab.htm)

[Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)