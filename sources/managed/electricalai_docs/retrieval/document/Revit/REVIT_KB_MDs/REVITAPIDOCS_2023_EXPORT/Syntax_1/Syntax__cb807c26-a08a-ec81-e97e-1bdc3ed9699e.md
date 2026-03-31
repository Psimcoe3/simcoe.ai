[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FamilyLoadingIntoDocument Event

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the FamilyLoadingInto event to be notified when Revit is just about to load a family into a document.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public event EventHandler<FamilyLoadingIntoDocumentEventArgs> FamilyLoadingIntoDocument ``` |

 

| Visual Basic |
| --- |
| ``` Public Event FamilyLoadingIntoDocument As EventHandler(Of FamilyLoadingIntoDocumentEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<FamilyLoadingIntoDocumentEventArgs^>^ FamilyLoadingIntoDocument { 	void add (EventHandler<FamilyLoadingIntoDocumentEventArgs^>^ value); 	void remove (EventHandler<FamilyLoadingIntoDocumentEventArgs^>^ value); } ``` |

# Remarks

This event is raised when Revit is just about to load a family into a document.

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

Event is cancellable. To cancel it, call the 'Cancel()' method in event's argument to True. Your application is responsible for providing feedback to the user about the reason for the cancellation.

The following API functions are not available for the current document during this event:

* All overloads of Autodesk.Revit.DB.Document.Import()
* [Close](da2f27b9-7255-4950-82a2-86e1432ff9f0.htm)  and similar overloads.
* [Save](8dec13b6-71f4-45d2-74e3-b109153721b5.htm)  .
* [SaveAs(String)](25c44d4a-b220-5898-b28c-a2cf6a8a8673.htm)  and similar overloads.

Exception  [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)  will be thrown if any of the above methods is called during this event.

Another  [FamilyLoadedIntoDocument](ca1d4dde-b446-d9d4-72a2-c649475eafe5.htm)  event will be raised immediately after family loading is finished.

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)