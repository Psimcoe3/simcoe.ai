---
created: 2026-01-28T20:53:26 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_html
author: 
---

# Help | Transactions | Autodesk

> ## Excerpt
> Transactions are context-like objects that encapsulate any changes to a Revit model. Any change to a document can only be made while there is an active transaction open for that document. Attempting to change the document outside of a transaction will throw an exception. Changes do not become a part of the model until the active transaction is committed. Consequently, all changes made in a transaction can be rolled back either explicitly or implicitly (by the destructor). Only one transaction per document can be open at any given time. A transaction may consist of one or more operations.

---
Transactions are context-like objects that encapsulate any changes to a Revit model. Any change to a document can only be made while there is an active transaction open for that document. Attempting to change the document outside of a transaction will throw an exception. Changes do not become a part of the model until the active transaction is committed. Consequently, all changes made in a transaction can be rolled back either explicitly or implicitly (by the destructor). Only one transaction per document can be open at any given time. A transaction may consist of one or more operations.

There are three main classes in the Revit API related to transactions:

-   Transaction
    
-   SubTransaction
    
-   TransactionGroup
    

This section will discuss each of these classes in more depth. Only the Transaction class is required to make changes to a document. The other classes can be used to better organize changes.

Note: An exception will be thrown if a transaction is started from an outside thread or outside modeless dialog. Transactions can only be started from supported API workflows, such as part of an external command, event, updater, or call-back.
