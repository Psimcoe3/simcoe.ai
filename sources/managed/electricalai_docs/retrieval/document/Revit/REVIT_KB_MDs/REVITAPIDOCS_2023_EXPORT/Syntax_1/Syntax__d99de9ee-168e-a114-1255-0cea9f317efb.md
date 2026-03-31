[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RollBack Method (FailureHandlingOptions)

---



|  |
| --- |
| [Transaction Class](308ebf8d-d96d-4643-cd1d-34fffcea53fd.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Rolls back all changes made to the model during the transaction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public TransactionStatus RollBack( 	FailureHandlingOptions options ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function RollBack ( _ 	options As FailureHandlingOptions _ ) As TransactionStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: TransactionStatus RollBack( 	FailureHandlingOptions^ options ) ``` |

#### Parameters

options
:   Type:  [Autodesk.Revit.DB FailureHandlingOptions](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)    
     A set of  [options](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)  to be used for handling eventual failures during this call.

    The options are only used temporarily during this rolling back process. After the transaction is finished, the options will be reset to their default values.

#### Return Value

If finished successfully, this method returns TransactionStatus.RolledBack.

Be aware that the returned status does not have to be necessarily the same like the status returned by  [GetStatus](fdf98941-eee4-d8af-e3f7-5b6c7ccc3c74.htm)  even when the method is called immediately after rolling back the transaction. Such difference may happen due to actions made by a transaction finalizer, if there was one set. (See  [FailureHandlingOptions](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)  for more details.)

# Remarks

By rolling back a transaction, all changes made to the model are discarded. RollBack may only be called for a transaction that has been started. (Use the  [GetStatus](fdf98941-eee4-d8af-e3f7-5b6c7ccc3c74.htm)  method to check the current state.) Be aware that rolling back may be delayed (as a result of failure handling.) Callers should always check the returned status to test whether a transaction was rolled back successfully. Only after rolling back is fully completed, the transaction may be started again.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
// All and any transaction should be enclosed in a 'using'
// block or guarded within a try-catch-finally blocks
// to guarantee that a transaction does not out-live its scope.
using (Transaction transaction = new Transaction(document))
{
   // Must start the transaction first to be able to modify a document
   transaction.Start("Creating Grid");

   // We create a line and use it as an argument to create a grid
   Line gridLine = Line.CreateBound(new XYZ(0, 0, elevation), new XYZ(20, 0, elevation));

   if ((null != gridLine) && (null != Grid.Create(document, gridLine)))
   {
      if (TransactionStatus.Committed == transaction.Commit())
      {
         return true;
      }
   }

   // We could not create the grid, so we roll the transaction back.

   // To demonstrate one particular property of failure handling options,
   // we can set clearing of accumulated warnings (if any) for this
   // transaction which is about to get rolled back anyway.
   // Clearing warnings is rarely desirable, but sometimes it is convenient.
   FailureHandlingOptions options = transaction.GetFailureHandlingOptions();

   transaction.RollBack(options.SetClearAfterRollback(true));
}
```

 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  VB.NET

```
' All and any transaction should be enclosed in a 'using'
' block or guarded within a try-catch-finally blocks
' to guarantee that a transaction does not out-live its scope.
Using transaction As New Transaction(document)
    ' Must start the transaction first to be able to modify a document
    transaction.Start("Creating Grid")

    ' We create a line and use it as an argument to create a grid
    Dim gridLine As Line = Line.CreateBound(New XYZ(0, 0, elevation), New XYZ(20, 0, elevation))

If (gridLine IsNot Nothing) AndAlso (Grid.Create(document, gridLine) IsNot Nothing) Then
   If TransactionStatus.Committed = transaction.Commit() Then
      Return True
   End If
End If

    ' We could not create the grid, so we roll the transaction back.


    ' To demonstrate one particular property of failure handling options,
    ' we can set clearing of accumulated warnings (if any) for this
    ' transaction which is about to get rolled back anyway.
    ' Clearing warnings is rarely desirable, but sometimes it is convenient.
    Dim options As FailureHandlingOptions = transaction.GetFailureHandlingOptions()

    transaction.RollBack(options.SetClearAfterRollback(True))
End Using
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The current status of the transaction is not 'Started'. Transaction must be started before calling Commit or Rollback. -or- The transaction's document is currently in failure mode. No transaction operations are permitted until failure handling is finished. |

# See Also

[Transaction Class](308ebf8d-d96d-4643-cd1d-34fffcea53fd.htm)

[RollBack Overload](2b534cc2-e464-d424-d504-d2ae260bd937.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)