[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetAdditionalElements Method

---



|  |
| --- |
| [FailureMessage Class](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)   [See Also](#seeAlsoToggle) |

Sets the additional reference elements for the failure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FailureMessage SetAdditionalElements( 	ICollection<ElementId> additionalElements ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetAdditionalElements ( _ 	additionalElements As ICollection(Of ElementId) _ ) As FailureMessage ``` |

 

| Visual C++ |
| --- |
| ``` public: FailureMessage^ SetAdditionalElements( 	ICollection<ElementId^>^ additionalElements ) ``` |

#### Parameters

additionalElements
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The additional elements.

#### Return Value

The FailureMessage.

# Remarks

Additional elements are used to highlight additional information to the user. They are not considered as causing the failure, but are related to it. User cannot delete them in extended error dialog.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailureMessage is already posted to a document |

# See Also

[FailureMessage Class](d0795bd6-f092-90f2-5c2c-3876e616454c.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)