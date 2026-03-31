[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SuppressSpaces Property

---



|  |
| --- |
| [FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)   [See Also](#seeAlsoToggle) |

Indicates if spaces around the dash should be suppressed in feet and fractional inches.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool SuppressSpaces { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property SuppressSpaces As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool SuppressSpaces { 	bool get (); 	void set (bool value); } ``` |

#### Field Value

True if spaces should be suppressed, false otherwise. The default is false.

# Remarks

This property is applicable to display units related to feet and fractional inches:

* DUT\_FEET\_FRACTIONAL\_INCHES
* DUT\_RISE\_OVER\_FOOT
* DUT\_RISE\_OVER\_10\_FEET

When SuppressLeadingZeros is true, spaces will not be inserted before and after the dash separating feet from inches. For example, 1' - 2 3/4" will be displayed as 1'-2 3/4".

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | UseDefault is true in this FormatOptions. -or- When setting this property: SuppressSpaces was set to true but spaces cannot be suppressed for the display unit in this FormatOptions. |

# See Also

[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)