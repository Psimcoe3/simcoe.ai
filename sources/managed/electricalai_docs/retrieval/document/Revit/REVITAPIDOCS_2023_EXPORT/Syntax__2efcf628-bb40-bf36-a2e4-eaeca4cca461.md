[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RollBack Method

---



|  |
| --- |
| [TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)   [See Also](#seeAlsoToggle) |

Rolls back the transaction group, which effectively undoes all transactions committed inside the group.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public TransactionStatus RollBack() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function RollBack As TransactionStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: TransactionStatus RollBack() ``` |

#### Return Value

If finished successfully, this method returns TransactionStatus.RolledBack.

# Remarks

Note that once a group is rolled back, the undone transactions cannot be redone.

RollBack can be called only when all inner transaction groups and transactions are finished, i.e. after they were either committed or rolled back.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The Transaction group has not been started (its status is not 'Started').. -or- The transaction's document is currently in failure mode. Transaction groups cannot be closed until failure handling is finished. You may use a transaction finalizer to close a group after the failure handling ends. |

# See Also

[TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)