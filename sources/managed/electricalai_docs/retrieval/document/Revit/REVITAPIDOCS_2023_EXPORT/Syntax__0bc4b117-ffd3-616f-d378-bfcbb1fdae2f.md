[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SaveToProjectAsImage Method

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [See Also](#seeAlsoToggle) |

Creates an image view from the currently active view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ElementId SaveToProjectAsImage( 	ImageExportOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SaveToProjectAsImage ( _ 	options As ImageExportOptions _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ SaveToProjectAsImage( 	ImageExportOptions^ options ) ``` |

#### Parameters

options
:   Type:  [Autodesk.Revit.DB ImageExportOptions](c2e823a1-6eb0-2bf3-f07b-ed46d8f7b70a.htm)    
     The options which govern the image creation.

#### Return Value

Id of the newly created view if the operation succeeded, invalid element id otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | options object is invalid: the ExportRange is invalid, must be CurrentView or VisibleRegionOfCurrentView, or the ViewName is invalid, must be non-empty, unique and should not contain prohibited characters. -or- The current view cannot be exported as an image |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)