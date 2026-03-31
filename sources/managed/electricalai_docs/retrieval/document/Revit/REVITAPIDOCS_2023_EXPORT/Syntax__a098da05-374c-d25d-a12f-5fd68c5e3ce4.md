[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanBeDissolved Method

---



|  |
| --- |
| [FormUtils Class](fe80084f-2b75-cc39-bf64-866bc2c27bb1.htm)   [See Also](#seeAlsoToggle) |

Validates that input contains one or more form elements or geom combinations containing form elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static bool CanBeDissolved( 	Document ADoc, 	ICollection<ElementId> elements ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CanBeDissolved ( _ 	ADoc As Document, _ 	elements As ICollection(Of ElementId) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool CanBeDissolved( 	Document^ ADoc,  	ICollection<ElementId^>^ elements ) ``` |

#### Parameters

ADoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

elements
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A collection of elements.

#### Return Value

True if inputs contain one or more form elements. Non-form element inputs are ignored. False if none of the inputs are form elements or do not contain form elements.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FormUtils Class](fe80084f-2b75-cc39-bf64-866bc2c27bb1.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)