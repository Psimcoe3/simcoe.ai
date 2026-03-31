[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleFilter Constructor (ScheduleFieldId, ScheduleFilterType, ElementId)

---



|  |
| --- |
| [ScheduleFilter Class](a5dfec9f-1efd-b507-d079-eabcbf5032f8.htm)   [See Also](#seeAlsoToggle) |

Creates a new ScheduleFilter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ScheduleFilter( 	ScheduleFieldId fieldId, 	ScheduleFilterType filterType, 	ElementId value ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	fieldId As ScheduleFieldId, _ 	filterType As ScheduleFilterType, _ 	value As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ScheduleFilter( 	ScheduleFieldId^ fieldId,  	ScheduleFilterType filterType,  	ElementId^ value ) ``` |

#### Parameters

fieldId
:   Type:  [Autodesk.Revit.DB ScheduleFieldId](e437cc01-b976-fe8a-225a-1a0024171fae.htm)    
     The ID of the field used to filter the schedule.

filterType
:   Type:  [Autodesk.Revit.DB ScheduleFilterType](9b696f55-de40-8739-8cfb-decd51995cff.htm)    
     The filter type.

value
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The filter value for a filter using an ElementId value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ScheduleFilter Class](a5dfec9f-1efd-b507-d079-eabcbf5032f8.htm)

[ScheduleFilter Overload](d2173e5d-1eef-b41e-a11a-6e29ade8c478.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)