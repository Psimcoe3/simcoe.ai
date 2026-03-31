---
created: 2026-01-28T20:35:31 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | Walkthrough: Add Hello World Ribbon Panel | Autodesk

> ## Excerpt
> In the Walkthrough: Hello World section you learn how to create an add-in application and invoke it in Revit. You also learn to create a .addin manifest file to register the add-in application as an external tool. Another way to invoke the add-in application in Revit is through a custom ribbon panel.

---
In the Walkthrough: Hello World section you learn how to create an add-in application and invoke it in Revit. You also learn to create a .addin manifest file to register the add-in application as an external tool. Another way to invoke the add-in application in Revit is through a custom ribbon panel.

### Create a New Project

Complete the following steps to create a new project:

1.  Create a C# project in Visual Studio using the Class Library template.
    
2.  Type AddPanel as the project name.
    
3.  Add references to the RevitAPI.dll and RevitAPIUI.dll using the directions in the previous walkthrough, Walkthrough: Hello World.
    
4.  Add the PresentationCore reference:
    
    -   In the Solution Explorer, right-click References to display a context menu.
    -   From the context menu, click Add Reference. The Add Reference dialog box appears.
    -   In the Add Reference dialog box, click the .NET Tab.
    -   From the Component Name list, select PresentationCore.
    -   Click OK to close the dialog box. PresentationCore appears in the Solution Explorer reference tree. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-457989F8-C552-4351-9CD9-E7C94942602F-low.png)**Figure 8: Add Reference**
5.  Add the WindowsBase reference as well as System.Xaml following similar steps as above.
    

### Change the Class Name

To change the class name, complete the following steps:

1.  In the class view window, right-click Class1 to display a context menu.
2.  From the context menu, select Rename and change the class' name to CsAddPanel.
3.  In the Solution Explorer, right-click the Class1.cs file to display a context.
4.  From the context menu, select Rename and change the file's name to CsAddPanel.cs.
5.  Double click CsAddPanel.cs to open it for editing.

### Add Code

The Add Panel project is different from Hello World because it is automatically invoked when Revit runs. Use the IExternalApplication interface for this project. The IExternalApplication interface contains two abstract methods, OnStartup() and OnShutdown(). For more information about IExternalApplication, refer to [Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html).

Add the following code to the file:

#### Code Region 2-5: Adding a ribbon panel

```
using System;
using System.Reflection;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System.Windows.Media.Imaging;

namespace Walkthrough
{
   /// <remarks>
   /// This application's main class. The class must be Public.
   /// </remarks>
   public class CsAddPanel : IExternalApplication
   {
      // Both OnStartup and OnShutdown must be implemented as public method
      public Result OnStartup(UIControlledApplication application)
      {
         // Add a new ribbon panel
         RibbonPanel ribbonPanel = application.CreateRibbonPanel("NewRibbonPanel");

         // Create a push button to trigger a command add it to the ribbon panel.
         string thisAssemblyPath = Assembly.GetExecutingAssembly().Location;
         PushButtonData buttonData = new PushButtonData("cmdHelloWorld",
            "Hello World", thisAssemblyPath, "Walkthrough.HelloWorld");

         PushButton pushButton = ribbonPanel.AddItem(buttonData) as PushButton;

         // Optionally, other properties may be assigned to the button
         // a) tool-tip
         pushButton.ToolTip = "Say hello to the entire world.";

         // b) large bitmap
         Uri uriImage = new Uri(@"D:\Sample\HelloWorld\bin\Debug\39-Globe_32x32.png"");
         BitmapImage largeImage = new BitmapImage(uriImage);
         pushButton.LargeImage = largeImage;

         return Result.Succeeded;
      }

      public Result OnShutdown(UIControlledApplication application)
      {
         // nothing to clean up in this simple case
         return Result.Succeeded;
      }
   }
   /// <remarks>
   /// The "HelloWorld" external command. The class must be Public.
   /// </remarks>
   [Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.Manual)]
   public class HelloWorld : IExternalCommand
   {
      // The main Execute method (inherited from IExternalCommand) must be public
      public Autodesk.Revit.UI.Result Execute(ExternalCommandData revit,
          ref string message, ElementSet elements)
      {
         TaskDialog.Show("Revit", "Hello World");
         return Autodesk.Revit.UI.Result.Succeeded;
      }
   }
}
```

### Build the Application

After completing the code, build the application. From the Build menu, click Build Solution. Output from the build appears in the Output window indicating that the project compiled without errors. AddPanel.dll is located in the project output directory.

### Create the .addin manifest file

To invoke the application in Revit, create a manifest file to register it into Revit.

1.  Create a new text file using Notepad.
2.  Add the following text to the file:

#### Code Region 2-6: Creating a .addin file for the external application

```
    <?xml version="1.0" encoding="utf-8" standalone="no"?>
    <RevitAddIns>
      <AddIn Type="Application">
        <Assembly>D:\Sample\AddPanel\AddPanel\bin\Debug\AddPanel.dll</Assembly>
        <AddInId>604b1052-f742-4951-8576-c261d1993108</AddInId>
        <FullClassName>Walkthrough.CsAddPanel</FullClassName>
        <VendorId>NAME</VendorId>
        <VendorDescription>Your Company Information</VendorDescription>
      </AddIn>
    </RevitAddIns>
```

3.  Save the file as HelloWorldRibbon.addin and put it in the following location:
    -   For Windows XP - C:\\Documents and Settings\\All Users\\Application Data\\Autodesk\\Revit\\Addins\\2014\\
    -   For Vista/Windows 7 - C:\\ProgramData\\Autodesk\\Revit\\Addins\\2014\\

Note: The AddPanel.dll file is in the default file folder in a new folder called Debug (D:\\Sample\\HelloWorld\\bin\\Debug\\AddPanel.dll). Use the file path to evaluate Assembly.

Refer to [Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html) for more information about .addin manifest files.

### Debugging

To begin debugging, build the project, and run Revit. A new ribbon panel appears on the Add-Ins tab named NewRibbonPanel and Hello World appears as the only button on the panel, with a large globe image.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-8EBB8680-BCD5-4983-829F-55288BBC16B6-low.png)**Figure 9: Add a new ribbon panel to Revit**

Click Hello World to run the application and display the following dialog box.

![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-2C537699-4312-459B-A8E4-224F8C7C163A-low.png)**Figure 10: Hello World dialog box**
