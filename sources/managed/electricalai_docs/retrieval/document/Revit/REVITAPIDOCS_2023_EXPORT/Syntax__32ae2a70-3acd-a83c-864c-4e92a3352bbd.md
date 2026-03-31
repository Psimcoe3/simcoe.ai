[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PaneIsBuiltIn Method

---



|  |
| --- |
| [DockablePane Class](671f5ed0-09af-face-532f-72d214131cda.htm)   [See Also](#seeAlsoToggle) |

Returns true if %id% refers to a built-in Revit dockable pane, rather than one created by an add-in.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool PaneIsBuiltIn( 	DockablePaneId id ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function PaneIsBuiltIn ( _ 	id As DockablePaneId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool PaneIsBuiltIn( 	DockablePaneId^ id ) ``` |

#### Parameters

id
:   Type:  [Autodesk.Revit.UI DockablePaneId](96149d8e-6393-9285-a721-76470e6c15b8.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DockablePane Class](671f5ed0-09af-face-532f-72d214131cda.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)