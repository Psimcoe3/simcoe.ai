[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### EditorInteraction Property

---



|  |
| --- |
| [DockablePaneProviderData Class](25c4224d-bc54-f2ed-589d-881a6ccbda87.htm)   [See Also](#seeAlsoToggle) |

Defines the interaction this pane has with the Active Editor when the pane becomes active.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public EditorInteraction EditorInteraction { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property EditorInteraction As EditorInteraction 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property EditorInteraction^ EditorInteraction { 	EditorInteraction^ get (); 	void set (EditorInteraction^ value); } ``` |

# Remarks

Set to KeepAlive to keep the current editor active and keep active the current selection or Dismiss to dismiss the Editor and clear the active selection. Default is to KeepAlive the current editor.

# See Also

[DockablePaneProviderData Class](25c4224d-bc54-f2ed-589d-881a6ccbda87.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)