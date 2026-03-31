[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ExecuteService Method (Guid, Document, IExternalData)

---



|  |
| --- |
| [ExternalServiceRegistry Class](fa14442f-3d47-2c21-467c-6d19e4cc0d9e.htm)   [See Also](#seeAlsoToggle) |

Execute the service for the given document.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static ExternalServiceResult ExecuteService( 	Guid executionKey, 	Document document, 	IExternalData data ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ExecuteService ( _ 	executionKey As Guid, _ 	document As Document, _ 	data As IExternalData _ ) As ExternalServiceResult ``` |

 

| Visual C++ |
| --- |
| ``` public: static ExternalServiceResult ExecuteService( 	Guid executionKey,  	Document^ document,  	IExternalData^ data ) ``` |

#### Parameters

executionKey
:   Type:  System Guid    
     Access key of the service to be executed. The key is not the same as the service's Id. It is the value that was returned to the caller who registered the service.

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document for which the service is going to be executed.

data
:   Type:  [Autodesk.Revit.DB.ExternalService IExternalData](d4f0854f-3b67-c60e-1696-8cffbaba065a.htm)    
     The associated data. The type must be of the class defined by the service.

#### Return Value

The result of executing the external service.

# Remarks

Execution of a service should be invoked only by the application that registered the service. The execution will use the active server (or servers in the case of a multi-server service) currently set for the given document. If there is no server specifically set for the document the current application-wide server (or servers) will be applied.

Please note that recordable services may only be executed in a document that is currently modifiable. An exception will be thrown if it isn't so. This requirement does not apply to non-recordable services.

This method is primarily intended for executing of recordable services, for it is assumed that any changes made to the model during the service's execution are likely tied with the service's currently active servers. If the service was registered as non-recordable, changes to the model may still be made, but the framework does not assume any explicit or implicit correlations between the document changes and servers that caused them, therefore it is not recorded which server did what. This fact is very important, particularly in work-sharing environment. If it may happen that different local users can have different servers installed and available, it is imperative for a non-serialized service that its servers are completely compatible with (or indifferent to) document modifications made by other servers of the same service. The responsibility for complying with this assumption is entirely on the service's provider.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The execution key is either invalid or of a service that is not registered. To execute a service, the key returned by RegisterService method must be used. -or- The execution key is of a service that is already being executed. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Executing a recordable service in a document that is not modifiable. |

# See Also

[ExternalServiceRegistry Class](fa14442f-3d47-2c21-467c-6d19e4cc0d9e.htm)

[ExecuteService Overload](441ae935-fa59-aa1e-23ba-57e334974c7f.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)