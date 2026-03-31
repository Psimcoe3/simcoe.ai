[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SelectionChanged Event

---



|  |
| --- |
| [UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the SelectionChanged event to be notified after the selection was changed.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public event EventHandler<SelectionChangedEventArgs> SelectionChanged ``` |

 

| Visual Basic |
| --- |
| ``` Public Event SelectionChanged As EventHandler(Of SelectionChangedEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<SelectionChangedEventArgs^>^ SelectionChanged { 	void add (EventHandler<SelectionChangedEventArgs^>^ value); 	void remove (EventHandler<SelectionChangedEventArgs^>^ value); } ``` |

# Remarks

This event is raised after the selection was changed in the current document. Handlers of this event are forbidden to make modifications to the current document. Handlers of this event are forbidden to change the selection to the current document. It is not allowed to open a new transaction in the active document when handling this event.

# See Also

[UIControlledApplication Class](4638c568-a118-1d57-ceed-a57595202644.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)