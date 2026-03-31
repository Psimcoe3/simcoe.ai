[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetElementIds Method

---



|  |
| --- |
| [Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)   [See Also](#seeAlsoToggle) |

Selects the elements.

**Namespace:**   [Autodesk.Revit.UI.Selection](11785869-cc9e-03fc-97db-767a59af10a1.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void SetElementIds( 	ICollection<ElementId> elementIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetElementIds ( _ 	elementIds As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetElementIds( 	ICollection<ElementId^>^ elementIds ) ``` |

#### Parameters

elementIds
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ids of the elements to be selected.

# Remarks

This function will select the specified elements within the project and update the UI. See  SetReferences  for more selection options.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Changing the selection is not permitted while handling SelectionChanged Event. |

# See Also

[Selection Class](31b73d46-7d67-5dbb-4dad-80aa597c9afc.htm)

[Autodesk.Revit.UI.Selection Namespace](11785869-cc9e-03fc-97db-767a59af10a1.htm)