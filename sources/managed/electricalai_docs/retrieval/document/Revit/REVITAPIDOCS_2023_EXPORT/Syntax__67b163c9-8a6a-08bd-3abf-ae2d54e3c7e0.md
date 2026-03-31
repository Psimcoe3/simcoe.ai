[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetSectionData Method

---



|  |
| --- |
| [PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)   [See Also](#seeAlsoToggle) |

Gets section data that will be written to

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public TableSectionData GetSectionData( 	SectionType sectionType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetSectionData ( _ 	sectionType As SectionType _ ) As TableSectionData ``` |

 

| Visual C++ |
| --- |
| ``` public: TableSectionData^ GetSectionData( 	SectionType sectionType ) ``` |

#### Parameters

sectionType
:   Type:  [Autodesk.Revit.DB SectionType](ad9a6cf0-aa1a-d011-b399-658345721aab.htm)    
     The section type

#### Return Value

The  [TableSectionData](a0e6f821-5f53-1eb0-eba1-16554b3c0dc8.htm)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[PanelScheduleView Class](ef4390e8-5a93-fe7f-580b-c8ec297f6b52.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)