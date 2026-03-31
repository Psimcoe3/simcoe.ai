[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDescription Method

---



|  |
| --- |
| [IExternalServer Interface](91e4af0b-59c0-d640-107a-eebc4d99fa76.htm)   [See Also](#seeAlsoToggle) |

Implement this method to return a description of the server.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` string GetDescription() ``` |

 

| Visual Basic |
| --- |
| ``` Function GetDescription As String ``` |

 

| Visual C++ |
| --- |
| ``` String^ GetDescription() ``` |

#### Return Value

Description of the server.

# Remarks

The purpose of this string is to describe the external server in more details than just a short name alone could do. The intended use is to show the string to the end user in UI when UI is appropriate for the corresponding external service.

Beside the requirement for it to be a non-empty string, there are no other general restrictions imposed by the External Services Framework. However, the external service may have some specific rules in place for its servers.

# See Also

[IExternalServer Interface](91e4af0b-59c0-d640-107a-eebc4d99fa76.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)