[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FloatingRectangle Property

---



|  |
| --- |
| [DockablePaneState Class](0255200b-8af3-3254-ca6b-043f5cc291cf.htm)   [See Also](#seeAlsoToggle) |

When %dockPosition% is Floating, this rectangle determines the size and position of the pane. Coordinates are relative to the upper-left-hand corner of the main Revit window. Note: the returned Rectangle is a copy. In order to change the pane state, you must call SetFloatingRectangle with a modified rectangle.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public Rectangle FloatingRectangle { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property FloatingRectangle As Rectangle 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Rectangle^ FloatingRectangle { 	Rectangle^ get (); } ``` |

# See Also

[DockablePaneState Class](0255200b-8af3-3254-ca6b-043f5cc291cf.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)