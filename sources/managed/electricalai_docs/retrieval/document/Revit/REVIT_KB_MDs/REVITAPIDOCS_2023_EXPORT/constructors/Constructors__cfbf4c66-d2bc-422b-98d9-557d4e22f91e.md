[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DockablePane Members

---



|  |
| --- |
| [DockablePane Class](671f5ed0-09af-face-532f-72d214131cda.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [DockablePane](671f5ed0-09af-face-532f-72d214131cda.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [DockablePane(DockablePane)](e957aebc-c7ab-c784-c3ab-33c0e79d16ce.htm) | Constructs a new copy of the input DockablePane object. |
| Public method | [DockablePane(DockablePaneId)](ce2c0837-4700-1990-0c89-73d49a3db889.htm) | Gets the pane with identifier %id%. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](0b2603ee-5d51-fd12-0af9-ccfa907d2667.htm) | Releases all resources used by the  [DockablePane](671f5ed0-09af-face-532f-72d214131cda.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetTitle](1c33c74a-d6fe-abd6-4bed-10034d447e95.htm) | Returns the current title (a.k.a. window caption) of the dockable pane. |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [Hide](b7e07918-5431-1af5-cc86-ce0569dc3f6b.htm) | If the pane is on screen, hide it. Has no effect on built-in Revit dockable panes. |
| Public method | [IsShown](bdf835cc-4bf1-2b78-4b3c-d807fedbbde3.htm) | Identify the pane is currently visible or in a tab. |
| Public method Static member | [PaneExists](113303aa-57ec-67d2-a5aa-76a1ad7ebeea.htm) | Returns true if %id% refers to a dockable pane window that currently exists in the Revit user interface, whether it's hidden or shown. |
| Public method Static member | [PaneIsBuiltIn](32ae2a70-3acd-a83c-864c-4e92a3352bbd.htm) | Returns true if %id% refers to a built-in Revit dockable pane, rather than one created by an add-in. |
| Public method Static member | [PaneIsRegistered](058ac1e7-900e-f310-e17a-d1eba04976e0.htm) | Returns true if %id% refers to a built-in Revit dockable pane, or an add-in pane that has been properly registered with %Autodesk.Revit.UI.UIApplication.RegisterDockablePane%. |
| Public method | [Show](023ec0ac-85aa-1ec3-fb0f-9747db237e2a.htm) | If the pane is not currently visible or in a tab, display the pane in the Revit user interface at its last docked location. |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Id](059e1c8a-9cf3-fa10-bc51-54f9c61f39a5.htm) | The unique identifier for this dockable pane. |
| Public property | [IsValidObject](8e530ce4-2422-84da-4519-46312a8143b7.htm) | Specifies whether the .NET object represents a valid Revit entity. |

# See Also

[DockablePane Class](671f5ed0-09af-face-532f-72d214131cda.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)