[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetActiveWorksetId Method

---



|  |
| --- |
| [WorksetTable Class](9ffa5fc8-e6a5-17d6-590e-8ecbfd7b85fb.htm)   [See Also](#seeAlsoToggle) |

Sets the active workset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015 Subscription Update

# Syntax

| C# |
| --- |
| ``` public void SetActiveWorksetId( 	WorksetId worksetId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetActiveWorksetId ( _ 	worksetId As WorksetId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetActiveWorksetId( 	WorksetId^ worksetId ) ``` |

#### Parameters

worksetId
:   Type:  [Autodesk.Revit.DB WorksetId](8bece327-c269-8101-b4c2-38632f593fe6.htm)    
     The workset Id.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | There is no workset in the document with this id. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[WorksetTable Class](9ffa5fc8-e6a5-17d6-590e-8ecbfd7b85fb.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)