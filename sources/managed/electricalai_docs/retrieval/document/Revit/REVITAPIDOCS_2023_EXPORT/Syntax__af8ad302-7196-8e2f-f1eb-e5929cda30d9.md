[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PickPoint Method (ObjectSnapTypes, String)

---



|  |
| --- |
| [Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Prompts the user to pick a point on the active work plane using specified snap settings while showing a custom status prompt string.

**Namespace:**   [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ PickPoint( 	ObjectSnapTypes snapSettings, 	string statusPrompt ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function PickPoint ( _ 	snapSettings As ObjectSnapTypes, _ 	statusPrompt As String _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ PickPoint( 	ObjectSnapTypes snapSettings,  	String^ statusPrompt ) ``` |

#### Parameters

snapSettings
:   Type:  [Autodesk.Revit.UI.Selection ObjectSnapTypes](806b68f7-9801-f58e-ee3e-94b85bfaea8f.htm)    
     Specifies the object snap types for this pick. Multiple object snap types can be combined with "|"

statusPrompt
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     Specifies the message shown on the status bar.

#### Return Value

The point picked by user.

Note: if the user cancels the operation (for example, through ESC), the method will throw an OperationCanceledException instance.

# Remarks

Revit users will be permitted to manipulate the Revit view (zooming, panning, and rotating the view), but will not be permitted to click other items in the Revit user interface. Users are not permitted to switch the active view, close the active document or Revit application in the pick session, otherwise an exception will be thrown.

Note: this method must not be called during dynamic update, otherwise ForbiddenForDynamicUpdateException will be thrown.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
public void PickPoint(UIDocument uidoc)
{
    ObjectSnapTypes snapTypes = ObjectSnapTypes.Endpoints | ObjectSnapTypes.Intersections;
    XYZ point = uidoc.Selection.PickPoint(snapTypes, "Select an end point or intersection");

    string strCoords = "Selected point is " + point.ToString();

    TaskDialog.Show("Revit", strCoords);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Public Sub PickPoint(uidoc As UIDocument)
    Dim snapTypes As ObjectSnapTypes = ObjectSnapTypes.Endpoints Or ObjectSnapTypes.Intersections
    Dim point As XYZ = uidoc.Selection.PickPoint(snapTypes, "Select an end point or intersection")

    Dim strCoords As String = "Selected point is " & point.ToString()

    TaskDialog.Show("Revit", strCoords)
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the argument statusPrompt is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when no work plane set in current view. |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | Thrown when the Revit user cancelled this operation. Thrown when the Revit user tried to switch the active view, close the active document or Revit application when responding to this mode. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | Thrown if this method is called during dynamic update. |

# See Also

[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)

[PickPoint Overload](a1d40214-13d6-2e11-36bb-905d49105168.htm)

[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.htm)