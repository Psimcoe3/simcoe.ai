[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewSchedule Class

---



|  |
| --- |
| [Members](b7a752f8-9f04-31dc-80f2-0086f24ed020.htm)   [See Also](#seeAlsoToggle) |

A schedule view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public class ViewSchedule : TableView ``` |

 

| Visual Basic |
| --- |
| ``` Public Class ViewSchedule _ 	Inherits TableView ``` |

 

| Visual C++ |
| --- |
| ``` public ref class ViewSchedule : public TableView ``` |

# Remarks

The ViewSchedule class represents schedules and other schedule-like views, including single-category and multi-category schedules, key schedules, material takeoffs, view lists, sheet lists, keynote legends, revision schedules, and note blocks. The ViewSchedule class is not used for panel schedules (see PanelScheduleView) or graphical column schedules.

A schedule is a tabular representation of data. A typical schedule shows all elements of a category (doors, rooms, etc.) with each row representing an element and each column representing a parameter. This basic structure can be modified using filters, sorting, grouping, totals, formulas, and other features.

The ScheduleDefinition class contains most settings that determine the contents of a schedule, including category, fields, filters, and sorting.

A graphical representation of a schedule can be placed on a sheet using the ScheduleSheetInstance class.

# Inheritance Hierarchy

System Object    
  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
  [Autodesk.Revit.DB TableView](ba608411-21af-e924-2aa2-3595548ab39f.htm)    
  Autodesk.Revit.DB ViewSchedule

# See Also

[ViewSchedule Members](b7a752f8-9f04-31dc-80f2-0086f24ed020.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)