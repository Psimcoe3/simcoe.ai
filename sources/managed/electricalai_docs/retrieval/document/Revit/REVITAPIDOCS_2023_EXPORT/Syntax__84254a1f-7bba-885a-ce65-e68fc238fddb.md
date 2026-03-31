[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TransactionMode Enumeration

---



|  |
| --- |
| [See Also](#seeAlsoToggle) |

All transaction modes supported by Revit external commands.

**Namespace:**   [Autodesk.Revit.Attributes](59587eb2-4714-707c-9ec9-766e70658df7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public enum TransactionMode ``` |

 

| Visual Basic |
| --- |
| ``` Public Enumeration TransactionMode ``` |

 

| Visual C++ |
| --- |
| ``` public enum class TransactionMode ``` |

# Members

| Member name | Description |
| --- | --- |
| Manual | The API framework will not create a transaction (but will create an outer group to roll back all changes if the external command returns a failure status). Instead, you may use combinations of transactions, sub-transactions, and groups. You will have to follow all rules regarding use of transactions and related classes. You will have to give your transactions names, which will then appear in the undo menu. Revit will check that all transactions (also groups and sub-transaction) are properly closed upon return from an external command. If not, it will discard all changes to the model. |
| ReadOnly | No transaction (nor group) will be created, and no transaction may be created for the lifetime of the command. The External command may use methods that only read from the model, but not methods that write anything to it. Exceptions will be thrown if the command either tries to start a transaction (or group) or attempts to write to the model. |

# See Also

[Autodesk.Revit.Attributes Namespace](59587eb2-4714-707c-9ec9-766e70658df7.htm)