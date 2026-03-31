[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FileImported Event

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the FileImported event to be notified immediately after Revit has finished importing a file of format supported by the API.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<FileImportedEventArgs> FileImported ``` |

 

| Visual Basic |
| --- |
| ``` Public Event FileImported As EventHandler(Of FileImportedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<FileImportedEventArgs^>^ FileImported { 	void add (EventHandler<FileImportedEventArgs^>^ value); 	void remove (EventHandler<FileImportedEventArgs^>^ value); } ``` |

# Remarks

This event is raised immediately after Revit has finished importing a file of format supported by the API. It is raised even when file importing failed or was cancelled (during FileImporting event).

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Check the 'Status' field in event's argument to see whether the action itself was successful or not.

This event is not cancellable, for the process of importing has already been finished.

If the action was not successful, the document may not be modified and new transactions may not be started.

The following API functions are not available for the current document during this event:

* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)