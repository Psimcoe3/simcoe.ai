[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetRevisionNumberOnSheet Method

---



|  |
| --- |
| [ViewSheet Class](af2ee879-173d-df3a-9793-8d5750a17b49.htm)   [See Also](#seeAlsoToggle) |

Gets the Revision Number for a particular Revision as it will appear on this sheet.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public string GetRevisionNumberOnSheet( 	ElementId revisionId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetRevisionNumberOnSheet ( _ 	revisionId As ElementId _ ) As String ``` |

 

| Visual C++ |
| --- |
| ``` public: String^ GetRevisionNumberOnSheet( 	ElementId^ revisionId ) ``` |

#### Parameters

revisionId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the Revision.

#### Return Value

Returns the Revision Number as it will appear on this sheet or    a null reference (  Nothing  in Visual Basic)  if the Revision does not appear on this sheet.

# Remarks

Returns    a null reference (  Nothing  in Visual Basic)  if the Revision does not appear on this sheet.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | revisionId is not a valid Revision. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ViewSheet Class](af2ee879-173d-df3a-9793-8d5750a17b49.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)