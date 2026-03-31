[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPublicAccessKey Method

---



|  |
| --- |
| [ExternalService Class](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)   [See Also](#seeAlsoToggle) |

Access key to use to execute a service.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public Guid GetPublicAccessKey() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPublicAccessKey As Guid ``` |

 

| Visual C++ |
| --- |
| ``` public: Guid GetPublicAccessKey() ``` |

#### Return Value

GUID representing the access key.

# Remarks

The service must be declared as public in order for callers be able to invoke this method. Services that are not public can be executed only by their owners (the ones who registered it).

Most services are not public and may only be executed by their respective owners. To see whether a service was declared as public, call the GetOptions method and check the IsPublic property.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The service is not public, thus the access key cannot be obtained. |

# See Also

[ExternalService Class](0408e6d9-12d3-20e4-911e-6d299fe31b81.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)