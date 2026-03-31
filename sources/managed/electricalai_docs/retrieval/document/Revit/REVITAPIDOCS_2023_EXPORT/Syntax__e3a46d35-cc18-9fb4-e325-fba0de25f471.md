[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PaperSource Property

---



|  |
| --- |
| [PrintParameters Class](59e6cfe9-b1e8-70c0-814b-ee69c8fca411.htm)   [See Also](#seeAlsoToggle) |

The page source.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public PaperSource PaperSource { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property PaperSource As PaperSource 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property PaperSource^ PaperSource { 	PaperSource^ get (); 	void set (PaperSource^ value); } ``` |

# Remarks

User can select the candidate via  [PaperSources](c22a7905-70b3-f31f-c832-531e6828b1fb.htm)  and then set the Page source of the Print Setting.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the input argument is invalid for current printer. |

# See Also

[PrintParameters Class](59e6cfe9-b1e8-70c0-814b-ee69c8fca411.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)