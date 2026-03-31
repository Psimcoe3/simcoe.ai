---
created: 2026-01-28T21:27:02 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_Hello_World_for_VB_NET_Debug_the_Program_html
author: 
---

# Help | Debug the Program | Autodesk

> ## Excerpt
> Running a program in Debug mode uses breakpoints to pause the program so that you can examine the state of variables and objects. If there is an error, you can check the variables as the program runs to deduce why the value is not what you might expect.

---
Running a program in Debug mode uses breakpoints to pause the program so that you can examine the state of variables and objects. If there is an error, you can check the variables as the program runs to deduce why the value is not what you might expect.

1.  In the Solution Explorer window, right-click the HelloWorld project to display a context menu.
    
2.  From the context menu, click Properties. The Properties window appears.
    
3.  Click the Debug tab.
    
4.  In the Debug window Start Action section, click Start external program and browse to the Revit.exe file. By default, the file is located at the following path, C:\\Program Files\\Autodesk\\Revit 20XX\\Revit.exe.
    
    ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-C132F87F-23E3-4199-A50C-0BC6AFB09892-low.png)
    

**Figure 175: Set Debug environment**

5.  From the Debug menu, select Toggle Breakpoint (or press F9) to set a breakpoint on the following line.

#### Code Region 30-11: TaskDialog

```
TaskDialog.Show("Revit", "Hello World")
```

6.  Press F5 to start the debug procedure.
    
7.  Test the debugging
    
    -   On the Add-Ins tab, HelloWorld appears in the External Tools menu-button.
        
        ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-20A02118-E891-4D76-A7E6-E3D670C4A017-low.png)
        
    -   _Figure 176: HelloWorld External Tools command\*_
        
    -   Click HelloWorld to execute the program, activating the breakpoint.
        
    -   Press F5 to continue executing the program. The following system message appears.
        
        ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-2C537699-4312-459B-A8E4-224F8C7C163A-low.png)
        
    -   _Figure 177: TaskDialog message\*_
