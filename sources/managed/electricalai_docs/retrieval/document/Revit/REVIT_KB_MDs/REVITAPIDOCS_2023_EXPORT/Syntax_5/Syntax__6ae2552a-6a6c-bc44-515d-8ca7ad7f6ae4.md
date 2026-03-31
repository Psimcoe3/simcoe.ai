[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DockableFrameVisibilityChanged Event

---



|  |
| --- |
| [UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)   [See Also](#seeAlsoToggle) |

Subscribe to this event to be notified when a Revit GenericDockableFrame has been shown or hidden in the Revit user interface. This event is called only for API-created GenericDockableFrames.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public event EventHandler<DockableFrameVisibilityChangedEventArgs> DockableFrameVisibilityChanged ``` |

 

| Visual Basic |
| --- |
| ``` Public Event DockableFrameVisibilityChanged As EventHandler(Of DockableFrameVisibilityChangedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<DockableFrameVisibilityChangedEventArgs^>^ DockableFrameVisibilityChanged { 	void add (EventHandler<DockableFrameVisibilityChangedEventArgs^>^ value); 	void remove (EventHandler<DockableFrameVisibilityChangedEventArgs^>^ value); } ``` |

# Remarks

This event is raised when the GenericDockableFrame is just about to be shown or hidden.

Event is not cancellable. The 'Cancellable' property of event's argument is always False.

No document may be modified at the time of the event.

The following API functions are not available for the current document during this event:

* All overloads of Autodesk.Revit.DB.Document.Export()
* All overloads of Autodesk.Revit.DB.Document.Import()
* Autodesk::Revit::DB::Document::Print
* [Print](1ea1e825-8044-7a27-d9b9-ca463443c3b9.htm)  and similar overloads.
* [SubmitPrint](0c9524b7-33b5-8c76-2843-c7024f03e4d7.htm)  and similar overloads.
* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  and similar overloads.
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

# See Also

[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)