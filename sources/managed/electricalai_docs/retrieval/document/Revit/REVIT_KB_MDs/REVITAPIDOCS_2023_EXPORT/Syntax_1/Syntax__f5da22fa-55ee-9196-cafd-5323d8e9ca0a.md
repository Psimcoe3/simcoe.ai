[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TransactWithCentralOptions Class

---



|  |
| --- |
| [Members](a382b180-be52-6fa7-dfe1-b478ccc6ed5f.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Options to customize Revit behavior when accessing the central model.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public class TransactWithCentralOptions : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class TransactWithCentralOptions _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class TransactWithCentralOptions : IDisposable ``` |

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public static void SynchWithCentralWithMessage(Document doc)
{
    // Checkout workset (for use with "keep checked out worksets" option later)
    FilteredWorksetCollector fwc = new FilteredWorksetCollector(doc);
    fwc.OfKind(WorksetKind.UserWorkset);
    Workset workset1 = fwc.First<Workset>(ws => ws.Name == "Workset1");

    WorksharingUtils.CheckoutWorksets(doc, new WorksetId[] { workset1.Id });

    // Make a change
    using (Transaction t = new Transaction(doc, "Add Level"))
    {
        t.Start();
        Level.Create(doc, 100);
        t.Commit();
    }

    // Tell user what we're doing
    TaskDialog td = new TaskDialog("Alert");
    td.MainInstruction = "Application 'Automatic element creator' has made changes and is prepared to synchronize with central.";
    td.MainContent = "This will update central with all changes currently made in the project by the application or by the user.  This operation " +
                     "may take some time depending on the number of changes made by the app and by the user.";

    td.AddCommandLink(TaskDialogCommandLinkId.CommandLink1, "Do not synchronize at this time.");
    td.AddCommandLink(TaskDialogCommandLinkId.CommandLink2, "Synchronize and relinquish all elements.");
    td.AddCommandLink(TaskDialogCommandLinkId.CommandLink3, "Synchronize but keep checked out worksets.");
    td.DefaultButton = TaskDialogResult.CommandLink1;

    TaskDialogResult result = td.Show();

    switch (result)
    {
        case TaskDialogResult.CommandLink1:
        default:
            {
                // Do not synch.  Nothing to do.
                break;
            }
        case TaskDialogResult.CommandLink2:
        case TaskDialogResult.CommandLink3:
            {
                // Prepare to synch
                // TransactWithCentralOptions has to do with the behavior related to locked or busy central models.
                // We'll use the default behavior.
                TransactWithCentralOptions twcOpts = new TransactWithCentralOptions();

                // Setup synch-with-central options (add a comment about our change)
                SynchronizeWithCentralOptions swcOpts = new SynchronizeWithCentralOptions();
                swcOpts.Comment = "Synchronized by 'Automatic element creator' with user acceptance.";

                if (result == TaskDialogResult.CommandLink3)
                {
                    // Setup relinquish options to keep user worksets checked out
                    RelinquishOptions rOptions = new RelinquishOptions(true);
                    rOptions.UserWorksets = false;
                    swcOpts.SetRelinquishOptions(rOptions);
                }

                doc.SynchronizeWithCentral(twcOpts, swcOpts);

                break;
            }
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Shared Sub SynchWithCentralWithMessage(doc As Document)
    ' Checkout workset (for use with "keep checked out worksets" option later)
    Dim fwc As New FilteredWorksetCollector(doc)
    fwc.OfKind(WorksetKind.UserWorkset)
    Dim workset1 As Workset = fwc.First(Function(ws) ws.Name = "Workset1")

    WorksharingUtils.CheckoutWorksets(doc, New WorksetId() {workset1.Id})

    ' Make a change
    Using t As New Transaction(doc, "Add Level")
        t.Start()
        Level.Create(doc, 100)
        t.Commit()
    End Using

    ' Tell user what we're doing
    Dim td As New TaskDialog("Alert")
    td.MainInstruction = "Application 'Automatic element creator' has made changes and is prepared to synchronize with central."
    td.MainContent = "This will update central with all changes currently made in the project by the application or by the user.  This operation " + "may take some time depending on the number of changes made by the app and by the user."

    td.AddCommandLink(TaskDialogCommandLinkId.CommandLink1, "Do not synchronize at this time.")
    td.AddCommandLink(TaskDialogCommandLinkId.CommandLink2, "Synchronize and relinquish all elements.")
    td.AddCommandLink(TaskDialogCommandLinkId.CommandLink3, "Synchronize but keep checked out worksets.")
    td.DefaultButton = TaskDialogResult.CommandLink1

    Dim result As TaskDialogResult = td.Show()

    Select Case result
        Case TaskDialogResult.CommandLink1
            If True Then
                ' Do not synch.  Nothing to do.
                Exit Select
            End If
        Case TaskDialogResult.CommandLink2, TaskDialogResult.CommandLink3
            If True Then
                ' Prepare to synch
                ' TransactWithCentralOptions has to do with the behavior related to locked or busy central models.
                ' We'll use the default behavior.
                Dim twcOpts As New TransactWithCentralOptions()

                ' Setup synch-with-central options (add a comment about our change)
                Dim swcOpts As New SynchronizeWithCentralOptions()
                swcOpts.Comment = "Synchronized by 'Automatic element creator' with user acceptance."

                If result = TaskDialogResult.CommandLink3 Then
                    ' Setup relinquish options to keep user worksets checked out
                    Dim rOptions As New RelinquishOptions(True)
                    rOptions.UserWorksets = False
                    swcOpts.SetRelinquishOptions(rOptions)
                End If

                doc.SynchronizeWithCentral(twcOpts, swcOpts)

                Exit Select
            End If
    End Select
End Sub
```

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  Autodesk.Revit.DB TransactWithCentralOptions

# See Also

[TransactWithCentralOptions Members](a382b180-be52-6fa7-dfe1-b478ccc6ed5f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)