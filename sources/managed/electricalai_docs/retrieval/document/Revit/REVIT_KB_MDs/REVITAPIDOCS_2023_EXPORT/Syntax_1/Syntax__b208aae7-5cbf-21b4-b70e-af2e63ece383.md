[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ViewActivated Event

---



|  |
| --- |
| [UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the ViewActivated event to be notified immediately after Revit has finished activating a view of a document.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2010

# Syntax

| C# |
| --- |
| ``` public event EventHandler<ViewActivatedEventArgs> ViewActivated ``` |

 

| Visual Basic |
| --- |
| ``` Public Event ViewActivated As EventHandler(Of ViewActivatedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<ViewActivatedEventArgs^>^ ViewActivated { 	void add (EventHandler<ViewActivatedEventArgs^>^ value); 	void remove (EventHandler<ViewActivatedEventArgs^>^ value); } ``` |

# Remarks

This event is raised immediately after Revit has finished activating a view of the document. It is raised even when view activating failed or was cancelled (during ViewActivating event).

Check the 'Status' field in event's argument to see whether the action itself was successful or not.

This event is not cancellable, for the process of view activating has already been finished.

The document may be modified during this event.

The following API functions are not available for the current document during this event:

* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  and similar overloads.
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

# See Also

[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)