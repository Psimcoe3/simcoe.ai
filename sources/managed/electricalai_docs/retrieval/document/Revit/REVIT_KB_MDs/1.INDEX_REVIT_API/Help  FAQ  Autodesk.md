---
created: 2026-01-28T21:30:45 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Getting_Started_Using_the_Autodesk_Revit_API_Deployment_Options_html
author: 
---

# Help | FAQ | Autodesk

> ## Excerpt
> Questions and answers about the Revit API language environment, development tools, best practices, and other common issues.

---
Questions and answers about the Revit API language environment, development tools, best practices, and other common issues.

## Development Environment

What versions of Visual Studio do I need for Revit API development? Can I use Visual C# Community?

-   To edit and debug your API applications, you need an interactive development environment such as Microsoft Visual Studio 2019 Professional or one of the MS Visual Studio Community Editions for C# or Visual Basic.NET

What languages are supported for Revit API development?

-   C#, VB.NET, and C++/CLI are supported for addin development. C#, VB.NET, and IronPython are supported for macro development. Other CLR languages may work with the Revit API, but they are untested and unsupported. Note that for mixed managed/native applications using C++, Revit uses the Visual C++ Redistributable for Visual Studio 2019.. Add-ins compiled with other versions of the VC runtime may not work correctly since the Revit install does not include any other VC runtimes.

## Addins

Is there a wizard to help generate Revit Addins?

-   Yes. Please see [http://thebuildingcoder.typepad.com/blog/2014/05/add-in-wizards-for-revit-2015.html](http://thebuildingcoder.typepad.com/blog/2014/05/add-in-wizards-for-revit-2015.html)

Why doesn't my C++ addin build?

-   You may be missing the `<TargetFrameworkVersion>v4.5.2</TargetFrameworkVersion>` node in the `<PropertyGroup Label="Globals">` section of your .vcxproj file -- the Visual C++ default framework without this node is .NET 4.0.

Why doesn't my external command show up?

-   There is a variety of reasons. Is your .addin manifest file properly installed to C:\\ProgramData\\Autodesk\\Revit\\Addins\\ 20xx? Is the path to your DLL in the .addin correct?

Why isn't my application's OnStartup method called when Revit starts?

-   Check the .addin manifest from the question above. Also, try checking to see if an exception is called in the constructor of your addin object when Revit starts.

## API Usage

How do I reference an element in Revit?

-   Each element has an ID. The ID that is unique in the model is used to make sure that you are referring to the same element across multiple sessions of Revit.

Can a model only use one shared parameter file?

-   Shared parameter files are used to hold bits of information about the parameter. The most important piece of information is the GUID (Globally Unique Identifier) that is used to insure the uniqueness of a parameter in a single file and across multiple models.
    
    Revit can work with multiple shared parameter files but you can only read parameters from one file at a time. It is then up to you to choose the same shared parameter file for all models or a different one for each model.
    
    In addition, your API application should avoid interfering with the user's parameter file. Ship your application with its own parameter file containing your parameters. To load the parameter(s) into a Revit file:
    
    -   The application must remember the user parameter file name.
    -   Switch to the application's parameter file and load the parameter.
    -   Then switch back to the user's file.

Do I need to distribute the shared parameters file with the model so other programs can use the shared parameters?

-   No. The shared parameters file is only used to load shared parameters. After they are loaded the file is no longer needed for that model.

Are shared parameter values copied when the corresponding element is copied?

-   Yes. If you have a shared parameter that holds the unique ID for an element in your database, append the Revit element Unique ID or add another shared parameter with the Revit element unique ID. Do this so that you can check it and make sure you are working with the original element ID and not a copy.

Are element Unique IDs (UID) universally unique and can they ever change?

-   The element UIDs are not universally unique but they are unique within a model as are element IDs. They are not universally unique since they can be duplicated when creating one document by copying another. However, UniqueIDs are stable for referencing elements in a worksharing environment because they will not change. Unlike UniqueIDs, regular IDs can be renumbered when synching with a central model, therefore they cannot be considered stable for referencing of elements.

Revit takes a long time to update when my application sends data back to the model. What do I need to do to speed it up?

-   Make sure you only call Document.Regenerate() as often as necessary. Although this method is required to make sure the elements in the Revit document reflect all changes, it can slow down your application. Keep in mind, too, that when a transaction is committed there is an automatic call to regenerate the document.

What do I do if I want to add shared parameters to elements that do not have the ability to have shared parameters bound to them? For example, Grids or Materials.

-   If an element type does not have the ability to add shared parameters, you need to add a project parameter. This does make it a bit more complicated when it is time to access the shared parameter associated with the element because it does not show up as part of the element's parameter list. By using tricks like making the project shared parameter a string and including the element ID in the shared parameter you can associate the data with an element by first parsing the string.

How do I access the saved models and content BMP?

-   The Preview.dll is a shell plug-in which is an object that implements the IExtractImage interface. IExtractImage is an interface used by the Windows Shell Folders to extract the images for a known file type.
    
    For more information, review the information at [Revit API Developers Guide](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_html) for Autodesk Revit.").
    
    CRevitPreviewExtractor implements standard API functions:
    

```
STDMETHOD(GetLocation)(LPWSTR pszPathBuffer,
        DWORD cchMax,
        DWORD *pdwPriority,
        const SIZE *prgSize,
        DWORD dwRecClrDepth,
        DWORD *pdwFlags);
        STDMETHOD(Extract)(HBITMAP*);
```

It registers itself in the registry.

Why is Element.Parameters taking so long to access?

-   This property executes many calculations internally. Caching specific properties in a separate data structure may be a good idea, depending on your applications' needs.

## Structural Engineering

Sometimes the default end releases of structural elements render the model unstable. How can I deal with this situation?

-   The Analytical Model Check feature introduced in Revit Structure R3 can find some of these issues. When importing the analytical model, you are asked if you want to retain the release conditions from RST (Revit Structure) or if you want to set all beams and columns to fixed. When re-importing the model to RST, always update the end releases and do not overwrite the end releases on subsequent export to analysis programs.

I am rotating the beam orientation so they are rotated in the weak direction. For example, the I of a W14X30 is rotated to look like an H by a 90 degree rotation. How is that rotation angle accessed in the API? Because the location is a LocationCurve not a LocationPoint I do not have access to the Rotation value so what is it I need to check? I have a FamilyInstance element to check so what do I do with it?

-   Take a look at the RotateFramingObject example in the SDK. It has examples of how to get and change the beam braces and columns rotation angle.

How do I add new concrete beam and column sizes to a model?

-   Take a look at the FrameBuilder sample code in the SDK

How do I view the true deck layer?

-   There is an example in the SDK called DeckProperties that provides information about how to get the layer information for the deck. The deck information is reported in exactly the same way as it is in the UI. The deck dimension parameters are shown as follows. ![](https://help.autodesk.com/cloudhelp/2023/ENU/Revit-API/images/GUID-05CADDA6-B674-437E-A3A6-C98A026114EE-low.png)

How do I tell when I have a beam with a cantilever?

-   There is no direct way in the Revit database to tell if a beam has a cantilever. However, one or more of the following options can give you a good guess at whether a section is a cantilever:
    
    There are two parameters called Moment Connection Start and Moment Connection End. If the value set for these two is not None then you should look and see if there is a beam that is co-linear and also has the value set to something other than None. Also ask the user to make sure to select Cantilever Moment option rather than Moment Frame option.
    
    Trace the connectivity back beyond the element approximately one or two elements.
    
    Look at element release conditions.
    

When exporting a model containing groups to an external program, the user receives the following error at the end of the export: "Changes to group "Group 1" are allowed only in group edit mode. Use the Edit Group command to make the change to all instances of the group. You may use the "Ungroup" option to proceed with this change by ungrouping the changed group instances."

-   Currently the API does not permit changes to group members. You can programmatically ungroup, make the change, regroup and then swap the other instances of the old group to the new group to get the same effect.

## General

Is the API binary compatible between major releases?

-   Partially. Any API marked obsolete will be supported for that release and removed in the following release. Therefore, your application must be up to date with the latest APIs at least every other release to remain compatible.
