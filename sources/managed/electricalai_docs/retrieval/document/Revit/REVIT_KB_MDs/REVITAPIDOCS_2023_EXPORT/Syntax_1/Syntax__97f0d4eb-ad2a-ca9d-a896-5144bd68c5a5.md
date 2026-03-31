[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CheckoutWorksets Method (Document, ICollection(WorksetId))

---



|  |
| --- |
| [WorksharingUtils Class](ae7857a0-4e9b-f9c1-84c7-8b250af68068.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Obtains ownership for the current user of as many specified worksets as possible.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static ICollection<WorksetId> CheckoutWorksets( 	Document document, 	ICollection<WorksetId> worksetsToCheckout ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CheckoutWorksets ( _ 	document As Document, _ 	worksetsToCheckout As ICollection(Of WorksetId) _ ) As ICollection(Of WorksetId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<WorksetId^>^ CheckoutWorksets( 	Document^ document,  	ICollection<WorksetId^>^ worksetsToCheckout ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document containing the worksets.

worksetsToCheckout
:   Type:  System.Collections.Generic ICollection   [WorksetId](8bece327-c269-8101-b4c2-38632f593fe6.htm)    
     The ids of the worksets to attempt to check out.

#### Return Value

The ids of all specified worksets that are now owned, including all that were owned prior to the function call.

# Remarks

For best performance, check out all worksets in one big call, rather than many small calls.

When there comes a contention error when locking the central model, this API would wait and retry endlessly until getting the lock of the central model.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
void CheckoutAllViewWorksets(Document doc)
{
    FilteredWorksetCollector collector = new FilteredWorksetCollector(doc);

    // find all view worksets
    collector.OfKind(WorksetKind.ViewWorkset);
    ICollection<WorksetId> viewworksets = collector.ToWorksetIds();
    ICollection<WorksetId> checkoutworksets = WorksharingUtils.CheckoutWorksets(doc, viewworksets);
    TaskDialog.Show("Checked out worksets", "Number of worksets checked out: " + checkoutworksets.Count);
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
Private Sub CheckoutAllViewWorksets(doc As Document)
    Dim collector As New FilteredWorksetCollector(doc)

    ' find all view worksets
    collector.OfKind(WorksetKind.ViewWorkset)
    Dim viewworksets As ICollection(Of WorksetId) = collector.ToWorksetIds()
    Dim checkoutworksets As ICollection(Of WorksetId) = WorksharingUtils.CheckoutWorksets(doc, viewworksets)
    TaskDialog.Show("Checked out worksets", "Number of worksets checked out: " + checkoutworksets.Count)
End Sub
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a workshared document. -or- document is not a primary document, it is a linked document. -or- document is read-only: It cannot be modified. -or- document has an open editing transaction and is accepting changes. -or- There are one or more ids with no corresponding workset. -or- Saving is not allowed in the current application mode. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions CentralFileCommunicationException](20094e4f-8326-8378-e5bc-452341d131c2.htm) | The file-based central model could not be reached, e.g. the network is down or the file server is down. |
| [Autodesk.Revit.Exceptions CentralModelAccessDeniedException](3e38b7b1-1ee8-c7f0-6cdd-bacf67bf61f4.htm) | Access to the central model was denied due to lack of access privileges. -or- Access to the central model was denied. A possible reason is because the model was under maintenance. |
| [Autodesk.Revit.Exceptions CentralModelContentionException](ad511076-c435-23c1-5720-1205c4ed28b9.htm) | The central model are locked by another client. |
| [Autodesk.Revit.Exceptions CentralModelException](0e2ac15f-ca64-42c3-b3ef-e6f7ca1cb59a.htm) | The central model is overwritten by other user. -or- The central model is missing. -or- An internal error happened on the central model, please contact the server administrator. |
| [Autodesk.Revit.Exceptions CentralModelVersionArchivedException](9b54c5a2-22f3-ac30-3efd-7ef80adff6ea.htm) | Last central version merged into the local model has been archived in the central model. This exception could only be thrown from cloud models. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Operation is not permitted when there is any open sub-transaction, transaction, or transaction group. |
| [Autodesk.Revit.Exceptions RevitServerCommunicationException](a0003d89-0113-6623-65da-0db5c568bfb6.htm) | The server-based central model could not be accessed because of a network communication error. |
| [Autodesk.Revit.Exceptions RevitServerInternalException](6dcd093c-d643-07cd-535f-36ffa9d2db52.htm) | An internal error happened on the server, please contact the server administrator. |

# See Also

[WorksharingUtils Class](ae7857a0-4e9b-f9c1-84c7-8b250af68068.htm)

[CheckoutWorksets Overload](189cde61-a876-1c58-749d-8ce40b84b542.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)