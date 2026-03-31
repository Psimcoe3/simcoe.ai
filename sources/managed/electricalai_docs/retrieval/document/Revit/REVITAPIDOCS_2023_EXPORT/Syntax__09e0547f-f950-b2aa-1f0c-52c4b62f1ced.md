[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DigitGroupingSymbol Property

---



|  |
| --- |
| [Units Class](89d89465-897f-4105-b935-27edf67aab3e.htm)   [See Also](#seeAlsoToggle) |

The symbol used to separate groups of digits when numbers are formatted with digit grouping.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public DigitGroupingSymbol DigitGroupingSymbol { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property DigitGroupingSymbol As DigitGroupingSymbol 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property DigitGroupingSymbol DigitGroupingSymbol { 	DigitGroupingSymbol get (); 	void set (DigitGroupingSymbol value); } ``` |

#### Field Value

The digit grouping symbol. The default is Comma.

# Remarks

This setting only has an effect when the UseDigitGrouping property is set to true in the FormatOptions object for the unit type being formatted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[Units Class](89d89465-897f-4105-b935-27edf67aab3e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)