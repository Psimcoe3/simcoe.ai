---
created: 2026-01-28T20:39:12 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/previous-versions/7k3w6w59(v=vs.140)
author: 
---

# Walkthrough: Creating a Wizard | Microsoft Learn

> ## Excerpt
> In Visual Studio 2013, add-ins are deprecated. We recommend that you upgrade your add-ins to VSPackage extensions. For more information about how to upgrade, see FAQ: Converting Add-ins to VSPackage Extensions.

---
___

#### Share via

___

In Visual Studio 2013, add-ins are deprecated. We recommend that you upgrade your add-ins to VSPackage extensions. For more information about how to upgrade, see [FAQ: Converting Add-ins to VSPackage Extensions](https://msdn.microsoft.com/en-us/library/dn246938(v=vs.140)).

Wizards, such as the **Add-in Wizard**, are programs that lead a user through a series of actions to accomplish a complex, repetitive, or difficult task. Windows, for example, uses wizards to connect to network resources, connect to printers, and so forth.

In Visual Studio, wizards generally ask a series of questions that solicit input from a user, and then use the results to generate code. Wizards, however, do not always display a user interface (UI). They can be programmed to invisibly generate code behind the scenes.

There are three different kinds of wizards.

-   **New Project wizards**—As the name suggests, these wizards are used to generate new code for a particular type of project, giving the user a starting point from which to add their own code. This is the most commonly used type of wizard.
    
-   **Add New Item wizards**—These wizards are used to add new items, such as Web forms, text files, HTML pages, XML pages, and so forth, to a project.
    
-   **Custom wizards**—These wizards are not called from a dialog box. Instead they are called directly from add-ins, macros, or other types of code. They may or may not display a UI. In either case, they generate code. This type of wizard is used the least often.
    

Regardless of the kind of wizard, they all have common traits.

-   They are .NET objects that implement the [IDTWizard](https://msdn.microsoft.com/en-us/library/feb3h5ea(v=vs.140)) interface and have an associated method, [Execute](https://msdn.microsoft.com/en-us/library/ehf2zfa2(v=vs.140)), which contains the code you want the wizard to run.
    
-   They all use a .vsz file to display themselves in Visual Studio.
    
-   They all generate code or perform some other task.
    

You can customize the appearance of elements in wizards that you create. Wizards most often consist of one or more windows, or pages. Pages can contain a descriptive image, such as on the top or to the left side of the page, a label description, instructions, and an area in which navigation controls such as **Next** and **Previous** can be placed.

The process for creating wizards in Visual C++ is a bit different from creating standard Visual Studio wizards. For additional information about how to create wizards targeted to Visual C++, see [Designing a Wizard](https://learn.microsoft.com/en-us/previous-versions/96xz4cw2(v=vs.140)) and [Creating a Custom Wizard](https://learn.microsoft.com/en-us/previous-versions/bhceedxx(v=vs.140)).

Note

Your computer might show different names or locations for some of the Visual Studio user interface elements in the following instructions. The Visual Studio edition that you have and the settings that you use determine these elements. For more information, see [Customizing Development Settings in Visual Studio](https://learn.microsoft.com/en-us/previous-versions/zbhkx167(v=vs.140)).

## An Example of a Basic Wizard

![Visual Studio Add In Wizard](https://learn.microsoft.com/en-us/previous-versions/images/7k3w6w59.vxadd-inwizardpanel(vs.140).gif "Visual Studio Add In Wizard")

This picture shows a panel of the **Add-In Wizard**, a new-project type of wizard that leads you through a series of steps to create an add-in. You can customize the appearance of your wizards, but the **Add-In Wizard** is a good example of the style of a standard type of wizard. Completed wizards become available templates in the **New Project** or **Add New Item** dialog box.

The following demonstrates how to create a basic wizard and optionally give it a custom icon.

### To create a basic wizard in Visual Basic and Visual C#

1.  Run Visual Studio as an Administrator. Registering the wizard requires updating the registry, so it needs this privilege.
    
2.  Create a new Class Library project named MyNewWizard.
    
3.  Add references to [EnvDTE](https://msdn.microsoft.com/en-us/library/k3dys0y2(v=vs.140)) and [EnvDTE80](https://msdn.microsoft.com/en-us/library/0e105c68(v=vs.140)) to the project.
    
    To do this, right-click the project and click **Add**, **Reference**. On the .NET tab of the **Reference** dialog box, click EnvDTE and EnvDTE80 and then click **OK**.
    

In the class module, include references to [EnvDTE](https://msdn.microsoft.com/en-us/library/k3dys0y2(v=vs.140)) and [EnvDTE80](https://msdn.microsoft.com/en-us/library/0e105c68(v=vs.140)) and implement the [IDTWizard](https://msdn.microsoft.com/en-us/library/feb3h5ea(v=vs.140)) interface. For this Visual C# example, you must also add a reference to **System.Windows.Forms** and **System.Runtime.InteropServices**.

```
Imports EnvDTE 
Imports EnvDTE80
Public Class Class1
    Implements IDTWizard
```

using System.Runtime.InteropServices;

```
namespace MyNewWizard
{
```

\[ComVisible(true)\]

\[Guid("20184B81-7C38-4E02-A1E3-8D564EEC2D25"),

ProgId("MyNewWizard.Class1")\]

```
    public class Class1 : IDTWizard
    {
    }
}
```

When you add the **Implements** statement to Visual Basic, position the cursor at the end of the line and press enter to automatically create an **Execute** method procedure. For Visual C#, however, you must add the **Execute** procedure manually:

```
public class Class1 : IDTWizard
    {
    public void Execute(object Application,  
        int hwndOwner, ref object[] contextParams,  
        ref object[] customParams,  
        ref EnvDTE.wizardResult retval)
```

1.  Add the code you want the wizard to run to the **Execute** procedure. For this example, we will just add a simple message box.
    
    You should have the following:
    
    ```
    Imports EnvDTE
    Imports EnvDTE80
    
    Public Class Class1
        Implements IDTWizard
    
        Public Sub Execute(ByVal Application As Object, ByVal _
        hwndOwner As Integer, ByRef ContextParams() As Object, ByRef _
        CustomParams() As Object, ByRef retval As EnvDTE.wizardResult) _
        Implements EnvDTE.IDTWizard.Execute
            MsgBox("The wizard is now running.")
        End Sub
    End Class 
    ```
    
    The **Execute** procedure is called when the wizard is started.
    
2.  Right-click your project in **Solution Explorer** and click **Properties** to open the **Project Properties** page, click the **Build** tab, and then check the **Register for COM interop** box at the bottom of the page.
    
3.  In the AssemblyInfo.cs file, find the **ComVisible** attribute and set it to true.
    
4.  Build the project to create the class library .dll by clicking **Build Solution** on the **Build** menu.
    
5.  Create a .vsz text file for the wizard named MyNewWizard.vsz.
    
    To do this, make a copy of an existing .vsz file, such as any of those located at <Visual Studio Install Directory>\\VC#\\CSharpProjectItems\\Windows Forms, and rename it "MyNewWizard.vsz".
    
    A .vsz file is a text file that enables Visual Studio to recognize the wizard and display it in the **New Project** or **Add New Item** dialog box. The Wizard parameter should be set to the progID (Project.Classname) of the project or the GUID. For more information, see [Configuring .Vsz Files to Start Wizards](https://learn.microsoft.com/en-us/previous-versions/b48hhx46(v=vs.140)).
    
6.  Replace the contents of MyNewWizard.vsz with the following:
    
    ```
    VSWizard 7.0
    Wizard=MyNewWizard.Class1
    Param=First Item
    Param=Second Item
    ```
    
7.  Save the new .vsz file in the directory where you want the wizard to appear.
    
    For this example, we want the wizard to appear in the **Add New Item** dialog box for Visual Basic projects, so save the .vsz file in the following directory: <Visual Studio Install Directory>\\VB\\VBProjectItems.
    
8.  Exit Visual Studio and then restart it.
    
    This forces Visual Studio to read the new .vsz file.
    
9.  Create a new Visual Basic project, such as a Windows Application project.
    
10.  Right-click the project, point to **Add**, and then click **New Item**.
    
    You should see your new wizard (MyNewWizard) in the **Add New Items** dialog box.
    
11.  Click the wizard and click the **Add** button.
    
    You see the message, "The wizard is now running."
    

### To display a custom icon for the new wizard

-   Place an icon file with the same base file name as the .dll file but with an .ico extension in the same directory as the wizard file.
    
    For example, if the wizard is named MyNewWizard.dll, name the .ico file MyNewWizard.ico.
    
    \-or-
    
-   If you have created a VSDir file, specify a path to the icon (.ico) file there.
    

## See Also

#### Tasks

[How to: Create an Add-In](https://learn.microsoft.com/en-us/previous-versions/80493a3w(v=vs.140))

#### Reference

[IDTWizard](https://msdn.microsoft.com/en-us/library/feb3h5ea(v=vs.140))

[PAVE Visual Studio Commands and Switches](https://learn.microsoft.com/en-us/previous-versions/kcc7tke7(v=vs.140))

#### Concepts

[Automation Object Model Chart](https://learn.microsoft.com/en-us/previous-versions/za2b25t3(v=vs.140))

[Adding Wizards to the Add Item and New Project Dialog Boxes by Using .Vsdir Files](https://learn.microsoft.com/en-us/previous-versions/2sc7ft4a(v=vs.140))

[Configuring .Vsz Files to Start Wizards](https://learn.microsoft.com/en-us/previous-versions/b48hhx46(v=vs.140))

#### Other Resources

[Creating Add-ins and Wizards](https://learn.microsoft.com/en-us/previous-versions/5abkeks7(v=vs.140))
