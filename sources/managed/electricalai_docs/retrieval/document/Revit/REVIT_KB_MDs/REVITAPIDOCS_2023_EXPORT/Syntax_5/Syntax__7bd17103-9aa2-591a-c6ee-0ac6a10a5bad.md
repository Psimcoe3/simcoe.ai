[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### InitialState Property

---



|  |
| --- |
| [DockablePaneProviderData Class](25c4224d-bc54-f2ed-589d-881a6ccbda87.htm)   [See Also](#seeAlsoToggle) |

The initial position of the docking pane.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public DockablePaneState InitialState { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property InitialState As DockablePaneState 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property DockablePaneState^ InitialState { 	DockablePaneState^ get (); 	void set (DockablePaneState^ value); } ``` |

# Remarks

This position will be used for the first Revit session in which the pane is registered; afterwards, the user is free to reposition the pane, and the user's saved position will be remembered in future sessions.

# See Also

[DockablePaneProviderData Class](25c4224d-bc54-f2ed-589d-881a6ccbda87.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)