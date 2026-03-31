[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SaveAndClose Method

---



|  |
| --- |
| [UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)   [See Also](#seeAlsoToggle) |

Close the document, prompting the user for saving it when necessary.

**Namespace:**   [Autodesk.Revit.UI](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)    
  **Assembly:**   RevitAPIUI  (in RevitAPIUI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool SaveAndClose() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SaveAndClose As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool SaveAndClose() ``` |

#### Return Value

False if closing procedure fails or if saving of a modified document was requested but failed. Also returns False if closing is cancelled by an external application during 'DocumentClosing' event. When function succeeds, True is returned.

# Remarks

UI dialogs may be shown during the call (e.g. when the document has been changed since last time it was saved) to get user responses. The currently active document may not be closed by this function. It can only be closed via Revit's UI.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when attempting to close the currently active document. Thrown if there are any transactions, sub-transactions or transaction groups which were opened by the API code, and not closed. All of these items must be handled before attempting to close the document. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown if this a linked file. |

# See Also

[UIDocument Class](295b48c8-0571-ad5c-eead-baea84a6787c.htm)

[Autodesk.Revit.UI Namespace](e86fd90a-8957-02a6-da7f-ced248966e3e.htm)