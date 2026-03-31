[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsByRange Property

---



|  |
| --- |
| [ColorFillScheme Class](c405eb5b-14fa-0fea-a750-dcd9925a90b0.htm)   [See Also](#seeAlsoToggle) |

Represents if the parameter values in entries are treated as value range or not.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public bool IsByRange { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IsByRange As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IsByRange { 	bool get (); 	void set (bool value); } ``` |

# Remarks

Notes:

* Only numeric parameter values could be treated as by range.
* There will exist at least two entries if the scheme is by range, and the first entry value should be always Int.MinValue or -Double.MaxValue.
* The entries will always be sorted by ascending in the scheme if it is by range.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The scheme entries cannot be explained by range. |

# See Also

[ColorFillScheme Class](c405eb5b-14fa-0fea-a750-dcd9925a90b0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)