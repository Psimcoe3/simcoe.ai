[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetActiveServer Method (Guid, Document)

---



|  |
| --- |
| [SingleServerService Class](8491691e-2a26-684e-f43c-e8e0095fd129.htm)   [See Also](#seeAlsoToggle) |

Change the active server for a specific document.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetActiveServer( 	Guid serverId, 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetActiveServer ( _ 	serverId As Guid, _ 	document As Document _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetActiveServer( 	Guid serverId,  	Document^ document ) ``` |

#### Parameters

serverId
:   Type:  System Guid    
     Id of the server.

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document for which the server is being set as active.

# Remarks

Only one server per document can be set as active at any given time in a single-server service. A document does not have to have an explicitly set active server though - the application-wide active server would be normally used when the service is executed for such a document.

Having an active server for a document overrules the active server set for the application. That means if the service gets executed in this particular document, the document-specific server will be used instead of the application-wide one.

It is possible to set a server as active when another server is already active for that service in this document. Making a server active will automatically deactivate the server that was active before this call.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given Id is not of a server registered with the service. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The operation is not allowed because the service is being executed. |

# See Also

[SingleServerService Class](8491691e-2a26-684e-f43c-e8e0095fd129.htm)

[SetActiveServer Overload](81afb322-3236-ab36-6088-9d3dfde28fb1.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)