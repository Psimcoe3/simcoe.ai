---
created: 2026-01-28T21:27:02 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_Hello_World_for_VB_NET_Add_Reference_and_Namespace_html
author: 
---

# Help | Add Reference and Namespace | Autodesk

> ## Excerpt
> VB.NET uses a process similar to C#. After you create the Hello World project, complete the following steps:

---
VB.NET uses a process similar to C#. After you create the Hello World project, complete the following steps:

1.  Right-click on References under the project name in the Solution Explorer to display a context menu.
    
2.  From the context menu, select Add Reference to open the Reference Manager dialog box. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/VBAddReferences.png)**Figure: Reference Manager**
    
3.  In the Reference Manager dialog box, click the Browse tab, then click the Browse button.
    
4.  Locate the folder where Revit is installed and click the RevitAPI.dll. For example, the installed folder location might be C:\\Program Files\\Autodesk\\Revit 2018.
    
5.  Click OK to add the reference.
    
6.  Repeat steps above to add a reference to RevitAPIUI.dll, which is in the same folder as Revit API.dll.
    
    ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-7B4CFEF2-7EE6-40E1-984B-4B89A6E946C5-low.png)
    
    **Figure: Add references**
    
7.  Click OK to close the Reference Manager dialog.
    
8.  To complete the process, click RevitAPI under References in the Solution Explorer. Set Copy Local to False in the Properties frame. Repeat for RevitAPIUI.
