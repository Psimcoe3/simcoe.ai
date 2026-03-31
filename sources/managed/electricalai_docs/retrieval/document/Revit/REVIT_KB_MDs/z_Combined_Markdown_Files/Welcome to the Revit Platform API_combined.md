


<!-- ===== BEGIN: Help  What You Will Need to Get Started  Autodesk.md ===== -->

---
created: 2026-01-28T19:26:53 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Welcome_to_the_Revit_Platform_API_User_Manual_html
author: 
---

# Help | What You Will Need to Get Started | Autodesk

> ## Excerpt
> A working understanding of Autodesk Revit.

---
1.  A working understanding of Autodesk Revit.
    
2.  An installation of an Autodesk Revit-based product, including the Software Development Kit.
    
3.  MS Visual Studio 2019 Community Edition (C# or VB.NET). Microsoft Visual Studio 2019 Professional is recommended, though, as Community editions do not support DLL debugging. Alternatively, you can use the built-in SharpDevelop development environment in Revit.
    
4.  Some experience in a .NET based development language. (Autodesk Revit API examples are provided in C# and Visual Basic.NET.)


<!-- ===== END: Help  What You Will Need to Get Started  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Installation  Autodesk.md ===== -->

---
created: 2026-01-28T19:26:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Welcome_to_the_Revit_Platform_API_User_Manual_html
author: 
---

# Help | Installation | Autodesk

> ## Excerpt
> The Autodesk Revit API is automatically installed with the default installation of the Autodesk Revit based product. Any .NET based application will reference the RevitAPI.dll and the RevitAPIUI.dll located in the Revit Program directory. The RevitAPI.dll contains methods used to access Revit's application, documents, elements and parameters at the database level. The RevitAPIUI.dll contains the interfaces related to manipulation and customization of the Revit user interface.

---
The Autodesk Revit API is automatically installed with the default installation of the Autodesk Revit based product. Any .NET based application will reference the RevitAPI.dll and the RevitAPIUI.dll located in the Revit Program directory. The RevitAPI.dll contains methods used to access Revit's application, documents, elements and parameters at the database level. The RevitAPIUI.dll contains the interfaces related to manipulation and customization of the Revit user interface.

Note that additional API functionality exists in RevitAPIIFC.dll, RevitAPIMacros.dll, and RevitAPIUIMacros.dll, which also install with Revit, but these assemblies are not immediately required to get started.

The Autodesk Revit API Software Development Kit (SDK) is installed from the Tools and Utilities section of the Autodesk Revit installation.


<!-- ===== END: Help  Installation  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Development Requirements  Autodesk.md ===== -->

---
created: 2026-01-28T19:26:32 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Welcome_to_the_Revit_Platform_API_User_Manual_html
author: 
---

# Help | Development Requirements | Autodesk

> ## Excerpt
> The Autodesk Revit API requires the Microsoft .NET Framework 4.8.

---
The Autodesk Revit API requires the Microsoft .NET Framework 4.8.

To edit and debug your API applications, you need an interactive development environment such as Microsoft Visual Studio 2019 Professional or MS Visual Studio Community for C# or Visual Basic.NET. (Visual Studio Professional is recommended, as Express editions do not support DLL debugging.) When developing with the Autodesk Revit API, ensure that your project references two DLLs: **RevitAPI.dll** and **RevitAPIUI.dll** contained in the Autodesk Revit Program directory.

Some programming skills are required to effectively use the API. If you are a beginner in programming, we strongly advise you to learn Microsoft Visual Studio 2019 and one of the compatible languages like C# or Visual Basic.NET. There are many good books and classes to get you started.

**Resources:**

Online resources

-   Free Visual Studio - [http://msdn.microsoft.com/VStudio/Express/](https://www.visualstudio.com/en-US/products/visual-studio-express-vs)
-   [http://www.codeguru.com/](http://www.codeguru.com/)
-   [http://devx.com/](http://devx.com/)
-   [http://www.msdn.microsoft.com/](http://www.msdn.microsoft.com/)
-   [http://msdn.microsoft.com/en-us/library/aa288436(v=vs.71).aspx](http://msdn.microsoft.com/en-us/library/aa288436(v=vs.71).aspx) Books:

-   Code Complete, Second Edition, by Steve McConnell
-   Software Project Survival Guide, by Steve McConnell
-   Pro C# 5.0 and the .NET 4.5 Framework, by Andrew Troelsen


<!-- ===== END: Help  Development Requirements  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  User Manual  Autodesk.md ===== -->

---
created: 2026-01-28T19:25:19 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Welcome_to_the_Revit_Platform_API_User_Manual_html
author: 
---

# Help | User Manual | Autodesk

> ## Excerpt
> This document is part of the Revit SDK. It provides an introduction to implementing Revit add-in applications using the Revit Platform API.

---
This document is part of the Revit SDK. It provides an introduction to implementing Revit add-in applications using the Revit Platform API.

Before creating a Revit Platform API add-in application read through the manual and try the sample code. If you already have some experience with the Revit Platform API, you may just want to review the Notes and Troubleshooting sections.

### Introduction to the Revit Platform API

The first two chapters present an introduction to the Revit Platform API and provide an overview of the User Manual.

[Welcome to the Revit Platform API](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Welcome_to_the_Revit_Platform_API_html) - Presents an introduction to the Revit Platform API and necessary prerequisite knowledge before you create your first add-in.

[Getting Started](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_html) - Step-by-step instructions for creating your first Hello World add-in application using Visual Studio 2019 and four other walkthroughs covering primary add-in functions.

### Basic Topics

These chapters cover the Revit Platform API basic mechanisms and functionality.

[Add-In Integration](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Add_In_Integration_html) - Discusses how an add-in is integrated into the Revit UI and invoked by user commands or specific Revit events such as program startup.

[Application and Document](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_html) - Application and Document classes respectively represent the Revit application and project file in the Revit Platform API. This chapter explains basic concepts and links to pertinent chapters and sections.

[Elements Essentials](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Elements_Essentials_html) - The bulk of the data in a Revit project is in a collection of Elements. This chapter discusses the essential Element mechanism, classification, and features.

[Filtering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Filtering_html) - Filtering is used to get a set of elements from the document.

[Selection](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Selection_html) - Working with the set of selected elements in a document

[Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_html)s - Most Element information is stored as Parameters. This chapter discusses Parameter functionality.

[Collections](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Collections_html) - Utility collection types such as Array, Map, Set collections, and related Iterators.

### Element Topics

Elements are introduced based on element classification. Make sure that you read the Elements Essentials and Parameter chapters before reading about the individual elements.

[Editing Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Editing_Elements_html) - Learn how to move, rotate, delete, mirror, group, and array elements.

[Walls, Floors, Ceilings, Roofs and Openings](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Walls_Floors_Ceilings_Roofs_and_Openings_html) - Discusses Elements, their corresponding ElementTypes representing built-in place construction, and different types of Openings in the API.

[Family Instances](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Family_Instances_html) - Learn about the relationship between family and family instance, family and family instance features, and how to load or create them.

[Family Creation](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_Family_Creation_html) - Learn about creation and modification of Revit Family documents.

[Conceptual Design](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Conceptual_Design_html) - Discusses how to create complex geometry and forms in a Revit Conceptual Mass document.

[Datum and Information Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Datum_and_Information_Elements_html) - Learn how to set up grids, add levels, use design options, and more.

[Annotation Elements](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Annotation_Elements_html) - Discusses document annotation including adding dimensions, detail curves, tags, and annotation symbols.

[Sketching](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Sketching_html) - Sketch functions include 2D and 3D sketch classes such as SketchPlane, ModelCurve, GenericForm, and more.

[Views](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Views_html) - Learn about the different ways to view models and components and how to manipulate the view in the API.

[Material](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Material_html) - Material data is an Element that identifies the physical materials used in the project as well as texture, color, and more.

### Advanced Topics

[Geometry](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Revit_Geometric_Elements_Geometry_html) - Discusses graphics-related types in the API used to describe the graphical representation of the model including the three classes that describe and store the geometry information.

[Place and Locations](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Place_and_Locations_html) - Defines the project location including city, country, latitude, and longitude.

[Shared Parameters](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_html)s - Shared parameters are external text files containing parameter specifications. This chapter introduces how to access to shared parameters through the Revit Platform API.

[Transactions](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_html) - Introduces the two uses for Transaction and the limits that you must consider when using Transaction.

[Events](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_Glossary_Events_html) - Discusses how to take advantage of Revit Events.

[Dynamic Model Update](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Dynamic_Model_Update_html) - Learn how to use updaters to modify the model in reaction to changes in the document.

[Failure Posting and Handling](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Failure_Posting_and_Handling_html) - Learn how to post failures and interact with Revit's failure handling mechanism.

[Analysis Visualization](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Analysis_Analysis_Visualization_html) - How to display analysis results in a Revit project.

### Discipline Specific

Revit includes discipline-specific features for architecture, structural engineering, and MEP engineering. Some APIs only work for specific feature sets.

[Architecture](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Architecture_html) - Discusses the APIs specific to the architectural features of Revit.

[Structural Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_Structural_Engineering_html) - Discusses the APIs specific to the structural engineering features of Revit.

[MEP Engineering](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Discipline_Specific_Functionality_MEP_Engineering_html) - Discusses the APIs specific to the mechanical, electrical, and plumbing features of Revit.

### Other

[Glossary](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_Glossary_html) - Definitions of terms used in this document.

[Appendices](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Appendices_html) - Additional information such as Frequently Asked Questions, Using Visual Basic.Net for programming, and more.


<!-- ===== END: Help  User Manual  Autodesk.md ===== -->

---



<!-- ===== BEGIN: Help  Documentation Conventions  Autodesk.md ===== -->

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


<!-- ===== END: Help  Documentation Conventions  Autodesk.md ===== -->

---

