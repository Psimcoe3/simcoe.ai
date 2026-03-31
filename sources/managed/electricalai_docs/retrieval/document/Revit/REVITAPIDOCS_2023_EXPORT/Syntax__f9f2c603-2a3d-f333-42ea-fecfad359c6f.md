[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PromptToPlaceElementTypeOnLegendView Method

---



|  |
| --- |
| [UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)   [See Also](#seeAlsoToggle) |

Prompts the user to place an element type onto a legend view.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void PromptToPlaceElementTypeOnLegendView( 	ElementType elementType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub PromptToPlaceElementTypeOnLegendView ( _ 	elementType As ElementType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void PromptToPlaceElementTypeOnLegendView( 	ElementType^ elementType ) ``` |

#### Parameters

elementType
:   Type:  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
     The ElementType of which instances are to be placed.

# Remarks

This method works only for non-annotation element types. For annotations, use PromptForFamilyInstancePlacement(Autodesk::Revit::DB::FamilySymbol) instead. This method uses its own transaction, so it's not permitted to be invoked in an active transaction. The user is not permitted to change the active legend view or during this placement operation (the operation will be cancelled). In a single invocation, the user can place multiple instances of the input element type until they finish the placement (with Cancel or ESC or a click elsewhere in the UI).

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input element type does not belong to a model-level category. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This document is not the currently active one. -or- Starting a new transaction is not permitted. It could be because another transaction already started and has not been completed yet, or the document is in a state in which it cannot start a new transaction. -or- Thrown when the active view isn't a legend view. -or- Can not create this kind of element in legend view. |

# See Also

[UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)