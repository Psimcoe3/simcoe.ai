[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsWorksetVisible Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Indicates whether the workset is visible in this view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool IsWorksetVisible( 	WorksetId worksetId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsWorksetVisible ( _ 	worksetId As WorksetId _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsWorksetVisible( 	WorksetId^ worksetId ) ``` |

#### Parameters

worksetId
:   Type:  [Autodesk.Revit.DB WorksetId](8bece327-c269-8101-b4c2-38632f593fe6.htm)    
     Id of the workset.

#### Return Value

Whether the workset is visible.

# Remarks

It will take into account whether the workset is opened or closed.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | There is no workset with this Id in the document associated with this view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)