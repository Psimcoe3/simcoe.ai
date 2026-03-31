[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Export Method (String, String, ICollection(ElementId), DWGExportOptions)

---



|  |
| --- |
| [Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Exports a selection of views in DWG format.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public bool Export( 	string folder, 	string name, 	ICollection<ElementId> views, 	DWGExportOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Export ( _ 	folder As String, _ 	name As String, _ 	views As ICollection(Of ElementId), _ 	options As DWGExportOptions _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool Export( 	String^ folder,  	String^ name,  	ICollection<ElementId^>^ views,  	DWGExportOptions^ options ) ``` |

#### Parameters

folder
:   Type:  System String    
     Output folder, into which file(s) will be exported. The folder must exist.

name
:   Type:  System String    
     Either the name of a single file or a prefix for a set of files. If empty, automatic naming will be used. If    a null reference (  Nothing  in Visual Basic)  , throw ArgumentException.

views
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Selection of views to be exported. The set must contain at least one valid view.

options
:   Type:  [Autodesk.Revit.DB DWGExportOptions](3e510f02-1a4c-3e4f-f923-e96972d03862.htm)    
     Various options applicable to the DWG format. If    a null reference (  Nothing  in Visual Basic)  , all options will be set to their respective default values.

#### Return Value

True if successful, otherwise False.

# Remarks

All the views must be printable for the Export to succeed. It can be assured by checking the CanBePrinted property of each view.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public bool ExportDWG(Document document, View view, string setupName)
{
    bool exported = false;
    // Get the predefined setups and use the one with the given name.
    IList<string> setupNames = BaseExportOptions.GetPredefinedSetupNames(document);
    foreach (string name in setupNames)
    {
        if (name.CompareTo(setupName) == 0)
        {
            // Export using the predefined options
            DWGExportOptions dwgOptions = DWGExportOptions.GetPredefinedOptions(document, name);

            // Export the active view
            ICollection<ElementId> views = new List<ElementId>();
            views.Add(view.Id);
            // The document has to be saved already, therefore it has a valid PathName.
            exported = document.Export(Path.GetDirectoryName(document.PathName), 
                Path.GetFileNameWithoutExtension(document.PathName), views, dwgOptions);
            break;
        }
    }

    return exported;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Function ExportDWG(document As Document, view As View, setupName As String) As Boolean
   Dim exported As Boolean = False
   ' Get the predefined setups and use the one with the given name.
   Dim setupNames As IList(Of String) = BaseExportOptions.GetPredefinedSetupNames(document)
   For Each name As String In setupNames
      If name.CompareTo(setupName) = 0 Then
         ' Export using the predefined options
         Dim dwgOptions As DWGExportOptions = DWGExportOptions.GetPredefinedOptions(document, name)

         ' Export the active view
         Dim views As ICollection(Of ElementId) = New List(Of ElementId)()
         views.Add(view.Id)
         ' The document has to be saved already, therefore it has a valid PathName.
         exported = document.Export(Path.GetDirectoryName(document.PathName), Path.GetFileNameWithoutExtension(document.PathName), views, dwgOptions)
         Exit For
      End If
   Next

   Return exported
End Function
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | NullOrEmpty -or- Contains invalid characters. -or- non empty list of views must be provided. -or- some of the views are not printable (exportable). -or- The modifiers set in layer info must be valid. -or- Thrown when the options in DWGExportOptions is invalid. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DirectoryNotFoundException](e6614e11-0fd4-df20-0d2d-02722b779128.htm) | Thrown when the directory does not exist. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Export is temporarily disabled. -or- Exporting is not allowed in the current application mode. |
| [Autodesk.Revit.Exceptions InvalidPathArgumentException](3f3c93a6-008b-f9de-40d4-5cd99bb32b34.htm) | The folder does not exist. |
| [Autodesk.Revit.Exceptions OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The DWG module is not available in the installed Revit. -or- The Graphics module is not available in the installed Revit. |

# See Also

[Document Class](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)

[Export Overload](2f535342-ee41-86f9-0022-92ba1f65112d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)