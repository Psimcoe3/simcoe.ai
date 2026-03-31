[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RegisterService Method (ISingleServerService, ExternalServiceOptions)

---



|  |
| --- |
| [ExternalServiceRegistry Class](fa14442f-3d47-2c21-467c-6d19e4cc0d9e.htm)   [See Also](#seeAlsoToggle) |

A method to register a single-server service.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static Guid RegisterService( 	ISingleServerService service, 	ExternalServiceOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function RegisterService ( _ 	service As ISingleServerService, _ 	options As ExternalServiceOptions _ ) As Guid ``` |

 

| Visual C++ |
| --- |
| ``` public: static Guid RegisterService( 	ISingleServerService^ service,  	ExternalServiceOptions^ options ) ``` |

#### Parameters

service
:   Type:  [Autodesk.Revit.DB.ExternalService ISingleServerService](ae967a42-6490-07ed-7976-71d324d250c4.htm)    
     An instance of the external service class that implements ISingleServerService interface.

options
:   Type:  [Autodesk.Revit.DB.ExternalService ExternalServiceOptions](80467d42-3f13-de3e-cd06-bf3b43afefe0.htm)    
     Optional settings to control the service's behavior.

#### Return Value

An access key to the service. The key is needed to execute the service.

# Remarks

Each service can only be registered once. Revit checks the Id of every service getting registered and throws an exception upon an attempt to register a service with an Id that already exists.

Services need to be registered before Revit ends its initialization. For external applications that means they have to register their services during OnStartup. This will give servers which need to register to services a chance to do so during the ApplicationInitialized event, which is raised after a successfully processing OnStartup routines.

A service can be registered as either recordable or non-recordable. It is expected that a service that is once registered as recordable will always be registered as recordable. Failure to comply with this policy may lead to data loss in some documents when they are opened in a Revit session with the service currently registered as non-recordable.

A service is supposed to be executed only by the application that registered it. To enforce this requirement, the registering method return an execution key (a Guid) that is required as an argument to ExecuteService methods. If the owner of a service allows executing it by anyone, it needs to register it as a public service (via the option argument). Once registered as public, The access key of the service can be obtained by any application, thus it can also be executed by any application. By default, a service is registered as private.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given service is not a valid implementation of ISingleServerService. -or- The given service does not return valid values from the interface methods. At least one of the Name, VendorId, Description, and ServiceId is either empty or invalid. -or- A service with this Id is either invalid or not unique. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Service cannot be registered because the registry of services has been already closed. All external services must be registered before the ApplicationInitialized event is raised. |

# See Also

[ExternalServiceRegistry Class](fa14442f-3d47-2c21-467c-6d19e4cc0d9e.htm)

[RegisterService Overload](6d690a5d-62c5-958c-842e-620a49421c1c.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)