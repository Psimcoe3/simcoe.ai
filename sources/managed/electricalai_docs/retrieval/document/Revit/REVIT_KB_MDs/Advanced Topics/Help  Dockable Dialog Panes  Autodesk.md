---
created: 2026-01-28T21:16:44 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dockable_Dialog_Panes_html
author: 
---

# Help | Dockable Dialog Panes | Autodesk

> ## Excerpt
> Since Revit 2013, applications have been able to use modeless dialogs by taking advantage of the Idling Event and the External Events class in the Revit API. Add-ins requiring modeless dialogs also have the option to use dockable modeless dialogs. Similar to standard modeless dialogs, dockable dialogs are registered Windows Presentation Foundation (WPF) dialog panes that participate in Revit's window docking system. A registered dockable pane can dock into the top, left, right, and bottom of the main Revit window, as well as be added as a tab to an existing system pane, such as the project browser. Additionally, dockable panes can float, behaving much like a standard modeless dialog.

---
Since Revit 2013, applications have been able to use modeless dialogs by taking advantage of the [Idling Event](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Events_User_Inteface_Events_html) and the [External Events](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_External_Events_html) class in the Revit API. Add-ins requiring modeless dialogs also have the option to use dockable modeless dialogs. Similar to standard modeless dialogs, dockable dialogs are registered Windows Presentation Foundation (WPF) dialog panes that participate in Revit's window docking system. A registered dockable pane can dock into the top, left, right, and bottom of the main Revit window, as well as be added as a tab to an existing system pane, such as the project browser. Additionally, dockable panes can float, behaving much like a standard modeless dialog.

### IDockablePaneProvider

Registering a dockable pane requires an instance of the IDockablePaneProvider interface. The SetupDockablePane() method of this interface is called during initialization of the Revit user interface to gather information about add-in dockable pane windows. SetupDockablePane() has one parameter of type DockablePaneProviderData, which is a container for information about the new dockable pane.

Implementations of the IDockablePaneProvider interface should set the FrameworkElement and InitialState properties of DockablePaneProviderData. The FrameworkElement property is the Windows Presentation Framework object containing the pane's user interface.

Note: It is recommended that the dockable dialog in the add-in be the class that implements IDockablePaneProvider and that it be subclassed from System.Windows.Controls.Page.

The InitialState property is the initial position and settings of the docking pane, indicated by the DockablePaneState class. The pane's DockPosition can be Top, Bottom, Left, Right, Floating or Tabbed. If the position is Tabbed, the DockablePaneState.TabBehind property can be used to specify which pane the new pane will appear behind. If the position is Floating, the DockablePaneState.FloatingRectangle property contains the rectangle that determines the size and position of the pane.

### DockablePane

To access a dockable pane during runtime, it needs to be registered by calling the UIApplication.RegisterDockablePane() method. This method requires a unique identifier for the new pane (DockablePaneId), a string specifying the caption for the pane, and an implementation of the IDockablePaneProvider interface.

Dockable panes can be accessed by calling UIApplication.GetDockablePane() and passing in the unique DockablePaneId.This method returns a DockablePane. DockablePane.Show() will display the pane in the Revit user interface at its last docked location, if not currently visible. DockablePane.Hide() will hide a visible dockable pane. However, it has no effect on built-in Revit dockable panes.
