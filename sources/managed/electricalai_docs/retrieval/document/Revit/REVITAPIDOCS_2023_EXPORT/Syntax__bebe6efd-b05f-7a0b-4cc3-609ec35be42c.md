[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetClearAfterRollback Method

---



|  |
| --- |
| [FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)   [See Also](#seeAlsoToggle) |

Sets a flag indicating that Revit should clear all posted failures silently when the failing transaction is being rolled back intentionally. If not set, the failures may still be displayed to the user during rollback.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FailureHandlingOptions SetClearAfterRollback( 	bool bFlag ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetClearAfterRollback ( _ 	bFlag As Boolean _ ) As FailureHandlingOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: FailureHandlingOptions^ SetClearAfterRollback( 	bool bFlag ) ``` |

#### Parameters

bFlag
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     True to clear posted failures silently if the transaction is being rolled back, false to keep these failures in place (they may be displayed to the user).

#### Return Value

This FailureHandlingOptions object.

# See Also

[FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)