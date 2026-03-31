[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetReferences Method

---



|  |
| --- |
| [Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)   [See Also](#seeAlsoToggle) |

Selects the references. The references can be an element or a subelement in the host or a linked document.

**Namespace:**   [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2023

# Syntax

| C# |
| --- |
| ``` public void SetReferences( 	IList<Reference> references ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetReferences ( _ 	references As IList(Of Reference) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetReferences( 	IList<Reference^>^ references ) ``` |

#### Parameters

references
:   Type:  System.Collections.Generic IList   [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The references to be selected.

# Remarks

This function will select the specified references and update the UI.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Changing the selection is not permitted while handling SelectionChanged Event. |

# See Also

[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)

[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.htm)