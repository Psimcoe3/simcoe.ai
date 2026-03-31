[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetCheckoutStatus Method (Document, ElementId)

---



|  |
| --- |
| [WorksharingUtils Class](ae7857a0-4e9b-f9c1-84c7-8b250af68068.htm)   [See Also](#seeAlsoToggle) |

Gets the ownership status of an element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static CheckoutStatus GetCheckoutStatus( 	Document document, 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetCheckoutStatus ( _ 	document As Document, _ 	elementId As ElementId _ ) As CheckoutStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: static CheckoutStatus GetCheckoutStatus( 	Document^ document,  	ElementId^ elementId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the element.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the element.

#### Return Value

A summary of whether the element is unowned, owned by the current user, or owned by another user.

# Remarks

This method returns a locally cached value which may not be up to date with the current state of the element in the central. Because of this, the return value is suitable for reporting to an interactive user (e.g. via a mechanism similar to Worksharing display mode), but cannot be considered a reliable indication of whether the element can be immediately edited by the application. Also, the return value may not be dependable in the middle of a local transaction. See the remarks on  [WorksharingUtils](ae7857a0-4e9b-f9c1-84c7-8b250af68068.htm)  for more details.

For performance reasons, the model is not validated to be workshared, and the element id is also not validated; the element will not be expanded.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[WorksharingUtils Class](ae7857a0-4e9b-f9c1-84c7-8b250af68068.htm)

[GetCheckoutStatus Overload](c0c14d7d-d3a3-eeb7-9e21-fbf84597e5fb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)