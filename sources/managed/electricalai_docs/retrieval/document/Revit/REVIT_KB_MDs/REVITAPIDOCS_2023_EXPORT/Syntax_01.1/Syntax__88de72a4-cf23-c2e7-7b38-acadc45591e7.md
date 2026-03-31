[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetOpenWorksetsConfiguration Method

---



|  |
| --- |
| [OpenOptions Class](c0004971-3810-eeb8-72bd-e116886ec3c8.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Sets the object used to configure the worksets to open when the model is opened.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public void SetOpenWorksetsConfiguration( 	WorksetConfiguration openConfiguration ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetOpenWorksetsConfiguration ( _ 	openConfiguration As WorksetConfiguration _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetOpenWorksetsConfiguration( 	WorksetConfiguration^ openConfiguration ) ``` |

#### Parameters

openConfiguration
:   Type:  [Autodesk.Revit.DB WorksetConfiguration](eefef6f4-0892-4bb5-8840-5e99aebc65c9.htm)    
     The options. If    a null reference (  Nothing  in Visual Basic)  , all user-created worksets will be opened.

# Remarks

These options are ignored for non-workshared models.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
Document OpenDocumentWithWorksets(Application app, ModelPath projectPath)
{
    Document doc = null;
    try
    {
        // Get info on all the user worksets in the project prior to opening
        IList<WorksetPreview> worksets = WorksharingUtils.GetUserWorksetInfo(projectPath);
        IList<WorksetId> worksetIds = new List<WorksetId>();
        // Find two predetermined worksets
        foreach (WorksetPreview worksetPrev in worksets)
        {
            if (worksetPrev.Name.CompareTo("Workset1") == 0 ||
                worksetPrev.Name.CompareTo("Workset2") == 0)
            {
                worksetIds.Add(worksetPrev.Id);
            }
        }

        OpenOptions openOptions = new OpenOptions();
        // Setup config to close all worksets by default
        WorksetConfiguration openConfig = new WorksetConfiguration(WorksetConfigurationOption.CloseAllWorksets);
        // Set list of worksets for opening 
        openConfig.Open(worksetIds);
        openOptions.SetOpenWorksetsConfiguration(openConfig);
        doc = app.OpenDocumentFile(projectPath, openOptions);
    }
    catch (Exception e)
    {
        TaskDialog.Show("Open File Failed", e.Message);
    }

    return doc;
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Function OpenDocumentWithWorksets(app As Application, projectPath As ModelPath) As Document
    Dim doc As Document = Nothing
    Try
        ' Get info on all the user worksets in the project prior to opening
        Dim worksets As IList(Of WorksetPreview) = WorksharingUtils.GetUserWorksetInfo(projectPath)
        Dim worksetIds As IList(Of WorksetId) = New List(Of WorksetId)()
        ' Find two predetermined worksets
        For Each worksetPrev As WorksetPreview In worksets
            If worksetPrev.Name.CompareTo("Workset1") = 0 OrElse worksetPrev.Name.CompareTo("Workset2") = 0 Then
                worksetIds.Add(worksetPrev.Id)
            End If
        Next

        Dim openOptions As New OpenOptions()
        ' Setup config to close all worksets by default
        Dim openConfig As New WorksetConfiguration(WorksetConfigurationOption.CloseAllWorksets)
        ' Set list of worksets for opening 
        openConfig.Open(worksetIds)
        openOptions.SetOpenWorksetsConfiguration(openConfig)
        doc = app.OpenDocumentFile(projectPath, openOptions)
    Catch e As Exception
        TaskDialog.Show("Open File Failed", e.Message)
    End Try

    Return doc
End Function
```

# See Also

[OpenOptions Class](c0004971-3810-eeb8-72bd-e116886ec3c8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)