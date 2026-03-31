[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Selection Class

---



|  |
| --- |
| [Members](8eccaa93-cc99-fd37-15ad-24d201985d9b.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Contains the current user selection of elements within the project.

**Namespace:**   [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 23.0.0.0 (23.1.0.0)

# Syntax

| C# |
| --- |
| ``` public class Selection : IDisposable ``` |

 

| Visual Basic |
| --- |
| ``` Public Class Selection _ 	Implements IDisposable ``` |

 

| Visual C++ |
| --- |
| ``` public ref class Selection : IDisposable ``` |

# Remarks

The Selection object is used to retrieve the current user selected elements when an external API command is executed.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
[Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.ReadOnly)]
public class Document_Selection : IExternalCommand
{
    public Autodesk.Revit.UI.Result Execute(ExternalCommandData commandData,
        ref string message, ElementSet elements)
    {
        try
        {
            // Select some elements in Revit before invoking this command

            // Get the handle of current document.
            UIDocument uidoc = commandData.Application.ActiveUIDocument;

            // Get the element selection of current document.
            Selection selection = uidoc.Selection;
            ICollection<ElementId> selectedIds = uidoc.Selection.GetElementIds();

            if (0 == selectedIds.Count)
            {
                // If no elements selected.
                TaskDialog.Show("Revit","You haven't selected any elements.");
            }
            else
            {
                String info = "Ids of selected elements in the document are: ";
                foreach (ElementId id in selectedIds)
                {
                   info += "\n\t" + id.ToString();
                }

                TaskDialog.Show("Revit",info);
            }
        }
        catch (Exception e)
        {
            message = e.Message;
            return Autodesk.Revit.UI.Result.Failed;
        }

        return Autodesk.Revit.UI.Result.Succeeded;
    }
    /// </ExampleMethod>
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
private void ChangeSelection(UIDocument uidoc)
{
    // Get selected elements from current document.
    ICollection<ElementId> selectedIds = uidoc.Selection.GetElementIds();

    // Display current number of selected elements
    TaskDialog.Show("Revit", "Number of selected elements: " + selectedIds.Count.ToString());

    // Go through the selected items and filter out walls only.
    ICollection<ElementId> selectedWallIds = new List<ElementId>();

    foreach (ElementId id in selectedIds)
    {
        Element elements = uidoc.Document.GetElement(id);
        if (elements is Wall)
        {
            selectedWallIds.Add(id);
        }
    }

    // Set the created element set as current select element set.
    uidoc.Selection.SetElementIds(selectedWallIds);

    // Give the user some information.
    if (0 != selectedWallIds.Count)
    {
        TaskDialog.Show("Revit", selectedWallIds.Count.ToString() + " Walls are selected!");
    }
    else
    {
        TaskDialog.Show("Revit","No Walls have been selected!");
    }
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
<Autodesk.Revit.Attributes.Transaction(Autodesk.Revit.Attributes.TransactionMode.[ReadOnly])> _
Public Class Document_Selection
    Implements IExternalCommand
    Public Function Execute(commandData As ExternalCommandData, ByRef message As String, elements As ElementSet) As Autodesk.Revit.UI.Result Implements IExternalCommand.Execute
        Try
            ' Select some elements in Revit before invoking this command


            ' Get the handle of current document.
            Dim uidoc As UIDocument = commandData.Application.ActiveUIDocument

            ' Get the element selection of current document.
            Dim selection As Selection = uidoc.Selection
            Dim selectedIds As ICollection(Of ElementId) = uidoc.Selection.GetElementIds()

            If 0 = selectedIds.Count Then
                ' If no elements selected.
                TaskDialog.Show("Revit", "You haven't selected any elements.")
            Else
                Dim info As [String] = "Ids of selected elements in the document are: "
                For Each id As ElementId In selectedIds
                    info += vbLf & vbTab + id.ToString()
                Next

                TaskDialog.Show("Revit", info)
            End If
        Catch e As Exception
            message = e.Message
            Return Autodesk.Revit.UI.Result.Failed
        End Try

        Return Autodesk.Revit.UI.Result.Succeeded
    End Function
    ' </ExampleMethod>
End Class
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub ChangeSelection(uidoc As UIDocument)
    ' Get selected elements from current document.
    Dim selectedIds As ICollection(Of ElementId) = uidoc.Selection.GetElementIds()

    ' Display current number of selected elements
    TaskDialog.Show("Revit", "Number of selected elements: " + selectedIds.Count.ToString())

    ' Go through the selected items and filter out walls only.
    Dim selectedWallIds As ICollection(Of ElementId) = New List(Of ElementId)()

    For Each id As ElementId In selectedIds
        Dim elements As Element = uidoc.Document.GetElement(id)
        If TypeOf elements Is Wall Then
            selectedWallIds.Add(id)
        End If
    Next

    ' Set the created element set as current select element set.
    uidoc.Selection.SetElementIds(selectedWallIds)

    ' Give the user some information.
    If 0 <> selectedWallIds.Count Then
        TaskDialog.Show("Revit", selectedWallIds.Count.ToString() + " Walls are selected!")
    Else
        TaskDialog.Show("Revit", "No Walls have been selected!")
    End If
End Sub
```

# Inheritance Hierarchy

System Object    
  Autodesk.Revit.UI.Selection Selection

# See Also

[Selection Members](8eccaa93-cc99-fd37-15ad-24d201985d9b.htm)

[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.htm)