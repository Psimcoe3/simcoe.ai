[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetColumnAttachment Method (FamilyInstance, ElementId)

---



|  |
| --- |
| [ColumnAttachment Class](848a6cb6-c6cf-584c-eb24-5a91b9d3261d.htm)   [See Also](#seeAlsoToggle) |

Look up a column attachment by specifying the target id.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ColumnAttachment GetColumnAttachment( 	FamilyInstance column, 	ElementId targetId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetColumnAttachment ( _ 	column As FamilyInstance, _ 	targetId As ElementId _ ) As ColumnAttachment ``` |

 

| Visual C++ |
| --- |
| ``` public: static ColumnAttachment^ GetColumnAttachment( 	FamilyInstance^ column,  	ElementId^ targetId ) ``` |

#### Parameters

column
:   Type:  [Autodesk.Revit.DB FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)    
     A column.

targetId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of a target element.

#### Return Value

The column attachment attaching the column to the target, or    a null reference (  Nothing  in Visual Basic)  if there is no such attachment.

# Remarks

May return either a top or base attachment.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ColumnAttachment Class](848a6cb6-c6cf-584c-eb24-5a91b9d3261d.htm)

[GetColumnAttachment Overload](e9bfd8bd-c82c-1628-cf6d-1f9178cca041.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)