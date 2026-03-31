---
created: 2026-01-28T20:39:52 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/dotnet/api/envdte.commands.addnamedcommand?view=visualstudiosdk-2022&redirectedfrom=MSDN#EnvDTE_Commands_AddNamedCommand_EnvDTE_AddIn_System_String_System_String_System_String_System_Boolean_System_Int32_System_Object____System_Int32_
author: dotnet-bot
---

# Commands.AddNamedCommand Method (EnvDTE) | Microsoft Learn

> ## Excerpt
> Creates a named command that is saved by the environment and made available the next time the environment starts, even if the VSPackage is not loaded on environment startup. Add-ins are now deprecated. For more information, see FAQ: Converting Add-ins to VSPackage Extensions.

---
Important

Some information relates to prerelease product that may be substantially modified before it’s released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Caution

AddIn related extension points are no longer supported in Visual Studio.

Creates a named command that is saved by the environment and made available the next time the environment starts, even if the VSPackage is not loaded on environment startup.

Add-ins are now deprecated. For more information, see [FAQ: Converting Add-ins to VSPackage Extensions](https://learn.microsoft.com/en-us/visualstudio/extensibility/faq-converting-add-ins-to-vspackage-extensions).

C++/WinRT

```
EnvDTE::Command AddNamedCommand(EnvDTE::AddIn const & AddInInstance, std::wstring const & Name, std::wstring const & ButtonText, std::wstring const & Tooltip, bool MSOButton, int Bitmap = 0, std::Array <winrt::Windows::Foundation::IInspectable const &> const & & ContextUIGUIDs, int vsCommandDisabledFlagsValue = 16);
```

#### Parameters

AddInInstance

[AddIn](https://learn.microsoft.com/en-us/dotnet/api/envdte.addin?view=visualstudiosdk-2022)

Required. The [AddIn](https://learn.microsoft.com/en-us/dotnet/api/envdte.addin?view=visualstudiosdk-2022) that adds the new command.

ButtonText

[String](https://learn.microsoft.com/en-us/dotnet/api/system.string)

Required. The name to use if the command is bound to a button that is displayed by name rather than by icon.

Tooltip

[String](https://learn.microsoft.com/en-us/dotnet/api/system.string)

Required. The text displayed when a user hovers the mouse pointer over any control bound to the new command.

MSOButton

[Boolean](https://learn.microsoft.com/en-us/dotnet/api/system.boolean)

Required. Indicates whether the named command's button picture is an Office picture. `True` = button. If `MSOButton` is `False`, then `Bitmap` is the ID of a 16x16 bitmap resource (but not an icon resource) in a Visual C++ resource DLL that must reside in a folder with the language's locale identifier (1033 for English).

Bitmap

[Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32)

Optional. The ID of a bitmap to display on the button.

ContextUIGUIDs

[Object](https://learn.microsoft.com/en-us/dotnet/api/system.object)\[\]

Optional. A SafeArray of GUIDs that determines which environment contexts (that is, debug mode, design mode, and so on) show the command. See [vsCommandDisabledFlags](https://learn.microsoft.com/en-us/dotnet/api/envdte.vscommanddisabledflags?view=visualstudiosdk-2022)..

vsCommandDisabledFlagsValue

[Int32](https://learn.microsoft.com/en-us/dotnet/api/system.int32)

#### Returns

A [Command](https://learn.microsoft.com/en-us/dotnet/api/envdte.command?view=visualstudiosdk-2022) object.

Attributes

## Remarks

You can later change the `ButtonText` name by responding to the `QueryStatus` method. If the text begins with "#", then the rest of the string is an integer that represents a resource ID in the registered satellite DLL.

The `ContextUIGUIDs` parameter and the `vsCommandStatusValue` parameter are used when the addin is not loaded and thus cannot respond to the `QueryStatus` method. If `ContextUIGUIDs` is empty, then the command is enabled until the addin is loaded and can respond to `QueryStatus`.

The VSPackage can receive invocation notification through the [IDTCommandTarget](https://learn.microsoft.com/en-us/dotnet/api/envdte.idtcommandtarget?view=visualstudiosdk-2022) interface. A button can be added by using the [OnConnection](https://learn.microsoft.com/en-us/dotnet/api/extensibility.idtextensibility2.onconnection?view=visualstudiosdk-2022) method of the [IDTExtensibility2](https://learn.microsoft.com/en-us/dotnet/api/extensibility.idtextensibility2?view=visualstudiosdk-2022) interface

## Applies to

| Product | Versions _(Obsolete)_ |
| --- | --- |
| Visual Studio SDK | 2015, 2017, 2019 _(2022)_ |
