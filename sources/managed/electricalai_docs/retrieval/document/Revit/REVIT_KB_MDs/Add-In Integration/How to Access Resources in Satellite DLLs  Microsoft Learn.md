---
created: 2026-01-28T20:38:37 (UTC -05:00)
tags: []
source: https://learn.microsoft.com/en-us/previous-versions/ms165653(v=vs.140)
author: 
---

# How to: Access Resources in Satellite DLLs | Microsoft Learn

> ## Excerpt
> Visual Studio add-ins are deprecated in Visual Studio 2013. You should upgrade your add-ins to VSPackage extensions. For more information about upgrading, see FAQ: Converting Add-ins to VSPackage Extensions.

---
___

#### Share via

___

Visual Studio add-ins are deprecated in Visual Studio 2013. You should upgrade your add-ins to VSPackage extensions. For more information about upgrading, see [FAQ: Converting Add-ins to VSPackage Extensions](https://msdn.microsoft.com/en-us/library/dn246938(v=vs.140)).

Once you have created a satellite DLL and added resources to it (icons, bitmaps, resource strings, and so forth), those resources now become available to your add-ins and other automation projects. The procedure below demonstrates how to do this.

Note

The dialog boxes and menu commands you see might differ from those described in Help depending on your active settings or edition. These procedures were developed with the General Development Settings active. To change your settings, choose **Import** and **ExportSettings** on the **Tools** menu. For more information, see [Customizing Development Settings in Visual Studio](https://learn.microsoft.com/en-us/previous-versions/zbhkx167(v=vs.140)).

### Accessing satellite DLL resources

1.  Open Visual Studio and either load an existing add-in project or create a new one.
    
2.  Add the following code example, compile, and run it.
    

## Example

The following is the general algorithm Visual Studio uses to find a satellite DLL. You can use this code to make sure that the satellite DLL is properly built, in the right location, and has the resource name you expect.

```
static void Main(string[] args)
{
    string path = @"<some path here>";
    System.Reflection.Assembly asm =    
    System.Reflection.Assembly.LoadFrom(path);
    // For enhanced security, use the LoadFrom overload 
    // System.Reflection.Assembly.LoadFrom(path, securityInfo);
    // where securityInfo is an instance of an Evidence object.
    System.Reflection.Assembly assemblyForResources = 
    asm.GetSatelliteAssembly(System.Threading.
    Thread.CurrentThread.CurrentCulture);
    System.IO.Stream stream =    
    assemblyForResources.GetManifestResourceStream
    (assemblyForResources.GetManifestResourceNames()[0]);
    ResourceReader resReader = new ResourceReader(stream);
    foreach (System.Collections.DictionaryEntry entry in resReader)
    {
        System.Windows.Forms.MessageBox.Show(entry.Key.ToString());
    }
}
```

## Compiling the Code

To use this example, create a Visual C# console application, add this code in place of the Main() function, and set the path variable to the path of the add-in assembly (not the path to the satellite DLL). When run, you will see all available resources in the satellite DLL.

## See Also

#### Tasks

[Walkthrough: Creating Managed Satellite DLLs](https://learn.microsoft.com/en-us/previous-versions/e9zazcx5(v=vs.140))
