---
created: 2026-01-28T20:38:20 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/previous-versions/e9zazcx5(v=vs.140)?redirectedfrom=MSDN
author: 
---

# Walkthrough: Creating Managed Satellite DLLs | Microsoft Learn

> ## Excerpt
> In vs_dev12, add-ins are deprecated. We recommend that you upgrade your add-ins to VSPackage extensions. For more information about how to upgrade, see FAQ: Converting Add-ins to VSPackage Extensions.

---
___

#### Share via

___

In vs\_dev12, add-ins are deprecated. We recommend that you upgrade your add-ins to VSPackage extensions. For more information about how to upgrade, see [FAQ: Converting Add-ins to VSPackage Extensions](https://msdn.microsoft.com/en-us/library/dn246938(v=vs.140)).

Satellite DLLs are useful for storing resource files, for example, icons, bitmaps, and resource strings, in a centralized location for use in add-ins and other automation projects. Satellite DLLs can be reused by other projects or add-ins. Furthermore, separating the strings and other resources from your add-in makes it easier to make centralized changes or localize the resources into different languages.

Earlier versions of Visual Studio used registry entries for SatelliteDllPath and SatelliteDllName. However, registry entries are now superseded by entries in the .addin registration file. When you require a resource in your project, you load the add-in and Visual Studio queries it for the satellite DLL. Consequently, you do not have to hard-code a resource path. Also, instead of using the #id method to specify a resource ID, you use @resource name (where resource name is the name of your resource, for example, @Icon1 or @String1), The @ symbol tells Visual Studio to look in the satellite DLL for the resource.

## Create Managed Satellite DLLs

The following steps show how to create a satellite DLL that contains icon and string resources, and how to modify an add-in to access those resources. It uses an add-in that has an **About** dialog box, which requires icon and string resources. Typically, if you create an add-in that has an **About** dialog box, a default icon and text are provided. The following steps also show how to replace the default icon and text by using your own.

### To create a managed satellite DLL

1.  On the **File** menu, click **New**, and then click **Project**.
    
2.  In the **New Project** dialog box, expand **Other Project Types** and then select **Extensibility Projects**.
    
3.  In the **Templates** pane, select **Visual Studio Add-in**.
    
4.  Follow the directions in the Visual Studio Add-in Wizard. On the **Choosing 'Help About' Information** page, select **Yes, I would like my Add-in to offer 'About' box information**. Accept the remaining default selections.
    
5.  On the **Project** menu, click **Add Reference**.
    
6.  On the **.NET** tab, click System.Drawing, and then click **OK**.
    
7.  Right-click the add-in project in **Solution Explorer**, click **Add**, and then click **New Item**.
    
8.  Select **Resources File** in the Templates list and click **Add**. Accept its default name (Resources1.resx).
    
    By default, this creates a resource file named Resource1.resx and starts the Visual Studio **Resource Editor**.
    
9.  In Resource1.resx, select **Icons** on the **Strings** list (the left-most button at the top).
    
10.  In the **Add Resource** list, click **Add New Icon**. For now, leave the default name (Icon1.bmp) and click **Add**.
    
    Alternatively, you can select an existing bitmap image for the icon, as long as it is 16 x 16 pixels and either 16 Color or True Color.
    
11.  After the icon opens in the **Icon Editor**, use the tools to modify it. When you are done, close the **Icon Editor** and save your changes.
    
12.  Select **Add New String** on the **Add Resource** list.
    
13.  Click the first box in the **Name** column.
    
    This creates a default string resource named String1.
    
14.  Type Line one in the **Value** box.
    
    This is the value for the first string resource.
    
15.  Create two more string resources, and name them "Line two" and "Line three".
    
16.  Close the **Resource Editor** and save the changes.
    
17.  In **Solution Explorer**, right-click Resource1.resx and then click **Properties**.
    
18.  In the **Properties** window, change **Build Action** from **Embedded Resource** to **None**.
    
    This prevents the resource from being built into the add-in assembly.
    
19.  Build the project.
    
20.  Create the satellite resource DLL. This is done in a two-step process by using ResGen and then AL (Assembly Linker) to build the satellite DLL.
    
    1.  Click **Start**, **All Programs**, **Microsoft Visual Studio 2010**, **Visual Studio Tools**, and then click **Microsoft Visual Studio Command Prompt (2010)**.
        
        This sets certain environment variables so that you can more easily reference Visual Studio tools.
        
    2.  At the command prompt, go to the folder that contains the .resx file and type **Resgen Resource1.resx**.
        
        Resgen is a utility that compiles the specified .resx file into a .resources file. For more information, see [Resgen.exe (Resource File Generator)](https://msdn.microsoft.com/en-us/library/ccec7sz1(v=vs.140)).
        
    3.  At the command prompt, type **AL.exe /embed:Resource1.resources /culture:en-US /out:**Add-In Name**.resources.dll**.
        
        Replace Add-In Name by using the name of your add-in. For example, if your add-in project is named MyAddin, then the **/out:** switch would be **/out:MyAddin.resources.dll**. The **/out:** name must match the name of your project; otherwise, the resource DLL will not be found.
        
        AL.exe (Assembly Linker) converts the specified .resources file into a DLL that you can reference in your add-in. (You can change the **/culture** switch to a language other than English.) For more information, see [Al.exe (Assembly Linker)](https://msdn.microsoft.com/en-us/library/c405shex(v=vs.140)).
        
21.  In File Explorer, browse to the DLL directory of the add-in and create a folder named \\en-US\\ (for English US, because you typed en-US as the culture value in AL.exe).
    
22.  Copy the Add-In Name.resources.dll file to the new \\en-US\\ folder.
    
23.  In File Explorer, browse to the \\Addins\\ directory, typically ..\\Documents and Settings\\user name\\My Documents\\Visual Studio 2010\\Addins\\.
    
24.  Modify the Visual Studio add-in definition file as follows:
    
    1.  Right-click the add-in definition file for your add-in, click **Open With**, and then click **Note Pad**.
        
    2.  Replace the following tags:
        
        ```
            <FriendlyName>@String1</FriendlyName>
            <Description>@String2</Description>
            <AboutBoxDetails>@String3</AboutBoxDetails>
            <AboutIconData>@Icon1</AboutIconData>
        ```
        
        The Friendlyname entry renames your add-in to Line1, which is what you entered for String1 in the Resource1.resx file. The Description in the **About** dialog box now contains "Line2", and the AboutIconData entry matches the icon you created for the **About** dialog box.
        
    3.  Insert .resources before the extension of the assembly name.
        
25.  Rebuild the project and select the add-in in **Add-in Manager**.
    
26.  On the **Help** menu, click **About Microsoft Visual Studio** and select **Line1** (the name of your add-in) in the list.
    
    The custom icon and the three strings that you created are displayed.
    

## See Also

#### Tasks

[How to: Access Resources in Satellite DLLs](https://learn.microsoft.com/en-us/previous-versions/ms165653(v=vs.140))

#### Concepts

[Add-In Registration](https://learn.microsoft.com/en-us/previous-versions/19dax6cz(v=vs.140))
