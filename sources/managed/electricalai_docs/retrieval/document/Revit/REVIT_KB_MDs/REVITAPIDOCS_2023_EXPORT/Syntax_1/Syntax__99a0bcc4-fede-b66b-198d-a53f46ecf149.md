[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentOpening Event

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the DocumentOpening event to be notified when Revit is just about to open a document.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<DocumentOpeningEventArgs> DocumentOpening ``` |

 

| Visual Basic |
| --- |
| ``` Public Event DocumentOpening As EventHandler(Of DocumentOpeningEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<DocumentOpeningEventArgs^>^ DocumentOpening { 	void add (EventHandler<DocumentOpeningEventArgs^>^ value); 	void remove (EventHandler<DocumentOpeningEventArgs^>^ value); } ``` |

# Remarks

This event is raised when Revit is just about to open a document.

Event is cancellable. To cancel it, call the 'Cancel()' method in event's argument to True. Your application is responsible for providing feedback to the user about the reason for the cancellation.

The document cannot be modified, for it is not opened yet at the time of the event.

Another  [DocumentOpened](b9415c2d-442e-f61d-aafa-de31cce7959b.htm)  event will be raised immediately after document is opened.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)