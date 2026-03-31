[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleFilterType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Type of schedule filter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum ScheduleFilterType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ScheduleFilterType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ScheduleFilterType ``` |

# Members

| Member name | Description |
| --- | --- |
| Invalid | An invalid filter. Do not use. |
| HasParameter | The element has the parameter specified by the field. Used with shared parameters. No value is specified for this filter type. |
| Equal | The field value is equal to the specified value. |
| NotEqual | The field value is not equal to the specified value. |
| GreaterThan | The field value is greater than the specified value. |
| GreaterThanOrEqual | The field value is greater than or equal to the specified value. |
| LessThan | Less The field value is less than to the specified value. |
| LessThanOrEqual | The field value is less than or equal to the specified value. |
| Contains | For a string field, the field value contains the specified string. |
| NotContains | For a string field, the field value does not contain the specified string. |
| BeginsWith | For a string field, the field value begins with the specified string. |
| NotBeginsWith | For a string field, the field value does not begin with the specified string. |
| EndsWith | For a string field, the field value ends with specified string. |
| NotEndsWith | For a string field, the field value does not end with the specified string. |
| IsAssociatedWithGlobalParameter | The field is associated with a specified global parameter of a compatible type |
| IsNotAssociatedWithGlobalParameter | The field is not associated with a specified global parameter of a compatible type |
| HasValue | The element has a value for the specified parameter. No value is specified. |
| HasNoValue | The element does not have a value for the specified parameter. No value is specified. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)