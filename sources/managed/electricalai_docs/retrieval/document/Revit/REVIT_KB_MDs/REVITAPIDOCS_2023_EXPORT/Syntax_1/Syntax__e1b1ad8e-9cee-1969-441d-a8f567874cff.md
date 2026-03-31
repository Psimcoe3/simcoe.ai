[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsModeEnabled Method

---



|  |
| --- |
| [TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.htm)   [See Also](#seeAlsoToggle) |

Tests whether a temporary view mode is currently enabled in the associated view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public bool IsModeEnabled( 	TemporaryViewMode mode ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsModeEnabled ( _ 	mode As TemporaryViewMode _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsModeEnabled( 	TemporaryViewMode mode ) ``` |

#### Parameters

mode
:   Type:  [Autodesk.Revit.DB TemporaryViewMode](8c0c72db-2801-3642-72bb-108cfdff23e1.htm)    
     The mode to evaluate

#### Return Value

True if the requested mode is available and enabled in the associated view; False otherwise.

# Remarks

Most of temporary modes are enabled in a specific context only. A programmer who wants to use a mode needs to first test whether it is currently available and enabled, or not.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)