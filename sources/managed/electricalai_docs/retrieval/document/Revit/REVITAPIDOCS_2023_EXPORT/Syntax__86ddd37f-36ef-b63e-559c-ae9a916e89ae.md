[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### WorksharingDisplay Property

---



|  |
| --- |
| [TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.htm)   [See Also](#seeAlsoToggle) |

The current state of the WorksharingDisplay mode in the associated view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016 Subscription Update

# Syntax

| C# |
| --- |
| ``` public WorksharingDisplayMode WorksharingDisplay { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property WorksharingDisplay As WorksharingDisplayMode 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property WorksharingDisplayMode WorksharingDisplay { 	WorksharingDisplayMode get (); 	void set (WorksharingDisplayMode value); } ``` |

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The WorksharingDisplay mode is either disabled or inapplicable in the associated view. |

# See Also

[TemporaryViewModes Class](cf6ecc84-e459-55c5-a4d7-d88ae4033a23.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)