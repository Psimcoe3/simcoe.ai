[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Number Property

---



|  |
| --- |
| [SpacingRule Class](d8a51fa2-f3cd-5f12-d8cc-87c3888570f9.htm)   [See Also](#seeAlsoToggle) |

The exact number of lines in the region.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public int Number { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property Number As Integer 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property int Number { 	int get (); 	void set (int value); } ``` |

# Remarks

This property is only available when  [Layout](81018421-ab61-9115-b171-c359e557f49e.htm)  is equal to FixedNumber. Lines will be placed exactly at the boundaries if possible, so if your region is 100' long and you specify Number = 11, your lines will be 10' apart. Must be between 1 and 200.

# See Also

[SpacingRule Class](d8a51fa2-f3cd-5f12-d8cc-87c3888570f9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)