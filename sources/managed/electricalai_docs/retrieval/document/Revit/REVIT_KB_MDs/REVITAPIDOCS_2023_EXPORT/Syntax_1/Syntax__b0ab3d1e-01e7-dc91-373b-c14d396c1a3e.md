[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsParameterLockable Method

---



|  |
| --- |
| [FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)   [See Also](#seeAlsoToggle) |

For Conceptual Mass and Curtain Panel families, indicate whether the specified parameter can be locked.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsParameterLockable( 	FamilyParameter familyParameter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsParameterLockable ( _ 	familyParameter As FamilyParameter _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsParameterLockable( 	FamilyParameter^ familyParameter ) ``` |

#### Parameters

familyParameter
:   Type:  [Autodesk.Revit.DB FamilyParameter](6175e974-870e-7fbc-3df7-46105f937a6e.htm)

#### Return Value

True if the family is a Conceptual Mass or Curtain Panel Family and the parameter drives one or more dimensions; false otherwise.

# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)