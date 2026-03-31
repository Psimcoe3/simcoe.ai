---
created: 2026-01-28T19:27:06 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Welcome_to_the_Revit_Platform_API_User_Manual_html
author: 
---

# Help | Documentation Conventions | Autodesk

> ## Excerpt
> This document contains class names in namespace format, such as Autodesk.Revit.DB.Element. In C++/CLI Autodesk.Revit.Element is Autodesk::Revit::DB::Element. Since only C# is used for sample code in this manual, the default namespace is Autodesk.Revit.DB. If you want to see code in Visual Basic, you will find several VB.NET applications in the SDK Samples directory.

---
This document contains class names in namespace format, such as Autodesk.Revit.DB.Element. In C++/CLI Autodesk.Revit.Element is Autodesk::Revit::DB::Element. Since only C# is used for sample code in this manual, the default namespace is Autodesk.Revit.DB. If you want to see code in Visual Basic, you will find several VB.NET applications in the SDK Samples directory.

### Indexed Properties

Some Revit Platform API class properties are "indexed", or described as overloaded in the API help file (RevitAPI.chm). For example, the Element.Geometry property. In the text of this document, these are referred to as properties, although you access them as if they were methods in C# code by pre-pending the property name with "get\_" or "set\_". For example, to use the Element.Geometry(Options) property, you use Element.get\_Geometry(Options).
