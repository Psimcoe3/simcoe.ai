[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExclusionFilter Constructor

---



|  |
| --- |
| [ExclusionFilter Class](28581bc9-42ad-9178-edcc-e33f42090bc9.htm)   [See Also](#seeAlsoToggle) |

Constructs a new instance of a filter to exclude elements automatically.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public ExclusionFilter( 	ICollection<ElementId> idsToExclude ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	idsToExclude As ICollection(Of ElementId) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ExclusionFilter( 	ICollection<ElementId^>^ idsToExclude ) ``` |

#### Parameters

idsToExclude
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ids to exclude from the results.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input collection of ids was empty, or its contents were not valid for iteration. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExclusionFilter Class](28581bc9-42ad-9178-edcc-e33f42090bc9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)