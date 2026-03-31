[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IExternalServer Interface

---



|  |
| --- |
| [Members](7fa1d772-484f-0544-4825-dbf2f7a71e3b.htm)   [See Also](#seeAlsoToggle) |

The base interface for all external servers.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public interface IExternalServer ``` |

 

| Visual Basic |
| --- |
| ``` Public Interface IExternalServer ``` |

 

| Visual C++ |
| --- |
| ``` public interface class IExternalServer ``` |

# Remarks

Every external service in Revit declares a specific interface for its servers. Each interface must be derived from this IExternalServer. Providers of external servers implement the server interfaces defined by the respective external services to which the servers belong. The whole process of creating a server and registering it with Revit as a server of a concrete external service can be outlined in the following steps:

1. A provider of an external service declares a server interface derived from IExternalServer
2. The provider of the service will make it known that this interface is for the servers of that service
3. An application wanting to have a server will implement the appropriate interface
4. The server's application obtains the service from Revit using the ExternalServiceRegistry.GetService method
5. An instance of the server class can then be registered with Revit by using the ExternalService.AddServer method

# See Also

[IExternalServer Members](7fa1d772-484f-0544-4825-dbf2f7a71e3b.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)