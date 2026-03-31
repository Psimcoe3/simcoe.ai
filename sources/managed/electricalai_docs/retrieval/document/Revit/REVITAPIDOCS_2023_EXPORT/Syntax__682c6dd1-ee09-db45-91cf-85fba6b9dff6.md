[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ValidateViewType Method

---



|  |
| --- |
| [ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)   [See Also](#seeAlsoToggle) |

Validates the incoming view type. As of today, the only allowed view type is Plan.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public static bool ValidateViewType( 	DirectShapeTargetViewType targetViewType ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ValidateViewType ( _ 	targetViewType As DirectShapeTargetViewType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool ValidateViewType( 	DirectShapeTargetViewType targetViewType ) ``` |

#### Parameters

targetViewType
:   Type:  [Autodesk.Revit.DB DirectShapeTargetViewType](1c5cd94e-3804-54da-73af-505655b0948f.htm)

#### Return Value

True if %targetViewType% is DirectShapeTargetViewType::Plan

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[ViewShapeBuilder Class](f99edd24-4519-56d5-a5d6-aa1565a893af.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)