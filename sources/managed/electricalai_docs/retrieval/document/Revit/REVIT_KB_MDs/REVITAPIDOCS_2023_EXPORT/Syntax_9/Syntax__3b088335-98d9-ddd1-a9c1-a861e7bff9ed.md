[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FrameworkElement Property

---



|  |
| --- |
| [DockablePaneProviderData Class](25c4224d-bc54-f2ed-589d-881a6ccbda87.htm)   [See Also](#seeAlsoToggle) |

The Windows Presentation Framework object containing the pane's user interface.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public FrameworkElement FrameworkElement { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property FrameworkElement As FrameworkElement 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property FrameworkElement^ FrameworkElement { 	FrameworkElement^ get (); 	void set (FrameworkElement^ value); } ``` |

# Remarks

Using a System.Windows.Controls.Page is recommended. This can be null, in which case it is assumed an IFrameworkElementCreator is provided to create the element on demand.

# See Also

[DockablePaneProviderData Class](25c4224d-bc54-f2ed-589d-881a6ccbda87.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)