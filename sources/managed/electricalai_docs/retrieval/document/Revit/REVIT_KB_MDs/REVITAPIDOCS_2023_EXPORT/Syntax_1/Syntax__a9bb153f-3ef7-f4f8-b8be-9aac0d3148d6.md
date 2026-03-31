[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanSortByField Method

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Checks whether a field can be used for sorting/grouping.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool CanSortByField( 	ScheduleFieldId fieldId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanSortByField ( _ 	fieldId As ScheduleFieldId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanSortByField( 	ScheduleFieldId^ fieldId ) ``` |

#### Parameters

fieldId
:   Type:  [Autodesk.Revit.DB ScheduleFieldId](e437cc01-b976-fe8a-225a-1a0024171fae.htm)    
     The ID of the field to check.

#### Return Value

True if the field can be used for sorting/grouping, false otherwise.

# Remarks

Schedules cannot be sorted/grouped by the Count field, Percentage fields, or Formula fields that depend on Percentage fields because those types of fields don't have meaningful values until after sorting and grouping takes place.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | fieldId is not the ID of a field in this ScheduleDefinition. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)