[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PickElementsByRectangle Method (String)

---



|  |
| --- |
| [Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Prompts the user to select multiple elements by drawing a rectangle while showing a custom status prompt string.

**Namespace:**   [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IList<Element> PickElementsByRectangle( 	string statusPrompt ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function PickElementsByRectangle ( _ 	statusPrompt As String _ ) As IList(Of Element) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Element^>^ PickElementsByRectangle( 	String^ statusPrompt ) ``` |

#### Parameters

statusPrompt
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The message shown on the status bar.

#### Return Value

A collection of elements selected by the user.

Note: if the user cancels the operation (for example, through ESC), the method will throw an OperationCanceledException instance.

# Remarks

Revit users will be permitted to manipulate the Revit view (zooming, panning, and rotating the view), but will not be permitted to click other items in the Revit user interface. Users are not permitted to switch the active view, close the active document or Revit application in the pick session, otherwise an exception will be thrown.

The selection will not be automatically added to the active selection buffer.

Note: this method must not be called during dynamic update, otherwise ForbiddenForDynamicUpdateException will be thrown.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// Use the rectangle picking tool to identify model elements to select.
IList<Element> pickedElements = uidoc.Selection.PickElementsByRectangle("Select by rectangle");
if (pickedElements.Count > 0)
{ 
    // Collect Ids of all picked elements
    IList<ElementId> idsToSelect = new List<ElementId>(pickedElements.Count);
    foreach (Element element in pickedElements)
    {
        idsToSelect.Add(element.Id);
    }

    // Update the current selection
    uidoc.Selection.SetElementIds(idsToSelect);
    TaskDialog.Show("Revit", string.Format("{0} elements added to Selection.", idsToSelect.Count));
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' Use the rectangle picking tool to identify model elements to select.
Dim pickedElements As IList(Of Element) = uidoc.Selection.PickElementsByRectangle("Select by rectangle")
If pickedElements.Count > 0 Then
    ' Collect Ids of all picked elements
    Dim idsToSelect As IList(Of ElementId) = New List(Of ElementId)(pickedElements.Count)
    For Each element As Element In pickedElements
        idsToSelect.Add(element.Id)
    Next

    ' Update the current selection
    uidoc.Selection.SetElementIds(idsToSelect)
    TaskDialog.Show("Revit", String.Format("{0} elements added to Selection.", idsToSelect.Count))
End If
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the statusPrompt is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | Thrown when the Revit user cancelled this operation. Thrown when the Revit user tried to switch the active view, close the active document or Revit application when responding to this mode. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | Thrown if this method is called during dynamic update. |

# See Also

[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)

[PickElementsByRectangle Overload](b486efdd-0c0d-589f-2dfd-b16d32dca046.htm)

[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.htm)