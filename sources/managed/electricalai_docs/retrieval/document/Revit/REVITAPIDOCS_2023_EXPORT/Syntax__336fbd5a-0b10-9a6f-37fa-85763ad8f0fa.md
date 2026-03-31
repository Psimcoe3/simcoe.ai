[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Split Method (Int32)

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

Splits the schedule into several segments by given segment number.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022.1

# Syntax

| C# |
| --- |
| ``` public void Split( 	int segmentNumber ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Split ( _ 	segmentNumber As Integer _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Split( 	int segmentNumber ) ``` |

#### Parameters

segmentNumber
:   Type:  System Int32    
     The segment number.

# Remarks

* The segment number must be greater than 0.
* A schedule can be split only when it is not split yet.
* A titleblock revision schedule cannot be split.
* Once a sheet specific schedule, i.e., the schedule is filtered by sheet, is split, the segments will be placed on its sheet view immediately.

* After split, all segments will have even height limits based on the schedule height and segment number except the last segment shown on the sheet view.
* The height limit of the last segment cannot be set, because the height of the schedule instances of the last segment will be determined by the schedule instances of previous segments and the height of the whole schedule.
* Check  [SetSegmentHeight(Int32, Double)](a1f5c540-42a8-a236-7b97-dbf027a7c5d7.htm)  to see more about segment height.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The segment number must be greater than 1. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Revision schedules cannot be split. -or- A schedule filtered by sheet can't be split. -or- This ViewSchedule is split. |

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[Split Overload](5d8197cc-86c5-5f08-f0e1-d5c996e97795.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)