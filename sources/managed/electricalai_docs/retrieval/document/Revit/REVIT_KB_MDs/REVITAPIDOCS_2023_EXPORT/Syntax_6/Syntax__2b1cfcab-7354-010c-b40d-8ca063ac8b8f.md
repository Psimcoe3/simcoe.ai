[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetActiveServers Method (IList(Guid), Document)

---



|  |
| --- |
| [MultiServerService Class](ac0494f1-bd1c-4596-e2bf-eec3ac36e3b4.htm)   [See Also](#seeAlsoToggle) |

Changes the active servers and/or their order for the given document.

**Namespace:**   [Autodesk.Revit.DB.ExternalService](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public void SetActiveServers( 	IList<Guid> serverIds, 	Document document ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetActiveServers ( _ 	serverIds As IList(Of Guid), _ 	document As Document _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetActiveServers( 	IList<Guid>^ serverIds,  	Document^ document ) ``` |

#### Parameters

serverIds
:   Type:  System.Collections.Generic IList   Guid    
     A set of Ids of servers that are to be set as active for this service in this document or an empty set if no server should currently be set as active in this particular document.

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document for which the servers are set as active.

# Remarks

More than one server per document can be set as active at any given time in a multi-server service. A document does not have to have an explicitly set active servers though - the application-wide active servers would be normally used when the service is executed for such a document.

Having active servers for a document overrules the active servers set for the application. That means if the service gets executed in this particular document, the document-specific servers will be used instead of the application-wide ones.

It is possible to set servers as active when other servers already are active for that service in this document. Setting a new set or the same set but with a different order will automatically replace the previously active servers in that document

All the servers must be valid (registered with the service) and must be unique in the set. The set may be empty though which allows to unset active servers from a document, which means that the document will be executed with the currently active servers set application-wide

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Some of the given Ids do not represent valid servers of the service. -or- The list of servers contains duplicates. The SetActiveServers method expects a set of unique servers. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The operation is not allowed because the service is being executed. |

# See Also

[MultiServerService Class](ac0494f1-bd1c-4596-e2bf-eec3ac36e3b4.htm)

[SetActiveServers Overload](9a109e4b-b9ca-da6e-ee6f-999e94fd35c2.htm)

[Autodesk.Revit.DB.ExternalService Namespace](a88f2d1d-c02f-a901-9543-44e4b5dd5fc9.htm)