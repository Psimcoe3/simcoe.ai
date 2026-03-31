[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IncludeLinkedFiles Property

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Indicates if the schedule includes elements from linked files.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IncludeLinkedFiles { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property IncludeLinkedFiles As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool IncludeLinkedFiles { 	bool get (); 	void set (bool value); } ``` |

#### Field Value

True if elements in linked files should be included, false otherwise.

# Remarks

For an embedded ScheduleDefinition, this setting is controlled by the primary ScheduleDefinition and cannot be set in the embedded ScheduleDefinition.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: This ScheduleDefinition does not support including elements from linked files. -or- When setting this property: This ScheduleDefinition is an embedded ScheduleDefinition. |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)