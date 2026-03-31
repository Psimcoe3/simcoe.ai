[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DockablePaneState Members

---



|  |
| --- |
| [DockablePaneState Class](0255200b-8af3-3254-ca6b-043f5cc291cf.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [DockablePaneState](0255200b-8af3-3254-ca6b-043f5cc291cf.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [DockablePaneState](a0cd9042-b64c-75ff-c45c-d0cb9db80c06.htm) | Creates a new DockablePaneState object. |
| Public method | [DockablePaneState(DockablePaneState)](58c79873-9e2c-b9ac-2c5d-a3cf5538c90a.htm) | Constructs a new copy of the input DockablePaneState object. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Dispose](68833347-063e-c708-5b6b-c12dec4efc5a.htm) | Releases all resources used by the  [DockablePaneState](0255200b-8af3-3254-ca6b-043f5cc291cf.htm) |
| Public method | Equals | Determines whether the specified  Object  is equal to the current  Object  . (Inherited from  Object  .) |
| Public method | GetHashCode | Serves as a hash function for a particular type. (Inherited from  Object  .) |
| Public method | GetType | Gets the  Type  of the current instance. (Inherited from  Object  .) |
| Public method | [SetFloatingRectangle](0dda1168-e11a-a276-1535-74c64c677c4c.htm) | When %dockPosition% is Floating, sets the rectangle used to determine the size and position of the pane when %dockPosition% is Floating. Coordinates are relative to the upper-left-hand corner of the main Revit window. |
| Public method | ToString | Returns a string that represents the current object. (Inherited from  Object  .) |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [DockPosition](3d87dd54-a970-c09b-c113-d2e700cd2f0f.htm) | Which part of the Revit application frame the pane should dock to. |
| Public property | [FloatingRectangle](d1dcb64c-2f08-d2a6-ddc7-01c76c1a6a59.htm) | When %dockPosition% is Floating, this rectangle determines the size and position of the pane. Coordinates are relative to the upper-left-hand corner of the main Revit window. Note: the returned Rectangle is a copy. In order to change the pane state, you must call SetFloatingRectangle with a modified rectangle. |
| Public property | [IsValidObject](9a1720f3-3bd2-61ae-37d6-0b1ca8104d30.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| Public property | [MinimumHeight](09e43d6f-77c2-0c81-654a-47a135280d43.htm) | When %dockPosition% is anything other than floating, the minimum height to use for the pane. Default is 200 pixels. |
| Public property | [MinimumWidth](f22b8f98-87c8-7a8f-45c7-5d8b67034a14.htm) | When %dockPosition% is anything other than floating, the minimum width to use for the pane. Default is 200 pixels. |
| Public property | [TabBehind](05fde7c9-8b43-bb29-e37f-0386a00b2525.htm) | Ignored unless %dockPosition% is Tabbed. The new pane will appear in a tab behind the specified existing pane ID. |

# See Also

[DockablePaneState Class](0255200b-8af3-3254-ca6b-043f5cc291cf.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)