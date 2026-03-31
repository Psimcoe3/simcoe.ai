[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsResolutionApplicable Method

---



|  |
| --- |
| [FailureDefinition Class](b0c061b0-d712-0c41-6054-b8ce8f996256.htm)   [See Also](#seeAlsoToggle) |

Checks if the given resolution type is applicable to the failure.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool IsResolutionApplicable( 	FailureResolutionType type ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsResolutionApplicable ( _ 	type As FailureResolutionType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsResolutionApplicable( 	FailureResolutionType type ) ``` |

#### Parameters

type
:   Type:  [Autodesk.Revit.DB FailureResolutionType](786e6422-f66d-5320-99f9-e530819e50a1.htm)    
     The resolution type to check.

#### Return Value

True if the given resolution type is applicable to the failure, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[FailureDefinition Class](b0c061b0-d712-0c41-6054-b8ce8f996256.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)