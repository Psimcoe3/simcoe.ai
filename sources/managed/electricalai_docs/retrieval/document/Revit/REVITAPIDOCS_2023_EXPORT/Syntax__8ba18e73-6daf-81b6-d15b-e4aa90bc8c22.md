[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Export Method

---



|  |
| --- |
| [ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)   [See Also](#seeAlsoToggle) |

Exports the schedule data to a text file.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void Export( 	string folder, 	string name, 	ViewScheduleExportOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub Export ( _ 	folder As String, _ 	name As String, _ 	options As ViewScheduleExportOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void Export( 	String^ folder,  	String^ name,  	ViewScheduleExportOptions^ options ) ``` |

#### Parameters

folder
:   Type:  System String    
     Path to the location where the file will be saved.

name
:   Type:  System String    
     Name of file.

options
:   Type:  [Autodesk.Revit.DB ViewScheduleExportOptions](f0bde7ea-ceab-820d-7c55-b09819f21607.htm)    
     Options that relate to schedule export.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | NullOrEmpty -or- Contains invalid characters. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileAccessException](187d56d7-0b37-699f-2abd-6ddebfa93f1e.htm) | The path indicated could not be accessed. |
| [Autodesk.Revit.Exceptions InvalidPathArgumentException](3f3c93a6-008b-f9de-40d4-5cd99bb32b34.htm) | The folder does not exist. |

# See Also

[ViewSchedule Class](0dae24ba-5dcb-9a34-cccc-0cf8cc52bcd3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)