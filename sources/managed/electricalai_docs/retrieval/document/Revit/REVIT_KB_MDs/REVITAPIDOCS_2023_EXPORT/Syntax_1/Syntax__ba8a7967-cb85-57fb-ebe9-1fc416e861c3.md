[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetDetailLevel Method

---



|  |
| --- |
| [OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)   [See Also](#seeAlsoToggle) |

Sets the detail level.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public OverrideGraphicSettings SetDetailLevel( 	ViewDetailLevel detailLevel ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetDetailLevel ( _ 	detailLevel As ViewDetailLevel _ ) As OverrideGraphicSettings ``` |

 

| Visual C++ |
| --- |
| ``` public: OverrideGraphicSettings^ SetDetailLevel( 	ViewDetailLevel detailLevel ) ``` |

#### Parameters

detailLevel
:   Type:  [Autodesk.Revit.DB ViewDetailLevel](1f75aa53-ca98-df48-3286-a06b56096054.htm)    
     Value of the detail level. ViewDetailLevel.Undefined means no override is set.

#### Return Value

Reference to the changed object.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[OverrideGraphicSettings Class](eb2bd6b6-b7b2-5452-2070-2dbadb9e068a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)