[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentPrinted Event

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the DocumentPrinted event to be notified immediately after Revit has finished printing a view or ViewSet of the document.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<DocumentPrintedEventArgs> DocumentPrinted ``` |

 

| Visual Basic |
| --- |
| ``` Public Event DocumentPrinted As EventHandler(Of DocumentPrintedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<DocumentPrintedEventArgs^>^ DocumentPrinted { 	void add (EventHandler<DocumentPrintedEventArgs^>^ value); 	void remove (EventHandler<DocumentPrintedEventArgs^>^ value); } ``` |

# Remarks

This event is raised immediately after Revit has finished printing a view or ViewSet of the document. It is raised even when document printing failed or was cancelled (during DocumentPriting event).

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Check the 'Status' field in event's argument to see whether the action itself was successful or not.

This event is not cancellable, for the process of printing has already been finished.

If the action was not successful, the document may not be modified and new transactions may not be started.

The following API functions are not available for the current document during this event:

* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)