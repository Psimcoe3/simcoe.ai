---
created: 2026-01-28T20:53:39 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Transactions_Failure_Handling_Options_html
author: 
---

# Help | Failure Handling Options | Autodesk

> ## Excerpt
> Failure handling options are options for how failures, if any, should be handled at the end of a transaction. Failure handling options may be set at any time before calling either Transaction.Commit() or Transaction.RollBack() using the Transaction.SetFailureHandlingOptions() method. However, after a transaction is committed or rolled back, the options return to their respective default settings.

---
Failure handling options are options for how failures, if any, should be handled at the end of a transaction. Failure handling options may be set at any time before calling either Transaction.Commit() or Transaction.RollBack() using the Transaction.SetFailureHandlingOptions() method. However, after a transaction is committed or rolled back, the options return to their respective default settings.

The SetFailureHandlingOptions() method takes a FailureHandlingOptions object as a parameter. This object cannot be created, it must be obtained from the transaction using the GetFailureHandlingOptions() method. Options are set by calling the corresponding Set method, such as SetClearAfterRollback(). The following sections discuss the failure handling options in more detail.

### ClearAfterRollback

This option controls whether all warnings should be cleared after a transaction is rolled back. The default value is False.

### DelayedMiniWarnings

This options controls whether mini-warnings, if any, are displayed at the end of the transaction currently being ended, or if they should be postponed until the end of next transaction. This is typically used within a chain of transactions when it is not desirable to show intermediate warnings at the end of each step, but rather to wait until the completion of the entire chain.

Warnings may be delayed for more than one transaction. The first transaction that does not have this option set to True will display all of its own warnings, if any, as well as all warnings that might have accumulated from previous transactions. The default value is False.

Note: This option is ignored in modal mode (see ForcedModalHandling below). ### ForcedModalHandling

This options controls whether eventual failures will be handled modally or modelessly. The default is True. Be aware that if the modeless failure handling is set, processing the transaction may be done asynchronously, which means that upon returning from the Commit or RollBack calls, the transaction will not be finished yet (the status will be 'Pending').

### SetFailuresPreprocessor

This interface, if provided, is invoked when there are failures found at the end of a transaction. The preprocessor may examine current failures and even try to resolve them. See [Failure Posting and Handling](https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Advanced_Topics_Failure_Posting_and_Handling_html) for more information.

### SetTransactionFinalizer

A finalizer is an interface, which, if provided, can be used to perform a custom action at the end of a transaction. Note that it is not invoked when the Commit() or RollBack() methods are called, but only after the process of committing or rolling back is completed. Transaction finalizers must implement the _ITransactionFinalizer_ interface, which requires two functions to be defined:

-   OnCommitted - called at the end of committing a transaction
-   OnRolledBack - called at the end of rolling back a transaction

Note: Since the finalizer is called after the transaction has finished, the document is not modifiable from the finalizer unless a new transaction is started.
