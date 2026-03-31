[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidSectionType Method

---



|  |
| --- |
| [TableView Class](ba608411-21af-e924-2aa2-3595548ab39f.htm)   [See Also](#seeAlsoToggle) |

Identifies if the section type is valid for this view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public bool IsValidSectionType( 	SectionType sectionType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidSectionType ( _ 	sectionType As SectionType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidSectionType( 	SectionType sectionType ) ``` |

#### Parameters

sectionType
:   Type:  [Autodesk.Revit.DB SectionType](ad9a6cf0-aa1a-d011-b399-658345721aab.htm)    
     The section type.

#### Return Value

True if the Section Type is valid, false otherwise.

# Remarks

Some TableViews do not contain all of the possible section types. For example, standard schedules have only a Heading and Body.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[TableView Class](ba608411-21af-e924-2aa2-3595548ab39f.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)