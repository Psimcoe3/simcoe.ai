[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FileImporting Event

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the FileImporting event to be notified when Revit is just about to import a file of format supported by the API.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<FileImportingEventArgs> FileImporting ``` |

 

| Visual Basic |
| --- |
| ``` Public Event FileImporting As EventHandler(Of FileImportingEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<FileImportingEventArgs^>^ FileImporting { 	void add (EventHandler<FileImportingEventArgs^>^ value); 	void remove (EventHandler<FileImportingEventArgs^>^ value); } ``` |

# Remarks

This event is raised when Revit is just about to import a file of format supported by the API.

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Event is cancellable. To cancel it, call the 'Cancel()' method in event's argument to True. Your application is responsible for providing feedback to the user about the reason for the cancellation.

The following API functions are not available for the current document during this event:

* All overloads of Autodesk.Revit.DB.Document.Import()
* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  .
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

Another  [FileImported](f72dee18-1a0d-dc0c-eb72-b75b0939c7c9.htm)  event will be raised immediately after file importing is finished.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)