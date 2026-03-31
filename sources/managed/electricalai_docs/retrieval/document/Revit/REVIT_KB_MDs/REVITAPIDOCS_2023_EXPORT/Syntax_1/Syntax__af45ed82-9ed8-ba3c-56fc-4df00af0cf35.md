[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewPrinting Event

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the ViewPrinting event to be notified when Revit is just about to print a view of the document.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<ViewPrintingEventArgs> ViewPrinting ``` |

 

| Visual Basic |
| --- |
| ``` Public Event ViewPrinting As EventHandler(Of ViewPrintingEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<ViewPrintingEventArgs^>^ ViewPrinting { 	void add (EventHandler<ViewPrintingEventArgs^>^ value); 	void remove (EventHandler<ViewPrintingEventArgs^>^ value); } ``` |

# Remarks

This event is raised when Revit is just about to print a view of the document. If multiple views are combined to a single file, this event will be raised only once.

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Event is not cancellable. The 'Cancellable' property of event's argument is always False.

The following API functions are not available for the current document during this event:

* All overloads of Autodesk.Revit.DB.Document.Export()
* Autodesk.Revit.DB.Document.Print()
* [Print](1ea1e825-8044-7a27-d9b9-ca463443c3b9.htm)  and similar overloads.
* [SubmitPrint](0c9524b7-33b5-8c76-2843-c7024f03e4d7.htm)  and similar overloads.
* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  .
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

Another event  [ViewPrinted](5f995f6a-15d8-b1c3-9bc4-3bd203dc16f6.htm)  will be raised immediately after view printing is finished.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)