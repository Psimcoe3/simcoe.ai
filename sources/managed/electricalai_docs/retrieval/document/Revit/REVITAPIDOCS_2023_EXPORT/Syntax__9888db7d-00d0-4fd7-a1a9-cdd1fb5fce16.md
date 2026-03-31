[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleFieldType Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

The type of data displayed in a schedule field.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2013   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum ScheduleFieldType ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ScheduleFieldType ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ScheduleFieldType ``` |

# Members

| Member name | Description |
| --- | --- |
| Instance | An instance parameter of the scheduled elements. All shared parameters also use this type, regardless of whether they are instance or type parameters. |
| ElementType | A type parameter of the scheduled elements. |
| Count | The number of elements appearing on the schedule row. |
| ViewBased | A specialized type of field used for a few parameters whose displayed values can change based on the settings of the view:   * ROOM\_AREA and ROOM\_PERIMETER in room and space schedules. * PROJECT\_REVISION\_REVISION\_NUM in revision schedules. * KEYNOTE\_NUMBER in keynote legends that are numbered by sheet. |
| Formula | A formula calculated from the values of other fields in the schedule. |
| Percentage | A value indicating what percent of the total of another field each element represents. |
| Room | A parameter of the room that a scheduled element belongs to. |
| FromRoom | A parameter of the room on the "from" side of a door or window. |
| ToRoom | A parameter of the room on the "to" side of a door or window. |
| ProjectInfo | A parameter of the Project Info element in the project that the scheduled element belongs to, which may be a linked file. Only allowed in schedules that include elements from linked files. |
| Material | In a material takeoff, a parameter of one of the materials of a scheduled element. |
| MaterialQuantity | In a material takeoff, a value representing how a particular material is used within a scheduled element. The parameter ID can be MATERIAL\_AREA, MATERIAL\_VOLUME, or MATERIAL\_ASPAINT. |
| RevitLinkInstance | A parameter of the RevitLinkInstance that an element in a linked file belongs to. Currently RVT\_LINK\_INSTANCE\_NAME is the only supported parameter. Only allowed in schedules that include elements from linked files. |
| RevitLinkType | A parameter of the RevitLinkType that an element in a linked file belongs to. Currently RVT\_LINK\_FILE\_NAME\_WITHOUT\_EXT is the only supported parameter. Only allowed in schedules that include elements from linked files. |
| StructuralMaterial | A parameter of the structural material of a scheduled element. |
| Space | A parameter of the space that a scheduled element belongs to. |
| Analytical | A parameter of the analytical element of a scheduled physical element. |
| PhysicalType | A type parameter of the physical element of a scheduled analytical element. |
| PhysicalInstance | An instance parameter of the physical element of a scheduled analytical element. |
| CombinedParameter | Combine parameters of the types that display in a specific part of a schedule. The values for the combined parameters will display in the same cell separated by a slash or other separator. You can add a prefix, suffix or sample value to the parameter. |

# See Also

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)