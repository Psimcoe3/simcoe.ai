---
created: 2026-01-28T20:33:05 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Registration_of_add_ins_html
author: 
---

# Help | Registration of add-ins | Autodesk

> ## Excerpt
> The Revit API offers the ability to register API applications via a .addin manifest file.

---
The Revit API offers the ability to register API applications via a .addin manifest file.

Manifest files will be read automatically by Revit when they are placed in one of two locations on a user's system:

-   **In a non-user specific location in "application data"**
    
    -   C:\\ProgramData\\Autodesk\\Revit\\Addins\\<version number>\\
-   **In a user specific location in "application data"**
    
    -   C:\\Users\\<user>\\AppData\\Roaming\\Autodesk\\Revit\\Addins\\<version number>\\

All files named .addin in these locations will be read and processed by Revit during startup.

A basic file adding one ExternalCommand looks like this:

| **Code Region: Basic manifest file for an ExternalCommand** |
| --- |
|  |

```
<?xml version="1.0" encoding="utf-16" standalone="no"?>
<RevitAddIns>
  <AddIn Type="Command">
    <Assembly>c:\MyProgram\MyProgram.dll</Assembly>
    <AddInId>76eb700a-2c85-4888-a78d-31429ecae9ed</AddInId>
    <FullClassName>Revit.Samples.SampleCommand</FullClassName>
    <Text>Sample command</Text>
    <VisibilityMode>NotVisibleInFamily</VisibilityMode>
    <VisibilityMode>NotVisibleInMEP</VisibilityMode>
    <AvailabilityClassName>Revit.Samples.SampleAccessibilityCheck </AvailabilityClassName>
  </AddIn>
</RevitAddIns>
```

A basic file adding one ExternalApplication looks like this:

| **Code Region: Basic manifest file for an ExternalApplication** |
| --- |
|  |

```
<?xml version="1.0" encoding="utf-16" standalone="no"?>
<RevitAddIns>
  <AddIn Type="Application">
    <Name>My sample application</Name>
    <Assembly>c:\MyProgram\MyProgram.dll</Assembly>
    <AddInId>604B1052-F742-4951-8576-C261D1993107</AddInId>
    <FullClassName>Revit.Samples.SampleApplication</FullClassName>
  </AddIn>
</RevitAddIns>
```

Multiple AddIn elements may be provided in a single manifest file.

See [Add-in Registration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_Add_in_Registration_html) for more information on the available XML tags for .addin files.
