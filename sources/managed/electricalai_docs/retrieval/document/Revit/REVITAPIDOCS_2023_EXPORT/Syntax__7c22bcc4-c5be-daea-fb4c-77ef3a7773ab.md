[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetField Method (Int32)

---



|  |
| --- |
| [ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)   [See Also](#seeAlsoToggle) |

Gets a field.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public ScheduleField GetField( 	int index ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetField ( _ 	index As Integer _ ) As ScheduleField ``` |

 

| Visual C++ |
| --- |
| ``` public: ScheduleField^ GetField( 	int index ) ``` |

#### Parameters

index
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The index of the field.

#### Return Value

The field.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | index is not a valid field index in this ScheduleDefinition. |

# See Also

[ScheduleDefinition Class](420696e3-f3ec-1a1d-1205-36a8119d81e5.htm)

[GetField Overload](6adf5d49-4644-1c45-7c01-573f061e9562.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)