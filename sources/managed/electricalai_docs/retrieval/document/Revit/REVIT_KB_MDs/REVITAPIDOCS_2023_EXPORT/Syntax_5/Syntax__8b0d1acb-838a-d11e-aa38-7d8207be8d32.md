[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RegisterDockablePane Method

---



|  |
| --- |
| [UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)   [See Also](#seeAlsoToggle) |

Adds a new dockable pane to the Revit user interface.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 19.0.0.0 (19.0.0.405)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void RegisterDockablePane( 	DockablePaneId id, 	string title, 	IDockablePaneProvider provider ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub RegisterDockablePane ( _ 	id As DockablePaneId, _ 	title As String, _ 	provider As IDockablePaneProvider _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void RegisterDockablePane( 	DockablePaneId^ id,  	String^ title,  	IDockablePaneProvider^ provider ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.UI DockablePaneId](96149d8e-6393-9285-a721-76470e6c15b8.htm)    
     Unique identifier for the new pane.

title
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     String to use for the pane caption.

provider
:   Type:  [Autodesk.Revit.UI IDockablePaneProvider](cde36571-ccf1-f628-9e34-6a720388d348.htm)    
     Your add-in's implementation of the IDockablePaneProvider interface.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if a dockable pane with identifier %id% has already been registered. |

# See Also

[UIApplication Class](51ca80e2-3e5f-7dd2-9d95-f210950c72ae.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)