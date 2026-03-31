[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetWorksetVisibility Method

---



|  |
| --- |
| [View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)   [See Also](#seeAlsoToggle) |

Returns the visibility settings of a workset for this particular view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public WorksetVisibility GetWorksetVisibility( 	WorksetId worksetId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetWorksetVisibility ( _ 	worksetId As WorksetId _ ) As WorksetVisibility ``` |

 

| Visual C++ |
| --- |
| ``` public: WorksetVisibility GetWorksetVisibility( 	WorksetId^ worksetId ) ``` |

#### Parameters

worksetId
:   Type:  [Autodesk.Revit.DB WorksetId](8bece327-c269-8101-b4c2-38632f593fe6.htm)    
     Id of the workset.

#### Return Value

The visibility of a workset for this particular view.

# Remarks

The settings does not reflect the fact of whether a workset is currently closed or not.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | There is no workset with this Id in the document associated with this view. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[View Class](fb92a4e7-f3a7-ef14-e631-342179b18de9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)