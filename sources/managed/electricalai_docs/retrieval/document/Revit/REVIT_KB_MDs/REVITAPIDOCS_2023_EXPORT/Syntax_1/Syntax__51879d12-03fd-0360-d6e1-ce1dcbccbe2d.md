[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DocumentWorksharingEnabled Event

---



|  |
| --- |
| [Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)   [See Also](#seeAlsoToggle) |

Subscribe to the DocumentWorksharingEnabled event to be notified when a document has become workshared.

**Namespace:**   [Autodesk.Revit.ApplicationServices](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public event EventHandler<DocumentWorksharingEnabledEventArgs> DocumentWorksharingEnabled ``` |

 

| Visual Basic |
| --- |
| ``` Public Event DocumentWorksharingEnabled As EventHandler(Of DocumentWorksharingEnabledEventArgs) ``` |

 

| Visual C++ |
| --- |
| ``` public:  event EventHandler<DocumentWorksharingEnabledEventArgs^>^ DocumentWorksharingEnabled { 	void add (EventHandler<DocumentWorksharingEnabledEventArgs^>^ value); 	void remove (EventHandler<DocumentWorksharingEnabledEventArgs^>^ value); } ``` |

# Remarks

This event is raised when Revit has just enabled worksharing in the document.

Handlers of this event are permitted to make modifications to any document (including the active document), except for documents that are currently in read-only mode.

# See Also

[Application Class](94db8ea8-d2c3-5e71-8030-466bcb8e4426.htm)

[Autodesk.Revit.ApplicationServices Namespace](91957e18-2935-006c-83ab-3b5b9dbb5928.htm)