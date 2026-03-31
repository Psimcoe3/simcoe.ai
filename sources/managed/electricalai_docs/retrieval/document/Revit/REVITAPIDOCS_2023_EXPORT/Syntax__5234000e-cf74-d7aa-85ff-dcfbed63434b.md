[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExecutionPolicy Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

Controls how servers of multi-server external services are executed.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public enum ExecutionPolicy ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration ExecutionPolicy ``` |

 

| Visual C++ |
| --- |
| ``` public enum class ExecutionPolicy ``` |

# Members

| Member name | Description |
| --- | --- |
| FirstApplicableServer | This policy instructs to find the first applicable server, which would be the first one that the service claims (by returning True from the CanExecute method) it can be executed. With that server the service will be called to execute it. If the execution fails or if an unhandled exception is raised from it the result will be ExternalServiceResult.Failed, otherwise it will be ExternalServiceResult.Succeeded, unless no applicable server can be found, which would cause returning ExternalServiceResult.Unhandled. |
| AllApplicableServers | Under this policy the framework will call to execute a service with all applicable servers, that is the servers that are currently set as active and for which the service responds affirmatively to the CanExecute method. If and only if the service can execute all applicable servers successfully the execution returns ExternalServiceResult.Succeeded. If execution of any applicable server fails, the execution loop breaks and the return value will be ExternalServiceResult.Failed. If no applicable servers can be found, the return value will be ExternalServiceResult.Unhandled. |

# See Also

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)