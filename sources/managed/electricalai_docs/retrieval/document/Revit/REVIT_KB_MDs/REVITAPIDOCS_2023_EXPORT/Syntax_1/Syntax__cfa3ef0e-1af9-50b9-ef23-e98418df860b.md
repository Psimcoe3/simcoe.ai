[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetClearAfterRollback Method

---



|  |
| --- |
| [FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)   [See Also](#seeAlsoToggle) |

Obtains the flag indicating if all posted failures should be removed silently when transaction is being rolled back.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public bool GetClearAfterRollback() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetClearAfterRollback As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool GetClearAfterRollback() ``` |

#### Return Value

True to clear posted failures silently if the transaction is being rolled back, false to keep these failures in place (they may be displayed to the user).

# See Also

[FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)