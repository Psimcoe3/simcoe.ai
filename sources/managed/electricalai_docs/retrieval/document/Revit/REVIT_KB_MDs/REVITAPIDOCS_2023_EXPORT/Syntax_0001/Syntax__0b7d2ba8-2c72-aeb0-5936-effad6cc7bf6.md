[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreatePipeConnector Method (Document, PipeSystemType, Reference, Edge)

---



|  |
| --- |
| [ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)   [See Also](#seeAlsoToggle) |

Create a new pipe ConnectorElement with a face and an edge.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static ConnectorElement CreatePipeConnector( 	Document document, 	PipeSystemType pipeSystemType, 	Reference planarFace, 	Edge edge ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CreatePipeConnector ( _ 	document As Document, _ 	pipeSystemType As PipeSystemType, _ 	planarFace As Reference, _ 	edge As Edge _ ) As ConnectorElement ``` |

 

| Visual C++ |
| --- |
| ``` public: static ConnectorElement^ CreatePipeConnector( 	Document^ document,  	PipeSystemType pipeSystemType,  	Reference^ planarFace,  	Edge^ edge ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to add the connector to.

pipeSystemType
:   Type:  [Autodesk.Revit.DB.Plumbing PipeSystemType](24165d09-9267-54b7-3e32-6405d1343c2e.htm)    
     The PipeSystemType of the connector.

planarFace
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The planar face to place the connector on.

edge
:   Type:  [Autodesk.Revit.DB Edge](7155ef49-fcd9-c80a-6232-70189a617bcc.htm)    
     One of the edges in the edge loop that defines the connector location on the planar face.

#### Return Value

The pipe ConnectorElement.

# Remarks

Regenerates the document.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The reference is not a planar face. -or- document is not a family document. -or- Thrown when the edge does not belong to the face. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | A value passed for an enumeration argument is not a member of that enumeration |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Connector creation is not allowed in this family. |

# See Also

[ConnectorElement Class](cd7d7579-1058-e8ca-d55a-c3a914843667.htm)

[CreatePipeConnector Overload](c6188202-bd11-204d-de6e-afa1c6799d50.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)