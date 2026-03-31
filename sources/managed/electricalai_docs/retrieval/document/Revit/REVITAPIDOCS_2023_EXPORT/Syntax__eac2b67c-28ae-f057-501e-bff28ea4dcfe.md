[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PickObjects Method (ObjectType, ISelectionFilter, String, IList(Reference))

---



|  |
| --- |
| [Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)   [See Also](#seeAlsoToggle) |

Prompts the user to select multiple objects which pass a custom filter while showing a custom status prompt string. A preselected set of objects may be supplied and will be selected at the start of the selection.

**Namespace:**   [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IList<Reference> PickObjects( 	ObjectType objectType, 	ISelectionFilter selectionFilter, 	string statusPrompt, 	IList<Reference> pPreSelected ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function PickObjects ( _ 	objectType As ObjectType, _ 	selectionFilter As ISelectionFilter, _ 	statusPrompt As String, _ 	pPreSelected As IList(Of Reference) _ ) As IList(Of Reference) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<Reference^>^ PickObjects( 	ObjectType objectType,  	ISelectionFilter^ selectionFilter,  	String^ statusPrompt,  	IList<Reference^>^ pPreSelected ) ``` |

#### Parameters

objectType
:   Type:  [Autodesk.Revit.UI.Selection ObjectType](2d0cbbba-d4ab-84b7-b081-36c14769d82c.htm)    
     Specifies the type of object to be selected.

selectionFilter
:   Type:  [Autodesk.Revit.UI.Selection ISelectionFilter](d552f44b-221c-0ecd-d001-41a5099b2f9f.htm)    
     The selection filter.

statusPrompt
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The message shown on the status bar.

pPreSelected
:   Type:  [System.Collections.Generic IList](http://msdn2.microsoft.com/en-us/library/5y536ey6)   [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The previously selected set of objects.

#### Return Value

A collection of references selected by the user.

Note: if the user cancels the operation (for example, through ESC), the method will throw an OperationCanceledException instance.

# Remarks

The user will be shown "Finish" and "Cancel" buttons on the dialog bar to complete the selection operation. Uncheck the "Multiple" check-box to select single object and it will return the selected object directly.

The previously selected set of objects will be highlighted.

Revit users will be permitted to manipulate the Revit view (zooming, panning, and rotating the view), but will not be permitted to click other items in the Revit user interface. Users are not permitted to switch the active view, close the active document or Revit application in the pick session, otherwise an exception will be thrown.

The selection will not be automatically added to the active selection buffer.

Note: this method must not be called during dynamic update, otherwise ForbiddenForDynamicUpdateException will be thrown.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | Thrown when the objectType is not a recognized value. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the selectionFilter is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when the Revit user cancelled this operation. Thrown when pPreSelected references has objects that are not the type of objectType. Thrown when objectType is PointOnElement which is not supported for selection involving preselected items. |
| [Autodesk.Revit.Exceptions OperationCanceledException](aea34480-ceb5-b49f-129d-0799e7bb1c21.htm) | Thrown when the Revit user cancelled this operation. Thrown when the Revit user tried to switch the active view, close the active document or Revit application when responding to this mode. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | Thrown if this method is called during dynamic update. |

# See Also

[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)

[PickObjects Overload](e5a547a2-3cf5-7638-2daa-ea85b4d3de2d.htm)

[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.htm)