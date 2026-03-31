[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### PostRequestForElementTypePlacement Method

---



|  |
| --- |
| [UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)   [See Also](#seeAlsoToggle) |

Places a request on Revit's command queue for the user to place instances of the specified ElementType. This does not execute immediately, but instead when control returns to Revit from the current API context.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void PostRequestForElementTypePlacement( 	ElementType elementType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub PostRequestForElementTypePlacement ( _ 	elementType As ElementType _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void PostRequestForElementTypePlacement( 	ElementType^ elementType ) ``` |

#### Parameters

elementType
:   Type:  [Autodesk.Revit.DB ElementType](ffb18296-0448-559c-580c-7857cbcdc094.htm)    
     The ElementType of which instances are to be placed.

# Remarks

This method starts its own transaction. In a single invocation, the user can place multiple instances of the input element type until they finish the placement (with Cancel or ESC or a click elsewhere in the UI). This method invokes the UI when control returns from the current API context; because of this, the normal Revit UI options will be available to the user, but the API will not be notified when the user has completed this action. Because this request is queued to run at the end of the current API context, only one such request can be set (between this and the commands set by UIApplication.PostCommand()). This differs from PromptForFamilyInstancePlacement() as that method can be run within the current API context, but the user is not permitted full access to the user interface options during placement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The user cannot be prompted to place the input type interactively. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This document is not the currently active one. -or- Starting a new transaction is not permitted. It could be because another transaction already started and has not been completed yet, or the document is in a state in which it cannot start a new transaction. |

# See Also

[UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)