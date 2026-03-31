[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetAvailableParameterCategories Method

---



|  |
| --- |
| [TableView Class](ba608411-21af-e924-2aa2-3595548ab39f.htm)   [See Also](#seeAlsoToggle) |

Get all available parameter categories.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public IList<ElementId> GetAvailableParameterCategories( 	SectionType sectionType, 	int row ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetAvailableParameterCategories ( _ 	sectionType As SectionType, _ 	row As Integer _ ) As IList(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: IList<ElementId^>^ GetAvailableParameterCategories( 	SectionType sectionType,  	int row ) ``` |

#### Parameters

sectionType
:   Type:  [Autodesk.Revit.DB SectionType](ad9a6cf0-aa1a-d011-b399-658345721aab.htm)    
     The section the row lies in.

row
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     The row.

#### Return Value

The available parameter categories.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The sectionType is not a valid type for this view. |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given row number row is invalid. -or- A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[TableView Class](ba608411-21af-e924-2aa2-3595548ab39f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)