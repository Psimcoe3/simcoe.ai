[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExportImage Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Exports a view or set of views into an image file.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void ExportImage( 	ImageExportOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ExportImage ( _ 	options As ImageExportOptions _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ExportImage( 	ImageExportOptions^ options ) ``` |

#### Parameters

options
:   Type:  [Autodesk.Revit.DB ImageExportOptions](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.htm)    
     The options which govern the image export.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The current view cannot be exported as an image |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions FileAccessException](187d56d7-0b37-699f-2abd-6ddebfa93f1e.htm) | The path indicated could not be accessed. |
| [Autodesk.Revit.Exceptions FileNotFoundException](73250198-dbc6-e760-4297-ec062f00f574.htm) | The path indicated could not be found. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Exporting is not allowed in the current application mode. -or- Failed to export image due to an error with the inputs. -or- Failed to export image due to an issue where the DirectX Device was lost. |
| [Autodesk.Revit.Exceptions OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The Graphics module is not available in the installed Revit. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)