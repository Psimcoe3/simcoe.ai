[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsCodeSuccess Method

---



|  |
| --- |
| [LinkLoadResult Class](f846bfb0-b047-9332-567f-75ae880d8359.htm)   [See Also](#seeAlsoToggle) |

Check if load result code signifies success.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static bool IsCodeSuccess( 	LinkLoadResultType code ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsCodeSuccess ( _ 	code As LinkLoadResultType _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsCodeSuccess( 	LinkLoadResultType code ) ``` |

#### Parameters

code
:   Type:  [Autodesk.Revit.DB LinkLoadResultType](11b095e1-24d9-91b9-ae2e-004f67c94d6e.htm)    
     Load result code to be verified.

#### Return Value

True if LinkLoadResultType argument is success, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |

# See Also

[LinkLoadResult Class](f846bfb0-b047-9332-567f-75ae880d8359.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)