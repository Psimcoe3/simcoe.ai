[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsElementsDeletionPermitted Method (IList(ElementId), String)

---



|  |
| --- |
| [FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)   [See Also](#seeAlsoToggle) |

Checks if resolution of the failures by deleting given collection of elements is permitted.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool IsElementsDeletionPermitted( 	IList<ElementId> idsToDelete, 	out string reason ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsElementsDeletionPermitted ( _ 	idsToDelete As IList(Of ElementId), _ 	<OutAttribute> ByRef reason As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsElementsDeletionPermitted( 	IList<ElementId^>^ idsToDelete,  	[OutAttribute] String^% reason ) ``` |

#### Parameters

idsToDelete
:   Type:  System.Collections.Generic IList   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The Ids of elements to be deleted.

reason
:   Type:  System String   %    
     A localized string explaining reason why the elements cannot be deleted.

#### Return Value

True if resolution of the failures by deleting given elements is permitted

# Remarks

Method does not confirm if deletion of the elements will or may resolve the failure - it simply verifies that given elements can be deleted in the current state of the document.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailuresAccessor is inactive (is used outside of failures processing). |

# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)

[IsElementsDeletionPermitted Overload](be9a4660-d27f-f062-060e-347277e7f39a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)