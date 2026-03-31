[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDefaultNameForSchedule Method (Document, ElementId)

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

Gets the default view name that will be used when creating a regular schedule.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static string GetDefaultNameForSchedule( 	Document document, 	ElementId categoryId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetDefaultNameForSchedule ( _ 	document As Document, _ 	categoryId As ElementId _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: static String^ GetDefaultNameForSchedule( 	Document^ document,  	ElementId^ categoryId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to which the new schedule will be added.

categoryId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ID of the category whose elements will be included in the schedule, or InvalidElementId for a multi-category schedule.

#### Return Value

The default view name.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document. -or- categoryId is not a valid category for a regular schedule. -or- The Areas category was specified but an area scheme ID was not provided. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[GetDefaultNameForSchedule Overload](f6494df4-739c-a9c4-4a77-856a453f3a3e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)