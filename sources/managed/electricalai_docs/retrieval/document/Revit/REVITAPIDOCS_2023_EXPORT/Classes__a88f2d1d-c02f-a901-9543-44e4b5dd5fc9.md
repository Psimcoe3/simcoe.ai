[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Autodesk.Revit.DB.ExternalService Namespace

---



|  |
| --- |
|  |

# Classes

|  | Class | Description |
| --- | --- | --- |
| Public class | [ExternalService](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm) | This base class represents an external service inside Revit application. |
| Public class | [ExternalServiceId](2bab66fa-f55d-4419-46d1-f33b9540e727.htm) | Unique identifier of an external service. |
| Public class | [ExternalServiceOptions](80467d42-3f13-de3e-cd06-bf3b43afefe0.htm) | Various options affecting the behavior of an External Service |
| Public class | [ExternalServiceRegistry](fa14442f-3d47-2c21-467c-6d19e4cc0d9e.htm) | This class gives access to external services. Use it to register external services with Revit and execute them. Only the application that registers a service is allowed to execute it. |
| Public class | [ExternalServices](12a99399-0a75-d501-ab77-f7c5db83e361.htm) | Provides a container of all Revit built-in ExternalServiceId instances. |
| Public class | [ExternalServices BuiltInExternalServices](f189eb3f-7a3a-2891-657a-e18cbf014987.htm) | A collection of ids for external services that are managed and used by Revit directly. |
| Public class | [MultiServerService](ac0494f1-bd1c-4596-e2bf-eec3ac36e3b4.htm) | This class represents a multi-server service inside Revit application. It is created when an instance of IMultiServerService is registered with Revit. |
| Public class | [SingleServerService](8491691e-2a26-684e-f43c-e8e0095fd129.htm) | This class represents a single-server service inside Revit application. It is created when an instance of ISingleServerService is registered with Revit. |

# Interfaces

|  | Interface | Description |
| --- | --- | --- |
| Public interface | [IExternalData](d4f0854f-3b67-c60e-1696-8cffbaba065a.htm) | The base interface for data classes used when executing servers of external services. |
| Public interface | [IExternalServer](91e4af0b-59c0-d640-107a-eebc4d99fa76.htm) | The base interface for all external servers. |
| Public interface | [IExternalService](37fe86a0-0668-5908-9966-dfac0e0c1fe3.htm) | The base interface class for all external services. |
| Public interface | [IMultiServerService](9704c8c0-2095-37e7-f17c-56d27ff44ed6.htm) | The base interface class for all multi-server services. |
| Public interface | [ISingleServerService](ae967a42-6490-07ed-7976-71d324d250c4.htm) | The base interface class for all single-server services. |

# Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
| Public enumeration | [DisparityResponse](29ab805b-5976-912d-3166-ef04d78d612f.htm) | An enumerated value to return from OnServerDiparity indicating what the service wants Revit to do as the post-action of the call. |
| Public enumeration | [ExecutionPolicy](5234000e-cf74-d7aa-85ff-dcfbed63434b.htm) | Controls how servers of multi-server external services are executed. |
| Public enumeration | [ExternalServiceResult](63c83d88-92c7-5283-8b39-efb0baeedcd8.htm) | An enumerated value representing a result from executing an external service. |
| Public enumeration | [ServerChangeCause](02016116-f6cf-5d3a-94df-811ef76bdebc.htm) | Indicates the cause for the active server to be changed |