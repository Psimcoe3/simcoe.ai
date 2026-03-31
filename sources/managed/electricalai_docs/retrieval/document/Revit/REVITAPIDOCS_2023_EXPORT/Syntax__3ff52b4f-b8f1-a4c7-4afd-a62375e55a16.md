[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DeleteWorksetSettings Constructor (DeleteWorksetOption, WorksetId)

---



|  |
| --- |
| [DeleteWorksetSettings Class](1952e14e-42d8-d672-0e72-d5fb1a83b73a.htm)   [See Also](#seeAlsoToggle) |

Constructs a DeleteWorksetSettings object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2022.1

# Syntax

| C# |
| --- |
| ``` public DeleteWorksetSettings( 	DeleteWorksetOption deleteWorksetOption, 	WorksetId elementsMoveInto ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	deleteWorksetOption As DeleteWorksetOption, _ 	elementsMoveInto As WorksetId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: DeleteWorksetSettings( 	DeleteWorksetOption deleteWorksetOption,  	WorksetId^ elementsMoveInto ) ``` |

#### Parameters

deleteWorksetOption
:   Type:  [Autodesk.Revit.DB DeleteWorksetOption](f49f5cf3-7707-f004-acec-e816ad74a08b.htm)

elementsMoveInto
:   Type:  [Autodesk.Revit.DB WorksetId](8bece327-c269-8101-b4c2-38632f593fe6.htm)

# Remarks

elementsMoveInto only takes effect when DeleteWorksetOption::Enum is MoveElementsToWorkset.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[DeleteWorksetSettings Class](1952e14e-42d8-d672-0e72-d5fb1a83b73a.htm)

[DeleteWorksetSettings Overload](6b4b08b1-e82e-5352-1111-75a2cbbead24.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)