[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExecuteService Method (Guid, IExternalData)

---



|  |
| --- |
| [ExternalServiceRegistry Class](fa14442f-3d47-2c21-467c-6d19e4cc0d9e.htm)   [See Also](#seeAlsoToggle) |

Execute a service independently of any document.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ExternalServiceResult ExecuteService( 	Guid executionKey, 	IExternalData data ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ExecuteService ( _ 	executionKey As Guid, _ 	data As IExternalData _ ) As ExternalServiceResult ``` |

 

| Visual C++ |
| --- |
| ``` public: static ExternalServiceResult ExecuteService( 	Guid executionKey,  	IExternalData^ data ) ``` |

#### Parameters

executionKey
:   Type:  System Guid    
     Access key of the service to be executed. The key is not the same as the service's Id. It is the value that was returned to the caller who registered the service.

data
:   Type:  [Autodesk.Revit.DB.ExternalService IExternalData](d4f0854f-3b67-c60e-1696-8cffbaba065a.htm)    
     The associated data. The type is defined by the service.

#### Return Value

The result of executing the external service.

# Remarks

Execution of a service should be invoked only by the application that registered the service. The execution will use the currently active server (or servers in the case of a multi-server service).

This method does not take a document as one of its arguments and therefore it is not intended for executions of recordable services that may modify documents. If the service (recordable) or its server(s) is expected to modify documents, the other ExecuteService method -- the one that takes a document as one of its arguments -- is supposed to be used.

Non-recordable services are free to modify documents during this ExecuteService call, because activities of non-recordable services are not recorded; the changes those services made are assumed to be independent of the presence of the service and/or its servers.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The execution key is either invalid or of a service that is not registered. To execute a service, the key returned by RegisterService method must be used. -or- The execution key is of a service that is already being executed. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ExternalServiceRegistry Class](fa14442f-3d47-2c21-467c-6d19e4cc0d9e.htm)

[ExecuteService Overload](441ae935-fa59-aa1e-23ba-57e334974c7f.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)