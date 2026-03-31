---
created: 2026-01-28T20:59:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_Create_a_addin_manifest_file_html
author: 
---

# Help | Create a .addin manifest file | Autodesk

> ## Excerpt
> The HelloWorld.dll file appears in the project output directory. If you want to invoke the application in Revit, create a manifest file to register it into Revit.

---
The HelloWorld.dll file appears in the project output directory. If you want to invoke the application in Revit, create a manifest file to register it into Revit.

To create a manifest file

1.  Create a new text file in Notepad.
2.  Add the following text:

#### Code Region 30-10: Creating a .addin manifest file for an external command

```
<?xml version="1.0" encoding="utf-8" standalone="no"?>
    <RevitAddIns>
    <AddIn Type="Command">
        <Name>HelloWorld</Name>
        <FullClassName>HelloWorld.HelloWorld</FullClassName>
        <Text>HelloWorld</Text>
        <Description>Show Hello World.</Description>
        <VisibilityMode>AlwaysVisible</VisibilityMode>
        <Assembly>C:\Samples\HelloWorld\HelloWorld\bin\Debug\HelloWorld.dll</Assembly>
        <AddInId>239BD853-36E4-461f-9171-C5ACEDA4E723</AddInId>
        <VendorId>ADSK</VendorId>
        <VendorDescription>Autodesk, Inc, www.autodesk.com</VendorDescription>
      </AddIn>
    </RevitAddIns>
```

Note: The FullClassName includes the Root namespace found on the Application tab of the properties for the project.

3.  Save the file as HelloWorld.addin and put it in the following location:
    -   C:\\ProgramData\\Autodesk\\Revit\\Addins{{RelYear}}\\

Refer to [Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html) for more details using manifest files.
