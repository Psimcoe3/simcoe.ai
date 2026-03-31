---
created: 2026-01-28T20:38:43 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/previous-versions/19dax6cz(v=vs.140)
author: 
---

# Add-In Registration | Microsoft Learn

> ## Excerpt
> Visual Studio add-ins are deprecated in Visual Studio 2013. You should upgrade your add-ins to VSPackage extensions. For more information about upgrading, see FAQ: Converting Add-ins to VSPackage Extensions.

---
___

#### Share via

___

Visual Studio add-ins are deprecated in Visual Studio 2013. You should upgrade your add-ins to VSPackage extensions. For more information about upgrading, see [FAQ: Converting Add-ins to VSPackage Extensions](https://msdn.microsoft.com/en-us/library/dn246938(v=vs.140)).

After an add-in is created, you must register it with Visual Studio before it can be activated in **Add-In Manager**. This is accomplished by using an XML file that has an .addin file name extension.

The .addin file describes the information that Visual Studio requires to display the add-in in **Add-In Manager**. When Visual Studio starts, it looks in the .addin file location for any available .addin files. If it finds any, it reads the XML file and gives **Add-In Manager** the information it requires to start the add-in when it is clicked.

The .addin file is created automatically when you create an add-in by using the Add-In Wizard. You can also create an .addin file manually by using the information in this topic.

## File Locations

Two copies of the .addin file are automatically created by the Add-In Wizard, as follows:

  
| 
**.Addin File Location**

 | 

**.Dll File Location**

 | 

**Description**

 |
| --- | --- | --- |
| 

Root project folder

\\Documents\\Visual Studio 2013\\Projects\\MyAddin1\\MyAddin1\\

 | 

Local path (MyAddin1.dll)

 | 

Used for deployment of the add-in project. Included in the project for ease of editing and has the local path for xcopy-style deployment.

 |
| 

Add-in folder

\\Documents\\Visual Studio 2013\\Addins\\

\-or-

Shared Documents Location\\Addins\\

 | 

Project debug folder

(For example, \\ Documents\\Visual Studio 2013

Projects\\MyAddin1\\MyAddin1\\bin\\)

 | 

Used for running the add-in in the debugging environment. Should always point to the output path of the current build configuration.

 |

To install the add-in on another computer, the .addin file must be placed in a location where Visual Studio checks for add-ins. These locations are listed in the **Options** dialog box, in the **Environment** node, on the **Add-in Security** page. For more information, see [Add-In Security](https://learn.microsoft.com/en-us/previous-versions/1326zbk3(v=vs.140)).

The .dll file that contains the add-in can be installed anywhere on the client computer. However, we recommend that you put it with the .addin file.

Note

The <Assembly> element of the .addin file must point to the .dll file that contains the binaries for the add-in.

## The .Addin File

The .addin XML file is split into the following tagged sections:

 
| 
**Section**

 | 

**Description**

 |
| --- | --- |
| 

Host Application

 | 

(Required.) Specifies the names and version numbers of the applications that can load the add-in.

 |
| 

Addin

 | 

(Required) Contains the elements that describe the add-in.

 |
| 

Tools Options Page

 | 

(Optional) Specifies a page in the **Options** dialog box where the add-in can be configured. Child nodes specify the category and subcategory of the **Options** page, and also its assembly name and full class name.

 |

The following elements are children of the <Addin> section:

 
| 
**Element**

 | 

**Description**

 |
| --- | --- |
| 

About Box Details

 | 

(Optional) Specifies the text that will be displayed for your add-in in the Visual Studio **About** dialog box.

 |
| 

About Icon Data

 | 

(Optional) Contains binary data that specifies the icon that will be displayed for your add-in in the Visual Studio **About** dialog box.

 |
| 

About Icon Location

 | 

(Optional) Specifies the absolute path or relative path of the icon that will be displayed for your add-in in the Visual Studio **About** dialog box.

 |
| 

Assembly

 | 

(Required.) Specifies the location of the add-in binaries. This field can be set to a local path, a network path, or a URL.

 |
| 

Command Line Safe

 | 

(Optional) Specifies the Visual Studio modes with which the add-in is compatible, for example, command-line only, integrated development environment (IDE)-only, or both.

 |
| 

Command Preload

 | 

(Optional) Specifies the preloaded state of the add-in; that is, whether the add-in should create its UI by using a method such as [Commands.AddNamedCommand](https://msdn.microsoft.com/en-us/library/sa001y04(v=vs.140)).

 |
| 

Full Class Name

 | 

(Required.) Specifies the name of the class that is used to connect to the add-in.

 |
| 

Load Behavior

 | 

(Optional) Defines whether an add-in is loaded at startup or manually.

 |

Here are the details for each setting. For more information about the hierarchical location many of the elements that are described, see "Example .Addin XML File" later in this topic.

## Host Application

The <Name> element in the Host Application section contains the name of the application. This is the name that is displayed on the title bar of the application or is returned by DTE.Name. For example, for Visual Studio, the tag would contain "Microsoft Visual Studio".

There can be more than one Host Application value per .addin file. Every value must be bracketed by using <Name> tags in the <HostApplication> element. In addition to containing a <Name> element, every <HostApplication> element must also include the version number of the application bracketed by <Version> tags. For example,

```
   <HostApplication>
      <!-- First Host App name (required). -->
      <Name>Microsoft Visual Studio</Name>
      <Version>12.0</Version>
   </HostApplication>
   <HostApplication>
      <!-- An additional supported program/version. -->
      <Name>Microsoft Visual Studio</Name>
      <Version>11.0</Version>
   </HostApplication>
```

Alternatively, you can specify an asterisk (\*) to represent the value for <Version> for any version of Visual Studio.

## Friendly Name

The <FriendlyName> element, which is located under the <Addin> element, specifies the string that will be displayed in the **Available Add-ins** column in **Add-in Manager**. For example,

```
   <FriendlyName>My New Super Addin</FriendlyName>
```

## Description

The <Description> element, which is located under the <Addin> element, specifies the string that will be displayed in the **Description** box in **Add-in Manager**. For example,

```
   <Description>This add-in will change your life!</Description>
```

## About Box Details

If you select the option to generate settings for the **About** dialog box when you create your add-in, this element is added to the .addin file. This element specifies the text that will be displayed in the Visual Studio **About** dialog box. For example,

```
   <AboutBoxDetails>For add-in support, call 1-800-xxx-
     xxxx.</AboutBoxDetails>
```

## About Icon Data

If you select the option to generate settings for the **About** dialog box when you create your add-in, this element is added to the .addin file. This element contains binary data that specifies the icon that will be displayed in the Visual Studio **About** dialog box. For example,

```
<AboutIconData>0000010006 . . . FFFF0000</AboutIconData>
```

## Assembly

The <Assembly> element, which is located under the <Addin> element, specifies the location of the add-in binary files. This element can be set to a relative path, an absolute path ("file"), a registered assembly name ("assembly"), or a URL ("url").

-   The following example shows an absolute path location. In this case, the src parameter is set to file to indicate the location of the add-in DLL.
    
    ```
    <Assembly src="file">C:\Documents and Settings\jdoe\Application Data\Microsoft\Visual Studio\12.0\AddIns\MyAddin4.dll</Assembly>
    ```
    
-   The following example shows a registered location. In this case, the src parameter is set to assembly to indicate a registered add-in DLL.
    
    ```
    <Assembly src="assembly">BookshelfDefineAddin</Assembly>
    ```
    
-   The following example shows a URL location. In this case, the src parameter is set to url to indicate the Web-based location of the add-in DLL.
    
    ```
    <Assembly src="url">https://somewebsite.com/MyAddin4.dll</Assembly>
    ```
    

## Full Class Name

The <FullClassName> element specifies the full name of the class that is used to connect to the add-in. This includes the namespace that contains the class. For example,

```
    <FullClassName>MyAddin4.Connect</FullClassName>
```

## Load Behavior

The <LoadBehavior> element defines whether an add-in is loaded automatically at IDE startup or is started manually. The <LoadBehavior> element is under the <Addin> element. For example,

```
    <LoadBehavior>1</LoadBehavior>
```

Although usage of <LoadBehavior> is optional, we recommend that you use it to explicitly define when an add-in loads.

 
| 
Value

 | 

Description

 |
| --- | --- |
| 

0

 | 

The add-in is not loaded at IDE startup and must be started manually.

 |
| 

1

 | 

The add-in is automatically loaded at IDE startup.

 |
| 

4

 | 

The add-in is loaded when devenv is started at a command prompt by using a build switch (**devenv /build**).

 |

## Command Preload

The <CommandPreload> element specifies whether the add-in must be preloaded. Preloading loads the add-in the first time that Visual Studio is started after the .addin file is installed. For example,

```
    <CommandPreload>1</CommandPreload>
```

This element lets you specify that an add-in must be loaded after Visual Studio is started. It gives your add-in a chance to create required UI elements such as command bar buttons, or perform other first-time-only initialization tasks such as creating default add-in settings. The add-in is then unloaded until a user executes one of the commands that the add-in created. Thereafter, the add-in is loaded as needed.

 
| 
Value

 | 

Description

 |
| --- | --- |
| 

0

 | 

The add-in does not load until either the user starts it by using **Add-In Manager** or the add-in is set to load on startup.

 |
| 

1

 | 

The add-in is loaded automatically when Visual Studio starts for the first time after the .addin file is installed.

 |

You can check the **OnConnection** method that you implement to see whether the type of connection, which is specified by using the second argument to **OnConnection**, is **ext\_cm\_UISetup**. If it is, you can perform whatever command placements you want by using either the **AddNamedCommand** or **AddControl** method.

## Command Line Safe

The optional <CommandLineSafe> element indicates whether the add-in was designed to avoid displaying a UI when it is started at a command prompt, for example, when you perform command-line builds or similar operations. (This is done by selecting **My Add-in will never put up a modal UI** in the **Add-in Wizard**.) Also, it specifies the Visual Studio modes with which the add-in is compatible, for example, command-line-only or IDE only. For example,

```
    <CommandLineSafe>0</CommandLineSafe>
```

 
| 
Value

 | 

Description

 |
| --- | --- |
| 

0

 | 

Specifies that the add-in is not command-line safe and may display a UI.

 |
| 

1

 | 

Specifies that the add-in is command-line safe and does not display a UI.

 |

## Tools Options Page

The optional <ToolsOptionsPage> element specifies an **Options** page so that users can configure the add-in. Child nodes specify the category and subcategory that the page appears in, and the assembly name and full class name of the **Options** page. The following example shows the hierarchy of this element:

```
  <ToolsOptionsPage>
    <Category Name="Text Editor">
      <SubCategory Name="General">
        <Assembly>"MyFilePath\MyAddInOptionPage.dll"</Assembly>
        <FullClassName>"MyNamespace.MyAddInOptionPage"</FullClassName>
      </SubCategory>
    </Category>
  </ToolsOptionsPage>
```

## Example .Addin XML File

The following example shows a complete .addin XML file. It shows the hierarchy and locations for the elements that are described in this topic.

```
<?xml version="1.0" encoding="UTF-16" standalone="no"?>
<Extensibility 
  xmlns="https://schemas.microsoft.com/AutomationExtensibility">
    <HostApplication>
        <Name>Microsoft Visual Studio</Name>
        <Version>12.0</Version>
    </HostApplication> 
    <HostApplication>
        <Name>Microsoft Visual Studio</Name>
        <Version>11.0</Version>
    </HostApplication>
    <Addin>
        <FriendlyName>My great new add-in.</FriendlyName>
        <Description>This add-in does it all.</Description>
        <AboutBoxDetails>Copyright 2013.</AboutBoxDetails>
        <AboutIconData>0000 . . . FFFF0000</AboutIconData>
        <Assembly>MyNewAddin.dll</Assembly>
        <FullClassName>MyNewAddin.Connect</FullClassName>
        <LoadBehavior>1</LoadBehavior>
        <CommandPreload>1</CommandPreload>
        <CommandLineSafe>0</CommandLineSafe>
    </Addin>
</Extensibility>
```

## See Also

#### Tasks

[How to: Control Add-Ins By Using the Add-In Manager](https://learn.microsoft.com/en-us/previous-versions/xwdatdwh(v=vs.140))

[How to: Create an Add-In](https://learn.microsoft.com/en-us/previous-versions/80493a3w(v=vs.140))

[Walkthrough: Creating a Wizard](https://learn.microsoft.com/en-us/previous-versions/7k3w6w59(v=vs.140))

#### Reference

[PAVE Visual Studio Commands and Switches](https://learn.microsoft.com/en-us/previous-versions/kcc7tke7(v=vs.140))

#### Concepts

[Automation Object Model Chart](https://learn.microsoft.com/en-us/previous-versions/za2b25t3(v=vs.140))

#### Other Resources

[Creating Add-ins and Wizards](https://learn.microsoft.com/en-us/previous-versions/5abkeks7(v=vs.140))
