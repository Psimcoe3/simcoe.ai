[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScheduleFilter Class

---



|  |
| --- |
| [Members](2c2fc999-859e-169b-d958-ee248d9d74b7.htm)   [See Also](#seeAlsoToggle) |

A filter in a schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class ScheduleFilter : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ScheduleFilter _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ScheduleFilter : IDisposable ``` |

# Remarks

The ScheduleFilter class represents a single filter in a schedule. A filter is a condition that must be satisfied for an element to appear in the schedule. All filters must be satisfied for an element to appear in the schedule.

A schedule can be filtered by data that is not displayed in the schedule by marking the field used for filtering as hidden using the ScheduleField.IsHidden property.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB ScheduleFilter

# See Also

[ScheduleFilter Members](2c2fc999-859e-169b-d958-ee248d9d74b7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)