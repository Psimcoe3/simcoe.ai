---
created: 2026-01-28T20:53:50 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_Temporary_transactions_html
author: 
---

# Help | Temporary transactions | Autodesk

> ## Excerpt
> It is not always required to commit a transaction. The transaction framework also allows for Trasactions to be rolled back. This is useful when there is an error during the processing of the transaction, but can also be leverage directly as a technique to create a temporary transaction.

---
It is not always required to commit a transaction. The transaction framework also allows for Trasactions to be rolled back. This is useful when there is an error during the processing of the transaction, but can also be leverage directly as a technique to create a temporary transaction.

Using a temporary transaction can be useful for certain types of analyses. For example, an application looking to extract geometric properties from a wall or other object before it is cut by openings should use a temporary transaction in conjunction with Document.Delete(). When the application deletes the elements that cut the target elements, the cut element’s geometry is restored to its original state (after the document has been regenerated).

To use a temporary transaction:

1.  Instantiate the Transaction using the Transaction constructor, and assign it a name.
2.  Call Transaction.Start()
3.  Make the temporary change(s) to the document (element modification, deletion or creation)
4.  Regenerate the document
5.  Extract the desired geometry and properties
6.  Call Transaction.RollBack() to restore the document to the previous state.

This technique is also applicable to SubTransactions.
