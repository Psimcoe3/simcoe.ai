[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanUserHaveOverrides Method

---



|  |
| --- |
| [WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)   [See Also](#seeAlsoToggle) |

Checks whether a single username can have customized graphic overrides.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public bool CanUserHaveOverrides( 	string username ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function CanUserHaveOverrides ( _ 	username As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool CanUserHaveOverrides( 	String^ username ) ``` |

#### Parameters

username
:   Type:  System String    
     The username to check.

#### Return Value

False if the username is on the list of removed users, True otherwise.

# Remarks

Only users that have not been removed can have overrides. Once it is removed, a username must be restored before its associated graphic overrides can be customized.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[WorksharingDisplaySettings Class](ec25e291-6582-7e8c-f273-efc0c391bcc4.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)