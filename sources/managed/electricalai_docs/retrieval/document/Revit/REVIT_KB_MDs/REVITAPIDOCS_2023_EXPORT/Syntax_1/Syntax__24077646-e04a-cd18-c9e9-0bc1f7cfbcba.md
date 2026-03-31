[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsRegisteredServerId Method

---



|  |
| --- |
| [ExternalService Class](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)   [See Also](#seeAlsoToggle) |

Checks if the Id represents a valid server that has been registered for the service.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public bool IsRegisteredServerId( 	Guid serverId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsRegisteredServerId ( _ 	serverId As Guid _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsRegisteredServerId( 	Guid serverId ) ``` |

#### Parameters

serverId
:   Type:  [System Guid](http://msdn2.microsoft.com/en-us/library/cey1zx63)    
     An Id of a server

#### Return Value

True if the specified server is currently registed for this service, false otherwise.

# See Also

[ExternalService Class](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)