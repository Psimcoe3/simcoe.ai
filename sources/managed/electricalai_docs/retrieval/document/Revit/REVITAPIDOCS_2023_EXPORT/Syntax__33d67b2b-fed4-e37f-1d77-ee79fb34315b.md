[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetDelayedMiniWarnings Method

---



|  |
| --- |
| [FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)   [See Also](#seeAlsoToggle) |

Sets a flag indicating if Revit should delay the display of the mini-warning dialog (if one is to be shown as a result of warnings in the current transaction) until the end of the next transaction.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FailureHandlingOptions SetDelayedMiniWarnings( 	bool bFlag ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetDelayedMiniWarnings ( _ 	bFlag As Boolean _ ) As FailureHandlingOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: FailureHandlingOptions^ SetDelayedMiniWarnings( 	bool bFlag ) ``` |

#### Parameters

bFlag
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     True to delay the display of the mini-warning dialog until the end of the next transation, false to display them as this transaction is completed.

#### Return Value

This FailureHandlingOptions object.

# Remarks

This controls warnings suitable for the mini-warnings dialog only. If the modal flag is set to true with  [SetForcedModalHandling(Boolean)](ce01ea28-ccb4-0943-33ba-3fe39dc76f8c.htm)  then this flag will be ignored.

# See Also

[FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)