[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InsertField Method (ScheduleFieldType, ElementId, Int32)

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Adds a regular field at the specified position in the list.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ScheduleField InsertField( 	ScheduleFieldType fieldType, 	ElementId parameterId, 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function InsertField ( _ 	fieldType As ScheduleFieldType, _ 	parameterId As ElementId, _ 	index As Integer _ ) As ScheduleField ``` |

 

| Visual C++ |
| --- |
| ``` public: ScheduleField^ InsertField( 	ScheduleFieldType fieldType,  	ElementId^ parameterId,  	int index ) ``` |

#### Parameters

fieldType
:   Type:  [Autodesk.Revit.DB ScheduleFieldType](9888db7d-00d0-4fd7-a1a9-cdd1fb5fce16.htm)    
     The type of data displayed by the field.

parameterId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ID of the parameter displayed by the field.

index
:   Type:  System Int32    
     The index in the list of fields.

#### Return Value

The new field.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | index is not a valid insert position. -or- A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | The field specified by fieldType and parameterId may not included in this ScheduleDefinition. -or- The field specified by fieldType and parameterId is already included in this ScheduleDefinition. |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[InsertField Overload](31528702-22e7-f515-5edc-9356585e3bc1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)