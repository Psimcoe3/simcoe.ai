[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SendToBack Method (Document, View, ElementId)

---



|  |
| --- |
| [DetailElementOrderUtils Class](7153db7b-62cc-f36b-b6a5-0ded8af7b5be.htm)   [See Also](#seeAlsoToggle) |

Places the given detail instance behind all detail instances in the view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static void SendToBack( 	Document pDocument, 	View pDBView, 	ElementId detailElementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub SendToBack ( _ 	pDocument As Document, _ 	pDBView As View, _ 	detailElementId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void SendToBack( 	Document^ pDocument,  	View^ pDBView,  	ElementId^ detailElementId ) ``` |

#### Parameters

pDocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

pDBView
:   Type:  [Autodesk.Revit.DB View](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)    
     The view.

detailElementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The detail elementId to send to back.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element detailElementId is not a detail element. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DetailElementOrderUtils Class](7153db7b-62cc-f36b-b6a5-0ded8af7b5be.htm)

[SendToBack Overload](ee58c342-1428-127f-17ac-0b0bce9dde8f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)