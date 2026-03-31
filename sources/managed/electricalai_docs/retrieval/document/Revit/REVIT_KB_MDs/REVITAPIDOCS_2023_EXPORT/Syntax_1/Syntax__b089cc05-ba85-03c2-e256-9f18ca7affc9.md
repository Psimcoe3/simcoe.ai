[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentClosed Event

---



|  |
| --- |
| [ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the DocumentClosing event to be notified when Revit is just about to close a document.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<DocumentClosedEventArgs> DocumentClosed ``` |

 

| Visual Basic |
| --- |
| ``` Public Event DocumentClosed As EventHandler(Of DocumentClosedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<DocumentClosedEventArgs^>^ DocumentClosed { 	void add (EventHandler<DocumentClosedEventArgs^>^ value); 	void remove (EventHandler<DocumentClosedEventArgs^>^ value); } ``` |

# Remarks

This event is raised immediately after Revit has finished closing a document. It is raised even when document closing failed or was cancelled (during DocumentClosing event).

This event is not cancellable, for the process of closing document has already been finished.

The document cannot be modified because the corresponding object does not exist anymore.

# See Also

[ControlledApplication Class](35859972-2407-3910-cb07-bbb337e307e6.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)