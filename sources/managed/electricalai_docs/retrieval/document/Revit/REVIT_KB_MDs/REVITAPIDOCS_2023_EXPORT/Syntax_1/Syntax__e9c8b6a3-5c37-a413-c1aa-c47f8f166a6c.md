[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanDeleteElement Method

---



|  |
| --- |
| [DocumentValidation Class](dc5c35f3-c58d-b7bd-de1b-46497dfb237e.htm)   [See Also](#seeAlsoToggle) |

Indicates if an element can be deleted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static bool CanDeleteElement( 	Document document, 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CanDeleteElement ( _ 	document As Document, _ 	elementId As ElementId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool CanDeleteElement( 	Document^ document,  	ElementId^ elementId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the element to check.

#### Return Value

True if the element can be deleted, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DocumentValidation Class](dc5c35f3-c58d-b7bd-de1b-46497dfb237e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)