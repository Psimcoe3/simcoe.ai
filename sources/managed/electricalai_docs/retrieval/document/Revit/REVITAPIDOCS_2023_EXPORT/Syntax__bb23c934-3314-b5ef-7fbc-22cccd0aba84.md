[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DeleteElements Method

---



|  |
| --- |
| [FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)   [See Also](#seeAlsoToggle) |

Resolves failures by deletion of elements related to the failures.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void DeleteElements( 	IList<ElementId> idsToDelete ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub DeleteElements ( _ 	idsToDelete As IList(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void DeleteElements( 	IList<ElementId^>^ idsToDelete ) ``` |

#### Parameters

idsToDelete
:   Type:  System.Collections.Generic IList   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Ids of elements to be deleted.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Resolution of the failures by deleting idsToDelete is not permitted |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailuresAccessor is inactive (is used outside of failures processing). |

# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)