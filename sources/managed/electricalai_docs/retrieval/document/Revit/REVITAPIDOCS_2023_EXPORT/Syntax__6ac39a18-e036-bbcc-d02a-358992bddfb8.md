[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidFormatOptions Method

---



|  |
| --- |
| [DimensionEqualityLabelFormatting Class](019b51cc-346a-5861-f093-669a7446c874.htm)   [See Also](#seeAlsoToggle) |

Checks whether a FormatOptions object is valid for the LabelType.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public bool IsValidFormatOptions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidFormatOptions As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidFormatOptions() ``` |

#### Return Value

True if the FormatOptions object is valid, false otherwise.

# Remarks

Only objects whose LabelType is LengthOfSegment or TotalLength can have FormatOptions assigned.

# See Also

[DimensionEqualityLabelFormatting Class](019b51cc-346a-5861-f093-669a7446c874.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)