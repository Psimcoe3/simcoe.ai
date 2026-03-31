[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RelinquishOwnership Method

---



|  |
| --- |
| [WorksharingUtils Class](ae7857a0-4e9b-f9c1-84c7-8b250af68068.htm)   [See Also](#seeAlsoToggle) |

Relinquishes ownership by the current user of as many specified elements and worksets as possible, and grants element ownership requested by other users on a first-come, first-served basis.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static RelinquishedItems RelinquishOwnership( 	Document document, 	RelinquishOptions generalCategories, 	TransactWithCentralOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function RelinquishOwnership ( _ 	document As Document, _ 	generalCategories As RelinquishOptions, _ 	options As TransactWithCentralOptions _ ) As RelinquishedItems ``` |

 

| Visual C++ |
| --- |
| ``` public: static RelinquishedItems^ RelinquishOwnership( 	Document^ document,  	RelinquishOptions^ generalCategories,  	TransactWithCentralOptions^ options ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the elements and worksets.

generalCategories
:   Type:  [Autodesk.Revit.DB RelinquishOptions](af30374c-7e99-d52e-f648-c5969e91e9d8.htm)    
     General categories of items to relinquish. See RelinquishOptions for details.

options
:   Type:  [Autodesk.Revit.DB TransactWithCentralOptions](f5da22fa-55ee-9196-cafd-5323d8e9ca0a.htm)    
     Options to customize access to the central model.    a null reference (  Nothing  in Visual Basic)  is allowed and means no customization.

#### Return Value

The elements and worksets that were relinquished.

# Remarks

Elements and worksets owned by other users are ignored.

Only unmodified elements already in central will be relinquished by this method. Newly added and modified elements cannot be relinquished until they have been synchronized with central.

For best performance, relinquish items in one big call, rather than many small calls.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a workshared document. -or- document is not a primary document, it is a linked document. -or- document is read-only: It cannot be modified. -or- document has an open editing transaction and is accepting changes. -or- Saving is not allowed in the current application mode. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions CentralFileCommunicationException](20094e4f-8326-8378-e5bc-452341d131c2.htm) | The file-based central model could not be reached, e.g. the network is down or the file server is down. |
| [Autodesk.Revit.Exceptions CentralModelAccessDeniedException](3e38b7b1-1ee8-c7f0-6cdd-bacf67bf61f4.htm) | Access to the central model was denied due to lack of access privileges. -or- Access to the central model was denied. A possible reason is because the model was under maintenance. |
| [Autodesk.Revit.Exceptions CentralModelContentionException](ad511076-c435-23c1-5720-1205c4ed28b9.htm) | The central model is locked by another client. |
| [Autodesk.Revit.Exceptions CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.htm) | The central model is overwritten by other user. -or- The central model is missing. -or- An internal error happened on the central model, please contact the server administrator. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Operation is not permitted when there is any open sub-transaction, transaction, or transaction group. |
| [Autodesk.Revit.Exceptions RevitServerCommunicationException](a0003d89-0113-6623-65da-0db5c568bfb6.htm) | The server-based central model could not be accessed because of a network communication error. |
| [Autodesk.Revit.Exceptions RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.htm) | An internal error happened on the server, please contact the server administrator. |

# See Also

[WorksharingUtils Class](ae7857a0-4e9b-f9c1-84c7-8b250af68068.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)