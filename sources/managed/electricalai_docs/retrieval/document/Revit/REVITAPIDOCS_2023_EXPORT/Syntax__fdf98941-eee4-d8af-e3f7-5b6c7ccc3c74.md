[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetStatus Method

---



|  |
| --- |
| [Transaction Class](308ebf8d-d96d-4643-cd1d-34fffcea53fd.htm)   [See Also](#seeAlsoToggle) |

Returns the current status of the transaction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public TransactionStatus GetStatus() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetStatus As TransactionStatus ``` |

 

| Visual C++ |
| --- |
| ``` public: TransactionStatus GetStatus() ``` |

#### Return Value

The current status of the transaction.

# Remarks

If the status was set to TransactionStatus.Pending as the result of calling Commit or RollBack, the status will be changed later to either 'Committed' or 'RolledBack' after failure handling is finished. That status change will be made asynchronously.

# See Also

[Transaction Class](308ebf8d-d96d-4643-cd1d-34fffcea53fd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)