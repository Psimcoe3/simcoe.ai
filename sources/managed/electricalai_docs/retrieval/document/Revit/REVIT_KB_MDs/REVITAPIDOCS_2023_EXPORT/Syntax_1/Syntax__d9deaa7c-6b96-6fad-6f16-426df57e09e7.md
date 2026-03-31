[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidResourceName Method

---



|  |
| --- |
| [ExternalResourceBrowserData Class](94a46450-5467-45f2-0228-4c9f9821b4c9.htm)   [See Also](#seeAlsoToggle) |

Checks whether the resource name is valid.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public bool IsValidResourceName( 	string resourceName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsValidResourceName ( _ 	resourceName As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsValidResourceName( 	String^ resourceName ) ``` |

#### Parameters

resourceName
:   Type:  System String    
     The resource name to check.

#### Return Value

True if the name is a valid resource name, false otherwise.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternalResourceBrowserData Class](94a46450-5467-45f2-0228-4c9f9821b4c9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)