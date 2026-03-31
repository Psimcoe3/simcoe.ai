[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetFieldOrder Method

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Reorders the fields in the schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetFieldOrder( 	IList<ScheduleFieldId> fieldIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetFieldOrder ( _ 	fieldIds As IList(Of ScheduleFieldId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetFieldOrder( 	IList<ScheduleFieldId^>^ fieldIds ) ``` |

#### Parameters

fieldIds
:   Type:  System.Collections.Generic IList   [ScheduleFieldId](e437cc01-b976-fe8a-225a-1a0024171fae.htm)    
     The field IDs in a new order.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | fieldIds does not contain exactly the same field IDs as this ScheduleDefinition currently contains. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)