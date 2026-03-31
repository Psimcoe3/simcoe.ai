[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFilter Method

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Replaces a filter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetFilter( 	int index, 	ScheduleFilter filter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFilter ( _ 	index As Integer, _ 	filter As ScheduleFilter _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFilter( 	int index,  	ScheduleFilter^ filter ) ``` |

#### Parameters

index
:   Type:  System Int32    
     The index of the filter to replace.

filter
:   Type:  [Autodesk.Revit.DB ScheduleFilter](a5dfec9f-1efd-b507-d079-eabcbf5032f8.htm)    
     The new filter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The field ID is not the ID of a field in this ScheduleDefinition. -or- The field and filter type cannot be used to filter this ScheduleDefinition. -or- The filter value is not valid for the field and filter type. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | index is not a valid filter index. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This ScheduleDefinition does not support filters. |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)