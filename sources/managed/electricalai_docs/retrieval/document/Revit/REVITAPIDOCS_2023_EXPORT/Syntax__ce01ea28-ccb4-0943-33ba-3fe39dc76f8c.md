[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetForcedModalHandling Method

---



|  |
| --- |
| [FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)   [See Also](#seeAlsoToggle) |

Sets a flag indicating whether Revit will show a modal (blocking) error dialog if the transaction failed to finish.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FailureHandlingOptions SetForcedModalHandling( 	bool bFlag ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetForcedModalHandling ( _ 	bFlag As Boolean _ ) As FailureHandlingOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: FailureHandlingOptions^ SetForcedModalHandling( 	bool bFlag ) ``` |

#### Parameters

bFlag
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     True to force Revit to use a modal error dialog, false to allow a non-blocking dialog for warnings resulting from this transaction.

#### Return Value

This FailureHandlingOptions object.

# See Also

[FailureHandlingOptions Class](c03bb2e5-f679-bf24-4e87-08b3c3a08385.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)