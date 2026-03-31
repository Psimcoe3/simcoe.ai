[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetFailureHandlingOptions Method

---



|  |
| --- |
| [FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)   [See Also](#seeAlsoToggle) |

Provides access to the failure handling options for the transaction currently being finished.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public FailureHandlingOptions GetFailureHandlingOptions() ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetFailureHandlingOptions As FailureHandlingOptions ``` |

 

| Visual C++ |
| --- |
| ``` public: FailureHandlingOptions^ GetFailureHandlingOptions() ``` |

#### Return Value

The failure handling options for transaction currently being finished.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This FailuresAccessor is inactive (is used outside of failures processing). |

# See Also

[FailuresAccessor Class](dea68b06-a061-fc05-d814-db741f2e7f14.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)